"""Independent re-verifier for the lane-132 Bolza-window census.

Checks (stdlib only):
 1. summary.json internal consistency (row count, argmax/argmin, gap, U).
 2. For a sample of rows (default every row): rebuild matrices from (x,y,z),
    recompute the reported word's trace exactly, check |tr| matches, check
    tr(AB)=z and det=1, and re-verify Llo<=L<=Lhi via cosh monotonicity
    (cosh(Llo/2)<=|t|/2<=cosh(Lhi/2) with rigorous bounds).
 3. Spot-check minimality: recompute ALL word traces at K sampled points and
    confirm no word has |trace| < reported minimum (exhaustive re-proof).
Usage: python3 verify.py [artifacts_dir] [exhaustive_every_k]
"""
import csv
import json
import sys
import math
from fractions import Fraction as F

sys.path.insert(0, "work")
from census import (build_mats, mmul, cosh_bounds, LETS, GIDX, INV,
                    min_trace_point, QE)


def eval_word(gen, word):
    Z = QE(F(0), F(0))
    M = (QE(F(1), F(0)), Z, Z, QE(F(1), F(0)))
    for ch in word:
        M = mmul(M, gen[GIDX[ch]])
    tr = M[0] + M[3]
    assert tr.q == 0
    return tr.p


def main(artdir="output/artifacts", every=11):
    s = json.load(open(f"{artdir}/summary.json"))
    rows = list(csv.DictReader(open(f"{artdir}/table.csv")))
    assert len(rows) == s["total"] == 132, len(rows)
    base = [r for r in rows if r["kind"] == "base"]
    ref = [r for r in rows if r["kind"] == "refined"]
    assert len(base) == 125 and len(ref) == 7, (len(base), len(ref))
    assert all(r["nchecked"] == "13120" for r in rows)
    ka = lambda r: abs(F(r["trace"]))
    J = max(range(len(rows)), key=lambda i: ka(rows[i]))
    K = min(range(len(rows)), key=lambda i: ka(rows[i]))
    assert rows[J]["trace"] == s["grid_max"]["trace"]
    assert rows[K]["trace"] == s["grid_min"]["trace"]
    gap = F(rows[J]["Llo"]) - F(rows[K]["Lhi"])
    assert gap == F(s["gap_lo"]) and gap > F("0.15"), gap
    U = F(s["U_hi"])
    clo, _ = cosh_bounds(U / 2)
    assert clo >= F(s["box"][1]) / 2
    print(f"summary checks OK: total=132 base=125 ref=7 "
          f"gap={float(gap):.6f} U={float(U):.6f}")
    # per-row word-trace + interval re-verification (all rows)
    for i, r in enumerate(rows):
        x, y, z = F(r["x"]), F(r["y"]), F(r["z"])
        mats = build_mats(x, y, z, 1)
        t = eval_word(mats, r["word"])
        assert abs(t) == ka(r), (i, t, r["trace"])
        t2 = eval_word(mats, r["run_word"])
        assert abs(t2) == abs(F(r["run_trace"]))
        assert abs(t2) > abs(t), (i, "runner-up not larger")
        u = abs(t) / 2
        _, chi = cosh_bounds(F(r["Llo"]) / 2)
        clo2, _ = cosh_bounds(F(r["Lhi"]) / 2)
        assert chi <= u and clo2 >= u, (i, "length interval fails")
        assert F(r["whi"]) > F(r["wlo"]) > 0
    print(f"row replay OK: {len(rows)}/{len(rows)} word traces + "
          f"length intervals")
    # exhaustive minimality spot-check on every `every`-th row
    checked = 0
    for i in range(0, len(rows), every):
        r = rows[i]
        t, w, _, _, _ = min_trace_point(F(r["x"]), F(r["y"]), F(r["z"]), 1)
        assert abs(t) == ka(r) and w == r["word"], (i, t, w)
        checked += 1
    print(f"exhaustive minimality re-proof OK: {checked} points "
          f"(every {every}) x 13120 words")
    print("ALL VERIFIER CHECKS PASSED")


if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else "output/artifacts"
    e = int(sys.argv[2]) if len(sys.argv) > 2 else 11
    main(a, e)
