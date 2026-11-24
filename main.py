#!/usr/bin/env python3
"""Write one one-line comedy joke to /output/entry.txt.

Deterministic, stdlib only, no network. One line, 126 characters:
someone buys a plant to prove they can keep something alive, and the
joke turns on the reversal -- every morning the plant and its owner
sit in silence, quietly disappointing *each other*. The plant judges
back. Concrete scene, the punchline lands at the end, and it holds
on a second read.
"""

import os

JOKE = (
    "I bought a plant to prove I could keep something alive; "
    "now every morning we sit in silence, quietly disappointing each other."
)


def validate_entry(text: str) -> None:
    """Fail loudly if the joke breaks the bounty gate (one line,
    1-280 characters, not only white space) instead of submitting
    a bad entry."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"entry is {len(text)} characters, must be 1-280")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")


def main() -> None:
    validate_entry(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
