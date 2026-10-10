# Test log — Yugatn Art

**Last code update reviewed:** 2026-10-10  
**Test execution status:** NOT RUN in a real browser or stylus device during this implementation pass. No pass is claimed.

## Repository observations

- Default branch: `main`.
- A GitHub Pages workflow exists at `.github/workflows/pages.yml` and is triggered by pushes to `main`/ `master` or manual dispatch.
- The repository owner reported that the Pages URL currently returns 404. The latest Pages deployment run failed at Configure Pages: the GitHub API returned `Not Found` for the Pages site and `Resource not accessible by integration` when attempting to create it. This requires enabling Pages in repository Settings or granting appropriate repository permissions; the workflow cannot self-enable it with its current token.
- Check **Settings → Pages** and **Actions → Deploy static prototype to GitHub Pages**. If Pages is not enabled, select GitHub Actions as the build/deployment source and rerun the workflow.
- The current repository prototype is a single `index.html`; modularization remains pending.
- A new `Validate prototype source` GitHub Actions workflow checks inline JavaScript syntax and required UI controls on pushes and pull requests. The workflow result must be inspected after this commit; adding the workflow is not itself a passing test.

## Features implemented in code, awaiting execution

- Editable project save/open using version-1 `.yugatn` JSON with base64 PNG data per layer.
- Debounced local autosave in IndexedDB and startup attempt to restore the last saved draft.
- Canvas zoom via wheel, pan via Space+drag, and fit/reset.
- Pressure response curve control for pointer pressure reported by a stylus.
- Autosave hooks for strokes and common layer/settings changes.
- A four-entry pixel-snapshot undo history limit.
- Layer lock, alpha lock, duplicate, up/down reordering, and solo-active-layer controls.

## Test results

| Test | Result | Evidence |
|---|---|---|
| Static source update present on `main` | OBSERVED | GitHub contents API returned the updated `index.html` after commits |
| Browser syntax/runtime | NOT RUN | No browser execution available in this pass; CI syntax workflow added but result not yet inspected |
| Chrome/Safari/Firefox drawing | NOT RUN | No browser/device test log supplied |
| `.yugatn` round-trip | NOT RUN | Manual checklist pending |
| IndexedDB reload recovery | NOT RUN | Manual checklist pending |
| Zoom/pan interactions | NOT RUN | Manual checklist pending |
| Real stylus pressure | NOT TESTED | Requires supported physical stylus/browser |
| Layer lock/alpha lock/duplicate/reorder/solo | NOT RUN | Implemented in source; manual verification pending |
| GitHub Pages deployment | BLOCKED | Latest run failed at Configure Pages: Pages site not found and integration cannot create it; enable Pages in repository Settings |

## Next test pass

Run every applicable item in `docs/TESTING.md`, record browser and OS versions, and attach reproducible defects before marking a feature complete.