#!/usr/bin/env python3
"""Independent finite checks for an anisotropic bounded-noise attractor.

All finite tests are auxiliary: the accompanying proof establishes infinite series,
regularity, and limits. Only Python's standard library is required.
"""
from fractions import Fraction as F
from math import atan, cos, sin, tan, log, isfinite


def radius(theta, a, b, eps=1.0, terms=250):
    q = b / a
    rho = b*b / a
    result = 0.0
    # Recurrence avoids loss from forming a**(2*n) in denominators.
    v, w = 1.0, 1.0
    for _ in range(terms):
        result += v / ((cos(theta)**2 + w * sin(theta)**2)**1.5)
        v *= rho
        w *= q*q
        if not isfinite(w):
            break
    return eps*result


def radius_safe(theta, a, b, eps=1.0, terms=250):
    # Equivalent ellipse-by-ellipse evaluation avoiding large powers.
    total = 0.0
    ax = by = 1.0
    c, s = cos(theta), sin(theta)
    for _ in range(terms):
        den = (ax*ax*c*c + by*by*s*s)**0.5
        if den == 0:
            break
        total += (ax*by)**2 / den**3
        ax *= a; by *= b
    return eps*total


def profile(s, q, rho, bound=250):
    res = 0.0
    for j in range(-bound, bound + 1):
        # Stable evaluation of rho^t / (1+q^(2t))^(3/2)
        t = j-s
        if t >= 0:
            res += (rho/q**3)**t / (1.0+q**(-2*t))**1.5
        else:
            res += rho**t / (1.0+q**(2*t))**1.5
    return res


def exact_identity_checks():
    checks=0
    for a,b in [(F(1,5),F(3,5)),(F(9,25),F(3,5)),(F(1,2),F(3,5))]:
        for n in range(8):
            A, B = a**(2*n),b**(2*n)
            for u,v in [(3,4),(5,12),(8,15),(0,1),(1,0)]:
                # All the pairs have u^2+v^2 equal to a square.
                k=(u*u+v*v)
                import math
                d=math.isqrt(k)
                assert d*d==k
                c,s=F(u,d),F(v,d)
                W=A*c*c+B*s*s
                W1=2*(B-A)*s*c
                W2=2*(B-A)*(c*c-s*s)
                assert W*W+W*W2/2-W1*W1/4 == A*B
                checks+=1
    return checks


def run():
    count=exact_identity_checks()
    # The flat and non-flat curvature regimes and the slow-axis formula.
    for a,b in [(0.5,0.6),(0.36,0.6),(0.25,0.6)]:
        rslow = radius_safe(3.141592653589793/2,a,b,terms=120)
        assert abs(rslow-1/(1-a*a/b))<1e-10
        for theta in [0.07, 0.2, 0.71, 1.0]:
            r1=radius(theta,a,b,terms=120)
            r2=radius_safe(theta,a,b,terms=120)
            assert abs(r1-r2) < 5e-9*max(1,r1,r2),(a,b,theta,r1,r2)
            count+=1
    # Finite-radius limit in the strong fast-axis contraction regime.
    a,b=0.5,0.6
    expected=1/(1-b*b/a)
    assert abs(radius_safe(0,a,b,terms=160)-expected)<1e-11
    for k in [20,30,40]:
        theta=atan((b/a)**(-k))
        assert abs(radius_safe(theta,a,b,terms=250)/expected-1)<0.02
        count+=1
    # Marginal logarithm: finite k has an O(1)/k correction.
    a,b=.36,.6
    q=b/a
    for k in [32,48,64]:
        theta=atan(q**(-k))
        ratio=radius_safe(theta,a,b,terms=250)/k
        assert abs(ratio-1)<0.04,(k,ratio)
        count+=1
    # Supercritical multiplicative limit profile (several distinct phases).
    a,b=.25,.6
    q=b/a; rho=b*b/a; sig=log(rho)/log(q)
    assert 0<sig<1
    for s in [0.0,0.2,0.47,0.91]:
        G=profile(s,q,rho)
        assert abs(G-profile(s+1,q,rho))<1e-10
        for k in [19,27,35]:
            theta=atan(q**(-(k+s)))
            norm=(1/radius_safe(theta,a,b,terms=210))/(tan(theta)**sig)
            expected=1/G
            assert abs(norm-expected)/expected < 0.002, (s,k,norm,expected)
            count+=1
    print('PASS: %d exact and numerical identities/limits; external dependencies: none' % count)
    return count


if __name__=='__main__':
    run()
