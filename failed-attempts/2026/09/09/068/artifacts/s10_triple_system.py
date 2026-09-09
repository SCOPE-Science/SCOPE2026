"""Step 10 (target deepening): three-coordinate shortening MacWilliams uniqueness.
Shorten S={1,2,3}. n_{w,i} = #{wt-w words with i ones on S}, i=0..3.
Complement symmetry n_{w,i} = n_{72-w,3-i}. Free vars: for each w in {16,20,24,28,32}:
i=0,1,2,3 (4 vars, idx 4k+j); w=36: a=n_{36,0}=n_{36,3}, b=n_{36,1}=n_{36,2},
2a+2b=A36 -> free a (idx 20), b determined.
Shortened C3 [69,33]: A3[w]=n_{w,0}. Triply-punctured P3 [69,36]:
B3[j]=n_{j,0}+n_{j+1,1}+n_{j+2,2}+n_{j+3,3}. Dual pair -> MW: B3=2^-33 K^{(69)} A3.
Solve 69 MW equations for 21 unknowns exactly; compare with triple-balanced
e_i(w) = C(w,i)C(72-w,3-i)/C(72,3) * A_w.
"""
from fractions import Fraction
from math import comb
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
WS = [16, 20, 24, 28, 32]
NV = 21


def n_expr(w, i):
    if i not in (0, 1, 2, 3):
        return {}
    if w < 0 or w > 72:
        return {}
    if w == 0:
        return {"one": Fraction(1)} if i == 0 else {}
    if w == 72:
        return {"one": Fraction(1)} if i == 3 else {}
    if A[w] == 0:
        return {}
    if w == 36:
        if i in (0, 3):
            return {20: Fraction(1)}
        return {"one": Fraction(A[36] // 2), 20: Fraction(-1)}
    if w in WS:
        return {4 * WS.index(w) + i: Fraction(1)}
    if 72 - w in WS:
        return n_expr(72 - w, 3 - i)
    return {}


def add(e1, e2, s=1):
    e = dict(e1)
    for k, v in e2.items():
        e[k] = e.get(k, Fraction(0)) + s * v
    return {k: v for k, v in e.items() if v != 0}


def cx(e, c):
    return {k: v * c for k, v in e.items() if v * c != 0}


A3, B3 = {}, {}
for w in range(70):
    A3[w] = n_expr(w, 0)
for j in range(70):
    e = {}
    for i in range(4):
        e = add(e, n_expr(j + i, i))
    B3[j] = e

K = {}
for j in range(70):
    for w in range(70):
        s = Fraction(0)
        for u in range(70):
            if 0 <= u <= w and 0 <= j - u <= 69 - w:
                s += Fraction((-1) ** u) * comb(w, u) * comb(69 - w, j - u)
        K[(j, w)] = s

rows = []
for j in range(70):
    e = dict(B3[j])
    for w in range(70):
        e = add(e, cx(A3[w], -K[(j, w)] / Fraction(2 ** 33)))
    rows.append((f"MW{j}", e))

M, labels = [], []
for lab, e in rows:
    row = [e.get(i, Fraction(0)) for i in range(NV)] + [-e.get("one", Fraction(0))]
    if any(v != 0 for v in row):
        M.append(row)
        labels.append(lab)
print(f"nontrivial equations: {len(M)} of {len(rows)}")
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
print("free vars:", free if free else "none (unique solution)")
part = [Fraction(0)] * NV
for i, c in enumerate(piv):
    part[c] = R[i][NV]
D = comb(72, 3)
ok = True
for w in WS:
    for i in range(4):
        eb = Fraction(comb(w, i) * comb(72 - w, 3 - i) * A[w], D)
        got = part[4 * WS.index(w) + i]
        m = (got == eb)
        ok &= m
        print(f"  w={w} i={i}: got {got} bal {eb} {'=' if m else 'NEQ'}")
eba = Fraction(A[36] // 2 - 0, 1)  # placeholder
# a36 balanced: C(36,0)C(36,3)/C(72,3)*A36
eb36 = Fraction(comb(36, 0) * comb(36, 3) * A[36], D)
print(f"  a36={part[20]} bal {eb36} {'=' if part[20]==eb36 else 'NEQ'}")
ok &= (part[20] == eb36)
print("ALL EQUAL balanced:", ok)
json.dump({"rank": r, "consistent": not incons, "free": free,
           "solution": [str(x) for x in part], "equals_balanced": ok},
          open(os.path.join(HERE, "s10_triple_system.json"), "w"), indent=1)
print("wrote s10_triple_system.json")
