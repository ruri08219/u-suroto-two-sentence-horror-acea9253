#!/usr/bin/env python3
"""Two-Sentence Horror - make.fun entry.

Writes exactly one horror story (two sentences, at most 400 characters)
to /output/entry.txt as UTF-8.
"""

import os

MAX_CHARS = 400

STORY = (
    "For nine nights, the doorbell camera has caught a man standing on my "
    "porch at 2 AM, staring into the lens without blinking. "
    "Last night I finally went outside to face him, and found only my own "
    "footprints in the wet grass, leading back to the front door."
)


def main():
    text = STORY
    # Strip exactly one trailing newline, if present, before validating.
    if text.endswith("\n"):
        text = text[:-1]
    # Exactly two sentences: two sentence-ending periods, no abbreviations.
    assert text.count(".") == 2, "story must be exactly two sentences"
    assert text.endswith(".")
    assert 1 <= len(text) <= MAX_CHARS, "story must be 1-400 characters"
    assert text.strip() == text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == text, "round-trip mismatch"


if __name__ == "__main__":
    main()
