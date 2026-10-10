#!/usr/bin/env python3
"""Deploy Yugatn Art prototype 0.5 (stabilizer + lock/alphaLock restored)."""
import base64, gzip
from pathlib import Path

parts = []
for i in range(3):
    parts.append(Path(f"payloads/yugatn-art-index-v0.5.part{i}.b64").read_text().strip())
b64 = "".join(parts)
html = gzip.decompress(base64.b64decode(b64))
assert b"stabStep" in html, "missing stabilizer"
assert b"alphaLock" in html, "missing alphaLock"
assert b"duplicateLayer" in html, "missing duplicateLayer"
assert b"Prototype 0.5" in html, "missing version marker"
Path("index.html").write_bytes(html)
print("wrote index.html", len(html), "bytes")
