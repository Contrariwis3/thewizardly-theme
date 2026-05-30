---
name: TheWizardly Theme — All-Night Pavilion
description: A Hugo theme for thewizardly.com. The All-Night Pavilion: sincere atompunk in a dark room, lit by drafting lamp and marquee bulb, where the wizard is awake while the world sleeps and holds the candle for tomorrow.
colors:
  night-shift-midnight: "oklch(32.6% 0.036 239.8)"
  exhibit-card-deep: "oklch(28% 0.034 240)"
  drafting-lamp-amber: "oklch(80.5% 0.138 75.9)"
  atomic-turquoise: "oklch(76.4% 0.094 180.5)"
  now-broadcasting-red: "oklch(65.5% 0.115 33.8)"
  brass-linework: "oklch(75.7% 0.040 79.9)"
  marquee-bulb-cream: "oklch(94.6% 0.018 78.2)"
typography:
  display:
    fontFamily: "'Bona Nova', serif"
    fontSize: "clamp(2.8rem, 8vw, 5rem)"
    fontWeight: 400
    lineHeight: 1.06
  headline:
    fontFamily: "'Bona Nova', serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1.25
  title:
    fontFamily: "'Bona Nova', serif"
    fontSize: "1.5rem"
    fontWeight: 400
    lineHeight: 1.3
  body:
    fontFamily: "'Atkinson Hyperlegible Next', sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "'Atkinson Hyperlegible Next', sans-serif"
    fontSize: "0.8rem"
    fontWeight: 400
  mono:
    fontFamily: "'Atkinson Hyperlegible Mono', monospace"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.5
rounded:
  small: "4px"
  medium: "8px"
spacing:
  xs: "3px"
  sm: "5px"
  md: "10px"
  lg: "15px"
  xl: "20px"
  xxl: "30px"
  xxxl: "40px"
components:
  exhibit-card:
    backgroundColor: "{colors.exhibit-card-deep}"
    rounded: "{rounded.medium}"
    padding: "30px"
  pavilion-display:
    backgroundColor: "{colors.exhibit-card-deep}"
    rounded: "{rounded.medium}"
    padding: "20px"
  link:
    textColor: "{colors.drafting-lamp-amber}"
  tag-sigil:
    textColor: "{colors.brass-linework}"
  fixture-title:
    textColor: "{colors.drafting-lamp-amber}"
  arcane-timestamp:
    textColor: "{colors.brass-linework}"
  pagination-page:
    textColor: "{colors.now-broadcasting-red}"
  book-cover:
    rounded: "{rounded.small}"
---

<!-- Documented in scan mode (FJ#4 Increment 6) from the shipped All-Night Pavilion implementation in frontend/sass/main.scss — real compiled tokens (palette, type scale, spacing, radii, shadows, focus rings) and real component specs. Palette, faces, and starfield were resolved per the closed #1/#2/#3 decisions; the previous Wizard's Workbench DESIGN.md is preserved in git history and was deliberately replaced. Frontmatter carries OKLCH, the project's canonical color space (Stitch's linter prefers hex sRGB and will warn; this is the accepted OKLCH-doctrine path) — the §2 table pairs each token with its sRGB source value. -->
<!-- Palette source: cross-bred from two Color Cube cards — surface, counter, signal, and a warm-light from card 689; the amber lead and brass-linework neutral from card 589. The cards donated a scheme; the names here are ours. -->
<!-- The deep bench (secondary tier, structural / fill / large-accent only, not primary roles): filament-glow #fbbf98, banked-ember #7c4c49, kiln-rust #8b4021, deep-dome-teal #018990, drafting-shadow #393631, walnut #4e3123. Documented in §2 prose; promoted to frontmatter only if/when implementation actually reuses them. -->

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

A warm-led night-shift palette: warm accents glowing against a cool night-navy ground. Drafting-Lamp Amber leads; Atomic Turquoise is the cool counter; Now-Broadcasting Red is the rare signal; a warm near-white cream carries every word. The palette is locked below (cross-bred from two donated Color Cube schemes), now resolved to OKLCH — the canonical target — with the sRGB hex retained as the source value. WCAG 2.2 AA ratios are computed against Night-Shift Midnight (`#233745`); the resolved tokens and their verified contrast are tabled here.

| Token | sRGB | OKLCH | Contrast on surface |
|---|---|---|---|
| Night-Shift Midnight | `#233745` | `oklch(32.6% 0.036 239.8)` | surface |
| Drafting-Lamp Amber | `#f2b24c` | `oklch(80.5% 0.138 75.9)` | 6.60:1 — AA body |
| Atomic Turquoise | `#68c6b5` | `oklch(76.4% 0.094 180.5)` | 6.06:1 — AA body |
| Now-Broadcasting Red | `#cd7561` | `oklch(65.5% 0.115 33.8)` | 3.71:1 — AA large/UI only |
| Brass Linework | `#beae94` | `oklch(75.7% 0.040 79.9)` | 5.68:1 — AA body |
| Marquee-Bulb Cream | `#f4ece0` | `oklch(94.6% 0.018 78.2)` | 10.52:1 — AAA |
| Exhibit-Card Deep | `#1c2d39` | `oklch(28% 0.034 240)` | card surface (cool-on-cool) |

The Deep Bench converts on the same basis; its four fill-only pigments fail body contrast by design (they are never text). The round-trip preserved every AA result — no lightness nudges were required.

### Primary
- **Drafting-Lamp Amber** (`#f2b24c`): The dominant warm accent. Carries link affordance, ornament glows, marquee details, the warm side of typography. Reads as a 60-watt incandescent bulb seen through paper; never as electric sodium-vapor yellow. Contrast on Night-Shift Midnight ≈ 6.5:1 — passes AA for body and large text, so amber links and emphasis are crisp.

### Secondary
- **Atomic Turquoise** (`#68c6b5`): The cool counter. Carries hover states on certain surfaces, ornamental linework, the "tomorrow shimmer" on slide-tray transitions and planetarium-style ornaments. Used sparingly and intentionally — turquoise should punctuate, never flood-fill. Contrast ≈ 6.0:1 — passes AA for body and large text. (Chosen over the deeper Deep-Dome-Teal `#018990`, which lands at ≈ 2.9:1 and is therefore large-ornament-only.)

### Tertiary
- **Now-Broadcasting Red** (`#cd7561`): The rare signal accent. Reads as a glowing neon tube. Contrast ≈ 3.6:1 — **passes AA for large text and UI/icon contexts, fails for body-size text.** Therefore it carries the timestamp icon, the page-number numerals, and the "live" indicator (all large/UI), but **not** inline `<strong>` at body size — inline emphasis uses font weight (with Drafting-Lamp Amber where a color is wanted). Used like a REC light: ≤1% of any screen. Never a button background, never a border, never a section divider.

### Neutral
- **Night-Shift Midnight** (`#233745`): Body background. A deep planetarium-navy with a cool blue cast. A starfield texture overlays at low opacity (4–8%); the constellation is not random — see The Named-Starfield Rule below.
- **Marquee-Bulb Cream** (`#f4ece0` = `oklch(94.6% 0.018 78.2)`, locked): All body text on every surface. A warm near-white — warmer than ivory, well clear of the AA floor (10.52:1 on the surface). Not on either donor card by design — body-on-dark wants a sourced near-white, not a saturated tan.
- **Brass Linework** (`#beae94`): Structural color for dividers, ornamental separators, low-emphasis rules, and muted metadata text. A desaturated greige-brass. Contrast ≈ 5.6:1 — passes AA for body, so it doubles as a legible muted-metadata text color. Used for the rules under section titles, between status entries, and around the bookshelf year groupings.
- **Exhibit-Card Deep**: Card and pavilion-display background, a shade off the body so cards read as nested pages rather than raised UI. Resolved to `oklch(28% 0.034 240)` ≈ `#1c2d39`: Night-Shift Midnight's hue and chroma held, lightness dropped ~4.5 points so the card reads as a recessed exhibit case, kept cool-on-cool. Do **not** use the warm-dark bench colors (Drafting-Shadow, Walnut) here; a warm-brown card on the cool navy body clashes.

### The Deep Bench (secondary tier — structural, fill, or large-accent only)

These pigments are decided and available but are **not** primary roles. They do not get used as accent voices; reaching for them as a fifth and sixth "accent color" is off-brand. Promote to frontmatter only when implementation actually reuses one.

- **Filament Glow** (`#fbbf98`): A light warm peach, ≈ 7.5:1. The halo of a lit bulb. Soft secondary warm, glow tint, hover wash.
- **Banked Ember** (`#7c4c49`): A muted deep maroon, text-fails on the surface. Structural fill only — blockquote bar, a deep warm panel.
- **Kiln Rust** (`#8b4021`): A deep rust, text-fails on the surface. Structural fill only — code-block tint, warm deep accent.
- **Deep-Dome Teal** (`#018990`): A saturated teal, ≈ 2.9:1 — large-ornament / focus-ring / big-element use only, never body text.
- **Drafting-Shadow** (`#393631`) and **Walnut** (`#4e3123`): Warm darks, fill only — possible code-block or footer fills. Keep off the primary card surface (see Exhibit-Card Deep).

### Named Rules

**The Drenched Rule.** Every surface — masthead, post card, pavilion display, footer arcade — sits in the night-shift scene. There is no escape hatch to a clean Substack-grey card. The page itself commits. If a future component feels like it wants to "step outside the room for clarity," the component has the wrong shape, not the room.

**The Named-Light Rule.** Light comes from sources you can name. A desk lamp. A CRT. A marquee bulb. A planetarium projector. A REC light on a console. If a glow doesn't have a clear physical analogue, it isn't earned and shouldn't be in the design. Ambient gradients with no source are the AI-atompunk-slop tell.

**The One-REC-Light Rule.** Now-Broadcasting Red signs one thing on a surface, then disappears. Timestamp icon, page-number, "live" indicator — pick the one that's signing this surface. Three reds visible at once means two are wrong. And because the signal red fails AA at body size, inline `<strong>` is not one of its jobs — emphasis there is weight, not red.

**The Tinted-Black Rule (preserved from Wizard's Workbench).** Pure `#000` and pure `#fff` are forbidden. Night-Shift Midnight carries the cool-blue cast of the body surface; Marquee-Bulb Cream carries the warm-incandescent cast of the text. Even rgba shadows over the body should be tinted toward warm-shadow, not toward absolute black.

**The Three-Pigment-Plus-One Rule.** Drafting-Lamp Amber, Atomic Turquoise, Brass Linework — those are the accent and structural pigments. Now-Broadcasting Red is the rare signal layered on top. The Deep Bench is structural/fill, not new accent voices. No new accent hues without explicit approval. Reaching for purple, magenta, or a fresh green is the sign the design has drifted off-brand.

**The Named-Starfield Rule.** The starfield texture under the body is a real, identifiable, low-density star map (a constellation, a sliver of the Milky Way, a recognizable star pattern). It is not random pixel noise. The exact star pattern is a designer choice; that it is *a real sky* and not a generated one is the rule. **Resolved — the Founding Sky:** a real ephemeris, the sky as it stood over 33.83°N, 117.92°W at 03:00 local on 22 April 2000. Source: the Yale Bright Star Catalogue, every star above the horizon at that instant down to magnitude ~6; each star's radius and opacity mapped to its magnitude, the field laid at 4–8% opacity over Night-Shift Midnight. Real catalogue stars only — no procedural fill, no "thickening." The projection and SVG construction land in the implementation issue.

## 3. Typography

**Display Font:** Bona Nova (OFL) — Mateusz Machalski's 2017 revival of Andrzej Heidrich's 1971 *Bona*, completed with the original author. A warm Polish book serif rooted in Renaissance antiqua: the obscure, period-authentic pick that stands beside the lineage rather than wearing its costume, chosen over the reflex atompunk serifs (Recoleta, DM Serif Display, Reckless Neue). Delivered via Bunny Fonts (privacy-first and GDPR-clean), which serves it alongside the Atkinson body and mono faces and retires the Google Fonts dependency; it holds character at the 4em Marquee Initial under amber glow, and it ships ornamental manicules that echo the ▸ of the Arcane Timestamp.
**Body Font:** Atkinson Hyperlegible Next (sans-serif fallback)
**Mono Font:** Atkinson Hyperlegible Mono (monospace fallback)
**Marquee/Ornament Variant:** Bona Nova Italic — the display face's own italic (the cut the original *Bona* began as), for the Arcane Timestamp and pavilion-display titles.

**Character:** The display face carries the EPCOT-Dreamer optimism — a sit-down-with-a-book editorial serif with mid-century warmth, the kind of letterform that lived on a 1962 children's encyclopedia spine or a 1964 World's Fair brochure cover. Atkinson Hyperlegible Next remains untouched on body, doing the actual work of carrying every word a reader reads. The pairing is intentionally unequal: the display decorates; the body works. Marquee moments — the masthead title and the Marquee Initial on essays — borrow the display face at extreme size, dressed in amber glow.

### Hierarchy
- **Display** (Bona Nova 400, ~3rem desktop / ~2.5rem ≤768px, line-height 1.2): The masthead. The site title under starlight, glowing softly in Drafting-Lamp Amber via the Marquee Glow.
- **Headline** (Bona Nova 400, ~2rem, line-height 1.25): h2. Section dividers within a post. Brass Linework rule beneath, 1px solid at ~30% opacity.
- **Title** (Bona Nova 400, ~1.5rem, line-height 1.3): h3. Sub-section headings within long posts. Drafting-Lamp Amber.
- **Body** (Atkinson Hyperlegible Next 400, 1rem, line-height 1.6): All paragraph text on Marquee-Bulb Cream. Cap line length at the 14/24 PureCSS column (~65–75ch) on desktop.
- **Body Large** (Atkinson Hyperlegible Next 400, ~1.2rem, line-height 1.6): The masthead tagline paragraph and any pull-quote treatment.
- **Label** (Atkinson Hyperlegible Next 400, 0.8rem): Tag sigils, status time, pagination tertiary copy.
- **Mono** (Atkinson Hyperlegible Mono 400, 0.9rem, line-height 1.5): All inline code and code blocks.
- **Ornament** (Bona Nova Italic 400, ~1.1rem): The Arcane Timestamp, pavilion-display titles, status time, pagination "Scroll N of M." Brass Linework or Drafting-Lamp Amber depending on context.
- **Marquee Initial** (Bona Nova 400, ~4em, line-height 0.8): The first letter of titled-essay bodies, in Drafting-Lamp Amber, floated left for a clean 2-line drop, with a soft Marquee Glow. Skipped on titleless microposts. Replaces the previous medieval-manuscript Drop Cap; same lockup math, different cultural reference.

### Named Rules

**The Hyperlegible Body Rule (preserved).** Atkinson Hyperlegible Next is the body face. Non-negotiable. The display face never carries paragraph text, button labels, form input text, or anything a reader reads in volume. If a heading has more than ~10 words, it stops being decorative and the choice should be reconsidered.

**The Marquee Glow Rule.** Soft Drafting-Lamp Amber text-shadow is reserved for the masthead h1, the Marquee Initial on essay posts, and link hover. Glow has a physical analogue (the marquee bulb, the desk-lamp halo, the candle catching a wet edge of ink) — it is never decoration without that anchor. Glow does not appear on h2, h3, body text, or buttons. (Tag sigils are links, so they take the ordinary Link Hover Glow on hover and nothing more.)

**The Three-Knobs Rule (preserved from Wizard's Workbench).** A floated Marquee Initial reserves vertical space equal to `cap font-size × cap line-height`; for a clean N-line drop, that product must equal `N × body line-height`. The previous design's 4em × 0.8 = 2 × 1.6em lockup is a working starting point. If body line-height changes, recompute Marquee Initial line-height to preserve the equation.

**The No-Geometric-Sans-Display Rule.** The display direction is editorial serif, not mid-century geometric sans. Futura, Avenir, and similar are the canonical atompunk choices and exactly for that reason they are *not* the choice here. The All-Night Pavilion reads warmer and more sincere than the geometric-sans atompunk house style; the serif carries that difference.

## 4. Elevation

Mostly flat with two atmospheric registers. Cards rest on the Night-Shift Midnight surface via a single warm-tinted drop shadow — the shadow a paper exhibit-card would cast on a varnished oak table under a drafting lamp. Glow is reserved for the wizardly flourish: the masthead, the Marquee Initial, and link hover. No surface lifts on hover; the room is calm by default. Motion energy is Responsive (state feedback and transitions only); choreographed entrances and scroll-driven sequences are out.

### Shadow Vocabulary

- **Exhibit Rest** (`box-shadow: 0 10px 30px color-mix(in oklch, var(--shadow-warm) 30%, transparent)`, where `--shadow-warm: oklch(20% 0.03 64)`; shipped as the `card-shadow()` mixin): The default shadow under every Exhibit Card, Pavilion Display, book cover, and framed plate. Diffuse, warm-tinted (toward Drafting-Lamp Amber, not toward black), low-contrast against the night-shift surface. Reads as paper resting on oak under a drafting lamp.
- **Trinket Hover Halo** (`box-shadow: 0 3px 8px color-mix(in oklch, <accent> 20%, transparent)`; shipped as the `hover-shadow($color, $alpha)` mixin): A small colored hover halo under book covers (and any trinket that earns one). The accent matches the trinket's own pigment (Drafting-Lamp Amber for warm trinkets, Atomic Turquoise for cool trinkets, Now-Broadcasting Red only for explicitly "live" affordances).
- **Marquee Glow** (`text-shadow: 0 0 12px color-mix(in oklch, var(--drafting-lamp-amber) 42%, transparent)`, the `--marquee-glow` token): The masthead h1 and Marquee Initials. Always-on, low intensity, atmospheric. Reads as a bulb seen through a paper letterform.
- **Link Hover Glow** (`text-shadow: 0 0 10px color-mix(in oklch, var(--drafting-lamp-amber) 50%, transparent)`, the `--link-hover-glow` token): A brief amber glow under hovered links, slightly stronger than Marquee Glow, present only while hovered.

### Named Rules

**The Page-Not-Button Rule (preserved).** Exhibit Cards do not lift on hover. A card is a resting paper exhibit; interactive feedback lives elsewhere. The Exhibit Rest shadow is a "paper on oak" cue, not a "click me" cue. It does not animate, intensify, or change on hover.

**The Earned-Glow Rule.** Glow has an explicit, namable physical source. The masthead glows like a marquee letter under bulbs. The Marquee Initial glows like a planetarium-show title slide. Links glow briefly like a candle catching a wet edge of ink. Nothing glows decoratively without a named physical analogue.

**The Hover-Halo Rule (preserved).** Trinket hover halos use `0 3px 8px rgba(<accent>, 0.2)` and tint the halo to the trinket's own accent. They do not exceed 8px blur, do not cast more than 3px down, and do not exceed 0.2 opacity. Hover is a whisper.

## 5. Components

Documented from the shipped implementation (`frontend/sass/main.scss`). Values are the real compiled tokens: spacing from the `$spacing` scale (`xs` 3px / `sm` 5px / `md` 10px / `lg` 15px / `xl` 20px / `xxl` 30px / `xxxl` 40px), radii from `$border-radius` (`small` 4px / `medium` 8px), shadows and glows from §4. Color names map to the §2 palette.

### Exhibit Cards
Paper exhibits resting on oak. The load-bearing content container; identity is carried by the Arcane Timestamp and the Marquee Initial, never by chrome on the edges. No spine.
- **Corner Style:** 8px (`radius(medium)`).
- **Background:** Exhibit-Card Deep, a shade off the body so the card reads as a recessed exhibit case rather than raised UI.
- **Internal Padding:** 30px (`space(xxl)`), tightening to 20px (`space(xl)`) ≤768px.
- **Shadow:** Exhibit Rest (§4). **Does not lift, intensify, or change on hover** (Page-Not-Button Rule).
- **Border:** none.

### Pavilion Displays
The trinket fixtures (Mystic Missives, Allied Mages, Random Incantations, Enchanted Emblems, Illuminations, Reading Pavilion, Arcane Sigils, Marginalia). They render as ruled cells on the home Great Catalog — no card: a ruled cell with a 1px warm-brass top rule and a mono uppercase, figure-numbered kicker (see Fixture Titles). Inner reading plates carry their back-matter in the colophon, not a trinket aside.

### Fixture Titles
- **Standalone** (e.g. the colophon's "Other Curiosities"): Bona Nova 400, 1.2rem (`size(large)`), Drafting-Lamp Amber, with a 1px Brass Linework bottom rule at 30% opacity (`subtle-border`).
- **Catalog:** Atkinson Hyperlegible Mono 400, 0.8rem (`size(small)`), uppercase, 0.14em tracking, warm-brass, prefixed with a figure number (`Fig. N ·`) or `Contents ·` for the Recent Scrolls index. The prefix recedes (0.82em, dimmer) so the fixture's NAME is the dominant token.

### Tag Sigils  (formerly Sigil Pills / Tag Pills)
A category renders as a sigil-link, not a filled chip. The ✦ sparkle in Drafting-Lamp Amber (the category's lamp-spark), the name in Brass Linework, carrying the site's universal link affordance inherited from the global `a` rule — the dotted→solid Amber underline, the Link Hover Glow on hover, the turquoise focus ring. No fill, no pill radius, no box: a tag is a catalog index entry in the same grammar as every other link, not a chip resting on the page; the leading sparkle delimits each entry where there is no enclosure. The old filled-pill shape and the separate Now-Broadcasting-Red response-tag species are retired — a scroll's response/reply lives in the reading plate's colophon, not a red pill. The taxonomy is a deliberately unclassifiable list (the Celestial Emporium of Benevolent Knowledge), so the sigil stays one uniform sparkle rather than a per-category pictogram: a literal glyph would domesticate categories the list exists to keep wild.
- **Sparkle:** Phosphor `ph-sparkle`, Drafting-Lamp Amber, `space(xs)` right margin. **Name:** Brass Linework. **Shape:** no fill, no radius, no box.

### Links
- **Rest:** Drafting-Lamp Amber text, 1px dotted Amber bottom border.
- **Hover:** border goes 1px solid; Link Hover Glow appears. No decorative underlines on non-links.
- **Focus (`:focus-visible`):** see Focus Rings.
- **Reserved-underline trick:** in baseline-aligned rows (runhead nav, Recent Scrolls, the Arcanum index) the 1px is reserved transparent at rest and only colored on hover, so hovering never reflows the row.

### Arcane Timestamp
The `Inscribed on <date>` dateline. Bona Nova italic, 1.1rem (`size(medium)`), Brass Linework. Its icon is the one REC light: a Now-Broadcasting Red filled circle (`.timestamp-icon`), marking the timestamp like a console's recording lamp. One REC light per surface.

### Marquee Initial  (replaces the Illuminated Drop Cap)
A glowing Bona Nova capital opening a titled essay's first paragraph: 4em, line-height 0.8, floated left for a clean 2-line drop (the Three-Knobs Rule: 4em × 0.8 = 3.2em = 2 × 1.6em body line-height), Drafting-Lamp Amber with the always-on Marquee Glow, 0.14em right margin. Skipped on titleless microposts and standing pages, where a 4em capital would be absurd.

### Blockquote
3px Brass Linework left-stripe (`accent-border`), italic, 15px left padding (`space(lg)`), desaturated to 0.8 opacity. One of the two sanctioned side-stripes (see Don'ts).

### Code
- **Inline:** Brass Linework 10% wash on the surface, 4px corners (`radius(small)`), Atkinson Hyperlegible Mono 0.9rem (`size(normal)`), 2px 4px padding.
- **Block (`pre`):** the same wash plus a 3px Drafting-Lamp Amber left-stripe (the preserved syntax-highlighter convention, the second sanctioned side-stripe), 15px padding (`space(lg)`), horizontal scroll on overflow.

### Slide Tray Counter  (Pagination)
Three columns (previous · counter · next). Arrows in Drafting-Lamp Amber; page numerals in Now-Broadcasting Red at 20px (`space(xl)`) — large enough to clear AA. Counter set in Bona Nova.

### Reading Pavilion  (Bookshelf, /bookshelf/)
A full-width Catalog plate: covers grouped by year-of-departure, bottom-aligned in a wrapping row like books on a shelf.
- **Cover:** 128×200px, 4px corners (`radius(small)`), `object-fit: cover`, Exhibit Rest shadow.
- **Hover:** a gentle Drafting-Lamp Amber Trinket Hover Halo (§4). **No card-lift.**
- **Art-less book:** the title set on an Exhibit-Card-Deep board with a 1px Brass edge, line-clamped to 7 lines, in place of an emoji. The home-fixture preview covers are 64×100px.

### Mystic Missives  (Status Feed)
A Pavilion Display of recent omg.lol statuses. Entries separated by 1px Brass Linework rules at 30% (a class-aware adjacent-sibling combinator, so the trailing footer never reads as the last entry); time in Bona Nova italic Brass; long URLs wrap with `overflow-wrap: anywhere`.

### Allied Mages  (Blogroll) · Random Incantations  (Random Posts)
Pavilion Displays of outbound links — the Network of Fellow Dreamers, and a curated jump elsewhere in the archive. Each entry inherits the global amber link treatment; lists are `.fixture-list` (unstyled, `space(xs)` row padding).

### Enchanted Emblems  (88×31 Web Buttons)
A centered flex-wrap of indie-web buttons at native pixel size (88×31, `max-width: none` to defeat the global responsive-image cap). **No filter, no scale, no border, no radius.** They render exactly as their authors made them.

### Focus Rings
Every interactive trinket shows a keyboard focus ring distinct from hover: `outline: 2px solid var(--atomic-turquoise); outline-offset: 3px; border-radius: 4px`, scoped to `:focus-visible` so it shows for keyboard users and not on mouse click. Atomic Turquoise is the reserved focus pigment — the cool counter reads as distinct from the warm amber hover and clears AA at 6.06:1. The masthead title uses the same ring at 6px offset to clear its glow. The skip-link is a Brass-edged Exhibit-Card-Deep chip parked off-screen via `transform`, sliding in on focus.

### The Great Catalog  (home front page)
The home is a dense, ruled catalog spread, not a feed: the most recent post is the feature ("Plate I", under a 2px lit-edge top rule), a "Contents" index (Recent Scrolls) keeps the rest reachable, and the trinkets are figure-numbered catalog cells on a 12-column dense grid. Max width 1180px; warm brass rules (`--catalog-rule`, `--catalog-rule-faint`) throughout. A single scroll reads as one centered reading plate at `max-width: 40rem`.

## 6. Do's and Don'ts

### Do

- **Do** keep Atkinson Hyperlegible Next as the body face on every screen. Decorative atmosphere is allowed in headings, ornaments, and the Marquee Initial — never in paragraph text or form-input text.
- **Do** verify every accent pigment against Night-Shift Midnight for WCAG 2.2 AA. Nudge lightness, not chroma, when contrast falls short.
- **Do** anchor every glow to a named physical light source: a desk lamp, a CRT, a marquee bulb, a planetarium projector, a REC light, a candle catching a wet edge. If you can't name the source, the glow isn't earned.
- **Do** treat the 88×31 web buttons as sincere indie-web participation. Display at native pixel resolution. Never filter, restyle, scale, or apply CSS effects.
- **Do** use the wizardly nomenclature in copy ("Inscribed on", "Mystic Missives", "Allied Mages", "Enchanted Emblems", "Teleportation Circle", "Random Incantations"). The voice carries the wizard while the visuals carry the era.
- **Do** retune the Marquee Initial's line-height alongside any change to its font-size or body line-height. The Three-Knobs Rule is non-negotiable.
- **Do** gate any planetarium-style rotation, slide-tray reveal, marquee-glow flicker, or starfield-shimmer animation behind `prefers-reduced-motion: no-preference`. The night shift is calm by default.
- **Do** show visible focus rings on every interactive trinket (web buttons, blogroll links, status feed entries, tag sigils, pagination, book covers, Marquee Initial if it is itself a link). Focus is distinct from hover.
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
- **Don't** color inline `<strong>` with Now-Broadcasting Red. At body size it lands at ≈ 3.6:1 on the surface and fails AA. Inline emphasis is font weight; the signal red is for icons, page numbers, and the "live" indicator, where it is large enough to pass.
- **Don't** add modals as a first thought. Inline disclosure, expanding cards, or a follow-up post are usually the better answer for a personal site.
- **Don't** apply glow to body text, h2, h3, or buttons. Glow lives on the masthead h1, the Marquee Initial, and link hover — nowhere else (tag sigils are links, so they take the ordinary link-hover glow, no more).
- **Don't** animate layout properties. If motion is added, animate `transform` and `opacity` only, with ease-out exponential curves, gated behind `prefers-reduced-motion`.
- **Don't** lift Exhibit Cards on hover. Cards are resting paper exhibits.
- **Don't** filter, restyle, or scale the 88×31 web buttons. They render at native pixel size and look like what they are.
- **Don't** generate a random-noise starfield. The Night-Shift Midnight starfield is a real, identifiable star pattern — a recognizable sky, a real constellation, a real slice of the Milky Way. A procedural pixel-noise field is the AI-atompunk-slop tell.
