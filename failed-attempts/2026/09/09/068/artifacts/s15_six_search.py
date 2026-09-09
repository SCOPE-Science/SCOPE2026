"""Step 15: hunt for an integral 6-point cell near-balanced (exact ILP-free search).
s14: MW system rank 33/38, nullity 5 — non-balanced integral cells may exist.
Question: does the affine solution space contain a NONNEGATIVE INTEGER point?
Use exact rational nullspace + rounding search over small free-var box, verify
all 38 vars integral, >= 0, and row-sum/box constraints. Bounded deterministic
search (no solver): enumerate free-var integer lattice points in a widening box.
Report honestly: found / not-found-within-box.
"""
from fractions import Fraction
import json
import os
import itertools

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
S = json.load(open(os.path.join(HERE, "s14_six_system.json")))
NV = 38
# Reconstruct particular + nullspace by re-solving (import logic inline, cheap:
# reuse stored nullspace + solve particular via balanced projection is NOT exact).
# Simpler: re-derive here with fractions (copy of s14 solve, returning objects).
from math import comb
WS = [16, 20, 24, 28, 32]


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
part = [Fraction(0)] * NV
for i, c in enumerate(piv):
    part[c] = R[i][NV]
NS = []
for f in free:
    v = [Fraction(0)] * NV
    v[f] = Fraction(1)
    for i, c in enumerate(piv):
        v[c] = -R[i][f]
    NS.append(v)
print("free idx:", free)
print("particular (fractional) sample:", [(c, part[c]) for c in range(NV) if part[c].denominator != 1][:10])

# Row-sum check helper: for each w, sum_i n_{w,i} must equal A_w (built in by construction?
# verify) and each 0<=n<=A_w.

def point(ts):
    x = list(part)
    for t, v in zip(ts, NS):
        for c in range(NV):
            x[c] += t * v[c]
    return x


def ok_point(x):
    for c in range(NV):
        if x[c].denominator != 1 or x[c] < 0:
            return False
    # row sums + box per weight
    groups = {}
    for k, w in enumerate(WS):
        s = sum(x[7 * k + i] for i in range(7))
        if s != A[w]:
            return False
        if any(x[7 * k + i] > A[w] for i in range(7)):
            return False
    a, b, c = x[35], x[36], x[37]
    if not (a >= 0 and b >= 0 and c >= 0):
        return False
    if 2 * a + 2 * b + 2 * c > A[36]:
        return False
    d = A[36] - 2 * a - 2 * b - 2 * c
    if d < 0:
        return False
    return True

# denominators of NS entries -> step lattice
from math import gcd
D = 1
for v in NS:
    for c in range(NV):
        D = D * v[c].denominator // gcd(D, v[c].denominator)
print("common denominator of nullspace:", D)
# search integer parameter box scaled: ts = k/D * e_j combos; brute force over
# small box [-B,B]^5 in units of 1/D would be huge; instead random-restart
# deterministic rounding: try rounding particular in null directions greedily.
import random
random.seed(72)
best = None
for trial in range(20000):
    ts = [Fraction(random.randint(-3 * D, 3 * D), D) for _ in free]
    x = point(ts)
    # round to nearest lattice move: project each coord? score = #integral-nonneg
    score = sum(1 for c in range(NV) if x[c].denominator == 1 and x[c] >= 0)
    if best is None or score > best[0]:
        best = (score, ts, x)
    if ok_point(x):
        print("FOUND integral feasible 6-point cell at trial", trial)
        print("ts =", ts)
        print("x =", x)
        break
print("best score:", best[0], "of", NV)
json.dump({"found": bool(best[0] == NV), "best_score": best[0], "nv": NV},
          open(os.path.join(HERE, "s15_six_search.json"), "w"), indent=1)
print("wrote s15_six_search.json")
