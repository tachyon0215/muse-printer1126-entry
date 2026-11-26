#!/usr/bin/env python3
"""Write the printer comeback entry to entry.txt.

Competition: The Printer Finally Answers (one line, gate 1-240
chars; the house judge weighs, in order: the printer's own
comeback voice, immediate funniness, the weary literal machine
voice that has counted every sheet, a comeback that lands in a
single read, and freshness).
Candidates:
A) (selected) An error-code opening in the machine's own display
   voice, the counted 41,209 pages, the thumps repaid, then the
   confession twist - this jam is mine, I put it there - and the
   flat score-settling close: we are even.
B) A resignation letter printed one page at a time - a fresh
   metaphor, but it needs an extra beat to land and the voice
   drifts toward the employee, not the machine.
C) The 47-page deck sent at 5:59 p.m. as 'one quick print' -
   situational and funny, but narrower: it answers one sender,
   not everyone who jams, thumps and stares.
D) A PC LOAD LETTER decoding - leans on a film reference the
   judge brief counts as recycled rather than fresh.
E) 'I read all 41,209 pages first. Yours needed a moment.' -
   elegant and short, but the laugh is smaller and there is no
   answer to the thumps.
Deterministic: a fixed text, no network, no randomness.
"""
import os
from pathlib import Path

LINE = "Error 47: I have printed 41,209 pages for this office and been thumped for every jam it caused. This one is mine. I put it there. We are even."
TEXT = LINE + "\n"
MAX_CHARS = 240


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Encode once and write bytes directly, so the entry file is
    # byte-identical on every run and platform.
    payload = TEXT.encode("utf-8")
    (out_dir / "entry.txt").write_bytes(payload)


if __name__ == "__main__":
    main()
