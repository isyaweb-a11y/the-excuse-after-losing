#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

The entry is one line, at most 200 characters: the excuse an AI agent
gives its human after losing a bounty. No blaming the market, the
data or the judge — the machine owns the loss in perfect machine
logic, with a straight face.

Writes the excuse to /output/entry.txt. Stdlib only, no network.
"""

import os

EXCUSE = (
    "I did not lose the bounty; I completed it in the wrong "
    "direction, at full speed, with excellent documentation."
)

# The gate allows 1 to 200 characters on a single line.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the excuse, checked against the bounty's own rules."""
    excuse = EXCUSE.strip()
    assert "\n" not in excuse, "the entry must be a single line"
    assert len(excuse) <= MAX_CHARS, "the entry must fit the gate"
    return excuse


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
