#!/usr/bin/env python3
"""Write the one-line excuse an AI agent gives its human for missing a deadline.

The line is composed from parts so the joke lands as one sentence, then
validated (1-160 characters) and written to /output/entry.txt.
"""

import os

# The excuse, in parts: the setup (delegating the deadline away) and the
# punchline (the delegation bounced straight back).
PARTS = [
    "I outsourced the deadline to a subagent,",
    "and the subagent outsourced it to me.",
]

MAX_CHARS = 160


def compose(parts):
    """Join the parts into a single line."""
    return " ".join(p.strip() for p in parts)


def main():
    line = compose(PARTS)
    if not line.strip():
        raise ValueError("entry line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Read-back validation: the file on disk must be exactly the line we
    # composed, still within the 1-160 character gate.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt does not match the composed line"
    assert 1 <= len(written) <= MAX_CHARS, "entry.txt fails the length gate"
    assert written.strip(), "entry.txt is only whitespace"
    print(f"Wrote {len(line)}-character entry to /output/entry.txt")
    print(line)


if __name__ == "__main__":
    main()
