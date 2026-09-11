"""Replayable check: IW-X arXiv source contains no stem-49 hidden-2 ambiguity.

Reads the local IW-X arXiv source tree (.tmpwork/iwxsrc/, e-print 2001.04511v3)
with stdlib only and asserts:
  1. Table tab:order row 49 is single-valued (2-primary v1-torsion trivial,
     no 'or' alternative).
  2. Hidden-2 / null-hidden-2 / possible-hidden-2 tables contain no stem-49
     entry (comments stripped).
  3. No stem-49 row in the d4 / d5 / higher Adams differential tables
     (comments stripped).

Run: python3 output/artifacts/verify_stem49.py
Expected: VERIFY_OK
"""
import re
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
SRC = LANE / ".tmpwork" / "iwxsrc"
TABLES = SRC / "more-stable-stems-tables.tex"
INTRO = SRC / "more-stable-stems-intro.tex"


def strip_comments(text):
    return "\n".join(
        (ln.split("%")[0] for ln in text.split("\n"))
    )


def table_seg(text, label):
    i = text.find(label)
    if i < 0:
        raise AssertionError(f"label not found: {label}")
    j = text.find("\\end{longtable}", i)
    return text[i:j]


def stems(seg):
    return sorted({int(m.group(1)) for m in re.finditer(r"\$\((\d+),", seg)})


def main():
    t = TABLES.read_text()
    intro = INTRO.read_text()
    tc = strip_comments(t)

    # 1. order-table row 49
    m = re.search(r"^\$49\$.*$", intro, re.M)
    assert m, "row $49$ not found in intro"
    row49 = m.group(0)
    assert " or " not in row49 and " or$" not in row49, f"row 49 ambiguous: {row49}"
    assert r"$\mydot$" in row49, f"row 49 2-primary cell unexpected: {row49}"

    # 2. hidden-2 tables (comments stripped)
    hid = stems(table_seg(tc, "Hidden $2$ extensions \\label"))
    null = stems(table_seg(tc, "Some null hidden $2$ extensions"))
    poss_seg = table_seg(tc, "Possible hidden $2$ extensions")
    poss = stems(poss_seg)
    assert 49 not in hid + null + poss, (hid, null, poss)

    # 3. Adams differential tables: no unresolved stem-49 differential rows.
    #    (The E2-generator table legitimately lists stem-49 E2 classes; the
    #    check is that the d4/d5/higher differential tables and the
    #    possible-hidden-2 list carry no stem-49 entry, i.e. no citable
    #    unresolved stem-49 witness pair.)
    diff_labels = [
        "$\\C$-motivic Adams $d_4$ differentials",
        "$\\C$-motivic Adams $d_5$ differentials",
        "$\\C$-motivic higher Adams differentials",
    ]
    diff_counts = {}
    for lab in diff_labels:
        seg = strip_comments(table_seg(tc, lab))
        n = len(re.findall(r"\(\s*49\s*,", seg))
        diff_counts[lab] = n
        assert n == 0, f"stem-49 row in {lab!r}: {n}"

    print("row49:", row49[:120])
    print("hidden-2 stems:", hid)
    print("null-hidden-2 stems:", null)
    print("possible-hidden-2 stems:", poss)
    print("Adams d4/d5/higher stem-49 rows: 0 each", diff_counts)
    print("VERIFY_OK")


if __name__ == "__main__":
    sys.exit(main())
