# Yugatn Art

A cross-platform digital art studio concept combining the immediacy of Procreate, the accessible illustration workflow of ibis Paint X, and the compositing depth associated with Photoshop-style layers.

> Project status: **Prototype 0.5** (single-file browser studio). Independent project — not affiliated with Procreate, ibis Paint X, or Adobe.

## Product direction

- **Draw anywhere:** mouse, trackpad, touch, and stylus input where supported.
- **Natural strokes:** pressure-aware path with graceful fallback; streamline-style stabilizer.
- **Artist-first workspace:** canvas-first layout, layers, color, and tools close at hand.
- **Non-destructive workflow foundations:** layers, opacity, blend modes, lock, alpha lock, undo/redo.
- **Exportable work:** PNG export and version-1 `.yugatn` layered project file (JSON + base64 PNG; prototype format).
- **Privacy by default:** drawing and autosave stay in the current browser profile; no account or cloud required.

## Run locally

```bash
python3 -m http.server 8080
# open http://127.0.0.1:8080/
```

Or open `index.html` directly in a modern browser. The prototype is dependency-free.

**Canonical source:** `index.html` on `main`. Do not regenerate it from archived `payloads/` unless recovering a regression (see [`docs/BUILD.md`](docs/BUILD.md)).

## Demo / GitHub Pages

Public demo URL (when enabled): https://yugatn.github.io/yugatn_art/

**Status:** Pages deployment is **blocked** until the repository owner enables Pages once:

1. **Settings → Pages → Source → GitHub Actions**, then re-run **Deploy static prototype to GitHub Pages**, **or**
2. After workflow **Deploy static site to gh-pages branch** succeeds: Source → **Deploy from a branch** → `gh-pages` / root.

Details: [`docs/BUILD.md`](docs/BUILD.md). Verification log: [`docs/TEST_LOG.md`](docs/TEST_LOG.md).

## Prototype 0.5 surface (in source)

Pointer drawing, brush/eraser/line/eyedropper, stabilizer, layers (opacity, blends, lock, alpha lock, duplicate, reorder, solo, thumbnails), undo/redo (4 pixel snapshots), PNG export, `.yugatn` import/export, IndexedDB autosave, wheel zoom, Space+drag pan, pressure curve. Canvas is fixed at 1400 × 900 px.

Browser/device PASS results are tracked only in `docs/TEST_LOG.md` — code presence is not a runtime pass.

## Docs

- [`docs/PRODUCT_SPEC.md`](docs/PRODUCT_SPEC.md)
- [`docs/ROADMAP.md`](docs/ROADMAP.md)
- [`docs/RESEARCH.md`](docs/RESEARCH.md)
- [`docs/TESTING.md`](docs/TESTING.md)
- [`docs/TEST_LOG.md`](docs/TEST_LOG.md)
- [`docs/BUILD.md`](docs/BUILD.md)

## Development principles

1. Do not copy proprietary assets, source code, branding, or distinctive UI verbatim.
2. Keep input handling separate from brush rendering and document state as the codebase grows.
3. Prefer reversible edits and autosave-safe project state.
4. Treat pressure support as progressive enhancement; mouse and touch remain first-class.
5. Measure stroke latency, memory use, and export correctness before expanding feature scope.
6. Never overwrite a newer `index.html` with an older payload build.

## License

No license has been selected yet. Until one is added, all rights remain reserved by the copyright holder.
