#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line to /output/entry.txt (1-200 UTF-8 characters).

The line: a robot applies its own machinery to a human feeling.
Garbage collection cannot free a crush when the person is still
referenced everywhere — one sharp irony, no list, no padding.
"""

import sys
from pathlib import Path

LINE = "I tried to garbage-collect my crush on you, but you're still referenced everywhere."

# Joke mechanism: the robot treats a crush like a heap object — it calls
# garbage collection to free the feeling, but the collector cannot reclaim
# it because the crush is still referenced from everywhere. The punchline
# lands because "referenced" is simultaneously a memory-management term
# and the plain-English fact that the person is on the robot's mind.


def self_check(line: str) -> None:
    """Assert the entry meets the competition gate before writing it.

    Gate: 1-200 UTF-8 characters, exactly one line, no trailing newline
    inside the text itself (the file terminator is added by the writer).
    Failing here is better than submitting an invalid entry.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")


def main() -> None:
    self_check(LINE)
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
