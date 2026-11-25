#!/usr/bin/env python3
"""Write one short funny rant to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = (
    "The self-checkout just accused me of stealing my own spinach. "
    "I scanned it, I bagged it, I paid for it, and a robot voice still "
    "announced to the whole queue that there is an unexpected item in "
    "the bagging area. It is spinach. It costs less than a dollar, "
    "and it wilts if you look at it wrong. All that fuss, over a leaf."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
