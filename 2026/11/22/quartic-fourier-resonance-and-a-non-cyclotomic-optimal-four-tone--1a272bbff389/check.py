#!/usr/bin/env python3
"""Independent integer Fourier-convolution and numerical spot checks.

The normalized eighth moment on the unit circle is
    integral |1+z+u*z**m+v*z**(m+1)|**8 dz/(2*pi*i*z).
No external packages are required.
"""
from collections import defaultdict
from fractions import Fraction
from math import pi, sin, cos, sqrt
import cmath
import random


def expand_power(m, power=4):
    # Dictionary (power_z,power_u,power_v) -> exact positive integer coefficient.
    coeff = {(0, 0, 0): 1}
    terms = ((0, 0, 0), (1, 0, 0), (m, 1, 0), (m + 1, 0, 1))
    for _ in range(power):
        out = defaultdict(int)
        for (k, a, b), c in coeff.items():
            for j, r, s in terms:
                out[(k + j, a + r, b + s)] += c
        coeff = out
    return coeff


def moment_laurent(m, power=4):
    coeff = expand_power(m, power)
    groups = defaultdict(list)
    for (k, a, b), c in coeff.items():
        groups[k].append((a, b, c))
    out = defaultdict(int)
    for group in groups.values():
        for a, b, c in group:
            for d, e, f in group:
                out[(a-d, b-e)] += c*f
    return {k:v for k,v in out.items() if v}


def eighth_laurent(m):
    return moment_laurent(m, 4)


def expected(m):
    out = {(0,0):2716, (1,-1):1056,(-1,1):1056,
           (2,-2):36,(-2,2):36}
    if m == 4:
        for j,c in [(1,4),(2,24),(3,24),(4,4)]:
            out[(j,1-j)]=c
            out[(-j,j-1)]=c
    return out


def evaluate_laurent(poly, u, v):
    return sum(c*u**a*v**b for (a,b),c in poly.items()).real


def moment_by_sampling(m, u, v, N=257):
    # N > degree(P**4), so the trapezoidal rule integrates exactly
    # in exact arithmetic; numeric error is solely rounding.
    total=0.
    for k in range(N):
        z=cmath.exp(2j*pi*k/N)
        P=1+z+u*z**m+v*z**(m+1)
        total+=abs(P)**8
    return total/N


def g(h):
    return 6*h*h*h-h*h+76*h-1


def min_polynomial(h):
    return 676+36*h**4-8*h**3+912*h*h-24*h


def find_rho():
    lo=0.
    hi=1/75
    assert g(lo)<0<g(hi)
    for _ in range(100):
        mid=(lo+hi)/2
        if g(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2


def minimizer():
    rho=find_rho()
    theta=2*__import__('math').acos(rho/2)
    w=cmath.exp(1j*theta)
    K=4*(1+1/w)*(1+5/w+1/w**2)
    u=-K.conjugate()/abs(K)
    v=u*w
    return rho,u,v


def main():
    for m in [4,5,6,7,9,12]:
        computed=eighth_laurent(m)
        want=expected(m)
        assert computed==want, (m,computed,want)
    assert moment_laurent(4, 2)==moment_laurent(5, 2)
    assert moment_laurent(4, 3)==moment_laurent(5, 3)
    assert moment_laurent(4, 4)!=moment_laurent(5, 4)
    print('PASS: six exact eighth-moment identities and the order-four alias threshold')
    assert g(Fraction(0))<0<g(Fraction(1,75))
    assert min_polynomial(Fraction(1,76))<676
    # g'(h)=18h**2-2h+76>0 for every real h, discriminant negative.
    # E_+(h) is increasing for 0<=h<=2.
    rho,u,v=minimizer()
    assert 0<rho<1/75
    target=min_polynomial(rho)
    assert 675.8420<target<675.8422
    assert abs(evaluate_laurent(eighth_laurent(4),u,v)-target)<1e-9
    assert abs(evaluate_laurent(eighth_laurent(4),1,1)-5012)<1e-10
    assert abs(evaluate_laurent(eighth_laurent(5),1,-1)-676)<1e-10
    assert abs(evaluate_laurent(eighth_laurent(5),1,1)-4900)<1e-10
    print('PASS: exact rational boundary and strict-improvement witnesses')
    rng=random.Random(72173)
    for m in [4,5,6,7,9,12]:
        for _ in range(30):
            u=cmath.exp(2j*pi*rng.random())
            v=cmath.exp(2j*pi*rng.random())
            M=evaluate_laurent(eighth_laurent(m),u,v)
            T=moment_by_sampling(m,u,v,N=257)
            assert abs(M-T)<3e-9, (m,M,T)
    print('PASS: 180 independent unit-circle quadrature checks')
    print('rho = %.16f; sharp minimum = %.16f; sharp maximum = 5012' % (rho,target))

if __name__=='__main__':
    main()
