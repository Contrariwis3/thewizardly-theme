---
name: TheWizardly Theme
description: A Hugo theme for thewizardly.com. The Wizard's Workbench: an indie-web curio shop set on parchment under inkwell midnight, lit by sage candlelight and sealed in rose wax.
colors:
  sage-grimoire: "#7ba05b"
  weathered-parchment: "#b5a693"
  rose-seal: "#b85c69"
  parchment-cream: "#f4f1e8"
  inkwell-midnight: "#1a1a2e"
  inkwell-midnight-deep: "#0f0f1a"
  card-bg: "#0f0f1acc"
  code-bg: "#b5a6931a"
typography:
  display:
    fontFamily: "Philosopher, serif"
    fontSize: "3rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "normal"
  display-mobile:
    fontFamily: "Philosopher, serif"
    fontSize: "2.5rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "normal"
  headline:
    fontFamily: "Philosopher, serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: "normal"
  title:
    fontFamily: "Philosopher, serif"
    fontSize: "1.5rem"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "normal"
  body:
    fontFamily: "Atkinson Hyperlegible Next, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  body-large:
    fontFamily: "Atkinson Hyperlegible Next, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  label:
    fontFamily: "Atkinson Hyperlegible Next, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "normal"
  mono:
    fontFamily: "Atkinson Hyperlegible Mono, monospace"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  ornament:
    fontFamily: "Philosopher, serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "normal"
  drop-cap:
    fontFamily: "Philosopher, serif"
    fontSize: "4em"
    fontWeight: 400
    lineHeight: 0.8
    letterSpacing: "normal"
rounded:
  sm: "4px"
  md: "8px"
  pill: "20px"
spacing:
  xs: "3px"
  sm: "5px"
  md: "10px"
  lg: "15px"
  xl: "20px"
  xxl: "30px"
  xxxl: "40px"
components:
  card:
    backgroundColor: "{colors.card-bg}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.md}"
    padding: "30px"
  card-mobile:
    backgroundColor: "{colors.card-bg}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.md}"
    padding: "20px"
  side-content:
    backgroundColor: "{colors.card-bg}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.md}"
    padding: "20px"
  side-title:
    textColor: "{colors.sage-grimoire}"
    typography: "{typography.body-large}"
    padding: "0 0 5px 0"
  tag:
    backgroundColor: "#b5a69333"
    textColor: "{colors.weathered-parchment}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
    typography: "{typography.label}"
  tag-hover:
    backgroundColor: "#b5a69333"
    textColor: "{colors.weathered-parchment}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  response-tag:
    backgroundColor: "#b85c6926"
    textColor: "{colors.rose-seal}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
    typography: "{typography.label}"
  arcane-timestamp:
    textColor: "{colors.weathered-parchment}"
    typography: "{typography.ornament}"
  drop-cap:
    textColor: "{colors.sage-grimoire}"
    typography: "{typography.drop-cap}"
  link:
    textColor: "{colors.sage-grimoire}"
  link-hover:
    textColor: "{colors.sage-grimoire}"
  blockquote:
    textColor: "{colors.parchment-cream}"
    padding: "0 0 0 15px"
  code-inline:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.sm}"
    padding: "2px 4px"
    typography: "{typography.mono}"
  code-block:
    backgroundColor: "{colors.code-bg}"
    textColor: "{colors.parchment-cream}"
    rounded: "{rounded.sm}"
    padding: "15px"
    typography: "{typography.mono}"
  book-cover:
    rounded: "{rounded.sm}"
    width: "128px"
    height: "200px"
  web-button:
    width: "88px"
    height: "31px"
---

# Design System: TheWizardly Theme

## 1. Overview

**Creative North Star: "The Wizard's Workbench"**

A workbench at twilight, lit by candlelight on parchment. A sage-bound notebook lies open. A rose wax seal is cooling on a letter. The room behind it is inkwell-dark, but the surfaces in arm's reach glow warm. This system is workmanlike and lived-in; things are out, in use, mid-thought. The wizardly framing belongs to the proprietor, not to the room: the room is just a person's workbench, faithfully rendered.

Density is high in the writing surface and modest in the chrome. The page reads top-to-bottom in a single column of long-form text framed by a sidebar of trinkets, sigils, and outbound links. There is one bound notebook (the post card), one mantel of small objects (the sidebar), and a parchment pattern faintly visible on the wall behind everything. Edges are hand-drawn rather than die-cut: dotted underlines, soft drop shadows, a single sage stripe down the spine of each card. Decoration is sincere, not winking, and it never overrides the body type.

This system explicitly rejects modern SaaS / Substack templates (white sans-serif blog with subscribe CTA), official D&D / WotC commercial fantasy gloss, goth-metal mysticism (pure black + blood red, blackletter, occult sigils), and ironic Web 2.0 nostalgia bait (Comic Sans, animated GIF chaos as costume). The 88x31 web buttons, blogroll, and status scrolls here are sincere indie-web participation, not pastiche.

**Key Characteristics:**
- Inkwell-midnight surface tinted faintly toward blue, never pure black
- Parchment-cream body type that never sacrifices legibility for atmosphere
- A three-pigment palette of sage, weathered parchment, and rose seal carrying all accent work
- Essay-form posts (those with titles) open with an illuminated drop cap in Sage Grimoire; titleless microposts skip it
- Every post carries the Arcane Timestamp inside the card: a Philosopher-italic "Inscribed on…" line with a Rose Seal calendar mark
- A subtle parchment SVG pattern washing the body at 8% opacity
- Soft glows on the display heading and on link hover; no other ambient effects
- Trinkets (web buttons, blogroll, status feed) treated as load-bearing, not chrome

## 2. Colors: The Workbench Palette

A three-pigment palette of sage ink, weathered parchment, and rose wax sealed onto an inkwell-midnight surface, with a single warm parchment-cream body color carrying every word.

### Primary
- **Sage Grimoire** (`#7ba05b`): The voice of the system. Carries every link, every body-copy emphasis you want a reader to follow, every h1 and h3 heading, the sage stripe down the left edge of cards and code blocks, and the dotted-underline link affordance. Used softly, never aggressively; never as a flood fill.

### Secondary
- **Weathered Parchment** (`#b5a693`): The voice of metadata. Carries h2 headings, blockquote text, the Arcane Timestamp ornament, tag pill text, and the muted "previous post" / "year group" labels. The color of margin notes and library spines.

### Tertiary
- **Rose Seal** (`#b85c69`): The voice of emphasis and reply. Carries `<strong>` text, the timestamp icon, response tag pills, the pagination page-number numerals. Used like a wax seal: rare, deliberate, signing one thing per surface.

### Neutral
- **Parchment Cream** (`#f4f1e8`): All body text on every surface. The page itself.
- **Inkwell Midnight** (`#1a1a2e`): Body background, with a parchment SVG pattern at 8% opacity layered over it. Faintly blue, never pure black.
- **Inkwell Midnight Deep** (`#0f0f1a` at 80% opacity, written `#0f0f1acc`): Card and sidebar background. Slightly deeper than the body so cards read as nested pages, not raised cards.
- **Code Overlay** (`#b5a693` at 10% opacity, written `#b5a6931a`): A whisper of weathered parchment laid over the card surface to mark inline code and code blocks.

### Named Rules

**The Three-Pigment Rule.** Sage, parchment, rose. No new accent hues without explicit approval. New surfaces compose from these three plus the two midnight neutrals; reaching for blue, gold, or yellow is a sign the design has drifted off-brand.

**The One Seal Rule.** Rose Seal is rare. It signs the timestamp icon, the response-tag pill, the page-number numerals, and `<strong>` emphasis. It does not get used as a button background, a heading color, a border, or a section divider. If the eye is finding rose in three places on a screen at once, two of them are wrong.

**The Tinted-Black Rule.** Pure `#000` and pure `#fff` are forbidden. Inkwell Midnight carries the blue-cast body; Parchment Cream carries the warm-cast text. Even rgba shadows over the body should fall on Inkwell Midnight Deep, not on `#000`.

## 3. Typography

**Display Font:** Philosopher (with serif fallback)
**Body Font:** Atkinson Hyperlegible Next (with sans-serif fallback)
**Mono Font:** Atkinson Hyperlegible Mono (with monospace fallback)

**Character:** Philosopher carries the wizardly tone in the headings, the side-titles, and small ornamental labels (the Arcane Timestamp, status-time, pagination "Scroll N of M"). Atkinson Hyperlegible Next carries every word a reader actually reads. The pairing is deliberately unequal: the display face decorates, the body face works.

### Hierarchy

- **Display** (Philosopher 400, 3rem desktop / 2.5rem ≤768px, line-height 1.2): The site title in the masthead. Glows softly in Sage Grimoire via a 10px text-shadow at 30% opacity. One Display per page, the masthead only.
- **Headline** (Philosopher 400, 2rem, line-height 1.25): h2. Weathered Parchment with a dotted 1px underline at 30% opacity. Section dividers within a post.
- **Title** (Philosopher 400, 1.5rem, line-height 1.3): h3. Sage Grimoire. Sub-section headings within long posts.
- **Body** (Atkinson Hyperlegible Next 400, 1rem / 16px, line-height 1.6): All paragraph text on Parchment Cream. Cap line length at the 14/24 PureCSS column (~65–75ch) on desktop.
- **Body Large** (Atkinson Hyperlegible Next 400, 1.2rem, line-height 1.6): The masthead tagline paragraph.
- **Label** (Atkinson Hyperlegible Next 400, 0.8rem): Tag pills, status time, response-tag pills, pagination tertiary copy.
- **Mono** (Atkinson Hyperlegible Mono 400, 0.9rem, line-height 1.5): All inline code and code blocks.
- **Ornament** (Philosopher 400 italic, 1.1rem): The Arcane Timestamp, side-content titles, status time, pagination "Scroll N of M". Weathered Parchment.
- **Drop Cap** (Philosopher 400, 4em, line-height 0.8): The first letter of titled-post bodies (essays), in Sage Grimoire, floated left for a clean 2-line drop. The medieval-manuscript capital. Skipped on titleless microposts.

### Named Rules

**The Hyperlegible Body Rule.** The body face is Atkinson Hyperlegible Next. It is non-negotiable. The Philosopher decorative face never carries paragraph text, button labels, form input text, or anything a reader reads in volume. If a heading has more than ~10 words, it stops being decorative and the choice should be reconsidered.

**The One Glow Rule.** Soft text-shadow glows are reserved for the site-title h1 (always, low intensity) and for link hover (briefly, while hovered). They do not appear on h2, h3, body text, or buttons. Glow is a flourish, not a tone.

**The Three-Knobs Rule (drop cap lockup).** A floated drop cap reserves vertical space equal to `cap font-size × cap line-height`; for a clean N-line drop, that product must equal `N × body line-height`. The current lockup is `4em × 0.8 = 3.2em = 2 × 1.6em`. There are three knobs (cap font-size, cap line-height, body line-height) and only two equations (the lockup, and any aesthetic preference). Tuning one without retuning another produces the "good but not great" sliver where the float reserves a fractional number of body lines and line 3 starts beside the cap awkwardly. If body line-height changes, recompute cap line-height to preserve `cap font-size × cap line-height = N × body line-height`.

## 4. Elevation

The system is mostly flat with two atmospheric registers. Cards float gently above the inkwell body via a single soft drop shadow, conveying "page resting on parchment" rather than "raised UI surface". Glow is reserved for the wizardly flourish: the masthead title, and link-hover feedback.

### Shadow Vocabulary

- **Card Rest** (`box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2)`): The default shadow under every card and side-content panel. Diffuse, soft, low-contrast against the inkwell surface. Reads as "page laid down", not "button lifted up".
- **Trinket Hover** (`box-shadow: 0 3px 8px rgba(<accent>, 0.2)`): A small colored hover halo under tags, response tags, status-link pills, and book covers. The accent color matches the trinket's own pigment (Sage Grimoire under primary trinkets, Weathered Parchment under tags, Rose Seal under response affordances).
- **Display Glow** (`text-shadow: 0 0 10px rgba(123, 160, 91, 0.3)`): The Sage Grimoire halo under the masthead h1. Always-on, low-intensity, atmospheric.
- **Link Hover Glow** (`text-shadow: 0 0 10px rgba(123, 160, 91, 0.5)`): A brief Sage glow under hovered links. Slightly stronger than Display Glow, present only while the link is hovered.

### Named Rules

**The Page-Not-Button Rule.** The Card Rest shadow is a "page on parchment" cue, not a "click me" cue. It does not animate, intensify, or lift on hover. A card is a resting page; a button is something else and gets explicit interactive feedback elsewhere.

**The Hover-Halo Rule.** Trinket hover halos use `0 3px 8px rgba(<accent>, 0.2)` and tint the halo to the trinket's own accent (sage, parchment, or rose). They do not exceed 8px blur, do not cast more than 3px down, and do not change opacity beyond 0.2. Hover is a whisper.

## 5. Components

### Cards (the manuscript page)
Cards are the primary writing surface. Their identity is carried by what's *inside* them, not by chrome on the edges: the Arcane Timestamp at the top of each card and the Illuminated Drop Cap on the first paragraph of titled essays. The card itself is a clean, faintly translucent page.

- **Shape:** Gently rounded edges (`border-radius: 8px`).
- **Background:** Inkwell Midnight Deep at 80% opacity (`#0f0f1acc`), letting the parchment body pattern subtly show through.
- **Edges:** No side stripe. No border. The Card Rest shadow alone defines the page's edge against the body.
- **Shadow:** Card Rest, always.
- **Internal Padding:** 30px desktop, 20px ≤768px.
- **Default Margin:** 40px below each card; cards never touch.
- **Overflow:** `hidden`, so floated book-cover images and any other floated child crops cleanly inside the rounded corners.

### Side Content (the mantel)
Sidebar containers stacked down the right column, each holding a different kind of trinket.

- **Shape:** `border-radius: 8px`.
- **Background:** Inkwell Midnight Deep at 80% opacity.
- **Padding:** 20px.
- **No spine on desktop**: a side-content container is a tray, not a page; the sage stripe re-appears only on the ≤768px stacked view to maintain the bound feel.
- **Side Title:** A Philosopher 1.2rem ornament label in Sage Grimoire with a 1px dotted Sage bottom rule at 30% opacity. Names the trinket category ("Teleportation Circle", "Mystic Missives", "Random Incantations", "Allied Mages", "Enchanted Emblems", "Arcane Tags").

### Tag Pills (the wax seals)
Two species of pill, distinguished only by pigment.

- **Shape:** Pill (`border-radius: 20px`), 3px / 10px padding.
- **Tag (category):** Weathered Parchment text on a Weathered Parchment 20% tint.
- **Response Tag (reply / status link):** Rose Seal text on a Rose Seal 15% tint.
- **Hover:** A 1px solid border in the pill's own pigment appears, plus a Trinket Hover halo. No background or text-color change.
- **Content:** Most tags carry a Phosphor `ph-sparkle` icon to the left of the label.

### Illuminated Drop Cap (the manuscript capital)
The first letter of an *essay* post's body text rendered as a large Philosopher capital in Sage Grimoire, floated left for a clean 2-line drop. This is the medieval manuscript practice of illumination, used here as the system's "this is an essay" signal.

- **Apply on:** The `::first-letter` of the first `<p>` inside `.post-content`, **only when the card has a title** (`<h2>`). On micro.blog this maps cleanly to "essay-form posts" — titleless posts are microposts and may be only a few words; a 4em capital on a 10-word post would be absurd. The CSS scope is `.card:has(> h2) .post-content > p:first-of-type::first-letter`. The existing `{{ if .Title }}<h2>...</h2>{{ end }}` pattern in the templates already provides the signal; the only template change required is wrapping `{{ .Content }}` in a `<div class="post-content">` so the selector has something to bite.
- **Typography:** Philosopher 400, 4em (relative to body), line-height 0.8, color Sage Grimoire.
- **Sizing math:** `4em × 0.8 = 3.2em = 2 × 1.6em`. The float reserves exactly 2 body line-heights of vertical space; the cap-baseline lands on body line 2's baseline. See **The Three-Knobs Rule** under Typography for what to recompute if body line-height ever changes.
- **Placement:** `float: left`, `margin-right: 0.12em`. No padding-top, no negative margins; the lockup math eliminates the need.
- **Restraint:** No background, no border, no glow. The size and the serif do all the work.
- **Where it doesn't go:** Titleless microposts on the index, summary excerpts, side-content panels, bookshelf entries, pagination cards. The `:has(> h2)` scope handles all of these by default.
- **Edge cases:** If the first character is a quotation mark or a parenthesis, the drop-cap still applies to the *first letter* (CSS `::first-letter` handles this naturally by including punctuation that precedes the first letter).

### Arcane Timestamp (the dateline)
A signature ornament on every post showing when it was inscribed. Lives inside the card, above the body text.

- **Form:** `<calendar icon> Inscribed on <linked date>`.
- **Typography:** Philosopher italic, 1.1rem, Weathered Parchment.
- **Icon:** Rose Seal, marking the timestamp like a wax seal beside the date.
- **Behavior:** The date itself is the post's permalink; hover applies the standard sage link affordance.

### Links
- **Default:** Sage Grimoire text, 1px dotted Sage underline.
- **Hover:** Underline becomes 1px solid Sage; Link Hover Glow appears.
- **Permalink class:** Identical treatment to default links.
- **Affordance honesty:** Underline appears only on real anchors. Decorative text is never underlined; non-anchor text is never sage-colored.

### Blockquote
- Left padding 15px; vertical bar via a 3px Weathered Parchment left stripe.
- Italic, Parchment Cream at 80% opacity.
- One of only two legitimate side-stripe locations in the system, the other being code blocks.

### Code (inline + block)
- **Background:** Code Overlay (`#b5a6931a`), a whisper of parchment over the card surface.
- **Spine:** 3px Sage Grimoire left stripe — a syntax-highlighter convention inherited from print and pre-LLM web codeblock styling.
- **Radius:** 4px.
- **Family:** Atkinson Hyperlegible Mono.
- **Inline padding:** 2px / 4px.
- **Block padding:** 15px, 20px vertical margin, horizontal scroll on overflow, no soft-wrap.

### Pagination (the scroll counter)
Three-column layout: Previous link, page counter, Next link.

- **Counter:** Philosopher with the page numerals in Rose Seal at 20px (one of the few legitimate Rose Seal uses).
- **Arrows:** Sage Grimoire `←` and `→` glyphs.
- **Lives inside a card** (no drop cap, no marginalia date — pagination is navigation, not a post).

### Bookshelf
A grid of book covers grouped by year.

- **Cover size:** 128 × 200px, 4px radius, Card Rest shadow.
- **Hover:** `translateY(-4px)` lift plus a Sage Grimoire Trinket Hover halo at 30% opacity. The only translate-on-hover in the system.
- **Placeholder cover:** Weathered Parchment 10% tint with a 1px subtle border at 30% opacity, centered 📚 emoji at 30% opacity.
- **Empty state:** Weathered Parchment italic, "empty" copy at 80% opacity.

### Web Button Collection (Enchanted Emblems)
The project's most distinctive trinket: a flexbox wrap of 88×31 indie-web buttons.

- **Image size:** Exactly 88 × 31px, no scaling, `display: block`.
- **Layout:** Flex-wrap with 5px gap, justify-center.
- **Sub-collection separator:** A "share these" sub-collection sits above with a 1px Weathered Parchment 20% bottom rule below it.
- **Caption:** `.emblem-note` in Weathered Parchment italic at 80% opacity, centered.
- **Honor the medium:** Buttons are GIFs and JPGs hosted at `static.thewizardly.com`. They are not styled, filtered, or resized; they look like 1999 web buttons because they are.

### Status Scroll (Mystic Missives)
A side-content panel rendering the three most recent statuses from omg.lol.

- **Each entry:** An emoji + dateline header (Philosopher italic in Weathered Parchment), the status content below.
- **Dividers:** 1px Sage Grimoire bottom rule at 30% opacity between entries; the last entry has no rule.
- **Footer link:** A Rose Seal "View all scrolls" pill (response-tag style), with a Phosphor scroll icon.

## 6. Do's and Don'ts

### Do
- **Do** keep Atkinson Hyperlegible Next as the body face on every screen. Decorative atmosphere is allowed in headings and ornaments, never in paragraph type or form input text.
- **Do** retune the drop cap's line-height alongside any change to its font-size or to body line-height. The Three-Knobs Rule is non-negotiable: `cap font-size × cap line-height = N × body line-height`.
- **Do** verify all sage / parchment / rose foreground colors against Inkwell Midnight (`#1a1a2e`) for WCAG 2.2 AA contrast (4.5:1 body, 3:1 large text). When contrast falls short, nudge lightness, not chroma.
- **Do** use the Three-Pigment Rule. Sage, parchment, rose. New accent hues require explicit approval.
- **Do** treat trinkets (web buttons, blogroll, status feed, bookshelf, random posts) as load-bearing architecture. New surfaces should make room for the next trinket, not eliminate the existing ones.
- **Do** cite the wizardly metaphor in copy ("Inscribed on", "Mystic Missives", "Allied Mages", "Enchanted Emblems"). The voice carries the bit so the visuals don't have to.
- **Do** use Philosopher for headings and small ornamental labels (Arcane Timestamp, side-content titles, status time, pagination counter).
- **Do** keep the Card Rest shadow soft (`0 10px 20px rgba(0,0,0,0.2)`) and the Trinket Hover halo small (`0 3px 8px rgba(<accent>, 0.2)`).
- **Do** show visible focus rings on every interactive trinket (web button images, blogroll links, status feed links, tag pills, pagination, book covers). Focus is distinct from hover.
- **Do** wrap any new motion in `@media (prefers-reduced-motion: no-preference)`.

### Don't
- **Don't** let the site look like a modern SaaS / Substack template (white sans-serif blog with author bio card, subscribe CTA, Medium-style scroll-optimized layout). This site is a hearth, not a funnel.
- **Don't** lean toward official D&D / WotC commercial fantasy gloss (red and black, scroll banners, stock fantasy art). The wizardly voice here is personal and weird, not licensed.
- **Don't** drift toward goth / metal mysticism (pure black + blood red, occult sigils, blackletter, edgelord posturing). The base is Inkwell Midnight, not pitch black; the accent is Rose Seal, not blood.
- **Don't** wear ironic Web 2.0 nostalgia bait (Comic Sans, animated GIF chaos for its own sake, "old web" worn as a meme costume). The 88×31 web buttons here are sincere indie-web participation; treat them straight.
- **Don't** add side-stripe borders to new components. Side-stripes greater than 1px exist in exactly two locations: the 3px Weathered Parchment stripe on blockquotes (a print typography convention) and the 3px Sage Grimoire stripe on code blocks (a syntax-highlighter convention). Cards have no spine; their identity is carried by the Illuminated Drop Cap and the Arcane Timestamp. Do not propagate the stripe to callouts, alerts, list items, sidebars, or any other surface.
- **Don't** use gradient text (`background-clip: text` over a gradient). Emphasis is via weight, size, or pigment, never via gradient.
- **Don't** use `#000` or `#fff` anywhere. Inkwell Midnight and Parchment Cream are the bounds of the value scale.
- **Don't** flood-fill with Sage Grimoire (no full sage button backgrounds, no sage section bands, no sage hero panels). Sage is a voice; it should not become a wall.
- **Don't** use Rose Seal as a background, button, border, or section divider. One Seal Rule: rose signs one thing on a surface, then disappears.
- **Don't** add modals as a first thought. Inline disclosure, expanding cards, or a follow-up post on the blog are usually the better answer for a personal site.
- **Don't** apply glow to body text, h2, h3, or buttons. Glow lives on the masthead h1 (always) and link hover (briefly), nowhere else.
- **Don't** animate layout properties. If hover transforms or scroll motion is added, animate `transform` and `opacity` only, with ease-out exponential curves, gated behind `prefers-reduced-motion`.
- **Don't** lift cards on hover. Cards are resting pages, not buttons. The Page-Not-Button Rule.
- **Don't** filter, restyle, or scale the 88×31 web buttons. They render at their native pixel size and look like what they are.
