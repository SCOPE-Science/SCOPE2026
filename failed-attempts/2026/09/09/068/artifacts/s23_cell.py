"""Step 23: certify the integral 6-point cell at boundary t=6117536880 (exact).
Rebuild x(t), verify: all 38 coords integral nonneg, row sums, box, both
MacWilliams systems (shortened [66,30] <-> punctured [66,36]) with zero residual.
Then print the full cell table.
"""
from fractions import Fraction
from math import comb
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
assert free == [37]
part = [Fraction(0)] * NV
for i, c in enumerate(piv):
    part[c] = R[i][NV]
v = [Fraction(0)] * NV
v[37] = Fraction(1)
for i, c in enumerate(piv):
    v[c] = -R[i][37]
t0 = Fraction(6117536880)
x = [part[c] + t0 * v[c] for c in range(NV)]
assert all(z.denominator == 1 for z in x), "integral"
assert all(z >= 0 for z in x), "nonneg"
X = [int(z) for z in x]
print("integral nonneg cell at t=6117536880:")
for k, w in enumerate(WS):
    row = [X[7 * k + i] for i in range(7)]
    print(f"  w={w}: {row} sum={sum(row)} (A={A[w]})")
    assert sum(row) == A[w]
a, b, c = X[35], X[36], X[37]
d = A[36] - 2 * a - 2 * b - 2 * c
print(f"  w=36: a={a} b={b} c={c} d={d}")
assert d >= 0
# shortened + punctured spectra + MW residual
An = {}
for w in range(67):
    An[w] = 0
for k, w in enumerate(WS):
    An[w] = X[7 * k]
    An[72 - w] = X[7 * k + 6]
An[36] = a
An[0] = 1
Bn = {}
for j in range(67):
    s = Fraction(0)
    # n_{j+i,i} numeric
    def num(ww, i):
        if ww == 0:
            return 1 if i == 0 else 0
        if ww == 72:
            return 1 if i == 6 else 0
        if A[ww] == 0:
            return 0
        if ww == 36:
            return {0: a, 1: b, 2: c, 3: d, 4: c, 5: b, 6: a}[i]
        if ww in WS:
            return X[7 * WS.index(ww) + i]
        if 72 - ww in WS:
            return X[7 * WS.index(72 - ww) + (6 - i)]
        return 0
    s = sum(num(j + i, i) for i in range(7))
    Bn[j] = s
print("sum shortened =", sum(An.values()), "expect", 2 ** 30)
print("sum punctured =", sum(Bn.values()), "expect", 2 ** 36)
assert sum(An.values()) == 2 ** 30 and sum(Bn.values()) == 2 ** 36
res = Fraction(0)
for j in range(67):
    lhs = Fraction(Bn[j])
    rhs = sum(Fraction(An[w]) * K[(j, w)] for w in range(67)) / Fraction(2 ** 30)
    res = max(res, abs(lhs - rhs))
print("MW residual:", res)
assert res == 0
print("min dist shortened:", next(w for w in range(1, 67) if An[w] != 0))
json.dump({"t": str(t0), "X": X, "shortened": {str(w): An[w] for w in An},
           "punctured": {str(j): Bn[j] for j in Bn}}, open(os.path.join(HERE, "s23_cell.json"), "w"), indent=1)
print("wrote s23_cell.json")
