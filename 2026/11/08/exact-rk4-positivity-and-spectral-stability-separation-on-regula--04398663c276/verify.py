#!/usr/bin/env python3
"""Exact rational replay for the RK4 graph-diffusion positivity theorem.

This checks symbolic polynomial identities and finite test cases. The universal
claims are established by the accompanying analytic proof, not by enumeration.
Uses only Python's standard library.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial


def padd(*polys):
    r = [Q(0)] * max(map(len, polys))
    for a in polys:
        for i, v in enumerate(a):
            r[i] += v
    return tuple(r)


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai * bj
    return tuple(out)


def pscale(a, t):
    return tuple(t * x for x in a)


def peval(a, x):
    v = Q(0)
    for c in reversed(a):
        v = v * x + c
    return v


def matmul(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def r4(p, q):
    n = len(p)
    ident = [[Q(i == j) for j in range(n)] for i in range(n)]
    x = [[p[i][j] - ident[i][j] for j in range(n)] for i in range(n)]
    power = ident
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for k in range(5):
        t = q**k / factorial(k)
        for i, j in product(range(n), repeat=2):
            out[i][j] += t * power[i][j]
        if k < 4:
            power = matmul(power, x)
    return out


def cycle(n, a, b):
    assert n >= 6 and n % 2 == 0
    p = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        j = (i+1) % n
        w = Q(a if i % 2 == 0 else b, a+b)
        p[i][j] = p[j][i] = w
    return p


def complete_bipartite(d):
    n = 2*d
    p = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(d):
        for j in range(d, n):
            p[i][j] = p[j][i] = Q(1,d)
    return p


def deleted_matching(d):
    # K_{d+1,d+1} with one perfect matching deleted: degree d.
    m = d+1
    p = [[Q(0) for _ in range(2*m)] for _ in range(2*m)]
    for i in range(m):
        for j in range(m):
            if i != j:
                p[i][m+j] = p[m+j][i] = Q(1,d)
    return p


def check_stochastic(p):
    assert all(sum(row) == 1 for row in p)
    assert all(x >= 0 for row in p for x in row)
    assert all(p[i][j] == p[j][i] for i, j in product(range(len(p)),repeat=2))


def nonnegative(a):
    return all(x >= 0 for row in a for x in row)


def main():
    checks = 0
    f = (Q(1), Q(-1), Q(1,2), Q(-1,6), Q(1,24))
    twof = tuple(f[k] * 2**k for k in range(5))
    assert padd((Q(1),), twof, pscale(f,-2)) == (Q(0),Q(0),Q(1),Q(-1),Q(7,12))
    assert padd((Q(1),), pscale(twof,-1)) == (Q(0),Q(2),Q(-2),Q(4,3),Q(-2,3))
    checks += 2
    # 24 f(x) = x^2(x-2)^2 + 8(x^2-3x+3).
    sos = padd(pmul((Q(0),Q(0),Q(1)),pmul((Q(-2),Q(1)),(Q(-2),Q(1)))),
                pscale((Q(3),Q(-3),Q(1)),Q(8)))
    assert sos == pscale(f,Q(24))
    checks += 1
    # Coefficients of P^j in f(q(I-P)).
    for q in (Q(0), Q(1,4), Q(1,2), Q(1)):
        c = []
        for j in range(5):
            c_j = sum((Q(comb(k,j),factorial(k)) * (-1)**(k-j) * q**k
                       for k in range(j,5)),Q(0))
            c.append(c_j)
        assert all(x >= 0 for x in c)
        assert sum(c) == 1
        assert c[3] == q**3*(1-q)/6
        checks += 3
    # Exact polynomial identity at q=1 and q=7/5 and a narrow rational bracket.
    c = (Q(-3),Q(3),Q(-2),Q(1))
    assert peval(c,Q(139264,100000)) < 0
    assert peval(c,Q(139265,100000)) > 0
    checks += 2
    for d in range(1,8):
        p = complete_bipartite(d)
        check_stochastic(p)
        for q, expected in ((Q(1),True),(Q(13,10),True),(Q(7,5),False)):
            out = r4(p,q)
            assert nonnegative(out) == expected
            assert all(sum(row) == 1 for row in out)
            if q > 0:
                # Every cross-part entry, including d=1, equals this quantity.
                cross = (1-peval(f,2*q))/(2*d)
                assert out[0][d] == cross
            checks += 3
    for n in (6,8,10,12):
        for a,b in ((1,1),(2,3),(3,7)):
            p=cycle(n,a,b)
            check_stochastic(p)
            pos = r4(p,Q(1))
            neg = r4(p,Q(6,5))
            assert nonnegative(pos)
            assert not nonnegative(neg)
            # Opposite vertices at distance exactly three have only odd walks.
            p3=matmul(matmul(p,p),p)
            i,j=0,3
            assert p[i][j] == 0 and matmul(p,p)[i][j] == 0
            assert matmul(p3,p)[i][j] == 0 and p3[i][j] > 0
            assert neg[i][j] == Q(6,5)**3*(1-Q(6,5))/6*p3[i][j]
            checks += 6
    for d in (2,3,4,5):
        p=deleted_matching(d)
        check_stochastic(p)
        assert nonnegative(r4(p,Q(1)))
        assert not nonnegative(r4(p,Q(11,10)))
        checks += 2
    print('VERIFY_OK: %d exact rational and polynomial checks' % checks)

if __name__ == '__main__':
    main()
