#!/usr/bin/env python3
"""Exact finite-sample checks for the hypercube return-bridge coordinate-support law.
No external dependencies. All exact comparisons use Fraction, never floating point.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial, comb, cosh, exp, tanh, sqrt


def coefficient(d, m):
    """Coefficient [z^(2m)] (cosh z)^d as an exact rational."""
    a = [Fraction(0)] * (m+1)
    a[0] = Fraction(1)
    for _ in range(d):
        b = [Fraction(0)] * (m+1)
        for k in range(m+1):
            for j in range(m-k+1):
                b[k+j] += a[k]/factorial(2*j)
        a=b
    return a[m]


def predicted_counts(d,m):
    """Number of ordered length-2m flip words returning home with V untouched coordinates."""
    den = coefficient(d,m)
    counts = {}
    for v in range(d+1):
        # expand (cosh z - 1)^(d-v) by inclusion/exclusion
        numerator = sum(((-1)**(d-v-h))*comb(d-v,h)*coefficient(h,m) for h in range(d-v+1))
        val = Fraction(comb(d,v)*factorial(2*m))*numerator
        assert val.denominator==1
        counts[v]=val.numerator
    assert sum(counts.values()) == factorial(2*m)*den
    return counts


def enumerated_counts(d,m):
    res = Counter()
    for s in product(range(d),repeat=2*m):
        counts = Counter(s)
        if all(x%2==0 for x in counts.values()):
            res[d-len(counts)] += 1
    return res


def exact_moments(d,m):
    c=coefficient(d,m)
    mean=Fraction(d)*coefficient(d-1,m)/c
    factorial_second=Fraction(d*(d-1))*coefficient(d-2,m)/c if d>=2 else Fraction(0)
    return mean,factorial_second+mean-mean*mean


def root_for_mean(mu):
    lo,hi=0.0,max(2.0,mu+1)
    for _ in range(80):
        mid=(lo+hi)/2
        if mid*tanh(mid)<mu:lo=mid
        else:hi=mid
    return (lo+hi)/2


def limiting_values(mu):
    lam=root_for_mean(mu)
    p=1/cosh(lam)
    vy=mu+lam**2 / cosh(lam)**2
    variance=p*(1-p)-(p*mu)**2/vy
    assert variance>0 and p>exp(-mu)
    return lam,p,variance


def main():
    assertions=0
    for d in range(1,8):
        for m in range(1,9):
            counts=predicted_counts(d,m)
            assert sum(counts.values())>0; assertions+=1
            for v,z in counts.items():
                assert z>=0; assertions+=1
            mean,var=exact_moments(d,m)
            total=sum(counts.values())
            direct_mean=sum(Fraction(v*z,total) for v,z in counts.items())
            direct_var=sum(Fraction((v*v)*z,total) for v,z in counts.items())-direct_mean**2
            assert direct_mean==mean and direct_var==var; assertions+=2
            if d<=4 and 2*m<=8:
                brute=enumerated_counts(d,m)
                assert all(brute.get(v,0)==z for v,z in counts.items()); assertions+=1
    for mu in [0.05,.1,.25,.5,1.,2.,3.,5.,10.]:
        lam,p,v=limiting_values(mu)
        assert abs(lam*tanh(lam)-mu)<1.e-12; assertions+=1
        assert 0<v<p*(1-p); assertions+=1
    print('PASS exact assertions:',assertions)
    print('asymptotic constants for 2m/d = 2: lambda, empty fraction, sigma2 =',limiting_values(2.0))

if __name__=='__main__':main()
