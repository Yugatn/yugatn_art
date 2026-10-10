#!/usr/bin/env python3
"""Deploy Yugatn Art prototype 0.4 (stabilizer + layer ops)."""
import base64, gzip
from pathlib import Path
B64 = Path("payloads/yugatn-art-index-v0.4.gz.b64").read_text().strip()
html = gzip.decompress(base64.b64decode(B64))
Path("index.html").write_bytes(html)
print("wrote index.html", len(html), "bytes")
