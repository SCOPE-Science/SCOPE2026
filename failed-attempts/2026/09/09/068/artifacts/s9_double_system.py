"""Step 9 (target deepening): two-coordinate shortening MacWilliams uniqueness.
Shorten coords S={1,2}. n_{w,i} = #{wt-w words with i ones on S}, i=0,1,2.
Constraints: sum_i n_{w,i} = A_w; complement symmetry n_{w,i} = n_{72-w,2-i}.
Free vars: for each pair representative w in {16,20,24,28,32}: a_w=n_{w,0}, b_w=n_{w,1}
  (then n_{w,2}=A_w-a_w-b_w; mirror weights determined); plus w=36: a36=n_{36,0},
  n_{36,1}=A36-2*a36, n_{36,2}=a36. Total 11 free vars.
Shortened C'' [70,34]: A2[w] = n_{w,0} (w=0..70).
Doubly-punctured C [70,36]: B2[j] = n_{j,0}+n_{j+1,1}+n_{j+2,2}.
Dual pair (C'')^\perp = punctured -> MacWilliams B2 = 2^-34 K^{(70)} A2.
Solve all 70 MW equations for 11 unknowns exactly; report rank/consistency/solution
vs pair-balanced s_w=w(w-1)A_w/(72*71).
"""
from fractions import Fraction
from math import comb
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]

PAIRS = [16, 20, 24, 28, 32]
# var index: for each pair w: a_w idx 2k, b_w idx 2k+1; a36 idx 10
NV = 11


def n_expr(w, i):
    """Affine expr dict {varidx or 'one': Fraction} for n_{w,i}."""
    if w < 0 or w > 72 or i not in (0, 1, 2):
        return {}
    if A[w] == 0 and w not in (36,) and (w not in PAIRS) and (72 - w not in PAIRS):
        # weight outside support: all zero (except w=0,72 handled below)
        if w == 0:
            return {"one": Fraction(1)} if i == 0 else {}
        if w == 72:
            return {"one": Fraction(1)} if i == 2 else {}
        return {}
    if w == 0:
        return {"one": Fraction(1)} if i == 0 else {}
    if w == 72:
        return {"one": Fraction(1)} if i == 2 else {}
    if w == 36:
        if i in (0, 2):
            return {10: Fraction(1)}
        else:
            return {"one": Fraction(A[36]), 10: Fraction(-2)}
    if w in PAIRS:
        k = PAIRS.index(w)
        if i == 0:
            return {2 * k: Fraction(1)}
        if i == 1:
            return {2 * k + 1: Fraction(1)}
        return {"one": Fraction(A[w]), 2 * k: Fraction(-1), 2 * k + 1: Fraction(-1)}
    if 72 - w in PAIRS:
        # n_{w,i} = n_{72-w,2-i}
        return n_expr(72 - w, 2 - i)
    return {}


def add(e1, e2, s=1):
    e = dict(e1)
    for k, v in e2.items():
        e[k] = e.get(k, Fraction(0)) + s * v
    return {k: v for k, v in e.items() if v != 0}


def cx(e, c):
    return {k: v * c for k, v in e.items() if v * c != 0}


A2, B2 = {}, {}
for w in range(71):
    A2[w] = n_expr(w, 0)
for j in range(71):
    e = {}
    e = add(e, n_expr(j, 0))
    e = add(e, n_expr(j + 1, 1))
    e = add(e, n_expr(j + 2, 2))
    # constant part: parent A_j contributes? No: n sums already include A. Just use e.
    B2[j] = e

K = {}
for j in range(71):
    for w in range(71):
        s = Fraction(0)
        for u in range(71):
            if 0 <= u <= w and 0 <= j - u <= 70 - w:
                s += Fraction((-1) ** u) * comb(w, u) * comb(70 - w, j - u)
        K[(j, w)] = s

rows = []
for j in range(71):
    e = dict(B2[j])
    for w in range(71):
        e = add(e, cx(A2[w], -K[(j, w)] / Fraction(2 ** 34)))
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
names = []
for w in PAIRS:
    names += [f"a{w}", f"b{w}"]
names += ["a36"]
print("solution vs pair-balanced:")
ok = True
for k, w in enumerate(PAIRS):
    eb2 = Fraction(w * (w - 1) * A[w], 72 * 71)          # both-one n_{w,2}
    eb1 = Fraction(2 * w * (72 - w) * A[w], 72 * 71)     # split n_{w,1}
    eb0 = Fraction((72 - w) * (71 - w) * A[w], 72 * 71)  # both-zero n_{w,0}=a_w
    m0 = part[2 * k] == eb0
    m1 = part[2 * k + 1] == eb1
    ok &= (m0 and m1)
    print(f"  w={w}: a=n0={part[2*k]} (bal {eb0}) {'=' if m0 else 'NEQ'}; "
          f"b=n1={part[2*k+1]} (bal {eb1}) {'=' if m1 else 'NEQ'}")
eb360 = Fraction(36 * 35 * A[36], 72 * 71)  # n_{36,0}=n_{36,2} by symmetry; cross-check only
print(f"  a36={part[10]} (pair-bal n0 {eb360}) {'=' if part[10]==eb360 else 'NEQ'}")
ok &= (part[10] == eb360)
print("ALL EQUAL balanced:", ok)
json.dump({"rank": r, "consistent": not incons, "free": free,
           "solution": [str(x) for x in part], "equals_balanced": ok},
          open(os.path.join(HERE, "s9_double_system.json"), "w"), indent=1)
print("wrote s9_double_system.json")
