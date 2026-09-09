"""Step 20b (CORRECTION AUDIT of s20): the s20 model forced x_w = x_{72-w}, which
assumes 1 in C0 AND symmetric split. General case: x_w + x_{72-w} = A_w
(complement may swap C0 with its complement coset). Moreover for Type II the
C0=ker(<.,x>) cosets do NOT have the 2-mod-4 shadow property (that is Type-I
machinery), so D_w = A_w on 0 mod 4 still holds (cosets C1,C2 have... actually
for general x the coset weights are unconstrained). Honest correction: solve the
GENERAL codim-1 subcode system: unknowns x_w (w=16..56 + 36 free-ish) with only
x_w + x_{72-w} = A_w, equations D_w = A_w for w = 0 mod 4 where D = 2^-35 K C0.
If consistent => s20 'exclusion' was a modeling artifact; report truthfully.
"""
from fractions import Fraction
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
WS = [16, 20, 24, 28, 32]  # free u_w = x_w; x_{72-w} = A_w - u_w; x36 = A36/2 fixed by symmetry? NO:
# x_36: complement fixes wt-36 words? c+1 has wt 36 iff wt c = 36. So complement acts
# WITHIN weight 36: x_36 = #{wt-36 words outside C0} is free in [0,A36] but constrained
# by C0∋1 or not. If 1 in C0: x_36 free even?; general: keep x36 free var.
NV = 6  # u16,u20,u24,u28,u32,x36


def x_expr(w):
    if w in (0, 72):
        return {}
    if A[w] == 0:
        return {}
    if w == 36:
        return {5: Fraction(1)}
    if w in WS:
        return {WS.index(w): Fraction(1)}
    if 72 - w in WS:
        e = {"one": Fraction(A[w])}
        e[WS.index(72 - w)] = Fraction(-1)
        return e
    return {}


def add(e1, e2, s=1):
    e = dict(e1)
    for k, v in e2.items():
        e[k] = e.get(k, Fraction(0)) + s * v
    return {k: v for k, v in e.items() if v != 0}


def cx(e, c):
    return {k: v * c for k, v in e.items() if v * c != 0}


C0 = {}
for w in range(73):
    C0[w] = add({"one": Fraction(A[w])}, cx(x_expr(w), Fraction(-1)))
K = {}
for j in range(73):
    for w in range(73):
        s = Fraction(0)
        for u in range(73):
            if 0 <= u <= w and 0 <= j - u <= 72 - w:
                s += Fraction((-1) ** u) * comb(w, u) * comb(72 - w, j - u)
        K[(j, w)] = s
D = {}
for j in range(73):
    e = {}
    for w in range(73):
        e = add(e, cx(C0[w], K[(j, w)] / Fraction(2 ** 35)))
    D[j] = e
eqs = []
for w in range(0, 73, 4):
    e = add(dict(D[w]), {"one": Fraction(-A[w])})
    eqs.append((w, e))
M, labels = [], []
for w, e in eqs:
    row = [e.get(i, Fraction(0)) for i in range(NV)] + [-e.get("one", Fraction(0))]
    if any(v != 0 for v in row):
        M.append(row)
        labels.append(w)
print(f"nontrivial 0-mod-4 equations: {len(M)}; unknowns {NV}")
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
print("rank =", r)
incons = [(labels[i], R[i][NV]) for i in range(len(R))
          if all(R[i][c] == 0 for c in range(NV)) and R[i][NV] != 0]
print("inconsistent:", incons if incons else "NONE — consistent")
free = [c for c in range(NV) if c not in piv]
print("free:", free)
json.dump({"rank": r, "consistent": not incons, "free": free,
           "inconsistent_rows": [[w, str(v)] for (w, v) in incons]},
          open(os.path.join(HERE, "s20b_neighbor_general.json"), "w"), indent=1)
print("wrote s20b_neighbor_general.json")
