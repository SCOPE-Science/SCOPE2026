"""Step 24: k-point shortening MacWilliams WITH row-sum constraints, k=7,8 (exact).
Same layout as s16 but adds sum_i n_{w,i} = A_w per w in {16,20,24,28,32}.
Reports rank/consistency/nullity/balanced-equality.
"""
from fractions import Fraction
from math import comb
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, "w72.json")))["A"]
WS = [16, 20, 24, 28, 32]


def build(k):
    nper = k + 1
    nb = len(WS) * nper
    nf = k // 2 if k % 2 == 0 else (k + 1) // 2
    NV = nb + nf

    def n_expr(w, i):
        if i not in range(k + 1) or w < 0 or w > 72:
            return {}
        if w == 0:
            return {"one": Fraction(1)} if i == 0 else {}
        if w == 72:
            return {"one": Fraction(1)} if i == k else {}
        if A[w] == 0:
            return {}
        if w == 36:
            if k % 2 == 0:
                m = k // 2
                if i < m:
                    return {nb + i: Fraction(1)}
                if i == m:
                    e = {"one": Fraction(A[36])}
                    for j in range(m):
                        e[nb + j] = Fraction(-2)
                    return e
                return n_expr(36, k - i)
            else:
                if i <= k // 2:
                    return {nb + i: Fraction(1)}
                return n_expr(36, k - i)
        if w in WS:
            return {WS.index(w) * nper + i: Fraction(1)}
        if 72 - w in WS:
            return n_expr(72 - w, k - i)
        return {}

    def add(e1, e2, s=1):
        e = dict(e1)
        for kk, v in e2.items():
            e[kk] = e.get(kk, Fraction(0)) + s * v
        return {kk: v for kk, v in e.items() if v != 0}

    def cx(e, c):
        return {kk: v * c for kk, v in e.items() if v * c != 0}

    Nn = 72 - k
    dim_s = 36 - k
    AA, BB = {}, {}
    for w in range(Nn + 1):
        AA[w] = n_expr(w, 0)
    for j in range(Nn + 1):
        e = {}
        for i in range(k + 1):
            e = add(e, n_expr(j + i, i))
        BB[j] = e
    K = {}
    for j in range(Nn + 1):
        for w in range(Nn + 1):
            s = Fraction(0)
            for u in range(Nn + 1):
                if 0 <= u <= w and 0 <= j - u <= Nn - w:
                    s += Fraction((-1) ** u) * comb(w, u) * comb(Nn - w, j - u)
            K[(j, w)] = s
    rows = []
    for j in range(Nn + 1):
        e = dict(BB[j])
        for w in range(Nn + 1):
            e = add(e, cx(AA[w], -K[(j, w)] / Fraction(2 ** dim_s)))
        rows.append((f"MW{j}", e))
    for w in WS:
        e = {"one": Fraction(-A[w])}
        for i in range(k + 1):
            e = add(e, n_expr(w, i))
        rows.append((f"ROW{w}", e))
    M, labels = [], []
    for lab, e in rows:
        row = [e.get(i, Fraction(0)) for i in range(NV)] + [-e.get("one", Fraction(0))]
        if any(v != 0 for v in row):
            M.append(row)
            labels.append(lab)
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
                R[i] = [R[i][kk] - q * R[r][kk] for kk in range(NV + 1)]
        piv.append(c)
        r += 1
    incons = [(labels[i], R[i][NV]) for i in range(len(R))
              if all(R[i][c] == 0 for c in range(NV)) and R[i][NV] != 0]
    free = [c for c in range(NV) if c not in piv]
    out = {"k": k, "NV": NV, "nontrivial": len(M), "rank": r,
           "consistent": not incons, "nullity": len(free), "free": free}
    if not incons and not free:
        part = [Fraction(0)] * NV
        for i, c in enumerate(piv):
            part[c] = R[i][NV]
        D = comb(72, k)
        ok = True
        for w in WS:
            for i in range(k + 1):
                eb = Fraction(comb(w, i) * comb(72 - w, k - i) * A[w], D)
                if part[WS.index(w) * nper + i] != eb:
                    ok = False
        out["equals_balanced"] = ok
        out["solution"] = [str(x) for x in part]
    print(f"k={k} rowsum: {len(M)} eqs, {NV} vars, rank {r}, "
          f"consistent={not incons}, nullity={len(free)}" +
          (f", balanced={out.get('equals_balanced')}" if not free and not incons else ""))
    json.dump(out, open(os.path.join(HERE, f"s24_{k}pt_rowsum.json"), "w"), indent=1)
    print(f"wrote s24_{k}pt_rowsum.json")


for k in ([int(s) for s in sys.argv[1:]] or [7, 8]):
    build(k)
