#!/usr/bin/env python3
"""Build a static public article index from Zarir Madon's Substack RSS feed."""
import email.utils
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

FEED = 'https://zarirmadon.substack.com/feed'
OUTPUT = Path(__file__).resolve().with_name('posts.json')

class Extract(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.image = None
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('style', 'script'):
            self.skip += 1
        if tag == 'img' and not self.image:
            u = a.get('src', '')
            if u.startswith('https://'):
                self.image = u
        if tag in ('p','div','br','li'):
            self.text.append(' ')
    def handle_endtag(self, tag):
        if tag in ('style', 'script') and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.text.append(data)

def read_text(element, name):
    node = element.find(name)
    return (node.text or '').strip() if node is not None else ''

def main():
    req = urllib.request.Request(FEED, headers={'User-Agent':'LightLogicLunacyIndex/1.0 (+https://github.com/zarirmadon)', 'Accept':'application/rss+xml, application/xml, text/xml'})
    with urllib.request.urlopen(req, timeout=40) as response:
        xml = response.read(8_000_000)
    root = ET.fromstring(xml)
    channel = root.find('channel')
    if channel is None:
        raise RuntimeError('Expected an RSS channel from Substack')
    items = []
    for node in channel.findall('item'):
        title = html.unescape(read_text(node, 'title'))
        url = read_text(node, 'link')
        host = urlparse(url).hostname or ''
        if not title or not url.startswith('https://') or not (host == 'zarirmadon.substack.com' or host.endswith('.zarirmadon.substack.com')):
            continue
        raw = read_text(node, 'description') or read_text(node, '{http://purl.org/rss/1.0/modules/content/}encoded')
        parsed = Extract()
        parsed.feed(raw)
        plain = re.sub(r'\s+', ' ', html.unescape(''.join(parsed.text))).strip()
        if len(plain) > 320:
            plain = plain[:317].rsplit(' ', 1)[0] + '…'
        image = None
        enclosure = node.find('enclosure')
        if enclosure is not None and enclosure.attrib.get('type','').startswith('image/'):
            image = enclosure.attrib.get('url')
        if not image:
            for child in node:
                if child.tag.endswith('thumbnail') or child.tag.endswith('content'):
                    candidate = child.attrib.get('url', '')
                    if candidate.startswith('https://') and (child.tag.endswith('thumbnail') or child.attrib.get('medium') == 'image'):
                        image = candidate
                        break
        image = image or parsed.image or ''
        if not image.startswith('https://'):
            image = ''
        published = read_text(node, 'pubDate')
        try:
            date = email.utils.parsedate_to_datetime(published).astimezone(timezone.utc).isoformat()
        except (TypeError, ValueError, OverflowError):
            date = ''
        items.append({'title':title,'url':url,'date':date,'excerpt':plain,'image':image})
    if not items:
        raise RuntimeError('Feed returned zero usable articles. Keeping the existing posts.json unchanged.')
    items.sort(key=lambda x:x['date'], reverse=True)
    payload = {'source':FEED,'updated':datetime.now(timezone.utc).isoformat(),'posts':items}
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'Indexed {len(items)} articles into {OUTPUT.name}')

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(f'Feed update failed: {exc}', file=sys.stderr)
        sys.exit(1)
