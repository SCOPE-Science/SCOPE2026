#!/usr/bin/env python3
"""Exact coefficient and finite-grid checks for a three-frequency even-moment theorem."""
from fractions import Fraction
from math import comb, cos, sin, pi, isclose


def coeff_power(a, b, c, h):
    v = [1]
    for _ in range(h):
        w = [0] * (len(v) + 2)
        for i, val in enumerate(v):
            w[i] += a * val
            w[i + 1] += b * val
            w[i + 2] += c * val
        v = w
    return v


def poly_data(h):
    A = [Fraction(comb(2 * h, 2 * j) * comb(2 * j, j), 2**j)
         for j in range(h + 1)]
    Q = [(j + 1) * A[j + 1] - (h - j) * A[j] for j in range(h)]
    prescribed = [A[j] * (h - j) * Fraction(2 * h - 3 * j - 2, j + 1)
                  for j in range(h)]
    assert Q == prescribed
    nonzero = [1 if q > 0 else -1 for q in Q if q]
    assert nonzero[0] == 1 and nonzero[-1] == -1
    assert sum(nonzero[i] != nonzero[i-1] for i in range(1, len(nonzero))) == 1
    return A, Q


def evaluate(v, x):
    return sum(float(co) * x ** k for k, co in enumerate(v))


def maximize(h):
    A, Q = poly_data(h)
    l, r = 0., 4.
    for _ in range(100):
        m = (l+r)/2
        if evaluate(Q, m) > 0: l=m
        else: r=m
    x=(l+r)/2
    return x, evaluate(A, x)/(1+x)**h


def cyc_moment(a, b, c, h, N):
    return sum(abs(a+b*complex(cos(2*pi*j/N),sin(2*pi*j/N)) +
                   c*complex(cos(4*pi*j/N),sin(4*pi*j/N)))**(2*h)
               for j in range(N))/N


if __name__ == '__main__':
    checks=0
    for h in range(2,16):
        A,Q=poly_data(h)
        for b in (1,2,3,5):
            coeffs=coeff_power(1,b,1,h)
            exact=sum(k*k for k in coeffs)
            polynomial=sum(A[j] * 2**j * b**(2*h-2*j) for j in range(h+1))
            assert exact == polynomial, (h,b,exact,polynomial)
            checks +=1
        x,K=maximize(h)
        assert 0 < x < 2
        assert K>1
        checks+=2
        if h <= 8:
            b=1/(1+x)**.5
            a=(x/(2*(1+x)))**.5
            coeffs=coeff_power(a,b,a,h)
            M=sum(v*v for v in coeffs)
            assert abs(M-K)<1e-7*max(1,K)
            assert abs(cyc_moment(a,b,a,h,2*h+1)-K)<1e-7*max(1,K)
            assert cyc_moment(a,b,a,h,2*h)>K+1e-9
            checks+=3
    for h in (20,40,70):
        x,K=maximize(h)
        # Quantitative numerical diagnostic only; asymptotics follow from Laplace's method.
        assert abs(h*(2-x)-1.5)<.04
        checks+=1
    print(f'THREE_MODE_EVEN_MOMENTS_PASS exact_and_grid_checks={checks} h=2..15')
