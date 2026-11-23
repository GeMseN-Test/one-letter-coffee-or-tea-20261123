#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A", to /output/entry.txt.

"A" stands for coffee. Why coffee, not tea:
  - Coffee is the morning ritual: bitter but honest, the fuel that turns
    a person into a functioning human before work starts.
  - It is the more vivid choice — hot, bitter, aromatic, you can feel it.
  - It is the funnier choice — "don't talk to me before my first coffee"
    is a rule millions of people genuinely live by.
  - It is the truer choice — tea waits patiently; coffee gets up and works.
"A" is also the first letter: the first cup of the day.

The output is deterministic: the same single byte every run.
Verified by running twice and comparing sha256 hashes — identical.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
