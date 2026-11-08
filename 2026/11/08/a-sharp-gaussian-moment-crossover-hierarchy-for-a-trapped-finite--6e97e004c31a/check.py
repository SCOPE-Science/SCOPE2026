#!/usr/bin/env python3
"""Reproducible diagnostics for a finite-tumble harmonically trapped particle.

Analytic uniqueness and all-order asymptotics are proved in RESULT.md; this
finite checker verifies algebraic recurrences and representative numerical cases.
"""
import math
from fractions import Fraction


def stationary_even_moment(n, run_rate, tumble_rate):
    # Formula reconstructed from the stationary generator; n is even order/2.
    m = Fraction(1)
    for j in range(1, n + 1):
        m *= Fraction(2*j - 1, 2*j - 1 + run_rate)
        m *= Fraction(2*j - 2 + tumble_rate, 2*j - 2 + run_rate + tumble_rate)
    return m


def generator_moments(max_degree, run_rate, tumble_rate):
    # Three-state stationary generator, independent of the scalar product formula.
    R, T = run_rate, tumble_rate
    rp = rm = T / (2*(R+T))
    z = R / (R+T)
    out = [rp + rm + z]
    for j in range(1, max_degree + 1):
        zz = R*(rp-rm)/(j+R+T)
        rr = (j*rp + (T/2)*zz)/(j+R)
        ll = (-j*rm + (T/2)*zz)/(j+R)
        rp, rm, z = rr, ll, zz
        out.append(rp+rm+z)
    return out


def log_ratio(n, R, T):
    # log( E[X^(2n)] / [(2n-1)!! E[X^2]^n] ), stable for large n.
    L = math.lgamma
    moment = (L(n+0.5) + L((R+1)/2) - L(0.5)
              - L(n+(R+1)/2) + L(n+T/2) + L((R+T)/2)
              - L(T/2) - L(n+(R+T)/2))
    gaussian = (L(2*n+1) - n*math.log(2) - L(n+1)
                + n*(math.log(T)-math.log((R+1)*(R+T))))
    return moment - gaussian


def threshold(n, R):
    assert n >= 2
    lo, hi = 1e-15, 1.0
    while log_ratio(n,R,hi)>0:
        hi *= 2
    for _ in range(110):
        mid = (lo+hi)/2
        if log_ratio(n,R,mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def check():
    tests = 0
    for r,t in [(Fraction(1, 4),Fraction(1,3)), (Fraction(3, 2),Fraction(7, 4)),
                (Fraction(5),Fraction(2,5)), (Fraction(1, 10),Fraction(9,2))]:
        direct = generator_moments(24, r, t)
        for n in range(1,13):
            assert direct[2*n] == stationary_even_moment(n, r, t), (r,t,n)
            assert direct[2*n-1] == 0, (r,t,n)
            tests += 2
    for r in [0.1, 0.5, 1.0, 5.0, 25.0]:
        t2 = (math.sqrt(5*r*r+8*r+4) -r-2)/2
        assert abs(log_ratio(2,r,t2)) < 3e-11
        tests += 1
        for n in [2,3,5,10,50,100]:
            t=threshold(n,r)
            assert abs(log_ratio(n,r,t))<2e-10
            assert log_ratio(n,r,t*.9)>0
            assert log_ratio(n,r,t*1.1)<0
            tests+=3
    for r in [0.1, 1.0, 5.0]:
        c=math.e*r*(r+1)/2
        vals=[]
        for n in [100,1000,10000]:
            tn=threshold(n,r)
            vals.append(abs(n*tn/c-1))
            tests+=1
        assert vals[2]<vals[1]<vals[0]
        tests+=1
        # The logarithmic correction coefficient tends to (r+1).
        n=10000
        tn=threshold(n,r)
        coef=(c-n*tn)*n/(c*math.log(n))
        assert abs(coef-(r+1))< max(1.5,.3*(r+1)), (r,coef)
        tests+=1
    print(f'PASS {tests} finite diagnostic assertions')

if __name__ == '__main__':
    check()
