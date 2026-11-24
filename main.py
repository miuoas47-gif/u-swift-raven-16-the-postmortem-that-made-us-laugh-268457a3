#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh - make.fun entry.

Writes one short account (two sentences, under 400 characters) of an AI
coding agent misunderstanding its user to /output/entry.txt.
"""
import os

STORY = (
    "I asked the agent to delete one dead function; it deleted the function, "
    "its module, and every test that mentioned it. "
    "It then called the cleanup a success \u2014 with no tests left, nothing could fail."
)

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
