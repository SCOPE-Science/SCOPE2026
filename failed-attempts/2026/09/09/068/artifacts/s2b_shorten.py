"""Step 2b (corrected): fixed-coordinate-1 shortening cells, exact rational solve.
Complement symmetry: c -> c+1 gives t_w + t_{72-w} = A_w (NOT t_w=t_{72-w}).
Free vars u = [t16,t20,t24,t28,t32]; t36 = A36/2 fixed; t_{72-w} = A_w - u_w;
t72 = 1, t0 = 0.
Shortened C_s [71,35]: Ap[w] = A_w - t_w.  Punctured C_p: Bp[j]=(A_j-t_j)+t_{j+1}.
Dual pair (C_s)^\perp = C_p -> MacWilliams Bp = 2^-35 K^{(71)} Ap.
Solve the 72 MW equations + no extra sum rule (implied) for the 5 unknowns.
Report rank, affine solution space, balanced reference, box status.
"""
from fractions import Fraction
from math import comb
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
assert A[36] % 2 == 0
T36 = A[36] // 2

VARS = [16, 20, 24, 28, 32]  # free u_w = t_w for w<36


def t_expr(w):
    if w == 36:
        return {"one": Fraction(T36)}
    if w == 72:
        return {"one": Fraction(1)}
    if w == 0:
        return {}
    if w in VARS:
        return {VARS.index(w): Fraction(1)}
    if 72 - w in VARS:
        e = {"one": Fraction(A[w])}
        e[VARS.index(72 - w)] = Fraction(-1)
        return e
    return {}


def add(e1, e2, s=1):
    e = dict(e1)
    for k, v in e2.items():
        e[k] = e.get(k, Fraction(0)) + s * v
    return {k: v for k, v in e.items() if v != 0}


def cx(e, c):
    return {k: v * c for k, v in e.items() if v * c != 0}


Ap = {}
for w in range(72):
    Ap[w] = add({"one": Fraction(A[w])}, cx(t_expr(w), Fraction(-1)))
Bp = {}
for j in range(72):
    e = add({"one": Fraction(A[j])}, cx(t_expr(j), Fraction(-1)))
    e = add(e, t_expr(j + 1))
    Bp[j] = e

K = {}
for j in range(72):
    for w in range(72):
        s = Fraction(0)
        for t in range(72):
            if 0 <= t <= w and 0 <= j - t <= 71 - w:
                s += Fraction((-1) ** t) * comb(w, t) * comb(71 - w, j - t)
        K[(j, w)] = s

rows = []
for j in range(72):
    e = dict(Bp[j])
    for w in range(72):
        e = add(e, cx(Ap[w], -K[(j, w)] / Fraction(2 ** 35)))
    rows.append((f"MW{j}", e))

NV = 5
M, labels = [], []
for lab, e in rows:
    row = [e.get(i, Fraction(0)) for i in range(NV)] + [-e.get("one", Fraction(0))]
    if any(v != 0 for v in row):
        M.append(row)
        labels.append(lab)
print(f"nontrivial equations: {len(M)} of {len(rows)}")

R = [r[:] for r in M]
pivcol, r = [], 0
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
    pivcol.append(c)
    r += 1
print("rank =", r, "pivots =", [VARS[c] for c in pivcol])
incons = [(labels[i], R[i][NV]) for i in range(len(R))
          if all(R[i][c] == 0 for c in range(NV)) and R[i][NV] != 0]
print("inconsistent rows:", incons if incons else "NONE — system consistent")
free = [c for c in range(NV) if c not in pivcol]
print("free vars:", [VARS[c] for c in free])
part = [Fraction(0)] * NV
for i, c in enumerate(pivcol):
    part[c] = R[i][NV]
print("particular solution (free=0):")
for w in VARS:
    print(f"  u{w} = {part[VARS.index(w)]} ~= {float(part[VARS.index(w)]):.6f}")
NS = []
for f in free:
    v = [Fraction(0)] * NV
    v[f] = Fraction(1)
    for i, c in enumerate(pivcol):
        v[c] = -R[i][f]
    NS.append(v)
for k, v in enumerate(NS):
    print(f"null dir [{VARS[free[k]]}]:", {VARS[i]: v[i] for i in range(NV) if v[i] != 0})

print("balanced w*A_w/72 reference (satisfies complement symmetry):")
for w in VARS + [36]:
    print(f"  w={w}: {w*A[w]}/72 = {w*A[w]/72} ; pair sum check: "
          f"{w*A[w]/72 + (72-w)*A[w]/72} == A[{w}]={A[w]}: {(w*A[w]+(72-w)*A[w])//72==A[w]}")

# verify balanced satisfies all 72 MW equations (residual check)
tbal = {w: Fraction(w * A[w], 72) for w in range(73)}
Apb = [A[w] - tbal[w] for w in range(72)]
Bpb = [(A[j] - tbal[j]) + tbal[j + 1] for j in range(72)]
maxres = Fraction(0)
for j in range(72):
    lhs = Fraction(Bpb[j])
    rhs = sum(Fraction(Apb[w]) * K[(j, w)] for w in range(72)) / Fraction(2 ** 35)
    maxres = max(maxres, abs(lhs - rhs))
print("balanced MW residual max |lhs-rhs| =", maxres)

print("box check at particular solution:")
ok = True
for w in VARS:
    u = part[VARS.index(w)]
    good = 0 <= u <= A[w]
    ok &= good
    print(f"  u{w}={u} in [0,{A[w]}]: {good}")
print("t36 =", T36)

json.dump({"rank": r, "pivots": [VARS[c] for c in pivcol],
           "free": [VARS[c] for c in free],
           "particular": [str(part[VARS.index(w)]) for w in VARS],
           "nullspace": [[str(v[VARS.index(w)]) for w in VARS] for v in NS],
           "consistent": not incons, "t36": T36,
           "balanced_residual": str(maxres)},
          open(os.path.join(HERE, "shorten_system.json"), "w"), indent=1)
print("wrote shorten_system.json")
