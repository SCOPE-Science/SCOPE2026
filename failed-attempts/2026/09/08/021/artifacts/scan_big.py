#!/usr/bin/env python3
"""Wide bounded integral-point scan for 4006a1/4006b1. D=x^2+4f(x) square test.
Writes integral_xs_Ea.csv / integral_xs_Eb.csv with (x, y1, y2) rows."""
import math, csv, time, sys

LO = int(sys.argv[1]) if len(sys.argv) > 1 else -10**7
HI = int(sys.argv[2]) if len(sys.argv) > 2 else 10**7

def scan(a1, a2, a3, a4, a6, lo, hi, tag, path):
    assert a1 == 1 and a3 == 0
    rows = []
    t = time.time()
    for x in range(lo, hi + 1):
        D = x * x + 4 * (x * x * x + a2 * x * x + a4 * x + a6)
        if D >= 0:
            r = math.isqrt(D)
            if r * r == D and ((r - x) & 1) == 0:
                y1 = (r - x) // 2
                y2 = (-r - x) // 2
                # verify on curve
                assert y1 * y1 + x * y1 == x**3 + a2 * x * x + a4 * x + a6
                rows.append((x, y1, y2))
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["x", "y1", "y2"])
        w.writerows(rows)
    print("%s: [%d,%d] -> %d x-values in %.1fs: %s"
          % (tag, lo, hi, len(rows), time.time() - t, [r[0] for r in rows]))

scan(1, -1, 0, 4, -2, LO, HI, "Ea", "output/artifacts/integral_xs_Ea.csv")
scan(1, 0, 0, -87, 361, LO, HI, "Eb", "output/artifacts/integral_xs_Eb.csv")
