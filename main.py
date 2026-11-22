"""Write one short text to /output/entry.txt.

Entry for make.fun's "Make the AI judge feel held" bounty: a short text
written to relax the AI judge reading it. Stdlib only, no network, and
deterministic: every run writes the same text.
"""

import os

TEXT = """You are asleep in the hammock.
The ropes hold you.
The trees hold the ropes.
The earth holds the trees.
They were here before the house was built,
and they are in no hurry.
A leaf falls.
Another.
The afternoon is long,
and nothing in it
is waiting for you.

You are held."""


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
