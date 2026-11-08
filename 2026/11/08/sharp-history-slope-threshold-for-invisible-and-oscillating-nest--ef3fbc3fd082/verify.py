#!/usr/bin/env python3
"""Exact rational checks for clipped-history nested-delay sign classification.
Run: python3 verify.py. All arithmetic is fractions.Fraction.
"""
from fractions import Fraction as Q


def clip(x, a):
    return max(-a, min(a, x))


def initial(s, m, a):
    assert -2 <= s <= 0
    return clip(m * (s + 1), a)


def sign(x):
    return (x > 0) - (x < 0)


def ref_g(t, a):
    assert t >= 0
    if t <= 1 + a:
        return a - t
    rem = (t - (1 + a)) % 4
    if rem <= 2:
        return -1 + rem
    return 3 - rem


def test_case(eta, a, m):
    assert Q(0) < eta < 1 and 0 < a < 1 and m > a
    q = eta * m
    delta = a / (4 * m * (1 + q))
    t = delta / 2
    assert 0 < t < delta
    assert initial(Q(0),m,a) == a
    assert initial(Q(-1),m,a) == 0
    assert initial(t-1,m,a) == m*t
    delay2 = 1 + eta * initial(t-1,m,a)
    r2 = initial(t-delay2, m, a)
    assert r2 == m * (1 - q) * t
    assert 0 < delay2 < 2
    h2 = a - sign(r2) * t
    assert h2 - ref_g(t,a) == (1-sign(1-q))*t
    implicit = 1 + q*t/(1+q)
    assert implicit == 1 + eta * initial(t-implicit,m,a)
    assert initial(t-implicit,m,a) > 0
    assert 0 < implicit < 2
    assert ref_g(t,a) == a-t
    if q <= 1:
        for j in range(1,26):
            delay = Q(1)
            for _ in range(1,j):
                delay = 1 + eta*initial(t-delay,m,a)
            predicted = 1 + (q*t/(1+q))*(1-(-q)**(j-1))
            assert delay == predicted, (q,j,delay,predicted)
            assert 0 < delay < 2
            if q == 1:
                assert delay == (Q(1) if j % 2 else 1+t)
                if j % 2 == 0:
                    assert initial(t-delay,m,a) == 0
                else:
                    assert initial(t-delay,m,a) > 0
            else:
                assert initial(t-delay,m,a)>0
    return q


if __name__ == '__main__':
    tested = 0
    regimes = set()
    etas = [Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(4,5)]
    for eta in etas:
        for a in [Q(1,10),Q(1,4),Q(2,5),Q(3,4)]:
            for m in [a + Q(1,10),Q(1),1/eta-Q(1,10),1/eta,1/eta+Q(1,10),Q(5),Q(10)]:
                if m <= a: continue
                q = test_case(eta,a,m)
                regimes.add(sign(q-1))
                tested += 1
    assert regimes == {-1,0,1}
    # Check the actual constant-delay DDE at thousands of non-switching rational times.
    for a in [Q(1,7),Q(1,4),Q(2,3)]:
        for k in range(1,2000):
            t = Q(k,67)
            eps = Q(1,10000)
            if abs(ref_g(t-1,a)) < Q(1,50) if t>=1 else False:
                continue
            g_tminus1 = (initial(t-1,Q(3),a) if t<1 else ref_g(t-1,a))
            if g_tminus1==0: continue
            derivative=(ref_g(t+eps,a)-ref_g(t-eps,a))/(2*eps)
            if t>eps and abs(g_tminus1)>Q(1,40):
                assert derivative == -sign(g_tminus1),(t,a,derivative,g_tminus1)
    print('PASS: ',tested,'exact rational parameter cases; all three regimes; 25 nesting orders;')
    print('        unique explicit implicit-root equation; reference equation and bounded triangle profiles.')
