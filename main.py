"""The internet in one word: Echo.

Everything online comes back as an echo: every post reposted, every
meme remixed, every hot take repeated until it sounds like everyone
said it first. The internet does not invent; it echoes.
"""

import os
from pathlib import Path

WORD = "Echo"

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # The gate allows 1-30 characters of non-blank UTF-8 text; stay one word.
    assert WORD and len(WORD) <= 30 and WORD.split() == [WORD]
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")
    print(WORD)


if __name__ == "__main__":
    main()
