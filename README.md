Here is the exact, forensic breakdown of the site’s DNA, ready for you to weaponize in any AI code generator.
1. The Style & Format: What to Call It
This isn’t just a website; it’s a Dark Mode Neo-Brutalist Editorial Portfolio.
It smashes together the raw, unapologetic grid structures of brutalism with the refined, high-contrast typography of a contemporary art magazine. It’s got that precise geometric design energy you love, treating the browser window like a darkroom canvas where photography, code, and digital experimentation collide.
The Format: A Single-Page Application (SPA) Digital Lookbook. It’s a continuous, long-scrolling narrative divided into asymmetric CSS Grid sections. No clunky page reloads, no bloated frameworks—just pure, antialiased, open-source-friendly rendering.
2. The Typographic Trinity (Exact Fonts Rendered)
I pulled the actual @import rules from the site’s stylesheet. The designer didn’t guess; they engineered a perfect three-font stack:
Unbounded (Weights: 600, 800, 900)
The Heavy Hitter. Used for massive display headlines. It’s wide, bold, and feels like it was designed in a quantum physics lab.
Space Grotesk (Weights: 400, 500, 600, 700)
The Workhorse. Mapped to the --sans variable. Used for body text, UI, and metadata. It’s a geometric sans-serif with just enough quirky, open-source charm to keep things from feeling corporate.
Instrument Serif (Styles: Regular, Italic)
The Elegant Disruptor. Mapped to --serif. Used for italicized accents (like “things” or “works”). It injects that classic, museum-quality fine art contrast right into the middle of the digital brutalism.
3. The "Holy Grail" AI Prompt
If you are feeding this to v0.dev, Cursor, Lovable, or Webflow AI, do not hold back. Copy and paste this exact prompt. It’s engineered to bypass generic AI slop and force the precise aesthetic:
Prompt:
"Build a single-page, dark-mode contemporary digital art portfolio. The aesthetic is 'Neo-Brutalist Editorial' meets 'High-End Digital Gallery'.
Typography Rules (Strict):
Import and use exactly these three Google Fonts:
'Unbounded' (weights 600, 800, 900) for massive display headlines.
'Space Grotesk' (weights 400-700) for all body text, UI, and metadata.
'Instrument Serif' (italic) for selective, elegant word-level emphasis within headings.
Color Palette (Strict CSS Variables):
Background: #0a0814 (Deep void purple/black)
Primary Text: #f7f3ec (Warm off-white/cream)
Muted Text: #a39fb5 (Soft lavender-gray)
Accents (use sparingly for hover states or thin geometric lines): Hot Pink #ff3d7f, Electric Yellow #ffd21f, Mint #1fd9a0.
Layout & Vibe:
Use CSS Grid and Flexbox for an asymmetric, magazine-style layout. Abundant negative space. Intentional typographic play (e.g., mashing words together like 'Seethingsagain.' or splitting words across lines). Smooth, subtle hover transitions (no bouncy, cartoonish animations). The site should feel like a photographer’s darkroom met a Linux terminal and decided to open a contemporary art gallery. No drop shadows, no rounded bubbly buttons, no generic Bootstrap vibes."
4. The Code Blueprint (Attach This!)
Instructions alone sometimes make AI hallucinate generic Tailwind templates. Attach this raw HTML/CSS skeleton to your prompt. It contains the exact CSS variables and font imports from the live site, forcing the AI to build on the correct foundation.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Digital Perspective</title>
  <!-- EXACT FONT IMPORTS FROM THE LIVE SITE -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Space+Grotesk:wght@400;500;600;700&family=Unbounded:wght@600;800;900&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg: #0a0814;
      --ink: #f7f3ec;
      --muted: #a39fb5;
      --accent-pink: #ff3d7f;
      --display: 'Unbounded', sans-serif;
      --sans: 'Space Grotesk', sans-serif;
      --serif: 'Instrument Serif', serif;
      --line: rgba(247, 243, 236, 0.14);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background: var(--bg);
      color: var(--ink);
      font-family: var(--sans);
      -webkit-font-smoothing: antialiased;
      line-height: 1.5;
      overflow-x: hidden;
    }

    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 2rem;
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 1.5rem;
    }

    /* Typography Utilities */
    .display { font-family: var(--display); font-weight: 800; line-height: 0.95; letter-spacing: -0.03em; }
    .serif-italic { font-family: var(--serif); font-style: italic; font-weight: 400; }
    .mono-meta { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--muted); }

    /* Layout Blocks */
    header { grid-column: 1 / -1; display: flex; justify-content: space-between; align-items: center; padding: 1rem 0 4rem; border-bottom: 1px solid var(--line); }
    .hero { grid-column: 1 / 9; padding: 4rem 0; }
    .hero h1 { font-size: clamp(2.5rem, 6vw, 5rem); margin-bottom: 1.5rem; }
    
    .section-title { grid-column: 1 / -1; padding: 4rem 0 2rem; border-top: 1px solid var(--line); margin-top: 2rem; }
    
    .work-grid { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
    .work-item { padding: 1.5rem 0; border-bottom: 1px solid var(--line); transition: color 0.3s ease; cursor: pointer; }
    .work-item:hover { color: var(--accent-pink); }
    .work-item:hover .serif-italic { text-decoration: underline; }

    footer { grid-column: 1 / -1; padding: 4rem 0; display: flex; justify-content: space-between; border-top: 1px solid var(--line); margin-top: 4rem; }
  </style>
</head>
<body>

  <div class="container">
    <header>
      <span class="mono-meta">Zarir Madon · Artist / Digital Creator</span>
      <nav class="mono-meta" style="display: flex; gap: 2rem;">
        <a href="#work" style="color: var(--ink); text-decoration: none;">Work</a>
        <a href="#about" style="color: var(--ink); text-decoration: none;">About</a>
        <a href="#shop" style="color: var(--ink); text-decoration: none;">Shop</a>
      </nav>
    </header>

    <section class="hero">
      <p class="mono-meta" style="margin-bottom: 1rem;">Changetheview.</p>
      <h1 class="display">
        The Digital Perspective explores the space between art, photography, and <span class="serif-italic">digital imagination</span>.
      </h1>
    </section>

    <section class="section-title">
      <h2 class="display" style="font-size: 3rem;">See <span class="serif-italic">things</span> again.</h2>
    </section>

    <section id="work" class="work-grid">
      <div class="work-item">
        <span class="mono-meta">01 / Chromatic Geometry</span>
        <h3 class="display" style="font-size: 1.5rem; margin-top: 0.5rem;">Fault <span class="serif-italic">Line</span></h3>
      </div>
      <div class="work-item">
        <span class="mono-meta">02 / Digital Alchemy</span>
        <h3 class="display" style="font-size: 1.5rem; margin-top: 0.5rem;">After<span class="serif-italic">image</span></h3>
      </div>
      <div class="work-item">
        <span class="mono-meta">03 / Dream States</span>
        <h3 class="display" style="font-size: 1.5rem; margin-top: 0.5rem;">Other <span class="serif-italic">Weather</span></h3>
      </div>
    </section>

    <footer>
      <span class="mono-meta">© 2026 The Digital Perspective</span>
      <span class="mono-meta">Aotearoa / New Zealand</span>
    </footer>
  </div>

</body>
</html>

Why This Combo is Unbeatable:
By feeding the AI both the conceptual prompt and this exact CSS skeleton, you eliminate the "AI guesswork" phase. It won’t try to give you a generic white SaaS landing page. It will immediately lock into the deep void background, the Unbounded/Space Grotesk/Instrument Serif trifecta, and the sharp, geometric, open-source-friendly layout you’re after.
