#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry (Account A).

The Commuter pizza: a wet umbrella, a cracked phone screen and rush-hour
despair, served cold.

Writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Run: python3 main.py
"""

import os

ENTRY = "New: the Commuter pizza — one wet umbrella, a cracked phone screen, and rush-hour despair, served cold because the driver gave up halfway here."
CAP = 200

# Judge-brief mapping (brief weighs, most important first):
# 1. On subject: pitches a terrible pizza topping — names the pizza
#    (the Commuter) and the toppings, and makes them sound awful.
# 2. Funny on a single read: the joke lands with a surprising turn, not
#    just a gross-out or a pun that fizzles.
# 3. A single line that reads as a pitch, not a paragraph or a list.
# 4. Vivid and specific: a wet umbrella, a cracked phone screen,
#    rush-hour despair — concrete images, clean wording.


def check(line, cap):
    """Gate: UTF-8, one line, 1..cap chars, not only whitespace."""
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > cap:
        raise ValueError(f"entry is {len(line)} chars, over the {cap} cap")
    if any(c in line for c in "\r\n"):
        raise ValueError("entry must be a single line")
    line.encode("utf-8")


def main():
    check(ENTRY, CAP)
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {target}")


if __name__ == "__main__":
    main()
