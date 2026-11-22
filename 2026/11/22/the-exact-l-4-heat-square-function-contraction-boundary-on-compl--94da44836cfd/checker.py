#!/usr/bin/env python3
"""Exact rational tests for the bipartite heat square-function theorem."""
from fractions import Fraction as Q


def rho(k, N):
    return Q(4 * k * N, (k + N) ** 2)


def square4(x, a, r):
    # For real inputs x,a: 4G^2 = x^2+a^2+2rxa.
    return (x*x + a*a + 2*r*x*a) ** 2


def exact_deficit(m, n, u, v, a, b):
    assert len(u) == m and len(v) == n
    assert sum(u) == sum(v) == 0 and m*a + n*b == 0
    ra, rb = rho(n, m+n), rho(m, m+n)
    lhs = sum((x+a)**4 for x in u) + sum((y+b)**4 for y in v)
    rhs = sum(square4(x,a,ra) for x in u) + sum(square4(y,b,rb) for y in v)
    first = 4*(1-ra)*sum(x**3*a for x in u)
    first += 4*(1-ra*ra)*sum((x*a)**2 for x in u)
    second = 4*(1-rb)*sum(y**3*b for y in v)
    second += 4*(1-rb*rb)*sum((y*b)**2 for y in v)
    assert lhs-rhs == first+second
    return lhs-rhs


def witness(m,n):
    assert m>=3
    d=Q(1,4)
    u=[Q(2),Q(-1),Q(-1)]+[Q(0)]*(m-3)
    v=[Q(0)]*n
    a,b=-d,Q(m,n)*d
    ra=rho(n,m+n)
    D=exact_deficit(m,n,u,v,a,b)
    expected=24*(1-ra)*d*((1+ra)*d-1)
    assert D==expected==Q(-3,2)*(1-ra)*(3-ra)
    assert D<0


def complex_test(m,n):
    u=([complex(2,1),complex(-2,-1)] if m==2 else [0j])
    v=([complex(1,-2),complex(-1,2)] if n==2 else [0j])
    for a in [complex(1,2),complex(-2,1),complex(0,1),0j]:
        b=-m*a/n
        ra, rb = float(rho(n,m+n)),float(rho(m,m+n))
        D = 0.0
        identity = 0.0
        for vec,base,r in [(u,a,ra),(v,b,rb)]:
            for h in vec:
                z=(h*base.conjugate()).real
                D+=abs(h+base)**4-(abs(h)**2+abs(base)**2+2*r*z)**2
                identity+=4*(1-r)*abs(h)**2*z+4*(1-r*r)*z*z
        assert abs(D-identity) < 1e-8
        assert D > -1e-8


def main():
    count=0
    for m in range(1,21):
        for n in range(1,21):
            if m>=3:
                witness(m,n)
                count+=1
            elif n>=3:
                witness(n,m)
                count+=1
    for m in [1,2]:
        for n in [1,2]:
            complex_test(m,n)
    print('PASS: %s exact witness instances and 16 complex input comparisons' % count)


if __name__=='__main__':
    main()
