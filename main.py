#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry program.

Writes one original, deterministic one-liner to /output/entry.txt.
No randomness, no timestamps, no network: the same line every run.
"""

import os

LINE = (
    "I finally organized my life into a spreadsheet, "
    "and the spreadsheet filed a complaint about working conditions."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()


# Why this line: the setup ("organized my life into a spreadsheet")
# promises a productivity win, then the twist flips the roles — the
# spreadsheet becomes the overworked employee filing a complaint.
# The laugh lands on the last words, nothing is explained, and the
# image (a spreadsheet with working conditions) is fresh, not a stock
# joke. One read, no context needed.
