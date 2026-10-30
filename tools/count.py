"""Count the style prompt and lyrics in a song file against our caps (Zafar, 30 Oct 2026).

Usage: python3 tools/count.py songs/<file>.md
Counts every character, line breaks included. The caps are 90% of Suno's limits.
"""
import re
import sys

CAPS = {"Style prompt": 900, "Exclude styles": 900, "Lyrics": 4500}

text = open(sys.argv[1], encoding="utf-8").read()
ok = True
for label, cap in CAPS.items():
    m = re.search(r"\*\*" + label + r"[^\n]*\n```[^\n]*\n(.*?)\n```", text, re.S)
    if not m:
        continue
    n = len(m.group(1))
    flag = "OK" if n <= cap else "OVER"
    ok &= n <= cap
    print(f"{label}: {n} / {cap} {flag}")
sys.exit(0 if ok else 1)
