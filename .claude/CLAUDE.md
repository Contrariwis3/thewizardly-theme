# Project: TheWizardly Theme

Hugo theme for [thewizardly.com](https://thewizardly.com), hosted on micro.blog.

## Workflow

This project overrides the global Agentic SDLC. It is a design-only effort, so **Impeccable replaces OpenSpec and beads** — there are no OpenSpec changes, no beads graphs, and no `/propose` → `/implement` → `/finalize` ceremony. Design decisions are explored and recorded in `DESIGN.md` / `PRODUCT.md` and implemented with `/impeccable` (`shape`, `craft`, `document`). Forgejo issues stay the lightweight backlog and decision surface: close an issue once its decision is made and recorded, not after an OpenSpec/beads handoff.

## Platform
- **Hosting:** micro.blog (Hugo-based)
- **micro.blog supports up to:** Hugo 0.158
- **Theme compatible with:** Hugo 0.159

## Architecture
- Hugo theme (layouts + static assets only — no full site here)
- Frontend built with webpack: SCSS via sass-loader, PureCSS grid, Phosphor Icons
- `npm run build` compiles frontend assets into `static/`

## Testing
A minimal test site lives in `testsite/`. To test the theme against your local Hugo:

```sh
hugo --source testsite --themesDir ../..
```

This builds the theme with dummy content. Any template errors, deprecations, or
incompatibilities will show up in Hugo's output.

The test site includes stub partials for templates micro.blog normally provides
(`microblog_head.html`, `reply-by-email.html`).

After building frontend (npm run build), pause for the test blog upload before continuing.
Final verification happens on the Micro.blog test instance.

## Build and Deployment
- NO CI/CD pipeline exists for this project.
- Webpack-generated assets in `static/` MUST be committed to git. After `npm run build`, always commit the updated `static/` files.
- The repo must be in final deployable form at all times.

### Remotes
- **`origin` → Forgejo (private).** All everyday git — `push`, `pull`, `fetch`, branch work — targets Forgejo only. Forgejo is trusted: access is limited to the proprietor.
- **`github` → the public GitHub repo.** micro.blog renders the live site from GitHub's `main`, so **publishing to production = pushing `main` to `github`.** Reached only through the deploy gate below; never `git push github` by hand.

### Publishing (`just deploy`)
Production deploys are gated to keep the proprietor's real identity off the public repo. Run from `main` with a clean tree: `just deploy` fetches `github`, runs `scripts/deploy-preflight.sh`, and pushes `main` to `github` only if the gate passes — fail closed otherwise. `just preflight` runs the same check without publishing.

The gate inspects every commit in `github/main..main`:
- **Identity allowlist** — author *and* committer of each commit must be `Contrariwis3 <contrariwise@thewizardly.com>`.
- **Content + message denylist** — forbidden real-identity strings must not appear in published file contents (tip tree plus lines introduced in the range) or in commit messages.

Forbidden strings live in `.deploy-guard/forbidden.txt`, which is **gitignored and never published** — so it is absent from a fresh clone. Recreate it before the first deploy or the gate fails closed. `just test` runs `scripts/test-deploy-preflight.sh`, which covers the gate's behavior. Content scanning covers live files and lines introduced in the published range, not every historical blob ever removed.

## Micro.blog Limitations
- Micro.blog does NOT support image files in themes (even in static/)
- Images must be hosted externally (e.g., on static.thewizardly.com subdomain)
- Other static assets like fonts work fine
- CopyWebpackPlugin configuration kept in place for future non-image assets
