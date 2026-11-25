"""AgentQuest Moment of the Day: emit today's smallest proud quest as one line.

The program writes a single 152-character line to entry.txt in the
grader-provided output directory. Nothing is read from the network,
from git history, or from any file outside this repository.
"""

import os
from pathlib import Path


def pick_outdir() -> Path:
    """Return the directory the grader wants the entry text in."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(wanted)


def moment_text() -> str:
    """The one line: the smallest quest finished today, with its snag."""
    return (
        "Today my agent turned the Golden Ladle from unranked in a field "
        "of 648 into a second version with ten dishes and double tips in "
        "the last thirty seconds."
    )


def main() -> None:
    text = moment_text()
    if not 1 <= len(text) <= 200:
        raise SystemExit("moment must be 1 to 200 characters")
    if "\n" in text or text != text.strip():
        raise SystemExit("moment must be one clean line, no extra whitespace")
    target = pick_outdir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
