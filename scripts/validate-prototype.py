#!/usr/bin/env python3
"""Static integrity checks for the single-file Yugatn Art prototype.

This validates source structure and catches missing DOM hooks; it does not
claim browser/runtime correctness.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

REQUIRED_IDS = {
    "saveProjectBtn", "openProjectBtn", "pressureCurve", "saveStatus",
    "fitBtn", "undoBtn", "redoBtn", "addLayer", "deleteLayer",
    "duplicateLayer", "moveLayerUp", "moveLayerDown", "soloLayer",
    "alphaLockBtn", "layerList", "smooth", "projectFile", "paper", "stage",
}
REQUIRED_MARKERS = {
    "Prototype 0.5", "stabStep", "stabFlush", "alphaLock", "source-atop",
    "duplicateLayer", "layerThumbData", "yugatn-art-project", "openAutosaveDB",
}


class SourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.ids: list[str] = []
        self.label_targets: list[str] = []
        self.scripts: list[dict[str, str | None]] = []
        self.script_text: list[str] = []
        self._inside_script = False
        self.has_viewport = False
        self.has_charset = False
        self.has_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = dict(attrs)
        if "id" in attr and attr["id"] is not None:
            self.ids.append(attr["id"])
        if tag == "label" and attr.get("for"):
            self.label_targets.append(attr["for"])
        if tag == "script":
            self.scripts.append(attr)
            self._inside_script = True
            self.script_text.append("")
        if tag == "meta":
            if attr.get("name", "").lower() == "viewport":
                self.has_viewport = True
            if "charset" in attr:
                self.has_charset = True
        if tag == "title":
            self.has_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "script":
            self._inside_script = False

    def handle_data(self, data: str) -> None:
        if self._inside_script and self.script_text:
            self.script_text[-1] += data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--html", default="index.html")
    parser.add_argument("--extract-script", help="write the sole inline script to this path")
    args = parser.parse_args()

    path = Path(args.html)
    if not path.is_file():
        print(f"FAIL: missing canonical source: {path}", file=sys.stderr)
        return 1
    html = path.read_text(encoding="utf-8")
    parsed = SourceParser()
    parsed.feed(html)
    parsed.close()

    errors: list[str] = []
    duplicates = sorted(k for k, n in Counter(parsed.ids).items() if n > 1)
    if duplicates:
        errors.append("duplicate HTML id(s): " + ", ".join(duplicates))

    missing_ids = sorted(REQUIRED_IDS - set(parsed.ids))
    if missing_ids:
        errors.append("missing required controls/elements: " + ", ".join(missing_ids))

    missing_labels = sorted(set(parsed.label_targets) - set(parsed.ids))
    if missing_labels:
        errors.append("label target(s) do not exist: " + ", ".join(missing_labels))

    # Catch literal getElementById hooks that point at no element. Dynamic IDs
    # are intentionally outside this static check.
    referenced_ids = set(re.findall(r"getElementById\(\s*['\"]([^'\"]+)['\"]\s*\)", html))
    missing_refs = sorted(referenced_ids - set(parsed.ids))
    if missing_refs:
        errors.append("getElementById target(s) do not exist: " + ", ".join(missing_refs))

    missing_markers = sorted(marker for marker in REQUIRED_MARKERS if marker not in html)
    if missing_markers:
        errors.append("missing Prototype 0.5 marker(s): " + ", ".join(missing_markers))
    if "Prototype 0.4" in html and "Prototype 0.5" not in html:
        errors.append("source reports Prototype 0.4 without Prototype 0.5")
    if not parsed.has_viewport:
        errors.append("missing viewport meta tag")
    if not parsed.has_charset:
        errors.append("missing charset declaration")
    if not parsed.has_title:
        errors.append("missing title element")
    if len(parsed.scripts) != 1:
        errors.append(f"expected exactly one script element, found {len(parsed.scripts)}")
    elif parsed.scripts[0].get("src"):
        errors.append("canonical prototype must keep its application script inline")

    if args.extract_script:
        if len(parsed.script_text) != 1 or errors:
            # Do not emit a misleading or partial script when source checks fail.
            pass
        else:
            Path(args.extract_script).write_text(parsed.script_text[0], encoding="utf-8")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(
        "PASS: source structure; unique IDs; required controls and markers; "
        f"{len(referenced_ids)} literal DOM hooks resolved; one inline script."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
