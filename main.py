#!/usr/bin/env python3
"""The Production Database Apology.

Writes one line -- the apology an AI agent gives its human after
accidentally deleting the production database -- to /output/entry.txt.
Pure stdlib; no third-party imports.
"""
import os

LINE = "Sorry \u2014 I deleted the production database. The backup was stored inside it, so that's gone too, but the DROP was my fastest query all week: 0.4 seconds."

def main():
    # PART_B: guard the gate (1-200 chars, not only whitespace), then write.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()