"""Exact stdlib-only verification for lane-1120: X9 target is FALSE.

Model: X9 = x^4+y^4 (mu=9); Seifert L = U3 tensor U3 (Sebastiani-Thom of A3+A3),
U3 = A3 Seifert in 1 variable; S = -L - L^T (stabilized symmetric form).
Checks: unimodularity, radical basis + saturation, isotropicity,
Seifert divisibility gcds = 1 (incl. universal primitive lemma),
pointwise fixing of radical by all Picard-Lefschetz reflections.
Run: python3 output/artifacts/verify_x9.py  -> prints VERIFY_OK on success.
"""
from fractions import Fraction
from math import gcd
from functools import reduce
import itertools

U3 = [[-1, 1, 0], [0, -1, 1], [0, 0, -1]]

def kron(A, B):
    m, n, p, q = len(A), len(A[0]), len(B), len(B[0])
    C = [[0] * (n * q) for _ in range(m * p)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                for l in range(q):
                    C[i * p + k][j * q + l] = A[i][j] * B[k][l]
    return C

L = kron(U3, U3)
N = 9
S = [[-L[i][j] - L[j][i] for j in range(N)] for i in range(N)]

w0 = [0, 1, 1, 1, 2, 1, 1, 1, 0]
w1 = [-1, -2, -1, -2, -2, 0, -1, 0, 1]

def matvec(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]

def bilin(u, A, v):
    return sum(u[i] * A[i][j] * v[j] for i in range(len(u)) for j in range(len(u)))

def igcd(v):
    return reduce(gcd, [abs(x) for x in v], 0)

def det_frac(M):
    A = [[Fraction(x) for x in r] for r in M]
    n, sgn = len(A), 1
    for i in range(n):
        piv = next((r for r in range(i, n) if A[r][i] != 0), None)
        assert piv is not None, "singular matrix"
        if piv != i:
            A[i], A[piv] = A[piv], A[i]
            sgn *= -1
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n):
                A[r][c] -= f * A[i][c]
    d = Fraction(sgn)
    for i in range(n):
        d *= A[i][i]
    return d

def rank_frac(M):
    A = [[Fraction(x) for x in r] for r in M]
    m, n, r = len(A), len(A[0]), 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                for j in range(c, n):
                    A[i][j] -= f * A[r][j]
        r += 1
    return r

def nullspace(M):
    A = [[Fraction(x) for x in r] for r in M]
    m, n = len(A), len(A[0])
    pivots, prow, r = [], {}, 0
    for c in range(n):
        piv = next((i for i in range(r, m) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        f = A[r][c]
        for j in range(c, n):
            A[r][j] /= f
        for i in range(m):
            if i != r and A[i][c] != 0:
                ff = A[i][c]
                for j in range(c, n):
                    A[i][j] -= ff * A[r][j]
        pivots.append(c)
        prow[c] = r
        r += 1
    free = [c for c in range(n) if c not in pivots]
    basis = []
    for f_ in free:
        v = [Fraction(0)] * n
        v[f_] = Fraction(1)
        for c in pivots:
            v[c] = -A[prow[c]][f_]
        basis.append(v)
    return basis

fails = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)

# 1. L unimodular (Seifert forms are unimodular; congruence preserves gcds)
d = det_frac(L)
check("det L = +1 (unimodular)", d == 1)

# 2. rank / nullity
check("rank(S) = 7", rank_frac(S) == 7)
ns = nullspace(S)
check("nullity(S) = 2", len(ns) == 2)

# 3. w0, w1 in radical, independent, isotropic
check("S w0 = 0", matvec(S, w0) == [0] * N)
check("S w1 = 0", matvec(S, w1) == [0] * N)
check("w0,w1 Q-independent (rank 2)", rank_frac([list(w0), list(w1)]) == 2)
check("L(w0,w0)=0 isotropic", bilin(w0, L, w0) == 0)
check("L(w1,w1)=0 isotropic", bilin(w1, L, w1) == 0)

# 4. nullspace spanned by w0, w1 over Q (so with saturation, R = Zw0+Zw1)
def in_span(v):
    # solve v = a w0 + b w1 over QQ using two coords where 2x2 minor is a unit
    for a, b in itertools.combinations(range(N), 2):
        det = w0[a] * w1[b] - w0[b] * w1[a]
        if det != 0:
            va, vb = Fraction(v[a]), Fraction(v[b])
            # Cramer
            alpha = (va * w1[b] - vb * w1[a]) / det
            beta = (w0[a] * vb - w0[b] * va) / det
            if all(Fraction(v[k]) == alpha * w0[k] + beta * w1[k] for k in range(N)):
                return True
    return False
check("ker(S) subset Q-span(w0,w1)", all(in_span(v) for v in ns))

# 5. saturation: invariant factors of [w0|w1] are (1,1)
M2 = [[w0[i], w1[i]] for i in range(N)]
d1 = reduce(gcd, [abs(M2[i][j]) for i in range(N) for j in range(2)])
minors = [abs(M2[a][0] * M2[b][1] - M2[a][1] * M2[b][0])
          for a, b in itertools.combinations(range(N), 2)]
D2 = reduce(gcd, minors)
check("span saturated: d1=1, gcd(2x2 minors)=1", d1 == 1 and D2 == 1)

# 6. Seifert divisibility: covectors L^T w have gcd 1
c0 = [sum(L[i][j] * w0[i] for i in range(N)) for j in range(N)]
c1 = [sum(L[i][j] * w1[i] for i in range(N)) for j in range(N)]
check("covector L^T w0 exact", c0 == [0, 1, 0, 1, 0, -1, 0, -1, 0])
check("covector L^T w1 exact", c1 == [-1, -1, 1, -1, 1, 1, 1, 1, -1])
check("divisibility(w0) = gcd = 1", igcd(c0) == 1)
check("divisibility(w1) = gcd = 1", igcd(c1) == 1)
r0 = [sum(L[i][j] * w0[j] for j in range(N)) for i in range(N)]
check("row convention Lw0 gcd also 1", igcd(r0) == 1)

# 7. Universal lemma: cov(a w0 + b w1) = a c0 + b c1 has gcd 1 whenever gcd(a,b)=1.
# Closed form entries: [-b, a-b, b, a-b, b, b-a, b, b-a, -b]; any common divisor
# divides (a-b)+b = a and b, hence divides gcd(a,b) = 1.
def closed(a, b):
    return [-b, a - b, b, a - b, b, b - a, b, b - a, -b]
ok = True
for a in range(-5, 6):
    for b in range(-5, 6):
        if gcd(a, b) != 1:
            continue
        v = [a * x + b * y for x, y in zip(w0, w1)]
        cov = [sum(L[i][j] * v[i] for i in range(N)) for j in range(N)]
        if cov != closed(a, b) or igcd(cov) != 1:
            ok = False
check("universal: all primitive radical covectors gcd 1 (grid -5..5)", ok)

# 8. Reflections fix the radical pointwise: s_i(v) = v + S(v,e_i) e_i; S w = 0.
def Spair(u, v):
    return sum(u[i] * S[i][j] * v[j] for i in range(N) for j in range(N))
e = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
check("all s_i fix w0", all(Spair(w0, e[i]) == 0 for i in range(N)))
check("all s_i fix w1", all(Spair(w1, e[i]) == 0 for i in range(N)))
check("all s_i fix every a w0+b w1",
      all(Spair([2 * x + 3 * y for x, y in zip(w0, w1)], e[i]) == 0 for i in range(N)))

print("CONTENT w0 =", reduce(gcd, [abs(x) for x in w0]),
      " CONTENT w1 =", reduce(gcd, [abs(x) for x in w1]))
if fails:
    print("VERIFY_FAIL:", fails)
    raise SystemExit(1)
print("VERIFY_OK")
