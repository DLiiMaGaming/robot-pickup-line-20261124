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


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
