"""Step 22: analyze the s21 nullity-1 family. Particular + null direction;
balanced point location; does the affine line contain ANY integral-nonnegative
point? 1-D exact analysis: parametrize x(t) = p + t*v, compute per-coord
constraints t-interval (integrality: t in (1/g)*Z lattice), report feasibility.
"""
from fractions import Fraction
from math import comb, gcd
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
WS = [16, 20, 24, 28, 32]
NV = 38


def n_expr(w, i):
    if i not in range(7):
        return {}
    if w < 0 or w > 72:
        return {}
    if w == 0:
        return {"one": Fraction(1)} if i == 0 else {}
    if w == 72:
        return {"one": Fraction(1)} if i == 6 else {}
    if A[w] == 0:
        return {}
    if w == 36:
        if i in (0, 6):
            return {35: Fraction(1)}
        if i in (1, 5):
            return {36: Fraction(1)}
        if i in (2, 4):
            return {37: Fraction(1)}
        return {"one": Fraction(A[36]), 35: Fraction(-2), 36: Fraction(-2), 37: Fraction(-2)}
    if w in WS:
        return {7 * WS.index(w) + i: Fraction(1)}
    if 72 - w in WS:
        return n_expr(72 - w, 6 - i)
    return {}


def add(e1, e2, s=1):
    e = dict(e1)
    for k, v in e2.items():
        e[k] = e.get(k, Fraction(0)) + s * v
    return {k: v for k, v in e.items() if v != 0}


def cx(e, c):
    return {k: v * c for k, v in e.items() if v * c != 0}


N = 66
A6, B6 = {}, {}
for w in range(N + 1):
    A6[w] = n_expr(w, 0)
for j in range(N + 1):
    e = {}
    for i in range(7):
        e = add(e, n_expr(j + i, i))
    B6[j] = e
K = {}
for j in range(N + 1):
    for w in range(N + 1):
        s = Fraction(0)
        for u in range(N + 1):
            if 0 <= u <= w and 0 <= j - u <= N - w:
                s += Fraction((-1) ** u) * comb(w, u) * comb(N - w, j - u)
        K[(j, w)] = s
rows = []
for j in range(N + 1):
    e = dict(B6[j])
    for w in range(N + 1):
        e = add(e, cx(A6[w], -K[(j, w)] / Fraction(2 ** 30)))
    rows.append(e)
for w in WS:
    e = {"one": Fraction(-A[w])}
    for i in range(7):
        e = add(e, n_expr(w, i))
    rows.append(e)
M = []
for e in rows:
    row = [e.get(i, Fraction(0)) for i in range(NV)] + [-e.get("one", Fraction(0))]
    if any(v != 0 for v in row):
        M.append(row)
R = [r[:] for r in M]
piv, r = [], 0
for c in range(NV):
    p = next((i for i in range(r, len(R)) if R[i][c] != 0), None)
    if p is None:
        continue
    R[r], R[p] = R[p], R[r]
    d = R[r][c]
    R[r] = [v / d for v in R[r]]
    for i in range(len(R)):
        if i != r and R[i][c] != 0:
            q = R[i][c]
            R[i] = [R[i][k] - q * R[r][k] for k in range(NV + 1)]
    piv.append(c)
    r += 1
free = [c for c in range(NV) if c not in piv]
assert len(free) == 1
f = free[0]
part = [Fraction(0)] * NV
for i, c in enumerate(piv):
    part[c] = R[i][NV]
v = [Fraction(0)] * NV
v[f] = Fraction(1)
for i, c in enumerate(piv):
    v[c] = -R[i][f]
print("free var idx:", f, "(var 37 = c = n_{36,2}=n_{36,4})")
print("null direction nonzero entries:", [(c, v[c]) for c in range(NV) if v[c] != 0])
print("particular nonzero sample:", [(c, part[c]) for c in range(NV) if part[c] != 0][:8])
# balanced t-value: balanced c36 = C(36,2)C(36,4)/C(72,6)*A36
D = comb(72, 6)
bal = {w: [Fraction(comb(w, i) * comb(72 - w, 6 - i) * A[w], D) for i in range(7)] for w in WS}
balc = Fraction(comb(36, 2) * comb(36, 4) * A[36], D)
print("balanced c36 =", balc)
# t_bal: part[37] + t*v[37] = balc
t_bal = (balc - part[37]) / v[37]
print("t_bal =", t_bal, "=", float(t_bal))
# feasibility: for each coord c: part[c]+t*v[c] integral >= 0
# t lattice: t = a/g with g = lcm of denominators of v
g = 1
for c in range(NV):
    g = g * v[c].denominator // gcd(g, v[c].denominator)
print("direction denominator lcm:", g)
lo, hi = None, None
for c in range(NV):
    if v[c] == 0:
        continue
    b = -part[c] / v[c]
    if v[c] > 0:
        lo = b if lo is None else max(lo, b)
    else:
        hi = b if hi is None else min(hi, b)
print("nonneg interval: t in [", lo, ",", hi, "]")
print("t_bal inside:", lo <= t_bal <= hi)
# balanced point itself non-integral? (s13 says yes for some (w,i))
print("balanced n-values integral check (w16):", [x.denominator == 1 for x in bal[16]])
# scan lattice points t = m/g in interval for fully-integral points
import math
mlo = math.ceil(lo * g)
mhi = math.floor(hi * g)
print(f"lattice window: m in [{mlo},{mhi}] ({mhi - mlo + 1} candidates)")
found = []
mm = mlo
while mm <= mhi and len(found) < 5:
    t = Fraction(mm, g)
    x = [part[c] + t * v[c] for c in range(NV)]
    if all(z.denominator == 1 for z in x):
        found.append((t, x))
    mm += 1
    if mm - mlo > 4000000:
        print("... window too large, stopping scan after 4M")
        break
print("integral points found:", len(found))
for t, x in found:
    print("  t =", t)
json.dump({"free_idx": f, "t_bal": str(t_bal), "lattice_step": str(Fraction(1, g)),
           "interval": [str(lo), str(hi)], "integral_found": len(found)},
          open(os.path.join(HERE, "s22_line.json"), "w"), indent=1)
print("wrote s22_line.json")
