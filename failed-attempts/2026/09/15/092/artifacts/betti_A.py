"""Case A: full 3x3 symmetric t=2 (affine Veronese), I = 6 quadrics in 6 vars.
vars order: a,b,c,d,e,f; matrix [[a,b,c],[b,d,e],[c,e,f]].
minors: ad-b^2, ae-bc, be-cd, af-c^2, bf-ce, df-e^2.
LTs (lex a>b>c>d>e>f): ad, ae, be, af, bf, df. All S-pairs must reduce to 0
(known: 2-minors of symmetric matrix are GB -- verify computationally).
Then HF + Betti(I) vs Betti(J) via Koszul homology. Expect codim 3, CM.
"""
import numpy as np, time
from math import comb
from itertools import combinations

P = 32003
N = 6

def E(*v):
    assert len(v) == N
    return tuple(v)

def divmod_term(t, lt):
    if all(t[k] >= lt[k] for k in range(N)):
        return tuple(t[k] - lt[k] for k in range(N))
    return None

def make_reducer(GB, LTs):
    GBwo = [{tt: c for tt, c in G.items() if tt != lt} for G, lt in zip(GB, LTs)]
    def red(D, cap=500000):
        D = {t: c % P for t, c in D.items() if c % P != 0}
        steps = 0
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
            for tt, c in GBwo[gi].items():
                u = tuple(tt[k] + q[k] for k in range(N))
                D[u] = (D.get(u, 0) - lc * c) % P
                if D[u] == 0:
                    del D[u]
            steps += 1
            assert steps <= cap
        return D
    return red

f1 = {E(1,0,0,1,0,0): 1, E(0,2,0,0,0,0): P - 1}   # ad-b^2
f2 = {E(1,0,0,0,1,0): 1, E(0,1,1,0,0,0): P - 1}   # ae-bc
f3 = {E(0,1,0,0,1,0): 1, E(0,0,1,1,0,0): P - 1}   # be-cd
f4 = {E(1,0,0,0,0,1): 1, E(0,0,2,0,0,0): P - 1}   # af-c^2
f5 = {E(0,1,0,0,0,1): 1, E(0,0,1,0,1,0): P - 1}   # bf-ce
f6 = {E(0,0,0,1,0,1): 1, E(0,0,0,0,2,0): P - 1}   # df-e^2
GB = [f1, f2, f3, f4, f5, f6]
LTs = [E(1,0,0,1,0,0), E(1,0,0,0,1,0), E(0,1,0,0,1,0),
       E(1,0,0,0,0,1), E(0,1,0,0,0,1), E(0,0,0,1,0,1)]
red = make_reducer(GB, LTs)

def spoly(F, G, ltf, ltg):
    L = tuple(max(a, b) for a, b in zip(ltf, ltg))
    qf = tuple(L[k] - ltf[k] for k in range(N))
    qg = tuple(L[k] - ltg[k] for k in range(N))
    D = {}
    for t, c in F.items():
        u = tuple(t[k] + qf[k] for k in range(N))
        D[u] = (D.get(u, 0) + c) % P
    for t, c in G.items():
        u = tuple(t[k] + qg[k] for k in range(N))
        D[u] = (D.get(u, 0) - c) % P
    return {t: c for t, c in D.items() if c % P != 0}

t0 = time.time()
for i, j in combinations(range(6), 2):
    r = red(spoly(GB[i], GB[j], LTs[i], LTs[j]))
    print(f"S({i},{j}) -> {r}", flush=True)
print(f"GB CHECK DONE ({time.time()-t0:.1f}s)", flush=True)

def monomials_of_degree(d):
    out = []
    def rec(k, rem, cur):
        if k == N - 1:
            out.append(tuple(cur + [rem])); return
        for v in range(rem + 1):
            rec(k + 1, rem - v, cur + [v])
    rec(0, d, [])
    return out

maxdeg, imax, jmax = 7, 4, 7
bI, bJ = {}, {}
for d in range(maxdeg + 1):
    bI[d] = [t for t in monomials_of_degree(d) if red({t: 1}) == {t: 1}]
    bJ[d] = [t for t in monomials_of_degree(d)
             if not any(divmod_term(t, lt) is not None for lt in LTs)]
print("HF R/I:", [len(bI[d]) for d in range(maxdeg + 1)], flush=True)
print("HF R/J:", [len(bJ[d]) for d in range(maxdeg + 1)], flush=True)
print("HF equal:", [len(bI[d]) for d in range(maxdeg+1)] == [len(bJ[d]) for d in range(maxdeg+1)], flush=True)
print(f"HF DONE ({time.time()-t0:.1f}s)", flush=True)

def rank_modp(A):
    A = (np.array(A, dtype=np.int64) % P)
    r, c = A.shape
    rank = 0
    for col in range(c):
        piv = -1
        for row in range(rank, r):
            if A[row, col] != 0:
                piv = row; break
        if piv < 0:
            continue
        if piv != rank:
            A[[piv, rank]] = A[[rank, piv]]
        inv = pow(int(A[rank, col]), -1, P)
        if inv != 1:
            A[rank] = (A[rank] * inv) % P
        for row in range(rank + 1, r):
            f = A[row, col]
            if f:
                A[row] = (A[row] - f * A[rank]) % P
        rank += 1
        if rank == r:
            break
    return rank

def build(basis, red):
    idx = {d: {t: i for i, t in enumerate(basis[d])} for d in basis}
    mult = {}
    for v in range(N):
        mult[v] = {}
        for d in range(maxdeg):
            table = []
            for t in basis[d]:
                u = list(t); u[v] += 1; u = tuple(u)
                r = red({u: 1})
                table.append([(c, idx[d + 1][s]) for s, c in r.items()])
            mult[v][d] = table
    return mult

mI, mJ = build(bI, red), build(bJ, make_reducer([{lt: 1} for lt in LTs], LTs))
print(f"MULT DONE ({time.time()-t0:.1f}s)", flush=True)

def betti(basis, mult, tag):
    subs = {i: list(combinations(range(N), i)) for i in range(imax + 2)}
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
            print(f"[{tag}] K({i},{j}): {nrows}x{ncols}", flush=True)
            R[(i, j)] = rank_modp(M)
            print(f"[{tag}] rank K({i},{j})={R[(i,j)]} ({time.time()-t0:.1f}s)", flush=True)
    B = {}
    for i in range(imax + 1):
        for j in range(jmax + 1):
            d = j - i
            if d < 0 or d > maxdeg:
                B[(i, j)] = 0; continue
            B[(i, j)] = len(subs[i]) * len(basis[d]) - R.get((i, j), 0) - R.get((i + 1, j), 0)
    return B

BI = betti(bI, mI, "I")
BJ = betti(bJ, mJ, "J")
for i in range(imax + 1):
    print(f"i={i} I: {[(j, BI[(i,j)]) for j in range(jmax+1) if BI[(i,j)]]} "
          f"J: {[(j, BJ[(i,j)]) for j in range(jmax+1) if BJ[(i,j)]]}", flush=True)
for tag, B, bb in (("I", BI, bI), ("J", BJ, bJ)):
    for j in range(jmax + 1):
        lhs = sum(((-1) ** i) * B[(i, j)] for i in range(imax + 1))
        rhs = sum(((-1) ** k) * comb(N, k) * len(bb[j - k])
                  for k in range(min(N, j) + 1) if j - k in bb)
        assert lhs == rhs, f"Euler {tag} j={j}: {lhs} vs {rhs}"
print("Euler checks passed", flush=True)
diff = {(i, j): (BI[(i, j)], BJ[(i, j)]) for i in range(imax + 1) for j in range(jmax + 1)
        if BI[(i, j)] != BJ[(i, j)]}
print("Betti(I)==Betti(J):", not diff, diff if diff else "", flush=True)
print("CASE A DONE", flush=True)
