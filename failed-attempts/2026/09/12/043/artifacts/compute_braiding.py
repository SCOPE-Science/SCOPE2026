"""Exact braided data for V2+W2 over D8 and its diagonalisation.

Old basis: 0=a=e_s, 1=b=e_{r2s}, 2=c=f_rs, 3=d=f_r3s.
New basis: e0=a+b, e1=a-b, e2=c+d, e3=c-d.
Checks (exact, sympy QQ): YD action, c-matrix, Yang-Baxter, diagonal q-matrix,
Cartan A2xA2, quad kernel basis, Serre ad^2, root-vector squares, cross
q-commutators, exact symmetrizer ranks S1..S4, exact factor (A2-pair) ranks.
Writes output/artifacts/ledger.json.
"""
import itertools
import json
from collections import defaultdict

import sympy as sp

# ---------- D8 ----------
def mmul(a, b):
    k1, e1 = a
    k2, e2 = b
    if e1 == 0:
        return ((k1 + k2) % 4, e2)
    return ((k1 - k2) % 4, (1 + e2) % 2)

def minv(a):
    k, e = a
    return ((-k) % 4, 0) if e == 0 else (k, 1)

def conj(a, b):
    return mmul(mmul(a, b), minv(a))

one = (0, 0)
s = (0, 1)
r2s = (2, 1)
rs = (1, 1)
r3s = (3, 1)
r2 = (2, 0)

Os = [s, r2s]
Ors = [rs, r3s]
xV = {s: one, r2s: rs}
xW = {rs: one, r3s: s}
assert conj(rs, s) == r2s and conj(s, rs) == r3s

def psi(h):
    assert h in (one, r2, s, r2s), h
    return 1 if h in (one, r2) else -1

def phi(h):
    assert h in (one, r2, rs, r3s), h
    return 1 if h in (one, r2) else -1

# act[h][j] = (gp, scalar)
basis_groups = Os + Ors
act = {}
for h in basis_groups:
    hi = basis_groups.index(h)
    row = {}
    for g in Os:
        gp = conj(h, g)
        t = mmul(mmul(minv(xV[gp]), h), xV[g])
        row[Os.index(g)] = (Os.index(gp), psi(t))
    for g in Ors:
        gp = conj(h, g)
        t = mmul(mmul(minv(xW[gp]), h), xW[g])
        row[2 + Ors.index(g)] = (2 + Ors.index(gp), phi(t))
    act[hi] = row
deg = [0, 1, 2, 3]

# ---------- braiding / symmetrizers (old basis) ----------
def braid_word(n, i):
    d = 4 ** n
    M = sp.zeros(d, d)
    for col in range(d):
        tmp = col
        t = [0] * n
        for k in range(n - 1, -1, -1):
            t[k] = tmp % 4
            tmp //= 4
        a2 = t[i]
        b2 = t[i + 1]
        gp, scc = act[deg[a2]][b2]
        u = list(t)
        u[i] = gp
        u[i + 1] = a2
        row = 0
        for k in range(n):
            row = row * 4 + u[k]
        M[row, col] = scc
    return M

def sym_matrix(n):
    d = 4 ** n
    S = sp.zeros(d, d)
    mats = [braid_word(n, i) for i in range(n - 1)] if n > 1 else [sp.eye(d)]
    from itertools import permutations as perms
    for pi in perms(range(n)):
        cur = list(pi)
        word = []
        for _ in range(n * n):
            for i in range(n - 1):
                if cur[i] > cur[i + 1]:
                    cur[i], cur[i + 1] = cur[i + 1], cur[i]
                    word.append(i)
        M = sp.eye(d)
        for i in word:
            M = mats[i] * M
        S = S + M
    return S

out = {}
C1, C2 = braid_word(3, 0), braid_word(3, 1)
out["yang_baxter_holds"] = bool((C1 * C2 * C1 - C2 * C1 * C2).is_zero_matrix)
assert out["yang_baxter_holds"]
for n in (1, 2, 3, 4):
    out[f"rank_S{n}_QQ"] = int(sym_matrix(n).rank())
assert (out["rank_S1_QQ"], out["rank_S2_QQ"],
        out["rank_S3_QQ"], out["rank_S4_QQ"]) == (4, 8, 12, 14)
S2 = sym_matrix(2)
S3 = sym_matrix(3)
S4 = sym_matrix(4)
ns2 = S2.nullspace()
out["ker_S2_dim"] = len(ns2)
old = ['a', 'b', 'c', 'd']
out["ker_S2_basis"] = [" + ".join(f"{v[c]}*{old[c//4]}{old[c%4]}"
                                  for c in range(16) if v[c] != 0) for v in ns2]
assert len(ns2) == 8

# ---------- diagonalisation ----------
P = {0: {0: 1, 1: 1}, 1: {0: 1, 1: -1}, 2: {2: 1, 3: 1}, 3: {2: 1, 3: -1}}
Q = {0: {0: sp.Rational(1, 2), 1: sp.Rational(1, 2)},
     1: {0: sp.Rational(1, 2), 1: sp.Rational(-1, 2)},
     2: {2: sp.Rational(1, 2), 3: sp.Rational(1, 2)},
     3: {2: sp.Rational(1, 2), 3: sp.Rational(-1, 2)}}
q = {}
for i in range(4):
    for j in range(4):
        acc = defaultdict(int)
        for a2, ca in P[i].items():
            for b2, cb in P[j].items():
                gp, sc = act[deg[a2]][b2]
                for ni, qa in Q[gp].items():
                    for nj, qb in Q[a2].items():
                        acc[(ni, nj)] += ca * cb * sc * qa * qb
        acc = {k: sp.simplify(v) for k, v in acc.items() if sp.simplify(v) != 0}
        assert list(acc.keys()) == [(j, i)], (i, j, acc)
        q[(i, j)] = sp.simplify(acc[(j, i)])
out["q_matrix"] = [[str(q[(i, j)]) for j in range(4)] for i in range(4)]
cartan = []
for i in range(4):
    row = []
    for j in range(4):
        if i == j:
            row.append(2)
        else:
            row.append(0 if sp.simplify(q[(i, j)] * q[(j, i)] - 1) == 0 else -1)
    cartan.append(row)
out["cartan_matrix"] = cartan
assert cartan == [[2, 0, 0, -1], [0, 2, -1, 0],
                  [0, -1, 2, 0], [-1, 0, 0, 2]]

# ---------- e-word -> old-word expansion, kernel tests ----------
def expand_to_old(d):
    acc = defaultdict(int)
    for t, cf in d.items():
        opts = [list(P[x].items()) for x in t]
        for combo in itertools.product(*opts):
            ot = tuple(a for a, _ in combo)
            cc = cf
            for _, ca in combo:
                cc *= ca
            acc[ot] += cc
    return {k: sp.simplify(v) for k, v in acc.items() if sp.simplify(v) != 0}

def oldvec(d_old, n):
    v = sp.zeros(4 ** n, 1)
    for t, cf in d_old.items():
        assert len(t) == n, (t, n)
        r = 0
        for x in t:
            r = r * 4 + x
        v[r, 0] += cf
    return v

def inker_e(d_e, n, S):
    d_old = expand_to_old({k: sp.simplify(v)
                           for k, v in d_e.items() if sp.simplify(v) != 0})
    if not d_old:
        return True
    return bool((S * oldvec(d_old, n)).is_zero_matrix)

def mul(d1, d2):
    acc = defaultdict(int)
    for t1, c1 in d1.items():
        for t2, c2 in d2.items():
            acc[t1 + t2] += c1 * c2
    return {k: sp.simplify(v) for k, v in acc.items() if sp.simplify(v) != 0}

def ad_e(i, d):
    nxt = defaultdict(int)
    for t, cf in d.items():
        nxt[(i,) + t] += cf
        qq = 1
        for tl in t:
            qq *= q[(i, tl)]
        nxt[t + (i,)] += -qq * cf
    return {k: sp.simplify(v) for k, v in nxt.items() if sp.simplify(v) != 0}

sq = {}
for i in range(4):
    assert inker_e({(i, i): 1}, 2, S2), i
    sq[f"e{i}^2"] = True
out["squares_in_ker_S2"] = sq

qcom = {}
for (i, j) in [(0, 1), (0, 2), (1, 3), (2, 3)]:
    d = {(i, j): 1, (j, i): -q[(i, j)]}
    assert inker_e(d, 2, S2), (i, j)
    qcom[f"e{i}e{j}-({q[(i,j)]})e{j}e{i}"] = True
out["disconnected_qcommutators_in_ker_S2"] = qcom

serre = {}
for (i, j) in [(0, 3), (3, 0), (1, 2), (2, 1)]:
    d2 = ad_e(i, ad_e(i, {(j,): 1}))
    assert inker_e(d2, 3, S3), (i, j)
    serre[f"ad_e{i}^2(e{j})"] = {str(k): str(v) for k, v in d2.items()}
out["serre_ad2_in_ker_S3"] = serre

z03 = {(0, 3): 1, (3, 0): 1}     # -q03 = +1
z12 = {(1, 2): 1, (2, 1): -1}    # -q12 = -1
for name, d in [("z03", z03), ("z12", z12)]:
    assert not inker_e(d, 2, S2), name  # nonzero root vectors in B2
    assert inker_e(mul(d, d), 4, S4), name  # squares vanish in B4
out["root_vectors_nonzero_B2_squares_in_ker_S4"] = ["z03", "z12"]

def qdeg(w1, w2):
    p = 1
    for i in w1:
        for j in w2:
            p *= q[(i, j)]
    return sp.simplify(p)

out["root_self_braidings"] = {"z03": str(qdeg((0, 3), (0, 3))),
                              "z12": str(qdeg((1, 2), (1, 2)))}
assert qdeg((0, 3), (0, 3)) == -1 and qdeg((1, 2), (1, 2)) == -1
# cross root relations (verified members of ker S3 / S4)
cross = {}
cross_checks = {
    "e1.z03-q.z03.e1": ({(1,): 1}, z03, 3, S3),
    "e2.z03-q.z03.e2": ({(2,): 1}, z03, 3, S3),
    "e0.z12-q.z12.e0": ({(0,): 1}, z12, 3, S3),
    "e3.z12-q.z12.e3": ({(3,): 1}, z12, 3, S3),
    "z03.z12-q.z12.z03": (z03, z12, 4, S4),
}
for name, (d1, d2, n, S) in cross_checks.items():
    w1 = next(iter(d1)) if len(d1) == 1 else None
    # q-factor uses generator word degrees: collect support degrees
    rel = dict(mul(d1, d2))
    # q-factor on total N^4-multidegrees (homogeneous elements: read off first term)
    t1 = next(iter(d1))
    t2 = next(iter(d2))
    tot1 = [0, 0, 0, 0]
    tot2 = [0, 0, 0, 0]
    for x in t1:
        tot1[x] += 1
    for x in t2:
        tot2[x] += 1
    qq = 1
    for i in range(4):
        for j in range(4):
            qq *= q[(i, j)] ** (tot1[i] * tot2[j])
    for t, c in mul(d2, d1).items():
        rel[t] = sp.simplify(rel.get(t, 0) - qq * c)
    rel = {k: sp.simplify(v) for k, v in rel.items() if sp.simplify(v) != 0}
    assert inker_e(rel, n, S), name
    cross[name] = True
out["cross_root_qcommutators"] = cross

# ---------- exact factor (A2-pair) symmetrizer ranks ----------
def factor_rank(q2, n):
    words = list(itertools.product([0, 1], repeat=n))
    d = len(words)
    idx = {w: k for k, w in enumerate(words)}
    S = sp.zeros(d, d)
    for pi in itertools.permutations(range(n)):
        cur = list(pi)
        word = []
        for _ in range(n * n):
            for i in range(n - 1):
                if cur[i] > cur[i + 1]:
                    cur[i], cur[i + 1] = cur[i + 1], cur[i]
                    word.append(i)
        for c, wrd in enumerate(words):
            sl = list(wrd)
            sg = 1
            for i in word:
                a, b = sl[i], sl[i + 1]
                sg *= q2[a][b]
                sl[i], sl[i + 1] = b, a
            S[idx[tuple(sl)], c] += sg
    return int(S.rank())

out["factor_A03_ranks_n0to5"] = [factor_rank([[-1, -1], [1, -1]], n) for n in range(6)]
out["factor_B12_ranks_n0to5"] = [factor_rank([[-1, 1], [-1, -1]], n) for n in range(6)]
assert out["factor_A03_ranks_n0to5"] == [1, 2, 2, 2, 1, 0]
assert out["factor_B12_ranks_n0to5"] == [1, 2, 2, 2, 1, 0]

with open("output/artifacts/ledger.json", "w") as f:
    json.dump(out, f, indent=2)
print("OK ledger.json written")
print(json.dumps({k: v for k, v in out.items()
                  if not k.startswith(("serre", "ker_S2_basis"))}, indent=2))
