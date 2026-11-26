#!/usr/bin/env python3
"""Reproduce analytic consistency checks for a two-absorber persistent particle.
Standard-library only; finite numerics and simulation supplement the paper proof.
"""
import math
import random


def root(c, n):
    # Positive Robin-Dirichlet characteristic root in ((n-1/2)pi,n pi).
    a = (n - .5) * math.pi + 1e-10
    b = n * math.pi - 1e-10
    def f(x):
        return x * math.cos(x) + c * math.sin(x)
    fa = f(a)
    assert fa * f(b) < 0, (c, n, a, b)
    for _ in range(58):
        m = (a + b) / 2
        if fa * f(m) > 0:
            a = m
            fa = f(m)
        else:
            b = m
    x = (a + b) / 2
    assert (n-.5)*math.pi < x < n*math.pi
    return x


def closed_pgf(c, q):
    u = math.sqrt(1-q)
    den = 1+c if u == 0 else math.cosh(c*u) + math.sinh(c*u)/u
    return (1+c)/den


def spectral_pgf(c, q, K=600):
    # Finite product: the omitted tail is O(c^2/K).
    s = 0.
    for n in range(1, K+1):
        r = root(c, n)/c
        s -= math.log1p((1-q)/(r*r))
    return math.exp(s)


def moments(c):
    m = c*c*(c+3)/(6*(c+1))
    v = c*c*(c**4+6*c**3+30*c**2+60*c+45)/(90*(c+1)**2)
    return m,v


def independent_simulation(c, trials=70000):
    rng = random.Random(20261113 + int(100*c))
    total = 0
    count = 0
    zeros = 0
    for _ in range(trials):
        x, direction, turns = 0., 1, 0
        for safety in range(1000000):
            xnew = x + direction*rng.expovariate(1.)
            if xnew >= c:
                assert turns%2 == 0
                count += 1
                total += turns//2
                zeros += (turns == 0)
                break
            if xnew <= 0:
                assert turns%2 == 1
                break
            x = xnew
            direction = -direction
            turns += 1
        else:
            raise RuntimeError('unexpectedly excessive reversals')
    return count/trials, total/count, zeros/count


def main():
    checks = 0
    for c in (.2, .5, 1., 2., 5., 10.):
        for q in (0., .1, .4, .7, 1.):
            true = closed_pgf(c, q)
            numerical = spectral_pgf(c, q)
            assert abs(numerical - true) < .0005, (c,q,numerical,true)
            checks += 1
        assert abs(closed_pgf(c, 0) -(1+c)*math.exp(-c))<1e-12
        assert abs(closed_pgf(c, 1)-1)<1e-12
        h=1e-4
        # One-sided difference, second order accurate, for E[M]=H'(1).
        fd=(3*closed_pgf(c,1)-4*closed_pgf(c,1-h)+closed_pgf(c,1-2*h))/(2*h)
        assert abs(fd-moments(c)[0])<max(.002, .00008*moments(c)[0]),(c,fd,moments(c)[0])
        checks+=3
    for c in (30.,100.,300.):
        for s in (.1, 1., 5.):
            observed=closed_pgf(c, math.exp(-s/c**2))
            expected=math.sqrt(s)/math.sinh(math.sqrt(s))
            assert abs(observed-expected)<.02, (c,s,observed,expected)
            checks+=1
    for c in (.5, 1., 3.):
        estimated_p, estimated_m, estimated_zero=independent_simulation(c)
        m,_=moments(c)
        assert abs(estimated_p-1/(1+c))<.013
        assert abs(estimated_m-m)<.09
        assert abs(estimated_zero-(1+c)*math.exp(-c))<.014
        checks+=3
    # The Poisson total intensity equals -log P(M=0).
    for c in (.1,.4,1.,3.,8.):
        assert abs(-math.log(closed_pgf(c,0))-(c-math.log1p(c))) < 1e-12
        checks+=1
    print('PASS:',checks,'independent finite checks; analytical theorem is in RESULT.md')


if __name__ == '__main__':
    main()
