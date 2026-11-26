#!/usr/bin/env python3
"""Finite sanity checks for the trace-zero generating-plane theorem.

The proof in RESULT.md is uniform in q. This script checks the orbit counts
for prime fields F_3,F_5,F_7 and binary fields F_2,F_4,F_8.
It is a finite check only, not a proof for all finite fields.
"""
from collections import deque
from itertools import product


def field(q):
    if q in (2, 4, 8):
        m = {2: 1, 4: 2, 8: 3}[q]
        poly = {2: 0b11, 4: 0b111, 8: 0b1011}[q]
        def add(a, b): return a ^ b
        def mul(a, b):
            out = 0
            while b:
                if b & 1:
                    out ^= a
                b >>= 1
                a <<= 1
                if a & (1 << m):
                    a ^= poly
            return out
        def neg(a): return a
        def inv(a):
            if a == 0: raise ZeroDivisionError
            for b in range(1, q):
                if mul(a, b) == 1: return b
            raise AssertionError('no inverse')
        def tr(a):
            z, x = 0, a
            for _ in range(m):
                z ^= x
                x = mul(x, x)
            assert z in (0, 1)
            return z
        return add, mul, neg, inv, tr
    assert q in (3, 5, 7)
    def add(a, b): return (a + b) % q
    def mul(a, b): return (a * b) % q
    def neg(a): return (-a) % q
    def inv(a): return pow(a, -1, q)
    def tr(a): raise AssertionError('trace only used in characteristic two')
    return add, mul, neg, inv, tr


def matmul(A, B, add, mul):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            s = 0
            for k in range(2): s = add(s, mul(A[i][k], B[k][j]))
            C[i][j] = s
    return C


def odd_field_check(q):
    add, mul, neg, inv, _ = field(q)
    def sub(a, b): return add(a, neg(b))
    def canon(v):
        for x in v:
            if x:
                c = inv(x)
                return tuple(mul(c, y) for y in v)
        raise AssertionError('zero projective vector')
    lines = [ (1, b, c) for b in range(q) for c in range(q) ]
    lines += [ (0, 1, c) for c in range(q) ]
    lines += [ (0, 0, 1) ]
    lines = [canon(v) for v in lines]
    squares = {mul(x, x) for x in range(q)}
    def Q(v):
        a, b, c = v
        return add(mul(a, a), mul(b, c))
    classes = {0: set(), 1: set(), 2: set()}
    for v in lines:
        x = Q(v)
        classes[0 if x == 0 else (1 if x in squares else 2)].add(v)
    # All GL_2 matrices act by conjugation on the normal line.
    GL = []
    for a, b, c, d in product(range(q), repeat=4):
        det = sub(mul(a, d), mul(b, c))
        if det:
            GL.append(((a, b, c, d), inv(det)))
    def act(gdet, v):
        (u, v0, w, z), idet = gdet
        a, b, c = v
        N = [[a, b], [c, neg(a)]]
        G = [[u, v0], [w, z]]
        Gi = [[mul(idet, z), mul(idet, neg(v0))],
              [mul(idet, neg(w)), mul(idet, u)]]
        T = matmul(matmul(G, N, add, mul), Gi, add, mul)
        return canon((T[0][0], T[0][1], T[1][0]))
    seen = set()
    orbit_sizes = []
    for v in lines:
        if Q(v) == 0 or v in seen: continue
        orb = {v}
        todo = deque([v])
        while todo:
            x = todo.popleft()
            for g in GL:
                y = act(g, x)
                assert Q(y) != 0
                assert (y in classes[1]) == (x in classes[1])
                if y not in orb:
                    orb.add(y); todo.append(y)
        seen |= orb
        orbit_sizes.append(len(orb))
    expected = sorted([q * (q + 1) // 2, q * (q - 1) // 2])
    assert len(classes[1]) == q * (q + 1) // 2
    assert len(classes[2]) == q * (q - 1) // 2
    assert sorted(orbit_sizes) == expected, (q, orbit_sizes, expected)
    print(f'odd q={q}: generating_planes={len(classes[1])+len(classes[2])}, orbit_sizes={sorted(orbit_sizes)}')


def even_field_check(q):
    add, mul, _, inv, tr = field(q)
    def sq(a): return mul(a, a)
    def neighbors(pair):
        a, b = pair
        out = set()
        for t in range(1, q):
            out.add((mul(a, inv(t)), mul(t, b)))
        for s in range(q):
            out.add((a, add(add(b, s), mul(sq(s), a))))
            out.add((add(add(a, s), mul(sq(s), b)), b))
        return out
    def invariant(pair): return tr(mul(pair[0], pair[1]))
    all_pairs = set(product(range(q), repeat=2))
    seen = set(); orbit_sizes = []
    for pair in sorted(all_pairs):
        if pair in seen: continue
        orb = {pair}; todo = deque([pair])
        while todo:
            x = todo.popleft()
            for y in neighbors(x):
                assert invariant(y) == invariant(x)
                if y not in orb:
                    orb.add(y); todo.append(y)
        seen |= orb
        orbit_sizes.append(len(orb))
    expected = sorted([q * (q + 1) // 2, q * (q - 1) // 2])
    assert sorted(orbit_sizes) == expected, (q, orbit_sizes, expected)
    counts = {0: 0, 1: 0}
    for p in all_pairs: counts[invariant(p)] += 1
    assert counts[0] == q * (q + 1) // 2
    assert counts[1] == q * (q - 1) // 2
    print(f'even q={q}: generating_planes={q*q}, trace_class_counts={counts}, orbit_sizes={sorted(orbit_sizes)}')


if __name__ == '__main__':
    for q in (3, 5, 7): odd_field_check(q)
    for q in (2, 4, 8): even_field_check(q)
    print('VERIFY_OK')
