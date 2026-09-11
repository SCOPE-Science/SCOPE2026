#!/usr/bin/env python3
"""Bounded fallback attempt: valuable partial target on stem 46.

Attempts the survey-profile valuable partial target -- "a proved motivic
differential on the stem-46 lift with logged classical Ext-cycle survival
check" -- against the audit-plan source (IW-X arXiv:2001.04511 v3 unpacked
at scratch/iwx/). Enumerates every stem-46 row in each differential /
extension table, flags any '?' or undecided entry, checks the uncertainty
registries (higher differentials, possible hidden extensions) for stem 46,
and reports BLOCKED when every stem-46 coordinate is already decided.

Replay (from lane root): python3 output/artifacts/check_stem46.py
Stdlib only. Exit 0 always; machine-readable report printed as JSON,
human verdict on the last line.
"""
import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
TABLES = BASE / "scratch" / "iwx" / "more-stable-stems-tables.tex"
INTRO = BASE / "scratch" / "iwx" / "more-stable-stems-intro.tex"


def sections(text):
    labels = [(m.group(1), m.start())
              for m in re.finditer(r"\\label\{(tab:[^}]+)\}", text)]
    out = {}
    for i, (name, s) in enumerate(labels):
        e = labels[i + 1][1] if i + 1 < len(labels) else len(text)
        out[name] = text[s:e]
    return out


def rows_in(chunk):
    """Yield (stem, rowtext) for each table row opening with $(s,...)."""
    for m in re.finditer(r"\$\((\d+),\s*\d+(?:,\s*\d+)?\)\$", chunk):
        end = chunk.find("\\\\", m.end())
        row = chunk[m.start(): end if end != -1 else m.end() + 200]
        yield int(m.group(1)), " ".join(row.split())


def main():
    t = TABLES.read_text()
    intro = INTRO.read_text()
    secs = sections(t)
    stem46 = {}
    for name, chunk in secs.items():
        hit = [r for s, r in rows_in(chunk) if s == 46]
        if hit:
            stem46[name] = hit
    qmarks = {name: [r for r in rows if "?" in r]
              for name, rows in stem46.items()}
    qmarks = {k: v for k, v in qmarks.items() if v}
    e2_status = []
    for r in stem46.get("tab:Adams-d2", []):
        cols = [c.strip() for c in r.split("&")]
        d2 = cols[2] if len(cols) > 2 else ""
        e2_status.append({"row": r[:120], "d2_blank": d2 in ("$$", "", "$", "$ $"),
                          "d2": d2[:80]})

    def stems(name):
        return sorted({s for s, _ in rows_in(secs.get(name, ""))})

    higher = stems("tab:Adams-higher")
    poss2 = stems("tab:2-extn-possible")
    poss_eta = stems("tab:eta-extn-possible")
    poss_nu = stems("tab:nu-extn-possible")
    order46 = [ln.strip()[:100] for ln in intro.splitlines()
               if re.search(r"\$46\$", ln)]
    blocked = (not qmarks and 46 not in higher and 46 not in poss2
               and 46 not in poss_eta and 46 not in poss_nu)
    report = {
        "stem46_tables": sorted(stem46),
        "n_stem46_rows": sum(len(v) for v in stem46.values()),
        "stem46_rows_with_question_mark": qmarks,
        "e2_d2_status": e2_status,
        "higher_table_stems": higher,
        "possible_2_extn_stems": poss2,
        "possible_eta_extn_stems": poss_eta,
        "possible_nu_extn_stems": poss_nu,
        "intro_order_row_46": order46,
        "intro_uncertainties_from_84": "Starting in dimension 84" in intro,
        "verdict": "BLOCKED" if blocked else "OPEN",
    }
    print(json.dumps(report, indent=1))
    if blocked:
        print("VERDICT: BLOCKED -- every stem-46 coordinate is already decided; "
              "no new motivic differential is available to prove.")
    else:
        print("VERDICT: OPEN -- undecided stem-46 material found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
