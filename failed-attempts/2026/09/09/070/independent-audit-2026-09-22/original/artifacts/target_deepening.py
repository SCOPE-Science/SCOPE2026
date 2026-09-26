"""Target deepening replay (stdlib only): quotient bases, min-poly t^5 + explicit
length-5 chain, socle-degree cap, Perazzo-shape identity, Jordan x^j rank table.
All exact integer/Fraction arithmetic. Prints DEEPENING_OK on success."""
from fractions import Fraction
from itertools import combinations_with_replacement
Nvars, D = 4, 4
names = ['x0', 'u', 'v', 'w']
def mons(k): return list(combinations_with_replacement(range(Nvars), k))
def nm(t): return '1' if not t else '*'.join(names[i] for i in t)
def tup2exp(t):
    e = [0]*Nvars
    for i in t: e[i] += 1
    return tuple(e)
F = {(1,1,1,1):1,(0,4,0,0):1,(0,0,4,0):1,(0,0,0,4):1}
def diff_once(poly, i):
    out = {}
    for e, c in poly.items():
        if e[i] > 0:
            ne = list(e); ne[i] -= 1; ne = tuple(ne)
            out[ne] = out.get(ne, 0) + c*e[i]
    return out
def apply_op(t, poly):
    for i in t: poly = diff_once(poly, i)
    return poly
def rref_piv(M):
    A = [[Fraction(x) for x in row] for row in M]; m = len(A); n = len(A[0])
    piv = []; r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i][c] != 0), None)
        if q is None: continue
        A[r], A[q] = A[q], A[r]; inv = 1/A[r][c]; A[r] = [x*inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a-f*b for a, b in zip(A[i], A[r])]
        piv.append(c); r += 1
    return piv
def rank_qq(M):
    A = [[Fraction(x) for x in row] for row in M]
    m = len(A); n = len(A[0]) if m else 0; r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i][c] != 0), None)
        if q is None: continue
        A[r], A[q] = A[q], A[r]; inv = 1/A[r][c]; A[r] = [x*inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]; A[i] = [a-f*b for a, b in zip(A[i], A[r])]
        r += 1
    return r
def matmul(A, B):
    m = len(A); k = len(B); n = len(B[0])
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]
Ck, Piv, H = {}, {}, {}
for k in range(D+1):
    rows = mons(D-k); cols = mons(k)
    ridx = {tup2exp(t): j for j, t in enumerate(rows)}
    M = [[0]*len(cols) for _ in rows]
    for j, t in enumerate(cols):
        for mon, c in apply_op(t, dict(F)).items():
            if sum(mon) == D-k and mon in ridx: M[ridx[mon]][j] = c
    Ck[k] = M; Piv[k] = rref_piv(M); H[k] = len(Piv[k])
# (c) quotient bases
exp_bases = {0: [()], 1: [(0,), (1,), (2,), (3,)],
             2: [(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)],
             3: [(0,1,2),(0,1,3),(0,2,3),(1,2,3)], 4: [(0,1,2,3)]}
for k in range(5):
    got = [mons(k)[j] for j in Piv[k]]
    assert got == exp_bases[k], (k, got)
    print(f"A_{k} basis:", [nm(t) for t in got])
# (e) Perazzo shape
assert diff_once(dict(F), 0) == {(0,1,1,1): 1}
assert {e: c for e, c in F.items() if e[0] == 0} == {(0,4,0,0):1,(0,0,4,0):1,(0,0,0,4):1}
print("Perazzo shape: F = X0*UVW + (U^4+V^4+W^4) OK")
# (d) socle cap: R_5, R_6 kill F
for k in (5, 6):
    for t in mons(k):
        assert apply_op(t, dict(F)) == {}, (k, t)
print("socle degree exactly 4 (h5=h6=0) OK; socle value x0*u*v*w ->",
      apply_op((0,1,2,3), dict(F)))
assert apply_op((0,1,2,3), dict(F)) == {(0,0,0,0): 1}
def solve_proj(C, piv, rhs):
    m = len(C); h = len(piv)
    CP = [[Fraction(C[i][j]) for j in piv] for i in range(m)]
    rhs = [Fraction(x) for x in rhs]
    G = [[sum(CP[i][a]*CP[i][b] for i in range(m)) for b in range(h)] for a in range(h)]
    bv = [sum(CP[i][a]*rhs[i] for i in range(m)) for a in range(h)]
    A = [row[:] + [b] for row, b in zip(G, bv)]
    for c_ in range(h):
        q = next(i for i in range(c_, h) if A[i][c_] != 0)
        A[c_], A[q] = A[q], A[c_]; inv = 1/A[c_][c_]; A[c_] = [x*inv for x in A[c_]]
        for i in range(h):
            if i != c_ and A[i][c_] != 0:
                f = A[i][c_]; A[i] = [a-f*bb for a, bb in zip(A[i], A[c_])]
    return [A[i][h] for i in range(h)]
def mult_mat(k, ell):
    ck = mons(k); ck1 = mons(k+1); idx1 = {t: j for j, t in enumerate(ck1)}
    Mk = [[Fraction(0)]*H[k] for _ in range(H[k+1])]
    for j, t in enumerate(ck):
        if j not in Piv[k]: continue
        pj = Piv[k].index(j)
        for i, c in enumerate(ell):
            if c == 0: continue
            nt = tuple(sorted(t+(i,)))
            v = [0]*len(ck1); v[idx1[nt]] = c
            C = Ck[k+1]
            rhs = [sum(C[r][s]*v[s] for s in range(len(v))) for r in range(len(C))]
            cc = solve_proj(C, Piv[k+1], rhs)
            for r_ in range(H[k+1]): Mk[r_][pj] += cc[r_]
    return Mk
ell = [1,1,1,1]
Ms = {k: mult_mat(k, ell) for k in range(4)}
offs = [0]
for k in range(5): offs.append(offs[-1]+H[k])
n = offs[-1]
N = [[Fraction(0)]*n for _ in range(n)]
for k in range(4):
    for a in range(H[k]):
        for b in range(H[k+1]):
            N[offs[k+1]+b][offs[k]+a] = Ms[k][b][a]
P = N
for _ in range(3): P = matmul(P, N)
P5 = matmul(P, N)
assert rank_qq(P) == 1 and rank_qq(P5) == 0
print("min-poly(N) = t^5 (rank N^4=1, N^5=0) OK")
v = {0: [Fraction(1)]}
for k in range(4):
    w = [sum(Ms[k][r][c]*v[k][c] for c in range(len(v[k]))) for r in range(H[k+1])]
    assert any(x != 0 for x in w)
    v[k+1] = w
print("explicit chain l^4 = 96 in A_4:", v[4])
assert v[4] == [Fraction(96)]
print("x^j rank table:")
for j in range(1, 5):
    row = []
    for i in range(0, 5-j):
        Pij = Ms[i]
        for s in range(1, j): Pij = matmul(Ms[i+s], Pij)
        row.append(((i, i+j), rank_qq(Pij)))
    print(" j =", j, row)
print("DEEPENING_OK")
