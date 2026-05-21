---
name: TheWizardly Theme — All-Night Pavilion (SEED)
description: A Hugo theme for thewizardly.com. The All-Night Pavilion: sincere atompunk in a dark room, lit by drafting lamp and marquee bulb, where the wizard is awake while the world sleeps and holds the candle for tomorrow.
---

<!-- SEED: re-run /impeccable document once the EPCOT-Dreamer redesign is implemented, to capture the real tokens, exact OKLCH values, font choices, and component snippets. The previous Wizard's Workbench DESIGN.md is preserved in git history and is being deliberately replaced. -->

# Design System: TheWizardly Theme — All-Night Pavilion

## 1. Overview

**Creative North Star: "The All-Night Pavilion"**

A drafting lamp burns in the upper window of the wizard's tower. Inside, a model city hums under starlight on a long oak table — half-built, alive, faithfully detailed, glowing. Brass marquee bulbs trace a path between the exhibits. A planetarium projector throws constellations on the dome above. The wizard is awake while the world sleeps, holding the candle for tomorrow.

This system is sincere atompunk in a dark room. Drenched in night-shift atmosphere — every surface in scene — with light arriving only from sources you can name: a desk lamp, a CRT, a marquee bulb, a planetarium projector, a single REC light on a console. The room is dark because the wizard is on the late shift, not because the world is grim. There is no gothic gloom and no ambient gradient slop. Decoration is committed and sincere — full-body, no smirk, no remove. The wizardly voice in copy carries the bit; the visuals carry the era. *We play. We dream.*

The kin we stand beside (never quoted, never named in site copy, named freely in this internal document for designer reference): the unbuilt 1966 EPCOT plan documents, the 1964 World's Fair pavilion brochures, the Eames studio's filmstrips and book design (*Powers of Ten*, *Mathematica*), the Hayden Planetarium of the early sixties, the Whole Earth Catalog, and the mid-century children's encyclopedias of *How Things Work*. Sincere wonder, careful design, hopeful engineering — the posture is inherited, the iconography is not.

This system explicitly rejects AI-rendered chrome-rocket atompunk gloss, generic Jetsons cartoon retrofuture, Mad Men corporate restraint, direct Disney / EPCOT / Imagineer branding marks, crypto-bro techno-optimism hype, modern SaaS / Substack templates, goth-metal mysticism, and ironic Web 2.0 nostalgia bait.

**Key Characteristics:**
- A warm-led, night-shift midnight surface lit only by named physical light sources
- Drafting-Lamp Amber as the dominant warm accent; Atomic Turquoise as the cool counter; one rare REC-light red as the signal pigment
- Marquee-Bulb Cream body type — warmer than parchment-cream, less yellow than ivory
- A faint starfield texture, not a gradient, sitting under the body
- An atompunk display serif paired with Atkinson Hyperlegible Next body — editorial, sincere, sit-down-with-a-book wonder
- 88×31 web buttons preserved at native pixel resolution, no filter, no scaling
- A Marquee Initial replacing the medieval Drop Cap on essay-form posts: a glowing letterform opening each essay like a marquee bulb-letter
- Soft amber glow on the masthead and on link hover; nowhere else
- Trinkets (Mystic Missives, Allied Mages, Enchanted Emblems, Reading Pavilion, Random Incantations) preserved as load-bearing architecture, re-bodied for the new room

## 2. Colors

A warm-led night-shift palette: a deep midnight surface lit by drafting-lamp amber, with one cool counter (atomic turquoise), one rare signal pigment (REC-light red), and a single warm body-text color carrying every word. Exact OKLCH values to be resolved during implementation; what follows is the intent and the named rules.

### Primary
- **Drafting-Lamp Amber** `[OKLCH to be resolved at implementation]`: The dominant warm accent. Carries link affordance, ornament glows, marquee details, the warm side of typography. Reads as a 60-watt incandescent bulb seen through paper; never as electric sodium-vapor yellow. Mid-range chroma, warm hue, lightness tuned to pass WCAG 2.2 AA on Night-Shift Midnight.

### Secondary
- **Atomic Turquoise** `[OKLCH to be resolved at implementation]`: The cool counter. Carries hover states on certain surfaces, ornamental linework, the "tomorrow shimmer" on slide-tray transitions and planetarium-style ornaments. Used sparingly and intentionally — turquoise should punctuate, never flood-fill.

### Tertiary
- **Now-Broadcasting Red** `[OKLCH to be resolved at implementation]`: The rare signal accent. Carries `<strong>` emphasis, the timestamp icon, the response-tag pill, and the "live" indicator on the status feed. Used like a REC light: ≤1% of any screen. Never a button background, never a border, never a section divider. The wax-seal pigment from the previous design's vocabulary, reincarnated as the console's recording lamp.

### Neutral
- **Night-Shift Midnight** `[OKLCH to be resolved at implementation]`: Body background. Deep planetarium navy, tuned faintly warmer than the previous inkwell-midnight so the room reads "drafting room at night" rather than "wizard's study." A starfield texture overlays at low opacity (4–8%); the constellation is not random — see the Named Starfield Rule below.
- **Marquee-Bulb Cream** `[OKLCH to be resolved at implementation]`: All body text on every surface. Warmer than the previous parchment-cream; less yellow than ivory. The page itself.
- **Brass Linework** `[OKLCH to be resolved at implementation]`: Structural color for dividers, ornamental separators, low-emphasis rules. Desaturated copper. Used for the rules under section titles, between status entries, and around the bookshelf year groupings.
- **Exhibit-Card Deep** `[OKLCH to be resolved at implementation]`: Card and pavilion-display background, slightly deeper than the body surface so cards read as nested pages rather than raised UI. Likely Night-Shift Midnight at ~85% opacity, exact ratio TBD.

### Named Rules

**The Drenched Rule.** Every surface — masthead, post card, pavilion display, footer arcade — sits in the night-shift scene. There is no escape hatch to a clean Substack-grey card. The page itself commits. If a future component feels like it wants to "step outside the room for clarity," the component has the wrong shape, not the room.

**The Named-Light Rule.** Light comes from sources you can name. A desk lamp. A CRT. A marquee bulb. A planetarium projector. A REC light on a console. If a glow doesn't have a clear physical analogue, it isn't earned and shouldn't be in the design. Ambient gradients with no source are the AI-atompunk-slop tell.

**The One-REC-Light Rule.** Now-Broadcasting Red signs one thing on a surface, then disappears. Timestamp icon, `<strong>`, response-tag, page-number, "live" indicator — pick the one that's signing this surface. Three reds visible at once means two are wrong.

**The Tinted-Black Rule (preserved from Wizard's Workbench).** Pure `#000` and pure `#fff` are forbidden. Night-Shift Midnight carries the cool-blue cast of the body surface; Marquee-Bulb Cream carries the warm-incandescent cast of the text. Even rgba shadows over the body should be tinted toward warm-shadow, not toward absolute black.

**The Three-Pigment-Plus-One Rule.** Drafting-Lamp Amber, Atomic Turquoise, Brass Linework — those are the accent and structural pigments. Now-Broadcasting Red is the rare signal layered on top. No new accent hues without explicit approval. Reaching for green, purple, or magenta is the sign the design has drifted off-brand.

**The Named-Starfield Rule.** The starfield texture under the body is a real, identifiable, low-density star map (a constellation, a sliver of the southern Milky Way, a recognizable star pattern). It is not random pixel noise. The exact star pattern is a designer choice; that it is *a real sky* and not a generated one is the rule.

## 3. Typography

**Display Font:** An atompunk editorial display serif `[exact face to be chosen at implementation — direction: Recoleta / Reckless Neue / DM Serif Display / similar — warm, mid-century-encyclopedia energy, not Futura-style geometric sans]`
**Body Font:** Atkinson Hyperlegible Next (sans-serif fallback)
**Mono Font:** Atkinson Hyperlegible Mono (monospace fallback)
**Marquee/Ornament Variant:** The italic of the display face, or a complementary display-italic with bulb-spaced warmth `[to be chosen at implementation]`

**Character:** The display face carries the EPCOT-Dreamer optimism — a sit-down-with-a-book editorial serif with mid-century warmth, the kind of letterform that lived on a 1962 children's encyclopedia spine or a 1964 World's Fair brochure cover. Atkinson Hyperlegible Next remains untouched on body, doing the actual work of carrying every word a reader reads. The pairing is intentionally unequal: the display decorates; the body works. Marquee moments — the masthead title and the Marquee Initial on essays — borrow the display face at extreme size, dressed in amber glow.

### Hierarchy
- **Display** (`[display serif]` 400, ~3rem desktop / ~2.5rem ≤768px, line-height 1.2): The masthead. The site title under starlight, glowing softly in Drafting-Lamp Amber via the Marquee Glow.
- **Headline** (`[display serif]` 400, ~2rem, line-height 1.25): h2. Section dividers within a post. Brass Linework rule beneath, 1px solid at ~30% opacity.
- **Title** (`[display serif]` 400, ~1.5rem, line-height 1.3): h3. Sub-section headings within long posts. Drafting-Lamp Amber.
- **Body** (Atkinson Hyperlegible Next 400, 1rem, line-height 1.6): All paragraph text on Marquee-Bulb Cream. Cap line length at the 14/24 PureCSS column (~65–75ch) on desktop.
- **Body Large** (Atkinson Hyperlegible Next 400, ~1.2rem, line-height 1.6): The masthead tagline paragraph and any pull-quote treatment.
- **Label** (Atkinson Hyperlegible Next 400, 0.8rem): Sigil pills, status time, response-tag pills, pagination tertiary copy.
- **Mono** (Atkinson Hyperlegible Mono 400, 0.9rem, line-height 1.5): All inline code and code blocks.
- **Ornament** (`[display serif italic]` 400, ~1.1rem): The Arcane Timestamp, pavilion-display titles, status time, pagination "Scroll N of M." Brass Linework or Drafting-Lamp Amber depending on context.
- **Marquee Initial** (`[display serif]` 400, ~4em, line-height 0.8): The first letter of titled-essay bodies, in Drafting-Lamp Amber, floated left for a clean 2-line drop, with a soft Marquee Glow. Skipped on titleless microposts. Replaces the previous medieval-manuscript Drop Cap; same lockup math, different cultural reference.

### Named Rules

**The Hyperlegible Body Rule (preserved).** Atkinson Hyperlegible Next is the body face. Non-negotiable. The display face never carries paragraph text, button labels, form input text, or anything a reader reads in volume. If a heading has more than ~10 words, it stops being decorative and the choice should be reconsidered.

**The Marquee Glow Rule.** Soft Drafting-Lamp Amber text-shadow is reserved for the masthead h1, the Marquee Initial on essay posts, and link hover. Glow has a physical analogue (the marquee bulb, the desk-lamp halo, the candle catching a wet edge of ink) — it is never decoration without that anchor. Glow does not appear on h2, h3, body text, sigil pills, or buttons.

**The Three-Knobs Rule (preserved from Wizard's Workbench).** A floated Marquee Initial reserves vertical space equal to `cap font-size × cap line-height`; for a clean N-line drop, that product must equal `N × body line-height`. The previous design's 4em × 0.8 = 2 × 1.6em lockup is a working starting point. If body line-height changes, recompute Marquee Initial line-height to preserve the equation.

**The No-Geometric-Sans-Display Rule.** The display direction is editorial serif, not mid-century geometric sans. Futura, Avenir, and similar are the canonical atompunk choices and exactly for that reason they are *not* the choice here. The All-Night Pavilion reads warmer and more sincere than the geometric-sans atompunk house style; the serif carries that difference.

## 4. Elevation

Mostly flat with two atmospheric registers. Cards rest on the Night-Shift Midnight surface via a single warm-tinted drop shadow — the shadow a paper exhibit-card would cast on a varnished oak table under a drafting lamp. Glow is reserved for the wizardly flourish: the masthead, the Marquee Initial, and link hover. No surface lifts on hover; the room is calm by default. Motion energy is Responsive (state feedback and transitions only); choreographed entrances and scroll-driven sequences are out.

### Shadow Vocabulary

- **Exhibit Rest** (`box-shadow: 0 10px 30px rgba(<warm-tinted-shadow>, 0.3)`): The default shadow under every Exhibit Card and Pavilion Display. Diffuse, warm-tinted (toward Drafting-Lamp Amber, not toward black), low-contrast against the night-shift surface. Reads as paper resting on oak under a drafting lamp.
- **Trinket Hover Halo** (`box-shadow: 0 3px 8px rgba(<accent>, 0.2)`): A small colored hover halo under sigil pills, response-tag pills, status-link pills, and book covers. The accent matches the trinket's own pigment (Drafting-Lamp Amber for warm trinkets, Atomic Turquoise for cool trinkets, Now-Broadcasting Red only for explicitly "live" affordances).
- **Marquee Glow** (`text-shadow: 0 0 12px rgba(<drafting-lamp-amber>, 0.4)`): The masthead h1 and Marquee Initials. Always-on, low intensity, atmospheric. Reads as a bulb seen through a paper letterform.
- **Link Hover Glow** (`text-shadow: 0 0 10px rgba(<drafting-lamp-amber>, 0.5)`): A brief amber glow under hovered links, slightly stronger than Marquee Glow, present only while hovered.

### Named Rules

**The Page-Not-Button Rule (preserved).** Exhibit Cards do not lift on hover. A card is a resting paper exhibit; interactive feedback lives elsewhere. The Exhibit Rest shadow is a "paper on oak" cue, not a "click me" cue. It does not animate, intensify, or change on hover.

**The Earned-Glow Rule.** Glow has an explicit, namable physical source. The masthead glows like a marquee letter under bulbs. The Marquee Initial glows like a planetarium-show title slide. Links glow briefly like a candle catching a wet edge of ink. Nothing glows decoratively without a named physical analogue.

**The Hover-Halo Rule (preserved).** Trinket hover halos use `0 3px 8px rgba(<accent>, 0.2)` and tint the halo to the trinket's own accent. They do not exceed 8px blur, do not cast more than 3px down, and do not exceed 0.2 opacity. Hover is a whisper.

## 5. Components

`[Seed: no implemented components yet. Component identity intent is captured below as a target for implementation; full token specs (radii, exact paddings, exact shadows, focus rings) will be filled in by a scan-mode pass after the redesign lands.]`

Component identity from the All-Night Pavilion brief:

- **Exhibit Cards** (formerly Cards): paper exhibits resting on oak. Same load-bearing role as the previous design's cards; warmer shadow, no spine, an opportunity for a marquee-style header strip if it earns it.
- **Pavilion Displays** (formerly Side Content): small exhibit cases on a model fairground, stacked down the right column. Each holds a named trinket category.
- **Sigil Pills** (formerly Tag Pills): two species — subject-tag (Drafting-Lamp Amber or Brass Linework on warm tint) and response-tag (Now-Broadcasting Red on red tint). Pill shape preserved.
- **Marquee Initial** (replaces Illuminated Drop Cap): a glowing display-serif capital opening an essay's first paragraph, floated left in a clean 2-line drop. Skipped on titleless microposts. Same lockup math as the previous Drop Cap.
- **Arcane Timestamp** (preserved in concept and copy): the `Inscribed on <date>` dateline inside every post card. The "wax seal" icon-and-pigment becomes the REC-light Now-Broadcasting Red, marking the timestamp like a console's recording lamp.
- **Slide Tray Counter** (formerly Pagination): three-column layout (previous, page counter, next), with the counter numerals in Now-Broadcasting Red and the arrows in Drafting-Lamp Amber.
- **Reading Pavilion** (formerly Bookshelf): a grid of book-cover thumbnails grouped by year-of-departure. Card-rest shadow on each cover, gentle hover-halo, no card-lift.
- **Mystic Missives** (Status Feed, name preserved): a Pavilion Display rendering the most recent statuses from omg.lol. "Transmissions on the wire" visual treatment; entries separated by Brass Linework rules at low opacity.
- **Allied Mages** (Blogroll, name preserved): the Network of Fellow Dreamers, as a Pavilion Display. Each entry an outbound link to another wizard's site.
- **Enchanted Emblems** (Web Button Collection, name preserved): a flexbox wrap of 88×31 indie-web buttons at native pixel resolution. Untouched by CSS effects: no filter, no scaling, no border. They render exactly as their authors made them.
- **Random Incantations** (Random Posts list): a Pavilion Display offering the reader a curated jump to elsewhere in the archive.
- **Links**: Drafting-Lamp Amber text, 1px dotted Amber underline at rest. On hover: underline becomes 1px solid Amber; Link Hover Glow appears. No decorative underlines on non-links.
- **Blockquote**: 3px Brass Linework left-stripe, italic body type, slight desaturation against the Exhibit Card background.
- **Code (inline + block)**: low-opacity wash of Brass Linework on the Exhibit Card surface as background; 3px Drafting-Lamp Amber left-stripe on block code (preserved syntax-highlighter convention); Atkinson Hyperlegible Mono throughout.

## 6. Do's and Don'ts

### Do

- **Do** keep Atkinson Hyperlegible Next as the body face on every screen. Decorative atmosphere is allowed in headings, ornaments, and the Marquee Initial — never in paragraph text or form-input text.
- **Do** verify every accent pigment against Night-Shift Midnight for WCAG 2.2 AA. Nudge lightness, not chroma, when contrast falls short.
- **Do** anchor every glow to a named physical light source: a desk lamp, a CRT, a marquee bulb, a planetarium projector, a REC light, a candle catching a wet edge. If you can't name the source, the glow isn't earned.
- **Do** treat the 88×31 web buttons as sincere indie-web participation. Display at native pixel resolution. Never filter, restyle, scale, or apply CSS effects.
- **Do** use the wizardly nomenclature in copy ("Inscribed on", "Mystic Missives", "Allied Mages", "Enchanted Emblems", "Teleportation Circle", "Random Incantations"). The voice carries the wizard while the visuals carry the era.
- **Do** retune the Marquee Initial's line-height alongside any change to its font-size or body line-height. The Three-Knobs Rule is non-negotiable.
- **Do** gate any planetarium-style rotation, slide-tray reveal, marquee-glow flicker, or starfield-shimmer animation behind `prefers-reduced-motion: no-preference`. The night shift is calm by default.
- **Do** show visible focus rings on every interactive trinket (web buttons, blogroll links, status feed entries, sigil pills, pagination, book covers, Marquee Initial if it is itself a link). Focus is distinct from hover.
- **Do** treat trinkets (Mystic Missives, Allied Mages, Enchanted Emblems, Reading Pavilion, Random Incantations) as load-bearing architecture. The site does the indie-web job of pointing outward; every trinket is evidence that other people are also dreaming.

### Don't

- **Don't** render fake chrome bezels, fake brushed-metal gradients, rendered-3D rocket fins, or fluorescent vector starbursts. The AI-rendered chrome-rocket atompunk slop pile is the closest first-order failure mode and we are not it.
- **Don't** lean toward generic Jetsons / Saturday-morning cartoon retrofuture: saturated primaries on cartoon curves, exaggerated UFO shapes, ironic-mascot atompunk. The wizard isn't a Hanna-Barbera character.
- **Don't** invoke Disney / EPCOT / Imagineer references in copy or visuals. No Mickey, no Sorcerer's-hat icon, no Tomorrowland callouts, no Carousel-of-Progress glyphs. We stand beside Walt; we never invoke him by name.
- **Don't** drift toward Mad Men corporate mid-century restraint: olive-green-and-Helvetica ad-agency cool. Atompunk here is a person's pavilion, not an expense account.
- **Don't** apply crypto-bro / SV techno-optimism hype: "We're so back" neon manifesto type, NFT-rocket emoji, beanie-vector founder energy. The optimism here is sincere, slow-burning, built — not pumped.
- **Don't** let the site look like a modern SaaS / Substack template (white sans-serif blog with subscribe CTA, author bio card, Medium scroll-optimized layout).
- **Don't** drift toward goth / metal mysticism (pitch black, blood red, occult sigils, blackletter, edgelord posturing).
- **Don't** wear ironic Web 2.0 nostalgia bait (Comic Sans, animated-GIF chaos as meme costume, "old web" worn ironically). The 88×31 web buttons here are sincere indie-web participation, not pastiche.
- **Don't** reach for Futura, Avenir, or similar mid-century geometric sans for the display face. They are the canonical atompunk default and exactly for that reason they are off-limits here. The All-Night Pavilion is editorial-serif territory.
- **Don't** add side-stripe borders ≥1px to new components. The two legitimate exceptions from the previous design are preserved: the 3px Brass Linework stripe on blockquote (a print typography convention) and the 3px Drafting-Lamp Amber stripe on code blocks (a syntax-highlighter convention). Cards have no spine; their identity is carried by the Marquee Initial and the Arcane Timestamp.
- **Don't** use gradient text (`background-clip: text` over a gradient). Emphasis is via weight, size, or pigment, never gradient.
- **Don't** use `#000` or `#fff` anywhere. Night-Shift Midnight and Marquee-Bulb Cream are the bounds of the value scale.
- **Don't** flood-fill with Drafting-Lamp Amber or Atomic Turquoise. They are voices; they do not become walls. No solid amber button backgrounds, no turquoise hero panels, no full-bleed accent bands.
- **Don't** use Now-Broadcasting Red as a background, button, border, or section divider. One REC light per surface, maximum.
- **Don't** add modals as a first thought. Inline disclosure, expanding cards, or a follow-up post are usually the better answer for a personal site.
- **Don't** apply glow to body text, h2, h3, sigil pills, or buttons. Glow lives on the masthead h1, the Marquee Initial, and link hover — nowhere else.
- **Don't** animate layout properties. If motion is added, animate `transform` and `opacity` only, with ease-out exponential curves, gated behind `prefers-reduced-motion`.
- **Don't** lift Exhibit Cards on hover. Cards are resting paper exhibits.
- **Don't** filter, restyle, or scale the 88×31 web buttons. They render at native pixel size and look like what they are.
- **Don't** generate a random-noise starfield. The Night-Shift Midnight starfield is a real, identifiable star pattern — a recognizable sky, a real constellation, a real slice of the Milky Way. A procedural pixel-noise field is the AI-atompunk-slop tell.
