#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — deterministic entry writer.

Writes one fixed line (the phone's last words as its battery hits
1 percent) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The program is fully deterministic: no clock, no randomness, no network,
no file reads. Every run produces byte-identical output.
"""

import os

ENTRY = "I'm dying the way I lived: ignoring the low-battery warning for six hours straight. Worth it."

# Gate: entry.txt must be UTF-8 text of 1 to 199 characters, not only
# whitespace. This line is 93 characters; guard it so a future edit
# cannot silently break the gate.
assert 1 <= len(ENTRY) <= 199 and ENTRY.strip(), "entry violates the 1-199 character gate"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
