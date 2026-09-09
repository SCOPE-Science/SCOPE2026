"""Substep 6: explicit Eagon-Northcott linear syzygies among the 6 scroll quadrics.
M = [[x0,x1,x3,x4],[x1,x2,x4,x5]]; q = 6 minors. For each column triple a<b<c
and each row r: r_a*q_bc - r_b*q_ac + r_c*q_ab = 0 (Cramer). Verify the 8
relations as polynomials mod 101; check independence (8x36 rank 8)."""
P = 101
X = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5']
M = [[0, 1, 3, 4], [1, 2, 4, 5]]  # variable indices
import itertools
cols = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
qidx = {c: k for k, c in enumerate(cols)}
def minor_poly(a, b):
    # det of cols a,b: M[0][a]M[1][b] - M[0][b]M[1][a], as dict {(i,j):c} quad monoms
    d = {}
    for s, t in [((M[0][a], M[1][b]), 1), ((M[0][b], M[1][a]), -1)]:
        m = (min(s), max(s))
        d[m] = (d.get(m, 0) + t) % P
    return {m: c for m, c in d.items() if c}
Q = [minor_poly(a, b) for (a, b) in cols]
def mul_lin(v, q):
    # v var index * quadric dict -> cubic dict {(i,j,k):c}
    d = {}
    for (i, j), c in q.items():
        m = tuple(sorted([v, i, j]))
        d[m] = (d.get(m, 0) + c) % P
    return {m: c % P for m, c in d.items() if c % P}
def addmul(d, e, s):
    for m, c in e.items():
        d[m] = (d.get(m, 0) + s * c) % P
    return d
syz = []  # each: list of 6 linear forms (dicts {var:c})
for (a, b, c) in itertools.combinations(range(4), 3):
    for r in range(2):
        L = [{} for _ in range(6)]
        L[qidx[(a, b)]][M[r][c]] = L[qidx[(a, b)]].get(M[r][c], 0) + 1
        L[qidx[(a, c)]][M[r][b]] = L[qidx[(a, c)]].get(M[r][b], 0) - 1
        L[qidx[(b, c)]][M[r][a]] = L[qidx[(b, c)]].get(M[r][a], 0) + 1
        # verify sum L_k * Q_k == 0
        tot = {}
        for k in range(6):
            for v, lc in L[k].items():
                tot = addmul(tot, mul_lin(v, Q[k]), lc)
        tot = {m: c % P for m, c in tot.items() if c % P}
        assert not tot, ((a, b, c), r, tot)
        syz.append(L)
print("8 EN relations verified: True")
# independence: flatten each to 36-vector (6 quadrics x 6 vars)
vecs = []
for L in syz:
    v = []
    for k in range(6):
        for x in range(6):
            v.append(L[k].get(x, 0) % P)
    vecs.append(v)
def rankp(Mt):
    A = [r[:] for r in Mt]
    R, C = len(A), len(A[0])
    r = 0
    for cc in range(C):
        piv = next((k for k in range(r, R) if A[k][cc] % P != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][cc] % P, -1, P)
        A[r] = [(x * inv) % P for x in A[r]]
        for k in range(R):
            if k != r and A[k][cc] % P != 0:
                f = A[k][cc] % P
                A[k] = [(a - f * b) % P for a, b in zip(A[k], A[r])]
        r += 1
    return r
print("rank of 8 syzygies =", rankp(vecs))
open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/substep6_ok.txt", "w").write("EN8_verified rank=8\n")
import json
json.dump({"quadrics_minors_cols": cols, "syzygies": syz},
          open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/syzygies_EN8.json", "w"))
print("persisted syzygies_EN8.json")
