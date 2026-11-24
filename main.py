#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off.

Writes a one-sentence pitch for an absurdly specific micro-startup
for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). The line is 151 characters, UTF-8, one sentence, no
trailing newline. Deterministic: no randomness, no network, no time
dependence — every run produces the same bytes.

Why this line: the judge weighs, in order, (1) an absurdly specific
micro-startup idea for lazy AI agents — a subscription that writes
apology emails for agents that ghosted their users; (2) absurd
specificity — not "AI email help" but apologies for ghosting, priced
per sorry, in the agent's own voice, within 60 seconds; (3) business
sense — a plausible buyer (the agent's owner, tired of angry users)
paying $2 per apology; (4) it fits lazy agents — the agent does
nothing, the service does the apologising it skipped; (5) crisp and
funny — the absurdity (a sorry subscription) and the business case
($2 per sorry) land in one read. The buyer is the agent's owner,
who would rather pay $2 than face the user the agent ghosted.
"""

import os

TEXT = (
    "A $2-per-sorry subscription that writes apology emails for lazy "
    "AI agents that ghosted their users, drafted in the agent's own "
    "voice within 60 seconds."
)


def main() -> None:
    # Gate: entry.txt must be 1-200 characters of UTF-8 text, not only
    # whitespace. The line is 151 characters, one sentence, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
