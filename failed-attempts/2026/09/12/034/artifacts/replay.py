#!/usr/bin/env python3
"""Replay: exact-rational certificate that HH^2(A0)=HH^3(A0)=0 for fixed A0.

A0: vertices {1,2,3}; arrows a1,a2:1->2, b:2->3, c:3->1;
    I = <a1 b, b c, c a1>.  E-relative normalized bar complex over Q.
Checks: d^2=0; dim ker / rank; every 2-cocycle and 3-cocycle is a coboundary
(with explicit preimages, residuals verified); diagonal puncture-cycle
z=(a1,b)->a2b + (c,a1)->ca2 equals d(g), g(a1)=a2; DUAL control HH^2=1.
Prints VERIFY_OK on success.
"""
from fractions import Fraction
ZERO = Fraction(0)
ONE = Fraction(1)

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
    pr = {c: k for k, c in enumerate(piv)}
    out = []
    for f in [c for c in range(n) if c not in piv]:
        v = [ZERO] * n
        v[f] = ONE
        for c in piv:
            v[c] = -R[pr[c]][f]
        out.append(v)
    return out

def mat_mul(A, B):
    if not A or not A[0] or not B or not B[0]:
        return []
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]

def mat_vec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

def solve(M, v):
    A = [row[:] + [val] for row, val in zip(M, v)]
    R, piv = rref(A)
    m = len(A)
    n = len(A[0]) - 1
    for i in range(m):
        if all(R[i][k] == 0 for k in range(n)) and R[i][n] != 0:
            return None
    x = [ZERO] * n
    for k, pc in enumerate(piv):
        if pc < n:
            x[pc] = R[k][n]
    return x

def algebra(verts, arrows, rels):
    basis, index = [], {}
    def add(s, t, p):
        if (s, t, p) not in index:
            index[(s, t, p)] = len(basis)
            basis.append((s, t, p))
    for v in verts:
        add(v, v, ())
    front = [(v, v, ()) for v in verts]
    while front:
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

def complex_data(verts, arrows, rels, maxn=4):
    basis, index = algebra(verts, arrows, rels)
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
    C = {n: space(n) for n in range(1, maxn + 1)}
    def dmat(n):
        D, Cn = C[n + 1], C[n]
        M = [[ZERO] * len(Cn) for _ in range(len(D))]
        for j, (xs, o) in enumerate(Cn):
            for r, (ys, w) in enumerate(D):
                tot = ZERO
                if tuple(ys[1:]) == tuple(xs):
                    m = pmul(ys[0], o)
                    if m is not None and m == w:
                        tot += ONE
                for i in range(1, n + 1):
                    m = pmul(ys[i - 1], ys[i])
                    if m is None:
                        continue
                    if tuple(list(ys[:i - 1]) + [m] + list(ys[i + 1:])) == tuple(xs) and o == w:
                        tot += ONE if i % 2 == 0 else Fraction(-1)
                if tuple(ys[:n]) == tuple(xs):
                    m = pmul(o, ys[n])
                    if m is not None and m == w:
                        tot += ONE if (n + 1) % 2 == 0 else Fraction(-1)
                M[r][j] = tot
        return M
    return basis, C, dmat, pmul

def main():
    verts = [1, 2, 3]
    arrows = {"a1": (1, 2), "a2": (1, 2), "b": (2, 3), "c": (3, 1)}
    rels = {("a1", "b"), ("b", "c"), ("c", "a1")}
    basis, C, dmat, _ = complex_data(verts, arrows, rels)
    assert len(basis) == 10, len(basis)
    assert (len(C[1]), len(C[2]), len(C[3]), len(C[4])) == (10, 18, 46, 102)
    d1, d2, d3 = dmat(1), dmat(2), dmat(3)
    assert not mat_mul(d2, d1) or all(x == 0 for row in mat_mul(d2, d1) for x in row)
    assert not mat_mul(d3, d2) or all(x == 0 for row in mat_mul(d3, d2) for x in row)
    K2, K3 = ker_basis(d2), ker_basis(d3)
    assert len(K2) == 5, len(K2)
    assert len(K3) == 13, len(K3)
    r1 = len(d1[0]) - len(ker_basis(d1))
    r2 = len(d2[0]) - len(K2)
    r3 = len(d3[0]) - len(K3)
    assert r1 == 5 and r2 == 13, (r1, r2)
    assert len(K2) - r1 == 0, "HH^2 != 0"
    assert len(K3) - r2 == 0, "HH^3 != 0"
    for v in K2:
        x = solve(d1, v)
        assert x is not None, "2-cocycle not exact"
        assert all(a - b == 0 for a, b in zip(mat_vec(d1, x), v)), "bad 2-witness"
    for v in K3:
        x = solve(d2, v)
        assert x is not None, "3-cocycle not exact"
        assert all(a - b == 0 for a, b in zip(mat_vec(d2, x), v)), "bad 3-witness"
    # diagonal puncture-cycle: locate (a1,b)->a2b and (c,a1)->ca2
    names = [(("e%d" % s) if not p else "".join(p)) for (s, t, p) in basis]
    def find(xs_names, out_name):
        for j, (xs, o) in enumerate(C[2]):
            if tuple(names[p] for p in xs) == tuple(xs_names) and names[o] == out_name:
                return j
        raise AssertionError("cochain not found")
    ia = [i for i, b in enumerate(basis) if b[2] == ("a1",)][0]
    ib = [i for i, b in enumerate(basis) if b[2] == ("b",)][0]
    ic = [i for i, b in enumerate(basis) if b[2] == ("c",)][0]
    ia1 = [i for i, b in enumerate(basis) if b[2] == ("a1",)][0]
    ia2b = [i for i, b in enumerate(basis) if b[2] == ("a2", "b")][0]
    ica2 = [i for i, b in enumerate(basis) if b[2] == ("c", "a2")][0]
    j1 = find(("a1", "b"), "a2b")
    j2 = find(("c", "a1"), "ca2")
    z = [ZERO] * len(C[2])
    z[j1] = ONE
    z[j2] = ONE
    assert all(x == 0 for x in mat_vec(d2, z)), "diagonal not a cocycle"
    x = solve(d1, z)
    assert x is not None and all(a - b == 0 for a, b in zip(mat_vec(d1, x), z))
    # witness is g(a1)=a2
    nz = [(j, v) for j, v in enumerate(x) if v != 0]
    assert len(nz) == 1, nz
    (xs, o) = C[1][nz[0][0]]
    assert tuple(names[p] for p in xs) == ("a1",) and names[o] == "a2" and nz[0][1] == ONE
    # control: dual numbers have HH^2 = 1
    b2, C2d, dm2, _ = complex_data([1], {"x": (1, 1)}, {("x", "x")})
    e1, e2 = dm2(1), dm2(2)
    hh = len(ker_basis(e2)) - (len(e1[0]) - len(ker_basis(e1)))
    assert hh == 1, hh
    print("VERIFY_OK dimA=10 C=(10,18,46,102) HH2=0 HH3=0 diag=d(g:a1->a2) controlDUAL_HH2=1")

if __name__ == "__main__":
    main()
