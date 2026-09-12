#!/usr/bin/env python3
"""Independent verification: E-relative normalized bar complex over Q (exact)
plus independent mod-p reimplementation; controls; candidate A0 variants.

Candidates:
 S0 (parallel): a1,a2:1->2, b:2->3, c:3->1; I=<a1 b, b c, c a1>
 S1 (two-cycle): a:1->2, as:2->1, b:2->3, c:3->1; I=<a as, b c>
 S2 (two-cycle mirror): a:1->2, as:2->1, b:2->3, c:3->1; I=<as a, c a>
 S3 (two-cycle repaired): a:1->2, as:2->1, b:2->3, c:3->1; I=<a as, as a, b c>
Controls: BASE (one vertex, no arrows), DUAL (one vertex, loop x, x^2=0).
"""
from fractions import Fraction
import json, sys

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1117/output/artifacts/verification.json"
ZERO = Fraction(0)
ONE = Fraction(1)

def build_algebra(verts, arrows, rels):
    basis, index = [], {}
    def add(s, t, p):
        if (s, t, p) not in index:
            index[(s, t, p)] = len(basis)
            basis.append((s, t, p))
    for v in verts:
        add(v, v, ())
    front = [(v, v, ()) for v in verts]
    guard = 0
    while front and guard < 5000:
        guard += 1
        nxt = []
        for (s, t, p) in front:
            for an, (u, v) in arrows.items():
                if u != t:
                    continue
                q = p + (an,)
                if any(tuple(q[k:k + 2]) in rels for k in range(len(q) - 1)):
                    continue
                if (s, v, q) not in index:
                    add(s, v, q)
                    nxt.append((s, v, q))
        front = nxt
    return basis, index

def rref(A):
    A = [row[:] for row in A]
    m = len(A)
    n = len(A[0]) if m else 0
    piv = []
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        v = A[r][c]
        A[r] = [x / v for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    return A, piv

def ker_basis(M):
    m = len(M)
    n = len(M[0]) if m else 0
    R, piv = rref(M)
    prow = {c: k for k, c in enumerate(piv)}
    out = []
    for f in [c for c in range(n) if c not in piv]:
        v = [ZERO] * n
        v[f] = ONE
        for c in piv:
            v[c] = -R[prow[c]][f]
        out.append(v)
    return out

def mat_mul(A, B):
    if not A or not A[0] or not B or not B[0]:
        return []
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]

def cohomology_dims(verts, arrows, rels):
    basis, index = build_algebra(verts, arrows, rels)
    NB = len(basis)
    src = [s for (s, t, p) in basis]
    tgt = [t for (s, t, p) in basis]
    arr = [p for (s, t, p) in basis]
    plus = [i for i in range(NB) if arr[i]]
    def pmul(i, j):
        if tgt[i] != src[j]:
            return None
        q = arr[i] + arr[j]
        if any(tuple(q[k:k + 2]) in rels for k in range(len(q) - 1)):
            return None
        return index.get((src[i], tgt[j], q))
    def space(n):
        elts, lut = [], {}
        def rec(cur):
            if len(cur) == n:
                s, t = src[cur[0]], tgt[cur[-1]]
                for o in range(NB):
                    if src[o] == s and tgt[o] == t:
                        lut[(tuple(cur), o)] = len(elts)
                        elts.append((tuple(cur), o))
                return
            for p in plus:
                if cur and tgt[cur[-1]] != src[p]:
                    continue
                rec(cur + [p])
        rec([])
        return elts, lut
    C = {n: space(n) for n in (1, 2, 3)}
    Cn, Cl = {}, {}
    for n in (1, 2, 3):
        Cn[n], Cl[n] = C[n]
    def delta(n):
        rows, cols = len(Cn[n + 1]), len(Cn[n])
        M = [[ZERO] * cols for _ in range(rows)]
        for j, (xs, o) in enumerate(Cn[n]):
            xs = list(xs)
            for r, (ys, w) in enumerate(Cn[n + 1]):
                ys = list(ys)
                tot = ZERO
                # left: y1 f(y2..)
                if tuple(ys[1:]) == tuple(xs):
                    m = pmul(ys[0], o)
                    if m is not None and m == w:
                        tot += ONE
                # middle
                for i in range(1, n + 1):
                    m = pmul(ys[i - 1], ys[i])
                    if m is None:
                        continue
                    key = tuple(ys[:i - 1] + [m] + ys[i + 1:])
                    if key == tuple(xs) and o == w:
                        tot += ONE if i % 2 == 0 else Fraction(-1)
                # right
                if tuple(ys[:n]) == tuple(xs):
                    m = pmul(o, ys[n])
                    if m is not None and m == w:
                        tot += ONE if (n + 1) % 2 == 0 else Fraction(-1)
                M[r][j] = tot
        return M
    d1, d2 = delta(1), delta(2)
    if mat_mul(d2, d1):
        assert all(x == 0 for row in mat_mul(d2, d1) for x in row), "d^2 != 0"
    K2 = ker_basis(d2)
    rk1 = (len(d1[0]) - len(ker_basis(d1))) if (d1 and d1[0]) else 0
    rk2 = (len(d2[0]) - len(K2)) if (d2 and d2[0]) else 0
    # exactness witnesses: each K2 vec in col-span of d1?
    def in_col_span(Mcols_rows, v):
        # Mcols_rows: matrix rows x cols; solve M x = v via rref of [M | v]
        A = [row[:] + [val] for row, val in zip(Mcols_rows, v)]
        R, piv = rref(A)
        m = len(A)
        n = len(A[0]) - 1
        for i in range(m):
            if all(R[i][k] == 0 for k in range(n)) and R[i][n] != 0:
                return False, None
        x = [ZERO] * n
        for k, pc in enumerate(piv):
            if pc < n:
                x[pc] = R[k][n]
        return True, x
    wit = []
    allok = True
    for v in K2:
        ok, x = in_col_span(d1, v)
        allok = allok and ok
        wit.append(x)
    return {"dimA": NB, "dimC1": len(Cn[1]), "dimC2": len(Cn[2]),
            "dimC3": len(Cn[3]), "kerD2": len(K2), "rankD1": rk1,
            "HH2": len(K2) - rk1, "rankD2": rk2,
            "exact_witnesses": allok,
            "witnesses": [[str(c) for c in x] if x else None for x in wit],
            "ker2": [[str(c) for c in v] for v in K2]}

res = {}
# controls
res["BASE"] = cohomology_dims([1], {}, set())
res["DUAL"] = cohomology_dims([1], {"x": (1, 1)}, {("x", "x")})
# candidates
res["S0"] = cohomology_dims([1, 2, 3],
    {"a1": (1, 2), "a2": (1, 2), "b": (2, 3), "c": (3, 1)},
    {("a1", "b"), ("b", "c"), ("c", "a1")})
res["S1"] = cohomology_dims([1, 2, 3],
    {"a": (1, 2), "as": (2, 1), "b": (2, 3), "c": (3, 1)},
    {("a", "as"), ("b", "c")})
res["S2"] = cohomology_dims([1, 2, 3],
    {"a": (1, 2), "as": (2, 1), "b": (2, 3), "c": (3, 1)},
    {("as", "a"), ("c", "a")})
res["S3"] = cohomology_dims([1, 2, 3],
    {"a": (1, 2), "as": (2, 1), "b": (2, 3), "c": (3, 1)},
    {("a", "as"), ("as", "a"), ("b", "c")})

for k, v in res.items():
    print(k, {kk: vv for kk, vv in v.items() if kk not in ("witnesses", "ker2")})

# mod-p independent check for S0 and S1 (different arithmetic, rank only)
P = 1000003
def rank_mod(verts, arrows, rels, n):
    basis, index = build_algebra(verts, arrows, rels)
    NB = len(basis)
    src = [s for (s, t, p) in basis]
    tgt = [t for (s, t, p) in basis]
    arr = [p for (s, t, p) in basis]
    plus = [i for i in range(NB) if arr[i]]
    def pmul(i, j):
        if tgt[i] != src[j]:
            return None
        q = arr[i] + arr[j]
        if any(tuple(q[k:k + 2]) in rels for k in range(len(q) - 1)):
            return None
        return index.get((src[i], tgt[j], q))
    def space(n):
        elts = []
        def rec(cur):
            if len(cur) == n:
                s, t = src[cur[0]], tgt[cur[-1]]
                for o in range(NB):
                    if src[o] == s and tgt[o] == t:
                        elts.append((tuple(cur), o))
                return
            for p in plus:
                if cur and tgt[cur[-1]] != src[p]:
                    continue
                rec(cur + [p])
        rec([])
        return elts
    def dmat(n):
        D, Cn = space(n + 1), space(n)
        lut = {key: j for j, key in enumerate(Cn)}
        M = [[0] * len(Cn) for _ in range(len(D))]
        for j, (xs, o) in enumerate(Cn):
            for r, (ys, w) in enumerate(D):
                tot = 0
                if tuple(ys[1:]) == tuple(xs):
                    m = pmul(ys[0], o)
                    if m == w:
                        tot += 1
                for i in range(1, n + 1):
                    m = pmul(ys[i - 1], ys[i])
                    if m is None:
                        continue
                    if tuple(list(ys[:i - 1]) + [m] + list(ys[i + 1:])) == tuple(xs) and o == w:
                        tot += 1 if i % 2 == 0 else -1
                if tuple(ys[:n]) == tuple(xs):
                    m = pmul(o, ys[n])
                    if m == w:
                        tot += 1 if (n + 1) % 2 == 0 else -1
                M[r][j] = tot % P
        return M
    def rank(M):
        A = [row[:] for row in M]
        m = len(A)
        n = len(A[0]) if m else 0
        r = 0
        for c in range(n):
            p = next((i for i in range(r, m) if A[i][c] % P != 0), None)
            if p is None:
                continue
            A[r], A[p] = A[p], A[r]
            inv = pow(A[r][c] % P, P - 2, P)
            A[r] = [(x * inv) % P for x in A[r]]
            for i in range(m):
                if i != r and A[i][c] % P != 0:
                    f = A[i][c] % P
                    A[i] = [(a - f * b) % P for a, b in zip(A[i], A[r])]
            r += 1
        return r
    d1, d2 = dmat(1), dmat(2)
    r1, r2 = rank(d1), rank(d2)
    return {"modp_rank_d1": r1, "modp_rank_d2": r2,
            "modp_HH2": (len(d2[0]) - r2 - r1) if d2 else None,
            "dimC": (len(d1[0]), len(d1), len(d2))}
res["modp_S0"] = rank_mod([1, 2, 3],
    {"a1": (1, 2), "a2": (1, 2), "b": (2, 3), "c": (3, 1)},
    {("a1", "b"), ("b", "c"), ("c", "a1")}, 1)
res["modp_S1"] = rank_mod([1, 2, 3],
    {"a": (1, 2), "as": (2, 1), "b": (2, 3), "c": (3, 1)},
    {("a", "as"), ("b", "c")}, 1)
print(res["modp_S0"], res["modp_S1"])

with open(OUT, "w") as f:
    json.dump(res, f, indent=1)
print("wrote", OUT)
