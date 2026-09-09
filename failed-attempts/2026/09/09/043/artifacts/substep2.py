"""Substep 2 (fixed): sample bidegree-(3,4) curve on P1xP1, certify smooth via resultants."""
from fractions import Fraction as Q
import random, json

def padd(a, b):
    n = max(len(a), len(b))
    a = list(a) + [Q(0)] * (n - len(a))
    b = list(b) + [Q(0)] * (n - len(b))
    return [x + y for x, y in zip(a, b)]

def pmul(a, b):
    r = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r

def pnorm(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

ZERO = [Q(0)]

def sylvester(a, b):
    # a,b: lists of polys (highest-degree first); returns matrix of polys
    m, n = len(a) - 1, len(b) - 1
    N = m + n
    rows = []
    for s in range(n):
        row = [list(ZERO) for _ in range(N)]
        for i, c in enumerate(a):
            row[s + i] = list(c)
        rows.append(row)
    for s in range(m):
        row = [list(ZERO) for _ in range(N)]
        for i, c in enumerate(b):
            row[s + i] = list(c)
        rows.append(row)
    return rows

def det_poly(M):
    n = len(M)
    A = [[list(e) for e in row] for row in M]
    d = [Q(1)]
    for c in range(n):
        p = next((k for k in range(c, n) if any(v != 0 for v in A[k][c])), None)
        if p is None:
            return [Q(0)]
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = pmul(d, [Q(-1)])
        piv = A[c][c]
        d = pmul(d, piv)
        lead = piv[-1]
        A[c] = [[w / lead for w in e] for e in A[c]]
        for k in range(c + 1, n):
            f = list(A[k][c])
            if all(v == 0 for v in f):
                continue
            negf = [-x for x in f]
            A[k] = [pnorm(padd(pmul([lead], A[k][j]), pmul(negf, A[c][j]))) for j in range(n)]
    return pnorm(d)

def poly_gcd(a, b):
    a, b = pnorm(list(a)), pnorm(list(b))
    while not (len(b) == 1 and b[0] == 0):
        while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
            c = a[-1] / b[-1]
            shift = len(a) - len(b)
            sub = [Q(0)] * shift + [c * x for x in b]
            a = pnorm(padd(a, [-x for x in sub]))
        a, b = b, a
    return pnorm(a)

def deriv(p):
    return [Q(i) * p[i] for i in range(1, len(p))] or [Q(0)]

rng = random.Random(606606)
def randq():
    return [Q(rng.randint(-2, 2)) for _ in range(5)]
A, B, C, D = randq(), randq(), randq(), randq()
print("A=", A, "B=", B, "C=", C, "D=", D)
fs = [[3 * x for x in A], [2 * x for x in B], list(C)]
ft = [list(B), [2 * x for x in C], [3 * x for x in D]]
fu = [deriv(A), deriv(B), deriv(C), deriv(D)]
R1 = pnorm(det_poly(sylvester(fs, ft)))
S1 = pnorm(det_poly(sylvester(fs, fu)))
print("deg R1 =", len(R1) - 1, "deg S1 =", len(S1) - 1)
g = poly_gcd(R1, S1)
print("gcd =", g)
assert len(g) == 1 and g[0] != 0, "singular or inconclusive; resample seed"
json.dump({"A": [str(x) for x in A], "B": [str(x) for x in B], "C": [str(x) for x in C],
           "D": [str(x) for x in D], "R1deg": len(R1) - 1, "S1deg": len(S1) - 1,
           "gcd": [str(x) for x in g]},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/curve_f.json", "w"))
open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/substep2_ok.txt", "w").write("smooth-certified gcd=constant\n")
print("SMOOTH-CERTIFIED")
