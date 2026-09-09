"""Substep 5: cubic kernel for trigonal C over F_101.
Param P1xP1->P5 by O(1,2). Sym_3(QQ^6)=56 -> H0(O(3,6)) dim 28.
Restrict to C: kernel = I_C,3 (expect 56-25=31 if h0=25). Mod-101 ranks."""
import json
P = 101
d = json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/curve_F101.json"))
C = d["coeffs"]
# bideg bases
def B(a, b):
    return [(i, j) for i in range(a + 1) for j in range(b + 1)]
B36 = B(3, 6); row = {m: r for r, m in enumerate(B36)}
# param exponents per var
PV = {0: (1, 2), 1: (1, 1), 2: (1, 0), 3: (0, 2), 4: (0, 1), 5: (0, 0)}
def add(p, q):
    return (p[0] + q[0], p[1] + q[1])
# cubic monomials k1<=k2<=k3
MM = [(i, j, k) for i in range(6) for j in range(i, 6) for k in range(j, 6)]
n, m = len(B36), len(MM)
# pullback matrix A: 28 x 56 over F_p (entries = multinomial coeffs 1,2,6)
import numpy as np
A = [[0] * m for _ in range(n)]
for c, (i, j, k) in enumerate(MM):
    from math import factorial as f
    from collections import Counter
    cnt = Counter([i, j, k])
    from math import prod
    mult = 6
    for v in cnt.values():
        mult //= f(v)
    mm = add(add(PV[i], PV[j]), PV[k])
    A[row[mm]][c] = (A[row[mm]][c] + mult) % P
# restriction res: H0(O(3,6)) -> H0(O(3,6)|_C): multiply by F is injective map
# H0(O(0,2)) (dim 3) -F-> H0(O(3,6)) (dim 28); coker dim 25. Build F-mult matrix 28x3.
B02 = B(0, 2)
Fcol = {}
for (i, j) in B(3, 4):
    Fcol[(i, j)] = C[i][j] % P
Mf = [[0] * len(B02) for _ in range(n)]
for c2, (u, v) in enumerate(B02):
    for (i, j), cf in Fcol.items():
        if cf:
            Mf[row[(i + u, j + v)]][c2] = (Mf[row[(i + u, j + v)]][c2] + cf) % P
def rankp(Mt, p):
    A2 = [r[:] for r in Mt]
    R, C2 = len(A2), len(A2[0])
    r = 0
    for cc in range(C2):
        piv = next((k for k in range(r, R) if A2[k][cc] % p != 0), None)
        if piv is None:
            continue
        A2[r], A2[piv] = A2[piv], A2[r]
        inv = pow(A2[r][cc] % p, -1, p)
        A2[r] = [(x * inv) % p for x in A2[r]]
        for k in range(R):
            if k != r and A2[k][cc] % p != 0:
                f2 = A2[k][cc] % p
                A2[k] = [(a - f2 * b) % p for a, b in zip(A2[k], A2[r])]
        r += 1
    return r
rF = rankp(Mf, P)
rA = rankp(A, P)
# compose: restrict = coker projection; ker(I3) = ker(coker(F) o A).
# Compute rank of stacked constraint via null of [A | Im F]: dim ker A-proj = m - rank([A cols] mod ImF).
# Direct: form matrix [A | Mf] (28 x 59); rank gives dim(ImA + ImF); ker dim = m - (rank_full - rank_F).
rFull = rankp([ra + rb for ra, rb in zip(A, Mf)], P)
ker3 = m - (rFull - rF)
out = f"rankA={rA} rankF={rF} rankFull={rFull} dimB36={n} nCub={m} kerCubics={ker3}\n"
open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/substep5_ok.txt", "w").write(out)
print(out)
