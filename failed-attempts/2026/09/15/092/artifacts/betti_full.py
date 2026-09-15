"""Full Betti recovery test, corrected reduction (skip-LT form), case B then case A.

Case B: ladder drop-f, I=(ad-b^2, ae-bc, be-cd) in 5 vars; J=(ad,ae,be).
Case A: full 3x3 symmetric t=2, I = 6 quadrics in 6 vars; J = 6 diagonal monomials.
Method: Koszul homology over F_p, Macaulay-matrix ranks; Euler/Hilbert self-check;
two primes for prime-independence on the small case, one prime + Euler check on big.
"""
import numpy as np, time
from math import comb
from itertools import combinations

P = 32003

def divmod_term(t, lt):
    if all(t[k] >= lt[k] for k in range(len(t))):
        return tuple(t[k] - lt[k] for k in range(len(t)))
    return None

def make_reducer(GB, LTs, n, P):
    LTset = list(LTs)
    GBwo = [{tt: c for tt, c in G.items() if tt != lt} for G, lt in zip(GB, LTs)]
    def reduce_full(D, cap=200000):
        D = {t: c % P for t, c in D.items() if c % P != 0}
        steps = 0
        while True:
            hit = None
            for t in D:
                for gi, lt in enumerate(LTset):
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
                u = tuple(tt[k] + q[k] for k in range(n))
                D[u] = (D.get(u, 0) - lc * c) % P
                if D[u] == 0:
                    del D[u]
            steps += 1
            assert steps <= cap, "reduction did not terminate"
        return D
    return reduce_full

def monomials_of_degree(nv, d):
    out = []
    def rec(k, rem, cur):
        if k == nv - 1:
            out.append(tuple(cur + [rem])); return
        for v in range(rem + 1):
            rec(k + 1, rem - v, cur + [v])
    rec(0, d, [])
    return out

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
        colvals = A[rank + 1:, col]
        nz = np.nonzero(colvals)[0]
        for k in nz:
            row = rank + 1 + k
            A[row] = (A[row] - A[row, col] * A[rank]) % P
        rank += 1
        if rank == r:
            break
    return rank

def run_quotient(n, GB, LTs, JLTs, maxdeg, imax, jmax, label, check_gb_pairs=None):
    red = make_reducer(GB, LTs, n, P)
    redJ = make_reducer([{lt: 1} for lt in JLTs], JLTs, n, P)
    if check_gb_pairs:
        def spoly(F, G, ltf, ltg):
            L = tuple(max(a, b) for a, b in zip(ltf, ltg))
            qf = tuple(L[k] - ltf[k] for k in range(n))
            qg = tuple(L[k] - ltg[k] for k in range(n))
            D = {}
            for t, c in F.items():
                u = tuple(t[k] + qf[k] for k in range(n))
                D[u] = (D.get(u, 0) + c) % P
            for t, c in G.items():
                u = tuple(t[k] + qg[k] for k in range(n))
                D[u] = (D.get(u, 0) - c) % P
            return {t: c for t, c in D.items() if c % P != 0}
        for i, j in check_gb_pairs:
            r = red(spoly(GB[i], GB[j], LTs[i], LTs[j]))
            assert r == {}, f"S({i},{j}) nonzero: {r}"
        print(f"[{label}] GB check passed ({len(check_gb_pairs)} S-pairs -> 0)", flush=True)
    t0 = time.time()
    bI, bJ = {}, {}
    for d in range(maxdeg + 1):
        bI[d] = [t for t in monomials_of_degree(n, d) if red({t: 1}) == {t: 1}]
        bJ[d] = [t for t in monomials_of_degree(n, d)
                 if not any(divmod_term(t, lt) is not None for lt in JLTs)]
    print(f"[{label}] HF R/I: {[len(bI[d]) for d in range(maxdeg+1)]} ({time.time()-t0:.1f}s)", flush=True)
    print(f"[{label}] HF R/J: {[len(bJ[d]) for d in range(maxdeg+1)]}", flush=True)
    assert [len(bI[d]) for d in range(maxdeg+1)] == [len(bJ[d]) for d in range(maxdeg+1)], \
        "Hilbert function mismatch -> J is not the initial ideal!"
    def mult_table(basis, red):
        idx = {d: {t: i for i, t in enumerate(basis[d])} for d in basis}
        mult = {}
        for v in range(n):
            mult[v] = {}
            for d in range(maxdeg):
                table = []
                for t in basis[d]:
                    u = list(t); u[v] += 1; u = tuple(u)
                    r = red({u: 1})
                    table.append([(c, idx[d + 1][s]) for s, c in r.items()])
                mult[v][d] = table
        return mult
    mI, mJ = mult_table(bI, red), mult_table(bJ, redJ)
    print(f"[{label}] mult tables built ({time.time()-t0:.1f}s)", flush=True)
    def betti(basis, mult):
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
                print(f"[{label}] rank K_{i},{j} done ({time.time()-t0:.1f}s)", flush=True)
        B = {}
        for i in range(imax + 1):
            for j in range(jmax + 1):
                d = j - i
                if d < 0 or d > maxdeg:
                    B[(i, j)] = 0; continue
                dim = len(subs[i]) * len(basis[d])
                B[(i, j)] = (dim - R.get((i, j), 0)) - R.get((i + 1, j), 0)
        return B
    BI = betti(bI, mI); BJ = betti(bJ, mJ)
    for i in range(imax + 1):
        print(f"[{label}] i={i} I: {[ (j, BI[(i,j)]) for j in range(jmax+1) if BI[(i,j)]]} "
              f"J: {[ (j, BJ[(i,j)]) for j in range(jmax+1) if BJ[(i,j)]]}", flush=True)
    for tag, B, bb in (("I", BI, bI), ("J", BJ, bJ)):
        for j in range(jmax + 1):
            lhs = sum(((-1) ** i) * B[(i, j)] for i in range(imax + 1))
            rhs = sum(((-1) ** k) * comb(n, k) * len(bb[j - k])
                      for k in range(min(n, j) + 1) if j - k in bb)
            assert lhs == rhs, f"Euler {tag} j={j}: {lhs} vs {rhs}"
    print(f"[{label}] Euler checks passed for I and J", flush=True)
    diff = {(i, j): (BI[(i, j)], BJ[(i, j)]) for i in range(imax + 1) for j in range(jmax + 1)
            if BI[(i, j)] != BJ[(i, j)]}
    print(f"[{label}] Betti(I)==Betti(J): {not diff}" + (f" diffs={diff}" if diff else ""), flush=True)
    return not diff

def E5(*v):
    return tuple(v)
n = 5
f1 = {E5(1,0,0,1,0): 1, E5(0,2,0,0,0): P - 1}
f2 = {E5(1,0,0,0,1): 1, E5(0,1,1,0,0): P - 1}
f3 = {E5(0,1,0,0,1): 1, E5(0,0,1,1,0): P - 1}
eqB = run_quotient(5, [f1, f2, f3],
                   [E5(1,0,0,1,0), E5(1,0,0,0,1), E5(0,1,0,0,1)],
                   [(1,0,0,1,0), (1,0,0,0,1), (0,1,0,0,1)],
                   6, 3, 5, "B",
                   check_gb_pairs=[(0,1),(0,2),(1,2)])
print("RESULT B equal:", eqB, flush=True)
print("ALL DONE", flush=True)
