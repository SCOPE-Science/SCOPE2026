"""Lean Betti recovery test for lane-20313 (no sympy).

Case B first: symmetric ladder dropping f, vars a,b,c,d,e, t=2.
I = (ad-b^2, ae-bc, be-cd). Assumed lex (a>b>c>d>e) GB with LTs ad, ae, be.
Check S-pairs reduce to zero, then Koszul-homology Betti tables for R/I, R/J.
"""
import numpy as np
from math import comb
from itertools import combinations

P = 32003

def sub_scaled(D, G, q, scale):
    for t, c in G.items():
        u = tuple(t[k] + q[k] for k in range(len(t)))
        D[u] = (D.get(u, 0) - scale * c) % P
        if D[u] == 0:
            del D[u]

def divmod_term(t, lt):
    if all(t[k] >= lt[k] for k in range(len(t))):
        return tuple(t[k] - lt[k] for k in range(len(t)))
    return None

def lt_lex(D, n):
    order = list(range(n))
    return max(D, key=lambda t: tuple(t[v] for v in order))

def reduce_full(D, GB, LTs):
    D = {t: c % P for t, c in D.items() if c % P != 0}
    while True:
        hit = None
        for t in D:
            for gi, lt in enumerate(LTs):
                q = divmod_term(t, lt)
                if q is not None:
                    hit = (t, gi, q); break
            if hit is not None:
                break
        if hit is None:
            return D
        t, gi, q = hit
        lc = D.pop(t)
        sub_scaled(D, GB[gi], q, lc)

def spoly(F, G, ltf, ltg):
    L = tuple(max(a, b) for a, b in zip(ltf, ltg))
    qf = tuple(L[k] - ltf[k] for k in range(len(L)))
    qg = tuple(L[k] - ltg[k] for k in range(len(L)))
    D = {}
    for t, c in F.items():
        u = tuple(t[k] + qf[k] for k in range(len(t)))
        D[u] = (D.get(u, 0) + c) % P
    for t, c in G.items():
        u = tuple(t[k] + qg[k] for k in range(len(t)))
        D[u] = (D.get(u, 0) - c) % P
    return {t: c for t, c in D.items() if c}

def E(*v):
    return tuple(v)

# Case B: vars a,b,c,d,e; f1=ad-b^2, f2=ae-bc, f3=be-cd
n = 5
f1 = {E(1,0,0,1,0): 1, E(0,2,0,0,0): P - 1}
f2 = {E(1,0,0,0,1): 1, E(0,1,1,0,0): P - 1}
f3 = {E(0,1,0,0,1): 1, E(0,0,2,0,0): 0, E(0,0,1,1,0): P - 1}
del f3[E(0,0,2,0,0)]
GB = [f1, f2, f3]
LTs = [lt_lex(g, n) for g in GB]
print("LTs:", LTs)
assert LTs == [E(1,0,0,1,0), E(1,0,0,0,1), E(0,1,0,0,1)], LTs
for i, j in combinations(range(3), 2):
    r = reduce_full(spoly(GB[i], GB[j], LTs[i], LTs[j]), GB, LTs)
    print(f"S({i},{j}) remainder: {r}")
    assert r == {}, "NOT a Groebner basis!"
print("GB check passed: 3 minors are a lex Groebner basis.")

def monomials_of_degree(nv, d):
    out = []
    def rec(k, rem, cur):
        if k == nv - 1:
            out.append(tuple(cur + [rem])); return
        for v in range(rem + 1):
            rec(k + 1, rem - v, cur + [v])
    rec(0, d, [])
    return out

def basis_of_deg(nv, LTs, d, GB):
    out = []
    for t in monomials_of_degree(nv, d):
        if GB is None:
            if not any(divmod_term(t, lt) is not None for lt in LTs):
                out.append(t)
        else:
            r = reduce_full({t: 1}, GB, LTs)
            assert set(r) <= {t}, f"monomial {t} not a normal monomial?!"
            if r.get(t) == 1:
                out.append(t)
    return out

maxdeg = 6
bI = {d: basis_of_deg(n, LTs, d, GB) for d in range(maxdeg + 1)}
JL = [(1,0,0,1,0), (1,0,0,0,1), (0,1,0,0,1)]
bJ = {d: basis_of_deg(n, JL, d, None) for d in range(maxdeg + 1)}
print("HF R/I:", [len(bI[d]) for d in range(maxdeg + 1)])
print("HF R/J:", [len(bJ[d]) for d in range(maxdeg + 1)])

def rank_modp(A):
    A = np.array(A, dtype=np.int64) % P
    r, c = A.shape
    rank = 0
    for col in range(c):
        piv = -1
        for row in range(rank, r):
            if A[row, col] % P != 0:
                piv = row; break
        if piv < 0:
            continue
        if piv != rank:
            A[[piv, rank]] = A[[rank, piv]]
        inv = pow(int(A[rank, col] % P), -1, P)
        A[rank] = (A[rank] * inv) % P
        for row in range(rank + 1, r):
            f = A[row, col] % P
            if f:
                A[row] = (A[row] - f * A[rank]) % P
        rank += 1
        if rank == r:
            break
    return rank

def mult_table(basis, LTs, GB):
    mult = {}
    for v in range(n):
        mult[v] = {}
        for d in range(maxdeg):
            idx = {t: i for i, t in enumerate(basis[d + 1])}
            table = []
            for t in basis[d]:
                u = list(t); u[v] += 1; u = tuple(u)
                r = reduce_full({u: 1}, LTs, GB) if GB is not None else (
                    {u: 1} if not any(divmod_term(u, lt) is not None for lt in LTs) else {})
                table.append([(c, idx[s]) for s, c in r.items()])
            mult[v][d] = table
    return mult

def betti(basis, mult, imax, jmax):
    subs = {i: list(combinations(range(n), i)) for i in range(imax + 2)}
    sidx = {i: {s: k for k, s in enumerate(subs[i])} for i in subs}
    R = {}
    for i in range(1, imax + 2):
        for j in range(jmax + 1):
            d = j - i
            if d < 0 or d + 1 > maxdeg:
                R[(i, j)] = 0; continue
            ncols = len(subs[i]) * len(basis[d])
            nrows = len(subs[i - 1]) * len(basis[d + 1])
            if ncols == 0 or nrows == 0:
                R[(i, j)] = 0; continue
            M = np.zeros((nrows, ncols), dtype=np.int64)
            for cs, S in enumerate(subs[i]):
                for cm in range(len(basis[d])):
                    col = cs * len(basis[d]) + cm
                    for pos, v in enumerate(S):
                        T = tuple(x for k, x in enumerate(S) if k != pos)
                        rt = sidx[i - 1][T]
                        for (c, m2) in mult[v][d][cm]:
                            row = rt * len(basis[d + 1]) + m2
                            M[row, col] = (M[row, col] + ((-1) ** pos) * int(c)) % P
            R[(i, j)] = rank_modp(M)
    B = {}
    for i in range(imax + 1):
        for j in range(jmax + 1):
            d = j - i
            if d < 0 or d > maxdeg:
                B[(i, j)] = 0; continue
            dim = len(subs[i]) * len(basis[d])
            B[(i, j)] = (dim - R.get((i, j), 0)) - R.get((i + 1, j), 0)
    return B

mI = mult_table(bI, LTs, GB)
mJ = mult_table(bJ, JL, None)
BI = betti(bI, mI, 3, 5)
BJ = betti(bJ, mJ, 3, 5)
for i in range(4):
    print(f"i={i} I:", {j: BI[(i, j)] for j in range(6) if BI[(i, j)]},
          " J:", {j: BJ[(i, j)] for j in range(6) if BJ[(i, j)]})
ok = True
for j in range(6):
    lhs = sum(((-1) ** i) * BI[(i, j)] for i in range(4))
    rhs = sum(((-1) ** k) * comb(n, k) * len(bI[j - k])
              for k in range(min(n, j) + 1) if j - k in bI)
    if lhs != rhs:
        ok = False; print("EULER I MISMATCH", j, lhs, rhs)
print("euler I ok:", ok)
ok = True
for j in range(6):
    lhs = sum(((-1) ** i) * BJ[(i, j)] for i in range(4))
    rhs = sum(((-1) ** k) * comb(n, k) * len(bJ[j - k])
              for k in range(min(n, j) + 1) if j - k in bJ)
    if lhs != rhs:
        ok = False; print("EULER J MISMATCH", j, lhs, rhs)
print("euler J ok:", ok)
diff = {(i, j): (BI[(i, j)], BJ[(i, j)]) for i in range(4) for j in range(6)
        if BI[(i, j)] != BJ[(i, j)]}
print("Betti tables equal:", not diff, diff if diff else "")
print("CASE B DONE")
