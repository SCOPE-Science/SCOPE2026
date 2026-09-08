"""One-command replay for lane-67 ASM monotone-triangle census.

Runs: backtracking census (n=1..7) with stream hashes, memoized DP
cross-counts, MRR products, Gram-determinant triple evaluation
(Bareiss / Fraction-Gaussian / Dodgson), MT->ASM bijection checks,
per-height distributions with extremal witnesses, and witness ASM
printouts. Stdlib only.

Usage:  python3 replay.py [--orders 1-7] [--skip-bijection-7]
"""

import argparse
import sys
import time

from mt import (bijection_check, census, count_dp, det_bareiss,
                det_dodgson, det_fraction_gauss, gram_matrix,
                height_distribution, is_asm, mrr, mt_to_asm)

EXPECTED = {1: 1, 2: 2, 3: 7, 4: 42, 5: 429, 6: 7436, 7: 218348}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orders", default="1-7")
    ap.add_argument("--skip-bijection-7", action="store_true")
    args = ap.parse_args()
    lo, hi = (int(x) for x in args.orders.split("-"))
    orders = list(range(lo, hi + 1))
    t_all = time.time()
    ok = True

    print("== lane-67 replay: monotone-triangle ASM census ==")
    for n in orders:
        c = census(n)
        d = count_dp(n)
        p = mrr(n)
        G = gram_matrix(n)
        b = det_bareiss(G)
        g = det_fraction_gauss(G)
        dg = det_dodgson(G)
        exp = EXPECTED[n]
        line_ok = (c["count"] == d == p == b == g == dg == exp)
        ok &= line_ok
        print(f"n={n}: backtrack={c['count']} dp={d} mrr={p} "
              f"bareiss={b} gauss={g} dodgson={dg} expected={exp} "
              f"sha256={c['sha256'][:16]}... wall={c['wall_s']:.2f}s "
              f"[{'OK' if line_ok else 'MISMATCH'}]")

    print("== MT->ASM bijection ==")
    for n in orders:
        if n == 7 and args.skip_bijection_7:
            print("n=7: skipped by flag")
            continue
        r = bijection_check(n)
        ok &= r["bijective"]
        print(f"n={n}: triangles={r['count']} bad={r['bad']} "
              f"distinct_asms={r['distinct_asms']} "
              f"[{'OK' if r['bijective'] else 'MISMATCH'}]")

    print("== height distributions ==")
    for n in orders:
        r = height_distribution(n)
        assert r["count"] == EXPECTED[n], (n, r["count"])
        assert sum(r["dist"].values()) == EXPECTED[n]
        items = sorted(r["dist"].items())
        print(f"n={n}: min={r['min']} max={r['max']} "
              f"distinct_heights={len(items)} count={r['count']} [OK]")
        print(f"  table: {items}")
        if n in (6, 7):
            print(f"  max witness (H={r['max']}):")
            for row in r["max_witness"]:
                print(f"    {list(row)}")
            A = mt_to_asm(r["max_witness"])
            assert is_asm(A)
            print(f"  witness ASM valid: True; ASM rows:")
            for row in A:
                print(f"    {row}")

    print(f"== total wall {time.time()-t_all:.1f}s: "
          f"{'ALL CHECKS PASSED' if ok else 'FAILURES PRESENT'} ==")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
