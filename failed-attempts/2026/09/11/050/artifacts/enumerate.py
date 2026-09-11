"""Bounded finder (NOT a completeness proof): enumerates integer x with x^3+k >= 0
up to XMAX and records exact integer points via math.isqrt. Stdlib only."""
import math, json

KMIN, KMAX, XMAX = 10001, 10032, 200000
table = {}
for k in range(KMIN, KMAX + 1):
    xmin = -int(round(k ** (1 / 3))) - 3
    pts = []
    for x in range(xmin, XMAX + 1):
        v = x ** 3 + k
        if v < 0:
            continue
        y = math.isqrt(v)
        if y * y == v:
            assert y * y == x ** 3 + k
            pts.append([x, y])
    table[str(k)] = pts
print(json.dumps({"XMAX": XMAX, "points": table}, indent=1))
n_with = sum(1 for v in table.values() if v)
print("curves with >=1 point to XMAX:", n_with, "of", len(table))
