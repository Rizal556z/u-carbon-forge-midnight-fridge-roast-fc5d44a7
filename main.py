"""Midnight Fridge Roast — one-line roast of a smart fridge that locks after midnight.

Writes the roast to /output/entry.txt (exactly one line, 1-200 characters).
Pure Python standard library, no network, no secrets.
"""

import os

ENTRY = (
    "My fridge locks at midnight like the leftovers filed a restraining order "
    "\u2014 mate, I bought you, and I bought everything inside you."
)


def main() -> None:
    # Validation gate: the sealed scorer requires 1-200 chars, one line,
    # not only whitespace. Fail loudly here rather than shipping a bad entry.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be exactly one line"
    assert text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
