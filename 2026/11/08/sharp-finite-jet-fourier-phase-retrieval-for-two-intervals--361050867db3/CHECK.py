"""Exact-rational checks of finite-jet two-interval intensity identities.

This is a reproducibility check, not a substitute for the analytic proof.
"""
from fractions import Fraction as F
from math import comb, isqrt, sin, cos, sqrt
import cmath


def moments(intervals, k):
    return [sum((v**(j+1)-u**(j+1))/F(j+1) for u,v in intervals)
            for j in range(k+1)]


def coeff_by_double_integral(intervals, k):
    m = moments(intervals,k)
    total = sum(F((-1)**j*comb(k,j))*m[k-j]*m[j] for j in range(k+1))
    factorial=1
    for j in range(2,k+1): factorial*=j
    return F((-1)**(k//2))*total/factorial


def formulas(a,b,g):
    s=a+b
    r=a*b
    q=r*g*(g+s)
    c2=-s**4/12-q
    c4=s**6/360+q*s*s/12+q*q/(12*r)-q*r/12
    return s,r,q,c2,c4


def sqrt_rational(z):
    assert z>=0
    p, q=isqrt(z.numerator),isqrt(z.denominator)
    assert p*p==z.numerator and q*q==z.denominator
    return F(p,q)


def inverse(s,c2,c4):
    q=-c2-s**4/12
    y=12*c4-s**6/30-q*s*s
    r=(sqrt_rational(y*y+4*q**3)-y)/(2*q)
    lens=frozenset(((s+sqrt_rational(s*s-4*r))/2,
                     (s-sqrt_rational(s*s-4*r))/2))
    d=sqrt_rational(s*s/4+q/r)
    return r,d-s/2,lens


def ft(a,b,g,t):
    start=a+g
    if t==0: return complex(a+b)
    return ((1-cmath.exp(-1j*t*a)) +
            (cmath.exp(-1j*t*start)-cmath.exp(-1j*t*(start+b))))/(1j*t)


def checks():
    total=0
    for A in range(1,7):
      for B in range(1,7):
       for G in range(1,7):
        a,b,g=F(A,3),F(B,4),F(G,5)
        intervals=[(F(0),a),(a+g,a+g+b)]
        s,r,q,c2,c4=formulas(a,b,g)
        assert s*s==sum(v-u for u,v in intervals)**2
        assert c2==coeff_by_double_integral(intervals,2)
        assert c4==coeff_by_double_integral(intervals,4)
        rr,gg,lens=inverse(s,c2,c4)
        assert rr==r and gg==g and lens==frozenset((a,b))
        bound=s**6/360+q*s*s/16+q*q/(3*s*s)
        assert c4>=bound and (c4==bound)==(a==b)
        total+=6
    # One explicit non-injectivity fiber with identical order-two data.
    s,q=F(3),F(4)
    for r in (F(1),F(2)):
      d=sqrt(float(s*s/4+q/r))
      assert d>float(s)/2
      assert -s**4/12-q==F(-s**4,12)-q
      total+=2
    # Independent direct Fourier-transform intensity versus sinc/cos representation.
    for a,b,g in ((0.8,1.7,0.45),(2.0,0.6,2.4),(1.2,1.2,0.3)):
      d=g+(a+b)/2
      for t in (0.1,0.21,0.47,1.1,2.7):
        fn=lambda u: sin(u)/u if u else 1
        intensity=a*a*fn(a*t/2)**2+b*b*fn(b*t/2)**2+2*a*b*fn(a*t/2)*fn(b*t/2)*cos(d*t)
        assert abs(abs(ft(a,b,g,t))**2-intensity)<5e-12
        total+=1
    print('FINITE_JET_INTENSITY_CHECKS_PASSED',total)


if __name__=='__main__':
    checks()
