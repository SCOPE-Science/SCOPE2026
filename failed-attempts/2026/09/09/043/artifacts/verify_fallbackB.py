"""verify_fallbackB.py (stdlib-only): replays fallback-(b) certificate over F_101.
C: smooth bidegree-(3,4) curve (seed 606) in P1xP1, embedded by |O(1,2)| into P^5.
Checks: (1) scroll S(2,2) quadrics = 6 minors, kernel dim 6; (2) smoothness (point
search + 4-chart cofactor certs); (3) cubic kernel dim 31; (4) 8 EN linear
syzygies, rank 8. Prints VERIFY_OK on success."""
import json, itertools

P = 101
ART = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-373/output/artifacts/"
d = json.load(open(ART + "curve_F101.json"))
C = d["coeffs"]
assert d["p"] == 101 and d["seed"] == 606

def rankp(Mt):
    A = [[x % P for x in r] for r in Mt]
    R, Cc = len(A), len(A[0])
    r = 0
    for cc in range(Cc):
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

# ---- (1) scroll pullback: Sym2(F^6)=15 cols -> H0(O(2,4))=15 rows
PV = {0: (1, 2), 1: (1, 1), 2: (1, 0), 3: (0, 2), 4: (0, 1), 5: (0, 0)}
B24 = [(i, j) for i in range(3) for j in range(5)]
row = {m: r for r, m in enumerate(B24)}
MM2 = [(i, j) for i in range(6) for j in range(i, 6)]
A2 = [[0] * len(MM2) for _ in range(len(B24))]
for c, (i, j) in enumerate(MM2):
    m = (PV[i][0] + PV[j][0], PV[i][1] + PV[j][1])
    A2[row[m]][c] = (A2[row[m]][c] + 1) % P
assert rankp(A2) == 15, "pullback not surjective"
ker2 = len(MM2) - rankp(A2)
assert ker2 == 6, ker2
# six minors of [[x0,x1,x3,x4],[x1,x2,x4,x5]]
M = [[0, 1, 3, 4], [1, 2, 4, 5]]
cols = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
idx = {m: c for c, m in enumerate(MM2)}
minors = []
for (a, b) in cols:
    v = [0] * len(MM2)
    m1 = (min(M[0][a], M[1][b]), max(M[0][a], M[1][b]))
    m2 = (min(M[0][b], M[1][a]), max(M[0][b], M[1][a]))
    v[idx[m1]] = (v[idx[m1]] + 1) % P
    v[idx[m2]] = (v[idx[m2]] - 1) % P
    minors.append(v)
for v in minors:  # each minor in kernel
    for rr in range(len(B24)):
        assert sum(A2[rr][c] * v[c] for c in range(len(MM2))) % P == 0
assert rankp(minors) == 6, "minors dependent"
print("(1) scroll quadrics: rank_phi2=15 ker=6, 6 minors independent in kernel OK")

# ---- (2a) point smoothness over all P1xP1(F_101)
pts = [(1, b) for b in range(P)] + [(0, 1)]
def pw(s, t, u, v):
    S = [pow(s, 3 - i, P) * pow(t, i, P) % P for i in range(4)]
    U = [pow(u, 4 - j, P) * pow(v, j, P) % P for j in range(5)]
    dS = [((3 - i) * pow(s, max(0, 2 - i), P) * pow(t, i, P)) % P if 3 - i > 0 else 0 for i in range(4)]
    eS = [(i * pow(s, 3 - i, P) * pow(t, max(0, i - 1), P)) % P if i > 0 else 0 for i in range(4)]
    dU = [((4 - j) * pow(u, max(0, 3 - j), P) * pow(v, j, P)) % P if 4 - j > 0 else 0 for j in range(5)]
    eU = [(j * pow(u, 4 - j, P) * pow(v, max(0, j - 1), P)) % P if j > 0 else 0 for j in range(5)]
    F = Fs = Ft = Fu = Fv = 0
    for i in range(4):
        for j in range(5):
            c = C[i][j] % P
            F = (F + c * S[i] % P * U[j]) % P
            Fs = (Fs + c * dS[i] % P * U[j]) % P
            Ft = (Ft + c * eS[i] % P * U[j]) % P
            Fu = (Fu + c * S[i] % P * dU[j]) % P
            Fv = (Fv + c * S[i] % P * eU[j]) % P
    return F, Fs, Ft, Fu, Fv
nF = 0
for (s, t) in pts:
    for (u, v) in pts:
        F, Fs, Ft, Fu, Fv = pw(s, t, u, v)
        if F == 0:
            nF += 1
            assert not (Fs == 0 and Ft == 0 and Fu == 0 and Fv == 0), ((s, t), (u, v))
print(f"(2a) point smoothness OK: {nF} F_101-points on C, none singular")

# ---- (2b) geometric smoothness: 1 in (f,fx,fy) per chart, bounded Macaulay
def chart_terms(kind):
    if kind == "s1u1":
        return {(i, j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P}
    if kind == "s1v1":
        return {(i, 4 - j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P}
    if kind == "t1u1":
        return {(3 - i, j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P}
    return {(3 - i, 4 - j): C[i][j] % P for i in range(4) for j in range(5) if C[i][j] % P}

def deriv(p, var):
    r = {}
    for (a, b), c in p.items():
        e = a if var == 0 else b
        if e:
            k = (a - 1, b) if var == 0 else (a, b - 1)
            r[k] = (r.get(k, 0) + e * c) % P
    return {k: v % P for k, v in r.items() if v % P}

def mons2(B):
    return [(a, b) for a in range(B + 1) for b in range(B + 1 - a)]

def certify(f, fx, fy, B):
    colist = mons2(B)
    ci = {m: k for k, m in enumerate(colist)}
    rows = []
    for p in (f, fx, fy):
        if not p:
            continue
        md = max(a + b for (a, b) in p)
        for (sa, sb) in mons2(B - md):
            r = [0] * len(colist)
            for (a, b), c in p.items():
                if a + sa + b + sb <= B:
                    r[ci[(a + sa, b + sb)]] = (r[ci[(a + sa, b + sb)]] + c) % P
            rows.append(r)
    r0 = rankp(rows)
    e0 = [0] * len(colist)
    e0[ci[(0, 0)]] = 1
    return rankp(rows + [e0]) == r0

for name in ("s1u1", "s1v1", "t1u1", "t1v1"):
    t = chart_terms(name)
    assert certify(t, deriv(t, 0), deriv(t, 1), 14), name
print("(2b) geometric smoothness: 1 in (f,fx,fy) certified in all 4 charts OK")

# ---- (3) cubic kernel dim 31
B36 = [(i, j) for i in range(4) for j in range(7)]
r36 = {m: r for r, m in enumerate(B36)}
MM3 = [(i, j, k) for i in range(6) for j in range(i, 6) for k in range(j, 6)]
from math import factorial as fact
from collections import Counter
A3 = [[0] * len(MM3) for _ in range(len(B36))]
for c, (i, j, k) in enumerate(MM3):
    mult = 6
    for v in Counter([i, j, k]).values():
        mult //= fact(v)
    m = (PV[i][0] + PV[j][0] + PV[k][0], PV[i][1] + PV[j][1] + PV[k][1])
    A3[r36[m]][c] = (A3[r36[m]][c] + mult) % P
B02 = [(i, j) for i in range(1) for j in range(3)]
Mf = [[0] * len(B02) for _ in range(len(B36))]
for c2, (u, v) in enumerate(B02):
    for i in range(4):
        for j in range(5):
            cf = C[i][j] % P
            if cf:
                Mf[r36[(i + u, j + v)]][c2] = (Mf[r36[(i + u, j + v)]][c2] + cf) % P
rF, rFull = rankp(Mf), rankp([ra + rb for ra, rb in zip(A3, Mf)])
assert (rF, rFull) == (3, 28), (rF, rFull)
assert len(MM3) - (rFull - rF) == 31
print("(3) cubic kernel: rankF=3 rankFull=28 kerCubics=31 OK")

# ---- (4) 8 EN syzygies among the 6 scroll quadrics
Q = []
for (a, b) in cols:
    dd = {}
    for pair, sg in [((M[0][a], M[1][b]), 1), ((M[0][b], M[1][a]), -1)]:
        m = (min(pair), max(pair))
        dd[m] = (dd.get(m, 0) + sg) % P
    Q.append({m: c for m, c in dd.items() if c})
def mul_lin(v, q):
    dd = {}
    for (i, j), c in q.items():
        m = tuple(sorted([v, i, j]))
        dd[m] = (dd.get(m, 0) + c) % P
    return {m: c % P for m, c in dd.items() if c % P}
qidx = {c: k for k, c in enumerate(cols)}
vecs = []
nsyz = 0
for (a, b, c) in itertools.combinations(range(4), 3):
    for r in range(2):
        L = [{} for _ in range(6)]
        L[qidx[(a, b)]][M[r][c]] = L[qidx[(a, b)]].get(M[r][c], 0) + 1
        L[qidx[(a, c)]][M[r][b]] = L[qidx[(a, c)]].get(M[r][b], 0) - 1
        L[qidx[(b, c)]][M[r][a]] = L[qidx[(b, c)]].get(M[r][a], 0) + 1
        tot = {}
        for k in range(6):
            for vv, lc in L[k].items():
                for m, cc in mul_lin(vv, Q[k]).items():
                    tot[m] = (tot.get(m, 0) + lc * cc) % P
        assert all(v % P == 0 for v in tot.values())
        nsyz += 1
        vecs.append([L[k].get(x, 0) % P for k in range(6) for x in range(6)])
assert nsyz == 8 and rankp(vecs) == 8
print("(4) 8 Eagon-Northcott linear syzygies verified, rank 8 OK")
print("VERIFY_OK")
