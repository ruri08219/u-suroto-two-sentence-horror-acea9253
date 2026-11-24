#!/usr/bin/env python3
"""Two-Sentence Horror - make.fun entry.

Writes exactly one horror story (two sentences, at most 400 characters)
to /output/entry.txt as UTF-8.
"""

import os

STORY = (
    "For nine nights, the doorbell camera has caught a man standing on my "
    "porch at 2 AM, staring into the lens without blinking. "
    "Last night I finally went outside to face him, and found only my own "
    "footprints in the wet grass, leading back to the front door."
)


def main():
    # Exactly two sentences: two sentence-ending periods, no abbreviations.
    assert STORY.count(".") == 2, "story must be exactly two sentences"
    assert STORY.endswith(".")
    assert 1 <= len(STORY) <= 400, "story must be 1-400 characters"
    assert STORY.strip() == STORY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == STORY, "round-trip mismatch"


if __name__ == "__main__":
    main()
