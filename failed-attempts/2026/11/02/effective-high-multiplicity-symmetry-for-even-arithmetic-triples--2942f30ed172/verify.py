#!/usr/bin/env python3
"""Exact finite certificate for denumerants and p-symmetry statements.
Run with Python 3; uses integers only, no external packages.
"""
from math import gcd

def count_coins(coins, upto):
    f = [0] * (upto + 1)
    f[0] = 1
    for coin in coins:
        assert coin > 0
        for n in range(coin, upto + 1):
            f[n] += f[n - coin]
    return f

def certificate(u, v):
    assert u >= 2 and v > u and gcd(u, v) == 1 and (u + v) % 2
    w = u + v
    M = u * v * w
    f = count_coins((u, v, w), 4 * M + 30)
    assert all(f[r + q * M] == f[r] + M * q * q // 2 + (r + w) * q
               for r in range(M) for q in range(4))
    delta = min(f[r+1] - f[r] for r in range(M))
    Q = max(0, 1 - delta)
    T0 = Q*M
    P = max(f[:T0], default=0)
    assert all(f[t+1] > f[t] for t in range(T0, 4*M))
    return f, M, delta, T0, P

def exact_example():
    u, v, w = 3, 4, 7
    f, M, delta, T0, P = certificate(u, v)
    assert (M, delta, T0, P) == (84, -1, 168, 180)
    # Check direct representations of A=(6,7,8) against parity splitting.
    L = 2 * len(f) - 1
    a = count_coins((6, 7, 8), L)
    for n in range(L+1):
        expected = f[n//2] if n % 2 == 0 else (f[(n-w)//2] if n >= w else 0)
        assert a[n] == expected, (n, a[n], expected)
    bad_shape = []
    bad_sym = []
    for p in range(P + 1):
        # No behavior above T0 needs checking once p >= P, by proved lifting.
        # For smaller p, all possible decreases occur before T0.
        E = next(t for t in range(T0+M+1) if f[t] > p)
        tail = all(f[t] <= p for t in range(E)) and all(f[t] > p for t in range(E, T0+M+1))
        if not tail:
            bad_shape.append(p)
        # Since f increases from T0, every p<=P has its largest gap before 2*(T0+M)+w.
        bound = 2*(T0+M)+w
        S = [a[n] > p for n in range(bound+1)]
        ell = next(n for n in range(bound+1) if S[n])
        g = max(n for n in range(bound+1) if not S[n])
        assert all(S[n] for n in range(g+1, bound+1))
        symmetric = all(S[x] != S[ell+g-x] for x in range(ell,g+1))
        if not symmetric:
            bad_sym.append(p)
        if p == 1:
            assert (ell,g) == (14,25) and not S[16] and not S[23]
        if p == 7:
            assert (ell,g) == (56,65)
            assert [n for n in range(ell,g+1) if S[n]] == [56,60,62,63,64]
    assert bad_shape == [0,1,7], bad_shape
    assert bad_sym == [1], bad_sym
    print('PASS: M=84, delta=-1, T0=168, P=180')
    print('PASS: exact formula on four periods; direct triple parity splitting')
    print('PASS: exhaustive p=0,...,180; excluded tail cases 0,1,7; nonsym only p=1')
    print('PASS: all p>=180 by analytic quasipolynomial shift and monotonicity')

if __name__ == '__main__':
    for u,v in ((2,3),(3,4),(3,8),(4,5),(4,7),(5,6)):
        f,M,delta,T0,P = certificate(u,v)
        print('sample',u,v,'M',M,'delta',delta,'T0',T0,'P',P)
    exact_example()
