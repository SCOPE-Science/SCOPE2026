"""Step 14 (decisive target probe): six-coordinate shortening MacWilliams system.
Shorten S, |S|=6. n_{w,i} = #{wt-w words with i ones on S}, i=0..6.
Complement symmetry n_{w,i} = n_{72-w,6-i}. Free vars: for each w in {16,20,24,28,32}:
7 vars (idx 7k+i); w=36: a=n0=n6, b=n1=n5, c=n2=n4, d=n3, 2a+2b+2c+d=A36 -> free
a,b,c (idx 35,36,37), d determined. Total 38 vars.
Shortened C6 [66,30]: A6[w]=n_{w,0}. Punctured P6 [66,36]:
B6[j]=sum_{i=0..6} n_{j+i,i}. Dual pair -> MW: B6=2^-30 K^{(66)} A6.
Solve 66 MW equations for 38 unknowns exactly over Q.
- If inconsistent or unique-nonintegral => GENUINE exclusion (target win).
- If underdetermined => report nullity; balanced non-integrality alone is NOT
  an obstruction (code could sit in a non-balanced cell). Honest verdict either way.
"""
from fractions import Fraction
from math import comb
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
WS = [16, 20, 24, 28, 32]
KSET = 6
NV = 35 + 3


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
    rows.append((f"MW{j}", e))

M, labels = [], []
for lab, e in rows:
    row = [e.get(i, Fraction(0)) for i in range(NV)] + [-e.get("one", Fraction(0))]
    if any(v != 0 for v in row):
        M.append(row)
        labels.append(lab)
print(f"nontrivial equations: {len(M)} of {len(rows)}; unknowns: {NV}")
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
print("rank =", r, "of", NV)
incons = [(labels[i], R[i][NV]) for i in range(len(R))
          if all(R[i][c] == 0 for c in range(NV)) and R[i][NV] != 0]
print("inconsistent:", incons if incons else "NONE — consistent")
free = [c for c in range(NV) if c not in piv]
print("nullity =", len(free), "free idx:", free)
if not free:
    part = [Fraction(0)] * NV
    for i, c in enumerate(piv):
        part[c] = R[i][NV]
    D = comb(72, 6)
    ok = True
    for w in WS:
        for i in range(7):
            eb = Fraction(comb(w, i) * comb(72 - w, 6 - i) * A[w], D)
            m = (part[7 * WS.index(w) + i] == eb)
            ok &= m
    print("unique solution equals balanced:", ok)
    print("unique solution integral:", all(part[c].denominator == 1 for c in range(NV)))
    json.dump({"rank": r, "consistent": True, "nullity": 0,
               "solution": [str(x) for x in part], "equals_balanced": ok},
              open(os.path.join(HERE, "s14_six_system.json"), "w"), indent=1)
else:
    NS = []
    for f in free:
        v = [Fraction(0)] * NV
        v[f] = Fraction(1)
        for i, c in enumerate(piv):
            v[c] = -R[i][f]
        NS.append(v)
    print("system UNDERDETERMINED: balanced non-integrality is not an obstruction;")
    print("integral non-balanced cells remain MacWilliams-admissible a priori.")
    json.dump({"rank": r, "consistent": True, "nullity": len(free), "free": free,
               "nullspace": [[str(x) for x in v] for v in NS]},
              open(os.path.join(HERE, "s14_six_system.json"), "w"), indent=1)
print("wrote s14_six_system.json")
