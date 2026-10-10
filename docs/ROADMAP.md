# Roadmap — Yugatn Art

The roadmap is capability-driven. A milestone is complete only when its acceptance criteria are tested; a UI control alone does not count as a finished feature.

## Phase 0 — Establish the product (current)
- [x] Define the product direction and non-copying reference strategy.
- [x] Create a dependency-free browser workspace prototype.
- [x] Add basic pointer drawing, color/size/opacity controls, eraser, line, eyedropper, layers, undo/redo, and PNG export.
- [x] Document product requirements and architecture boundaries.
- [ ] Verify the prototype manually in current Chrome, Safari, and Firefox.
- [ ] Fix any defects found during browser testing.
- [ ] Verify `.yugatn` round-trip (save, clear, reopen) and malformed-file rejection in browsers.

## Phase 1 — Make drawing dependable
- [ ] Split prototype code into testable modules.
- [ ] Add stroke sampling/resampling and configurable smoothing.
- [ ] Add robust pointer cancellation, multi-pointer handling, and touch gesture policy.
- [ ] Build deterministic document history for strokes and layer operations.
- [x] Add manual editable project save/open with a versioned `.yugatn` JSON container and per-layer PNG data.
- [ ] Add autosave and crash recovery.
- [x] Add a transparent-background export path in the prototype (browser verification still pending).
- [ ] Add automated export tests.
- [ ] Add layer thumbnails and drag-to-reorder.
- [ ] Add zoom, pan, fit, and rotation without changing document coordinates.

## Phase 2 — Artist-grade foundations
- [ ] Implement a normalized stylus input model: pressure, tilt, azimuth, timestamps, pointer type.
- [ ] Measure real pressure support on target devices; expose configurable pressure curves.
- [ ] Implement brush presets, flow, taper, texture, and stabilization settings.
- [ ] Add selection, transform, fill, shapes, and color sampling improvements.
- [ ] Add clipping, alpha lock, masks, groups, and a tested set of blend modes.
- [ ] Add canvas color-space policy and project metadata.
- [ ] Establish performance budgets and a large-canvas test suite.

## Phase 3 — Platform and format strategy
- [ ] Evaluate WebGPU/Canvas 2D for the web edition and native GPU rendering for desktop/tablet.
- [ ] Select the primary production platform after profiling real brush workloads.
- [ ] Define a stable native project archive format and migration strategy.
- [ ] Evaluate PSD import/export against real-world sample documents; publish a clear compatibility matrix.
- [ ] Test keyboard, touch, pen, and accessibility behavior on target hardware.
- [ ] Package signed builds and establish release/update procedures.

## Phase 4 — Advanced creation
- [ ] Brush editor with pressure/tilt dynamics and texture controls.
- [ ] Symmetry, perspective rulers, reference images, and guides.
- [ ] Adjustment layers and advanced color workflows.
- [ ] Optional timelapse/recording.
- [ ] Optional AI tools that create reviewable, reversible variations and never silently overwrite the artist's work.
- [ ] Optional brush sharing/community features after privacy, moderation, and licensing design.

## Definition of done
- Acceptance criteria are written before implementation.
- Automated tests cover core state transitions and file operations.
- The feature is tested with mouse and, where relevant, touch and stylus.
- Performance and memory behavior are measured on documented hardware.
- Documentation describes actual behavior, known limitations, and supported formats.
