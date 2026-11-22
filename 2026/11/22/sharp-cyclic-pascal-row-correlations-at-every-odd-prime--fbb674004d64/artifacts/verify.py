#!/usr/bin/env python3
"""Exact rational and finite cyclic checks of odd-prime Pascal-row correlations."""
from fractions import Fraction
from functools import lru_cache


def coefficients(p, d):
    assert 0 <= d < p
    A = sum((x+1)*(x+d+1) for x in range(p-d))
    B = sum((x+1)*(x+d+1-p) for x in range(p-d, p))
    assert A == (p-d)*(p-d+1)*(2*p+d+1)//6
    assert B == d*(d+1)*(3*p-d+1)//6
    return A, B


def digit_product(n, p):
    z = 1
    while n:
        n, d = divmod(n,p)
        z *= d+1
    return z


def limit_function(p):
    S = sum((d+1)**2 for d in range(p))
    alpha = Fraction(2*(p+1), 2*p+5)
    @lru_cache(None)
    def c(h):
        if h == 0: return Fraction(1)
        q, d = divmod(h, p)
        if d == 0: return c(q)
        if h == 1: return alpha
        A, B = coefficients(p, d)
        return (A*c(q) + B*c(q+1))/S
    return c


def check():
    checks = 0
    for p in (3,5,7,11,13):
        S = sum((d+1)**2 for d in range(p))
        alpha = Fraction(2*(p+1),2*p+5)
        A1,B1 = coefficients(p,1)
        assert Fraction(A1, S-B1) == alpha; checks += 1
        assert S == p*(p+1)*(2*p+1)//6; checks += 1
        c = limit_function(p)
        for d in range(1,p):
            A,B = coefficients(p,d)
            assert S-A-B == d*p*(p-d)//2; checks += 1
            assert 6*(2*p+5)*(alpha*S-A-alpha*B) == 3*(p-d)*(d-1)*(d+2*p*p+3*p+1); checks += 1
        for h in range(1,1001):
            v = c(h)
            assert 0 < v <= alpha; checks += 1
            power = h
            while power % p == 0: power //= p
            assert (v == alpha) == (power == 1); checks += 1
        for r in range(1, 5):
            N = p**r
            if N > 3000: break
            values = [digit_product(n,p) for n in range(N)]
            assert sum(values) == (p*(p+1)//2)**r; checks += 1
            assert sum(v*v for v in values) == S**r; checks += 1
            for h in range(0,min(N,23)):
                H = sum(values[n]*values[(n+h)%N] for n in range(N))
                if h:
                    q,d = divmod(h,p)
                    A,B=coefficients(p,d)
                    lower=[digit_product(n,p) for n in range(N//p)]
                    H0=sum(lower[n]*lower[(n+q)%(N//p)] for n in range(N//p))
                    H1=sum(lower[n]*lower[(n+q+1)%(N//p)] for n in range(N//p))
                    assert H==A*H0+B*H1;checks += 1
                else:
                    assert H==S**r; checks+=1
                if h==1:
                    assert (H*alpha.denominator == alpha.numerator*S**r+(alpha.denominator-alpha.numerator)*p**r); checks += 1
    print('CHECK_OK', checks, 'exact assertions')

if __name__ == '__main__':
    check()
