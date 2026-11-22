"""Reproduce algebraic and numeric checks for a two-memory three-pulse model.

The analytic proof is in RESULT.md; sampled tests are NOT infinite certification.
Standard Python 3 library only.
"""
from __future__ import annotations
import math
import random
from fractions import Fraction


def risk(t, T, a, b, alpha, beta):
    def kernel(x):
        return a * math.exp(-alpha * x) - b * math.exp(-beta * x)
    return kernel(t) + kernel(T-t) + kernel(T)


def edge_minus_middle(T, a, b, alpha, beta):
    return a * (-math.expm1(-alpha*T/2))**2 - b * (-math.expm1(-beta*T/2))**2


def assert_close(x, y, *, rel=2e-11):
    if not math.isclose(x, y, rel_tol=rel, abs_tol=rel):
        raise AssertionError((x, y))


def main():
    count = 0
    # Rational attenuation factors: alpha=1, beta=2, a=1, b=1/2.
    for numerator in range(1, 100):
        q = Fraction(numerator, 101)
        # exp(-T/2)=q, so exp(-T)=q^2 and exp(-2T)=q^4.
        middle = 2*(q - Fraction(1,2)*q*q) + (q*q-Fraction(1,2)*q**4)
        edge = (Fraction(1,2)) + (q*q-Fraction(1,2)*q**4) + (q*q-Fraction(1,2)*q**4)
        diff = (1-q)**2-Fraction(1,2)*(1-q*q)**2
        assert edge-middle == diff
        count += 1
    Tloc = 2*math.log(2)
    Tcrit = 2*math.log(1+math.sqrt(2))
    assert Tloc < Tcrit
    assert_close(1/(1+math.exp(-Tcrit/2)), 1/math.sqrt(2))
    count += 2
    for T in (0.3, 1.0, Tloc, 1.6, Tcrit, 2.4, 5.0):
        d = edge_minus_middle(T, 1, 0.5, 1, 2)
        assert_close(d, risk(0,T,1,0.5,1,2)-risk(T/2,T,1,0.5,1,2))
        count += 1
        if T > Tloc+1e-6:
            u = math.acosh(math.exp(T/2)/2)
            assert 0<u<T/2
            barrier=risk(T/2+u,T,1,0.5,1,2)
            assert barrier>max(risk(0,T,1,0.5,1,2),risk(T/2,T,1,0.5,1,2))
            count += 2
    rng=random.Random(441642)
    for i in range(1800):
        alpha=10**rng.uniform(-1,0.6)
        beta=alpha*rng.uniform(1.02,6)
        a=10**rng.uniform(-1,0.8)
        b=a*10**rng.uniform(-2,0.9)
        T=10**rng.uniform(-1.5,1.4)
        q=edge_minus_middle(T,a,b,alpha,beta)
        e=risk(0,T,a,b,alpha,beta)
        m=risk(T/2,T,a,b,alpha,beta)
        assert_close(e-m,q,rel=3e-10)
        count+=1
        # The computed global candidate is never beaten by the 181-point sample.
        best=min(e,m)
        for j in range(1,181):
            z=risk(T*j/181,T,a,b,alpha,beta)
            assert z>=best-2e-10*(1+abs(best))
            count+=1
        # Proof's one-sign-change derivative criterion: H(u) strictly increasing.
        us=[T*k/24 for k in range(1,12)]
        # compare logarithmic H to prevent overflow
        def log_sinh(v):
            return v-math.log(2)+math.log(-math.expm1(-2*v))
        hh=[log_sinh(beta*u)-log_sinh(alpha*u) for u in us]
        assert all(x<y+5e-13 for x,y in zip(hh,hh[1:]))
        count+=1
    # Phase boundary of the normalized slope-balanced example.
    for T, expect in [(1.0,-1),(1.6,-1),(2.4,+1),(4.0,+1)]:
        diff=edge_minus_middle(T,1,.5,1,2)
        assert diff*expect>0
        count+=1
    print(f"PASS: {count} supplementary assertions; universal claim requires the symbolic proof.")

if __name__=='__main__':
    main()
