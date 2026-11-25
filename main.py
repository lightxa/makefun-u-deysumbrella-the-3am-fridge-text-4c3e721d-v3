"""The 3AM Fridge Text (variant 3): the one line a smart fridge texts
its owner at 3am.

Fresh angle, different from variant 1 (the hum since 2019) and variant 2
(something moved in the crisper drawer): the fridge catches its owner
standing in front of it in the dark, and drafts the pickles as witnesses.
Deadpan machine voice, one concrete physical scene opened mid-moment,
addressed to "you", closing on the lingering image of the pickles having
seen everything. No milk, no ice, no door left open.
"""

# The entry: one line, written exactly as-is to /output/entry.txt.
ENTRY_LINE = (
    "It's 3am. You're standing here in the dark again, and I just want "
    "you to know the pickles saw everything."
)


def write_entry(line: str) -> None:
    """Write exactly the line to /output/entry.txt, no trailing newline.

    Guard the kit gate (UTF-8 text, 1 to 140 characters, not only
    whitespace) so a future edit cannot silently break the contract.
    """
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    write_entry(ENTRY_LINE)
    print(ENTRY_LINE)
