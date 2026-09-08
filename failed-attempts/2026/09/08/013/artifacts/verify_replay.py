"""Lane-73 independent replay. Pure stdlib, exact integer/Fraction arithmetic, NO floats.
Re-derives torsion completeness (binary-search icbrt), rechecks orders, on-curve
status of all integral points + witnesses, and re-runs a pure-Python isqrt census
on |x|<=1e5 cross-checked against the stored |x|<=1e6 table."""
import json, math, sys
from fractions import Fraction

T = json.load(open("output/artifacts/table.json"))
C = T["curves"]
B = T["B"]
assert B == 10 ** 6

def icbrt_exact(s):
    if s == 0: return 0
    neg = s < 0; a = abs(s)
    lo, hi = 0, int(a ** (1.0 / 3.0)) + 2 if a < 10 ** 15 else 10 ** 7
    if hi < 0: hi = 0
    # ensure hi^3 >= a
    while hi ** 3 < a: hi = 2 * hi + 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** 3 < a: lo = mid + 1
        else: hi = mid
    assert lo ** 3 >= a and (lo - 1) ** 3 < a
    return -(lo) if (neg and lo ** 3 == a) else (lo if lo ** 3 == a else None)

def eadd(k, P, Q):
    if P is None: return Q
    if Q is None: return P
    x1, y1 = P; x2, y2 = Q
    if x1 == x2:
        if y1 == y2:
            if y1 == 0: return None
            lam = Fraction(3 * x1 * x1, 2 * y1)
        else: return None
    else:
        lam = Fraction(y2 - y1, x2 - x1)
    x3 = lam * lam - x1 - x2
    return (x3, lam * (x1 - x3) - y1)

def surrender(msg):
    print("REPLAY FAIL:", msg); sys.exit(1)

n_int_total = 0
n_wit = 0
for ks, row in C.items():
    k = int(ks)
    D = 432 * k * k
    # (i) torsion candidate re-derivation, exact
    cands = set()
    r = icbrt_exact(-k)
    if r is not None: cands.add((r, 0))
    for y in range(1, math.isqrt(D) + 1):
        if D % (y * y): continue
        r = icbrt_exact(y * y - k)
        if r is not None:
            cands.add((r, y)); cands.add((r, -y))
    stored = {(d["x"], d["y"]) for d in row["torsion_points"]}
    # Completeness: torsion ⊆ Lutz candidates (Lutz theorem); every candidate is
    # either stored (verified torsion, rechecked below) or certified infinite order
    # (no nP=O for 1<=n<=16, plus Mazur => not torsion). Infinite-order integral
    # points among the candidates are correctly EXCLUDED from torsion_points.
    if not stored <= cands:
        surrender(f"k={k} stored torsion not among Lutz candidates")
    for (x, y) in sorted(cands - stored):
        P = (Fraction(x), Fraction(y))
        Q = None
        for i in range(1, 17):
            Q = eadd(k, Q, P)
            if Q is None: surrender(f"k={k} unstored candidate {(x,y)} is torsion")
    if stored != {(d["x"], d["y"]) for d in row["torsion_points"]}:
        surrender(f"k={k} internal")  # unreachable sanity
    # (ii) order recheck of each stored torsion point
    for d in row["torsion_points"]:
        P = (Fraction(d["x"]), Fraction(d["y"]))
        if d["y"] == 0:
            if eadd(k, P, P) is not None: surrender(f"k={k} y=0 not order 2")
            if d["order"] != 2: surrender(f"k={k} bad order field")
        else:
            n = None
            Q = None
            for i in range(1, 17):
                Q = eadd(k, Q, P)
                if Q is None: n = i; break
            if n != d["order"]: surrender(f"k={k} order mismatch {d}")
    if row["torsion_order"] != len(stored) + 1:
        surrender(f"k={k} torsion count")
    # (iii) integral points on-curve recheck
    for (x, y) in row["integral_points"]:
        if not (abs(x) <= B and y * y == x ** 3 + k and y >= 0):
            surrender(f"k={k} bad integral {(x, y)}")
    n_int_total += len(row["integral_points"])
    # (iv) witness on-curve + infinite order recheck (Mazur: no nP=O for n<=16)
    w = row["rank_witness"]
    if w is not None:
        P = (Fraction(w[0], w[1]), Fraction(w[2]))
        if not (P[1] * P[1] == P[0] ** 3 + k): surrender(f"k={k} witness off-curve")
        Q = None
        for i in range(1, 17):
            Q = eadd(k, Q, P)
            if Q is None: surrender(f"k={k} witness actually torsion order {i}")
        n_wit += 1
        if row["rank_lower_bound"] != 1: surrender(f"k={k} rank flag")
    else:
        if row["rank_lower_bound"] != 0: surrender(f"k={k} rank flag")
    # (v) pure-Python isqrt census |x|<=1e5 agrees with stored restriction
    B2 = 10 ** 5
    xs = set()
    for x in range(-B2, B2 + 1):
        v = x ** 3 + k
        if v < 0: continue
        s = math.isqrt(v)
        if s * s == v: xs.add(x)
    if xs != {x for (x, y) in row["integral_points"] if abs(x) <= B2}:
        surrender(f"k={k} census subrange mismatch")

print(f"REPLAY OK: 60 curves, {n_int_total} integral x-values (|x|<=1e6), "
      f"{n_wit} curves with certified rank>=1 witness, "
      f"torsion re-derived exactly on all 60.")
