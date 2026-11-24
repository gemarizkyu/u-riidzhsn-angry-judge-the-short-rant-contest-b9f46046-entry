"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. The rant is a fixed original text: no clock, no
randomness, no network, no model calls, nothing read from outside
this file. 332 characters, inside the 1-400 gate.
"""

from pathlib import Path

RANT = (
    # One concrete annoyance (the self-checkout), told in short beats
    # that escalate: accusation, alarm, summon, one-button rescue,
    # then the punch that the purchase happened in my head minutes ago.
    # No throat-clearing, no list of complaints, one scene only.
    "I bought one bag of rice. The self-checkout yelled "
    "UNEXPECTED ITEM IN THE BAGGING AREA like I'd smuggled in a goose. "
    "A red light spun. A recorded voice summoned a human. "
    "The human pressed one button, sighed, and walked off. "
    "The machine, satisfied, finally let me pay for the rice I had "
    "already paid for in my head three minutes ago."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = RANT.strip()
    if not text:
        raise ValueError("rant is empty")
    if len(text) > 400:
        raise ValueError(f"rant is {len(text)} characters, over the 400 limit")
    if text != text.strip():
        raise ValueError("rant has leading or trailing whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
