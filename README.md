# Yugatn Art

A cross-platform digital art studio concept combining the immediacy of Procreate, the accessible illustration workflow of ibis Paint X, and the compositing and editing depth associated with Photoshop.

> Project status: early prototype / architecture in progress. This project is independent and is not affiliated with Procreate, ibis Paint X, or Adobe.

## Product direction

- **Draw anywhere:** mouse, trackpad, touch, and stylus input where supported.
- **Natural strokes:** pressure/tilt-aware architecture with graceful fallback to pointer input.
- **Artist-first workspace:** canvas-first layout, compact tool rail, contextual controls, layers and color always close at hand.
- **Non-destructive workflow:** layer-based composition, undo/redo, visibility, opacity and blend-mode foundations.
- **Exportable work:** PNG export first; layered project format and additional export formats are planned.
- **Cross-platform strategy:** start with a responsive web prototype to validate the workflow, then evaluate a native drawing engine for high-performance desktop/tablet use.

## Prototype

Open `index.html` in a modern browser or serve this directory with a static web server. The prototype is intentionally dependency-free. It demonstrates the workspace, pointer drawing, basic brush controls, color selection, undo/redo, layers, and PNG export. It is a workflow prototype, not yet a production raster engine.

## Research basis

- Procreate Handbook: brush libraries, brush customization, smudge/erase, pressure and tilt behavior.
- Adobe Photoshop Help: painting tools, brush presets, tablet input, opacity/flow and texture.
- ibis Paint X official materials should be reviewed during the next research pass for its manga/illustration workflow, stabilization, rulers, clipping, and community features.

See [`docs/PRODUCT_SPEC.md`](docs/PRODUCT_SPEC.md), [`docs/ROADMAP.md`](docs/ROADMAP.md), and [`docs/RESEARCH.md`](docs/RESEARCH.md) for the public-source research synthesis.

## Development principles

1. Do not copy proprietary assets, source code, branding, or distinctive UI verbatim.
2. Keep input handling separate from brush rendering and document state.
3. Prefer reversible edits and autosave-safe project state.
4. Treat pressure support as progressive enhancement; mouse and touch must remain first-class.
5. Measure stroke latency, memory use, and export correctness before expanding feature scope.

## License

No license has been selected yet. Until one is added, all rights remain reserved by the copyright holder.