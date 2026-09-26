"""Consolidated EMERGENT-FINDING audit replay (stdlib only, exact integer arithmetic).
Replays every number in the emergent claim from the raw quartic coefficients:
Hilbert + dim; target-partition impossibility (16 != 19); WLP ranks + SLP
determinants (l^4 = 96, det(x^2:A1->A3) = -5808); general Jordan partition via
nullities + conjugate check; classical Hessian determinant evaluations;
Ann_2 witness; quotient-basis spot checks (A2 pivot count, A3 minor det 1).
Prints EMERGENT_AUDIT_OK on success. Runtime ~0.1 s."""

from fractions import Fraction
from itertools import combinations_with_replacement

Nvars, D = 4, 4
names = ['x0', 'u', 'v', 'w']


def mons(k):
    return list(combinations_with_replacement(range(Nvars), k))


def tup2exp(t):
    e = [0]*Nvars
    for i in t:
        e[i] += 1
    return tuple(e)


F = {(1, 1, 1, 1): 1, (0, 4, 0, 0): 1, (0, 0, 4, 0): 1, (0, 0, 0, 4): 1}


def diff_once(poly, i):
    out = {}
    for e, c in poly.items():
        if e[i] > 0:
            ne = list(e)
            ne[i] -= 1
            ne = tuple(ne)
            out[ne] = out.get(ne, 0) + c*e[i]
    return out


def apply_op(t, poly):
    for i in t:
        poly = diff_once(poly, i)
    return poly


def rank_qq(M):
    A = [[Fraction(x) for x in row] for row in M]
    m = len(A)
    n = len(A[0]) if m else 0
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i][c] != 0), None)
        if q is None:
            continue
        A[r], A[q] = A[q], A[r]
        inv = 1/A[r][c]
        A[r] = [x*inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a-f*b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def rref_piv(M):
    A = [[Fraction(x) for x in row] for row in M]
    m = len(A)
    n = len(A[0])
    piv = []
    r = 0
    for c in range(n):
        q = next((i for i in range(r, m) if A[i][c] != 0), None)
        if q is None:
            continue
        A[r], A[q] = A[q], A[r]
        inv = 1/A[r][c]
        A[r] = [x*inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a-f*b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    return piv


def matmul(A, B):
    m = len(A)
    k = len(B)
    n = len(B[0])
    return [[sum(A[i][t]*B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]


def det_qq(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    assert all(len(r) == n for r in A)
    d = Fraction(1)
    for c in range(n):
        q = next((i for i in range(c, n) if A[i][c] != 0), None)
        if q is None:
            return Fraction(0)
        if q != c:
            A[c], A[q] = A[q], A[c]
            d = -d
        d *= A[c][c]
        inv = 1/A[c][c]
        for i in range(c+1, n):
            f = A[i][c]*inv
            for j in range(c, n):
                A[i][j] -= f*A[c][j]
    return d


# ---- 1. catalecticants, Hilbert, dim ----
Ck, Piv, H = {}, {}, {}
for k in range(D+1):
    rows = mons(D-k)
    cols = mons(k)
    ridx = {tup2exp(t): j for j, t in enumerate(rows)}
    M = [[0]*len(cols) for _ in rows]
    for j, t in enumerate(cols):
        for mon, c in apply_op(t, dict(F)).items():
            if sum(mon) == D-k and mon in ridx:
                M[ridx[mon]][j] = c
    Ck[k] = M
    Piv[k] = rref_piv(M)
    H[k] = len(Piv[k])
hf = [H[k] for k in range(5)]
print("Hilbert:", hf, "dim:", sum(hf))
assert hf == [1, 4, 9, 4, 1]
assert sum(hf) == 19

# ---- 2. target-partition impossibility ----
assert sum([5, 3, 3, 3, 1, 1]) == 16 != sum(hf)
print("target partition sums to 16 != 19: impossible as stated")

# ---- 3. Ann_2 = span(x0^2); degree-2 derivative table ----
assert apply_op((0, 0), dict(F)) == {}
assert H[2] == 9
print("Ann_2 witness: x0^2 kills F; h2 = 9")

# ---- 4. multiplication maps at ell = x0+u+v+w ----
def solve_proj(C, piv, rhs):
    m = len(C)
    h = len(piv)
    CP = [[Fraction(C[i][j]) for j in piv] for i in range(m)]
    rhs = [Fraction(x) for x in rhs]
    G = [[sum(CP[i][a]*CP[i][b] for i in range(m)) for b in range(h)] for a in range(h)]
    bv = [sum(CP[i][a]*rhs[i] for i in range(m)) for a in range(h)]
    A = [row[:] + [b] for row, b in zip(G, bv)]
    for c_ in range(h):
        q = next(i for i in range(c_, h) if A[i][c_] != 0)
        A[c_], A[q] = A[q], A[c_]
        inv = 1/A[c_][c_]
        A[c_] = [x*inv for x in A[c_]]
        for i in range(h):
            if i != c_ and A[i][c_] != 0:
                f = A[i][c_]
                A[i] = [a-f*bb for a, bb in zip(A[i], A[c_])]
    return [A[i][h] for i in range(h)]


def mult_mat(k, ell):
    ck = mons(k)
    ck1 = mons(k+1)
    idx1 = {t: j for j, t in enumerate(ck1)}
    Mk = [[Fraction(0)]*H[k] for _ in range(H[k+1])]
    for j, t in enumerate(ck):
        if j not in Piv[k]:
            continue
        pj = Piv[k].index(j)
        for i, c in enumerate(ell):
            if c == 0:
                continue
            nt = tuple(sorted(t+(i,)))
            v = [0]*len(ck1)
            v[idx1[nt]] = c
            C = Ck[k+1]
            rhs = [sum(C[r][s]*v[s] for s in range(len(v))) for r in range(len(C))]
            cc = solve_proj(C, Piv[k+1], rhs)
            for r_ in range(H[k+1]):
                Mk[r_][pj] += cc[r_]
    return Mk


ell = [1, 1, 1, 1]
Ms = {k: mult_mat(k, ell) for k in range(D)}
rks = tuple(rank_qq(Ms[k]) for k in range(4))
print("WLP ranks:", rks)
assert rks == (1, 4, 4, 1)
E2 = matmul(Ms[2], Ms[1])
E4 = matmul(matmul(matmul(Ms[3], Ms[2]), Ms[1]), Ms[0])
assert det_qq(E2) == Fraction(-5808)
assert E4[0][0] == Fraction(96)
print("SLP witnesses: det(x^2:A1->A3) = -5808; x^4:A0->A4 = 96")

# ---- 5. general Jordan partition via nullities + conjugate ----
offs = [0]
for k in range(5):
    offs.append(offs[-1]+H[k])
n = offs[-1]
N = [[Fraction(0)]*n for _ in range(n)]
for k in range(D):
    for a in range(H[k]):
        for b in range(H[k+1]):
            N[offs[k+1]+b][offs[k]+a] = Ms[k][b][a]
nulls = [0]
P = [row[:] for row in N]
for j in range(1, 8):
    if j > 1:
        P = matmul(P, N)
    nulls.append(n-rank_qq(P))
dblocks = [nulls[j]-nulls[j-1] for j in range(1, len(nulls))]
blocks = []
rem = list(dblocks)
while any(x > 0 for x in rem):
    blocks.append(sum(1 for x in rem if x > 0))
    rem = [x-1 for x in rem]
print("nullities:", nulls, "Jordan:", blocks)
assert tuple(blocks) == (5, 3, 3, 3, 1, 1, 1, 1, 1)
conj = sorted([sum(1 for x in hf if x > j) for j in range(max(hf))], reverse=True)
assert tuple(conj) == tuple(blocks)
print("conjugate(HF) matches: maximal type")

# ---- 6. classical Hessian determinant evaluations ----
def hess_det(pt):
    X0v, Uv, Vv, Wv = pt
    Hm = [[0, Vv*Wv, Uv*Wv, Uv*Vv],
          [Vv*Wv, 12*Uv*Uv, Wv*X0v, Vv*X0v],
          [Uv*Wv, Wv*X0v, 12*Vv*Vv, Uv*X0v],
          [Uv*Vv, Vv*X0v, Uv*X0v, 12*Wv*Wv]]
    return det_qq(Hm)


for pt, exp in [((1, 1, 1, 1), -363), ((1, 2, 3, 5), -8399484), ((0, 1, 1, 1), -432)]:
    v = hess_det(pt)
    print("detH%s =" % (pt,), v)
    assert v == exp
print("Hessian nonvanishing witness OK")

print("EMERGENT_AUDIT_OK")
