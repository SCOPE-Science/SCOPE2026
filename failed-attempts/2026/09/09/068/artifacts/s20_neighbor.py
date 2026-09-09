"""Step 20 (target escalation): C0-neighbor shadow system (exact).
Putative Type II C [72,36] w/ enumerator A. Let C0=[72,35] doubly-even subcode,
1 in C0. x_w = #{wt-w words of C outside C0}; x_0=x_72=0, x_w=x_{72-w}.
Free: x16,x20,x24,x28,x32,x36.
C_w = A_w - x_w. D = 2^-35 K^{(72)} C (enumerator of C0^perp).
Key: C0^perp = C union C1 union C2 with C1,C2 singly-even => D_w = A_w for all
w = 0 mod 4. Impose these equations; solve exactly; report rank/consistency.
If inconsistent => GENUINE enumerator-level exclusion (target win).
If consistent => check residual s_w = D_w - A_w >= 0 on 2 mod 4 weights.
"""
from fractions import Fraction
from math import comb
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
WS = [16, 20, 24, 28, 32, 36]


def x_expr(w):
    if w in (0, 72):
        return {}
    if A[w] == 0:
        return {}
    if w in WS:
        return {WS.index(w): Fraction(1)}
    if 72 - w in WS:
        return {WS.index(72 - w): Fraction(1)}
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
# equations D_w = A_w for w = 0 mod 4
eqs = []
for w in range(0, 73, 4):
    e = add(dict(D[w]), {"one": Fraction(-A[w])})
    eqs.append((w, e))
NV = 6
M, labels = [], []
for w, e in eqs:
    row = [e.get(i, Fraction(0)) for i in range(NV)] + [-e.get("one", Fraction(0))]
    if any(v != 0 for v in row):
        M.append(row)
        labels.append(w)
print(f"nontrivial 0-mod-4 equations: {len(M)} of {len(eqs)}; unknowns {NV}")
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
print("free:", [WS[c] for c in free] if free else "none")
if not incons:
    part = [Fraction(0)] * NV
    for i, c in enumerate(piv):
        part[c] = R[i][NV]
    print("particular solution:", {WS[c]: part[c] for c in range(NV)})
    # residual shadow s_w = D_w - A_w evaluated at particular (free=0)
    NS = []
    for f in free:
        v = [Fraction(0)] * NV
        v[f] = Fraction(1)
        for i, c in enumerate(piv):
            v[c] = -R[i][f]
        NS.append(v)
    def point(ts):
        x = list(part)
        for t, v in zip(ts, NS):
            for c in range(NV):
                x[c] += t * v[c]
        return x
    x0 = point([Fraction(0)] * len(free))
    # evaluate D - A at x0 for all weights
    # rebuild numeric C0/D at x0
    xv = {w: Fraction(0) for w in range(73)}
    for c, w in enumerate(WS):
        xv[w] = x0[c]
        xv[72 - w] = x0[c]
    Cv = [A[w] - xv[w] for w in range(73)]
    Dv = [sum(Cv[w] * K[(j, w)] for w in range(73)) / Fraction(2 ** 35) for j in range(73)]
    sv = [Dv[j] - A[j] for j in range(73)]
    print("shadow residual s_w = D_w - A_w at particular:")
    neg = []
    for j in range(73):
        if sv[j] != 0:
            print(f"  s[{j}] = {sv[j]} = {float(sv[j]):.4f}")
            if sv[j] < 0:
                neg.append(j)
    print("negative shadow residuals:", neg if neg else "none")
    print("support outside 2 mod 4:", [j for j in range(73) if sv[j] != 0 and j % 4 != 2 and j != 0] or "none")
    print("sum s =", sum(sv), "(expect 2^36 =", 2 ** 36, ")")
    json.dump({"rank": r, "consistent": True, "free": [WS[c] for c in free],
               "particular": [str(x) for x in x0],
               "shadow": [str(sv[j]) for j in range(73)],
               "negative": neg}, open(os.path.join(HERE, "s20_neighbor.json"), "w"), indent=1)
else:
    json.dump({"rank": r, "consistent": False,
               "inconsistent_rows": [[w, str(v)] for (w, v) in incons]},
              open(os.path.join(HERE, "s20_neighbor.json"), "w"), indent=1)
print("wrote s20_neighbor.json")
