"""Step 25: LP feasibility probe of the 6-point family via vertex enumeration.
s21/s22: 1-D family x(t)=p+t*v, nonneg interval [t_lo,t_hi]=[6117536880,6117831720].
LP angle: (i) does every t in the interval satisfy ALL MacWilliams dual
inequalities B'_j(t) >= 0 for the shortened [66,30] code? B'_j(t) is affine in t;
check minimum over the interval exactly (endpoint check per j). Report min/arg.
(ii) Delsarte dual: shortened code's distance distribution must satisfy all
Krawtchouk nonnegativity — same check. Exact Fractions throughout.
"""
from fractions import Fraction
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
S = json.load(open(os.path.join(HERE, "s23_cell.json")))
WS = [16, 20, 24, 28, 32]

# rebuild particular + direction (copy of s22 solve, condensed)
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
part = [Fraction(0)] * NV
for i, c in enumerate(piv):
    part[c] = R[i][NV]
v = [Fraction(0)] * NV
v[37] = Fraction(1)
for i, c in enumerate(piv):
    v[c] = -R[i][37]

t_lo, t_hi = Fraction(6117536880), Fraction(6117831720)
# shortened enumerator affine in t: A'(w;t) = n_{w,0}(t); dual B'(j;t) = 2^-30 K A'
# Only coords 0..34,37,38? null direction nonzero entries listed in s22: coords
# 0..37. A'(w) uses coords: w16->0, w20->7, w24->14, w28->21, w32->28, w36->35, mirror.
amap = {16: 0, 20: 7, 24: 14, 28: 21, 32: 28, 36: 35, 40: 34, 44: 27, 48: 20, 52: 13, 56: 6}
print("dual-spectrum minimum over t-interval (exact, endpoint check):")
worst = None
for j in range(N + 1):
    # B'(j;t) = sum_w K[j,w]/2^30 A'(w;t); A'(w;t) = part[c]+t*v[c]
    slope = sum(K[(j, w)] * v[c] for (w, c) in amap.items()) / Fraction(2 ** 30)
    b0 = sum(K[(j, w)] * part[c] for (w, c) in amap.items()) / Fraction(2 ** 30)
    # + constant contributions from w=0 (1) and w=72? shortened length 66: w=72
    # contributes? n_{72,0}=0 (all-ones has 6 ones on S). w=0: n=1 constant.
    b0 += Fraction(K[(j, 0)] * 1, 2 ** 30)
    lo_v = b0 + slope * (t_lo if slope >= 0 else t_hi)
    hi_v = b0 + slope * (t_hi if slope >= 0 else t_lo)
    if worst is None or lo_v < worst[1]:
        worst = (j, lo_v)
    if lo_v < 0:
        print(f"  j={j}: NEGATIVE min {lo_v} — LP exclusion at this j!")
    assert lo_v.denominator != 0
print("worst dual coeff:", worst[0], "=", worst[1], "=", float(worst[1]))
print("all dual min >= 0:", all(
    (sum(K[(j, w)] * v[c] for (w, c) in amap.items()) / Fraction(2 ** 30) >= 0)
    * 0 + (sum(K[(j, w)] * part[c] for (w, c) in amap.items()) / Fraction(2 ** 30)
           + Fraction(K[(j, 0)], 2 ** 30)
           + min(Fraction(0), sum(K[(j, w)] * v[c] for (w, c) in amap.items()) / Fraction(2 ** 30) * (t_hi - t_lo) if (sum(K[(j, w)] * v[c] for (w, c) in amap.items())) >= 0 else sum(K[(j, w)] * v[c] for (w, c) in amap.items()) / Fraction(2 ** 30) * (t_hi - t_lo)) + sum(K[(j, w)] * v[c] for (w, c) in amap.items()) / Fraction(2 ** 30) * t_lo if (sum(K[(j, w)] * v[c] for (w, c) in amap.items())) >= 0 else sum(K[(j, w)] * part[c] for (w, c) in amap.items()) / Fraction(2 ** 30) + Fraction(K[(j, 0)], 2 ** 30) + sum(K[(j, w)] * v[c] for (w, c) in amap.items()) / Fraction(2 ** 30) * t_hi) >= 0
    for j in range(N + 1)))
json.dump({"worst_j": worst[0], "worst_val": str(worst[1])},
          open(os.path.join(HERE, "s25_lp.json"), "w"), indent=1)
print("wrote s25_lp.json")
