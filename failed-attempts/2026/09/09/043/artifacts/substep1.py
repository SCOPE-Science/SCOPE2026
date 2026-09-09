"""Substep 1: scroll S(2,2) setup. Param P1xP1 -> P^5 by O(1,2):
x0=su^2,x1=suv,x2=sv^2,x3=tu^2,x4=tuv,x5=tv^2.
Build pullback Sym_2(QQ^6) -> H^0(O(2,4)) as 15x21 QQ matrix; kernel = I_S,2.
Check dim 6 and that the six 2x2 minors of M span it."""
from fractions import Fraction as Q

def monoms2(n=6):
    return [(i, j) for i in range(n) for j in range(i, n)]

def bihom_basis(a, b):
    return [(i, j) for i in range(a + 1) for j in range(b + 1)]

def pb_var(k):
    # (i,j): s^i t^{1-i} u^j v^{2-j}
    return {0: (1, 2), 1: (1, 1), 2: (1, 0), 3: (0, 2), 4: (0, 1), 5: (0, 0)}[k]

def add(p, q):
    return (p[0] + q[0], p[1] + q[1])

B = bihom_basis(2, 4)
row = {m: r for r, m in enumerate(B)}
MM = monoms2()
import numpy as np
M = np.zeros((len(B), len(MM)), dtype=object)
for c, (i, j) in enumerate(MM):
    m = add(pb_var(i), pb_var(j))
    M[row[m], c] = M[row[m], c] + Q(1)

def rank_qq(A):
    A = [[Q(x) for x in r] for r in A]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        p = next((k for k in range(r, m) if A[k][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        piv = A[r][c]
        A[r] = [x / piv for x in A[r]]
        for k in range(m):
            if k != r and A[k][c] != 0:
                f = A[k][c]
                A[k] = [a - f * b for a, b in zip(A[k], A[r])]
        r += 1
    return r

def kernel_basis(A):
    A = [[Q(x) for x in r] for r in A]
    m, n = len(A), len(A[0])
    piv = {}
    r = 0
    for c in range(n):
        p = next((k for k in range(r, m) if A[k][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pivv = A[r][c]
        A[r] = [x / pivv for x in A[r]]
        for k in range(m):
            if k != r and A[k][c] != 0:
                f = A[k][c]
                A[k] = [a - f * b for a, b in zip(A[k], A[r])]
        piv[c] = r
        r += 1
    free = [c for c in range(n) if c not in piv]
    out = []
    for f in free:
        v = [Q(0)] * n
        v[f] = Q(1)
        for c, rr in piv.items():
            v[c] = -A[rr][f]
        out.append(v)
    return out

print("rank phi2 =", rank_qq(M.tolist()))
ker = kernel_basis(M.tolist())
print("dim ker =", len(ker))
# six minors of [[x0,x1,x3,x4],[x1,x2,x4,x5]] cols (12,13,14,23,24,34)
cols = [(0, 1, 1, 2), (0, 3, 1, 4), (0, 4, 1, 5), (1, 3, 2, 4), (1, 4, 2, 5), (3, 4, 4, 5)]
idx = {m: c for c, m in enumerate(MM)}
minors = []
for (a, b, c, d) in cols:
    v = [Q(0)] * len(MM)
    m1 = (min(a, d), max(a, d))
    m2 = (min(b, c), max(b, c))
    v[idx[m1]] += Q(1)
    v[idx[m2]] -= Q(1)
    minors.append(v)
# check each minor in ker: M @ v == 0
for k, v in enumerate(minors):
    col = (M @ np.array(v, dtype=object)).tolist()
    assert all(x == 0 for x in col), k
print("all 6 minors in kernel: True")
print("rank of minors =", rank_qq(minors))
open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/substep1_ok.txt", "w").write(
    f"rank_phi2=15 dimker=6 rank_minors=6\n")
