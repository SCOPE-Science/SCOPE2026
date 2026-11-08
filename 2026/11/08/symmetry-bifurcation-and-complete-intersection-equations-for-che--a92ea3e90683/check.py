"""Independent finite-state checks for Chebyshev--Lucas triple semigroups.

Run: python3 check.py. Standard library only.
This is a finite cross-check; proofs of all parameters are in RESULT.md.
"""
from math import gcd
from heapq import heappush, heappop

def lucas(u, top):
    p = [0, 1]
    for _ in range(2, top + 1):
        p.append(u * p[-1] - p[-2])
    return p

def apery_mod(a, b, c):
    dist = [None] * a
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        x, r = heappop(queue)
        if x != dist[r]:
            continue
        for w in (b, c):
            t = (r + w) % a
            z = x + w
            if dist[t] is None or z < dist[t]:
                dist[t] = z
                heappush(queue, (z, t))
    assert all(z is not None for z in dist)
    F = max(dist) - a
    G, rem = divmod(sum(dist) - a * (a - 1) // 2, a)
    assert rem == 0
    return F, G, dist

case_count = 0
sym_count = 0
for u in range(2, 8):
    p = lucas(u, 23)
    for n in range(4, 21, 2):
        a, b, c = p[n], p[n+2], p[n+3]
        if a > 100000:
            continue
        assert a < b < c
        assert gcd(gcd(a, b), c) == 1
        assert gcd(a, b) == u
        assert gcd(a, c) == (u*u-1 if n % 3 == 0 else 1)
        assert (u*u-1)*b == a + u*c
        F, G, ap = apery_mod(a, b, c)
        actual_sym = (2*G == F+1)
        predicted_sym = (n == 4 or n % 3 == 0)
        assert actual_sym == predicted_sym, (u,n,F,G)
        if predicted_sym:
            sym_count += 1
            if n == 4:
                A, B = a//u, b//u
                assert c == (B-1)*A + B
                expect_F = u*A*B-a-b+(u-1)*c
                assert F == expect_F,(u,n,F,expect_F)
                # Canonical Apéry residues modulo b for gluing.
                residue_set = {(i*a+j*c)%b for i in range(B) for j in range(u)}
                assert len(residue_set) == b, (u,n,'apery')
                if b <= 100000:
                    ap_b = apery_mod(b, a, c)[2]
                    assert sorted(i*a+j*c for i in range(B) for j in range(u)) == sorted(ap_b)
            else:
                d = u*u-1
                A, C = a//d, c//d
                assert b == A + u*C
                expect_F = a*C-a-c+(d-1)*b
                assert F == expect_F,(u,n,F,expect_F)
                if c <= 100000:
                    ap_c = apery_mod(c, a, b)[2]
                    assert sorted(i*a+j*b for i in range(C) for j in range(d)) == sorted(ap_c)
        case_count += 1
        print(f'PASS u={u} n={n} a={a} F={F} genus={G} symmetric={actual_sym}')
print(f'VERIFY_OK cases={case_count} symmetric_cases={sym_count}')
