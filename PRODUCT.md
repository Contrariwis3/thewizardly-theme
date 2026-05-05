# Product

## Register

brand

## Users

Friends and concentric circles of people who already know Contrariwise the Wizardly. They arrive via direct link, RSS, micro.blog timeline, or by following a button or blogroll edge from another personal site. They're not strangers being converted into readers; they're people checking in.

The job to be done: keep up with what Contrariwise is reading, thinking, and doing, and find the connective tissue out to the rest of the indie web (status updates, blogroll, web buttons, bookshelf).

## Product Purpose

A personal blog at thewizardly.com, hosted on micro.blog and rendered by this Hugo theme. The site is a hearth, not a funnel: a place where Contrariwise writes posts, lists books, posts status updates from omg.lol, and trades buttons with the rest of the indie web.

Success looks like a friend opening the site and feeling like they've walked into a room that belongs to a specific person, with specific taste, who has been here for a while. The wizardly framing is the proprietor's persona, not the whole aesthetic; the surrounding furniture (web buttons, blogroll, status scrolls, bookshelf) is the indie web doing its actual job of linking outward.

## Brand Personality

Playful, mischievous, warm.

Voice is fully committed to the wizardly bit ("Inscribed on", "Mystic Missives", "Allied Mages", "Enchanted Emblems", "Teleportation Circle"), but committed in the direction of fun, not solemnity. The wizard is delighted to show you a thing. Puns, asides, easter eggs, and small enthusiasms are welcome. Snark, edgelord posturing, and self-importance are not.

The host is bookish and well-read but not gatekeepy: generous with attribution, generous with outbound links, happy when you wander off to a friend's site.

## Anti-references

This site should NOT look or feel like:

- **Modern SaaS / Substack templates.** White sans-serif blog with author bio card, subscribe CTA, Medium-style layout, optimized for scroll depth. Anti-personal, anti-place.
- **Official D&D / WotC brand.** Red and black, scroll banners, stock fantasy art, commercial-fantasy gloss. The wizardly voice here is personal and weird, not licensed.
- **Goth / metal mysticism.** Pure black + blood red, occult sigils, blackletter, edgelord atmosphere. Too dark, too serious.
- **Ironic Web 2.0 nostalgia bait.** Comic Sans, animated GIF chaos for its own sake, "old web" worn as a meme costume. The indie-web spirit here (88x31 buttons, blogroll, status feed) is sincere participation, not pastiche.

## Design Principles

1. **Wizard as proprietor, not as set dressing.** The mystical voice belongs to the host. It shows up in copy, section names, and small flourishes — not in heavy visual costuming over every component. When a design choice requires you to either lean harder on the bit or step back, step back; the writing carries the bit on its own.

2. **Hand-made over polished.** This is a curio shop, not a design system. Visible texture, small imperfections, and evidence of a person are features. Defaults come from an indie-web sensibility (PureCSS grid, web buttons, parchment SVG pattern), not from reaching for a component library.

3. **Trinkets are the architecture.** The sidebar's buttons, blogroll, status feed, and random-post list are not chrome to be tidied away. They are the point: the site exists in part to link outward. New surfaces should make room for the next trinket, not eliminate the existing ones.

4. **Sincere, not winking.** The wizardly framing is committed and warm. It is not an ironic costume, not a knowing meta-bit, and not Renaissance-faire camp. If a design or copy choice only works as a wink, rewrite it so it works straight.

5. **Legibility is sacred.** Atmosphere never wins over readability. Body type stays Atkinson Hyperlegible. Contrast meets WCAG 2.2 AA across all text including secondary metadata. If a mystical flourish dims the text below the floor, the flourish goes, not the floor.

## Accessibility & Inclusion

- **Target: WCAG 2.2 AA** across all body, link, and metadata text on the dark theme. Verify the sage / parchment / rose-seal palette against the midnight background; nudge lightness rather than chroma when contrast falls short.
- **Body typography stays Atkinson Hyperlegible Next** (and Atkinson Hyperlegible Mono for code). The Philosopher heading face is decorative and may carry the wizardly tone; the body face must not.
- **Focus states are obvious.** Every interactive trinket (web buttons, blogroll links, status feed, tag pills, pagination) shows a visible focus ring distinct from hover.
- **Outbound links are honest.** Link affordances (dotted underline, hover glow) make link-versus-not-link unambiguous; no decorative underlines on non-links.
- **Reduced motion is respected** when motion is added. The current theme is mostly static; if hover transforms or animations are introduced, gate them behind `prefers-reduced-motion: no-preference`.
