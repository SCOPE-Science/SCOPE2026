#!/usr/bin/env python3
"""Standalone supplemental checks of an exact Boolean two-shell Fourier-ratio theorem.

No outside dependencies.  Finite tests support the algebra; they do not prove the
universal theorem or the normal-limit argument.
"""
import cmath
import math
import random
from fractions import Fraction
from itertools import product


def krawtchouk2(d, k):
    return ((d - 2*k)**2 - d)//2


def discrete_formula(d):
    counts = [math.comb(d, k) for k in range(d+1)]
    out = []
    for j in range(d//2 + 1):
        u = Fraction((d-2*j)**2, d)
        mean = sum(Fraction(counts[k], 2**d) * abs(Fraction((d-2*k)**2,d)-u)
                   for k in range(d+1))
        den2 = (1-u)**2 + Fraction(2*(d-1),d)
        out.append((float(mean)/math.sqrt(float(den2)),j,u,mean,den2))
    return min(v[0] for v in out), [v for v in out if abs(v[0]-min(x[0] for x in out)) < 1e-13]


def fourier_ratio(d, a, b):
    # Direct Walsh transform of the signal; no use of Krawtchouk identity here.
    values = [a if x == 0 else b if x.bit_count() == 2 else 0 for x in range(2**d)]
    hat = [sum(values[x] * (-1 if (x & z).bit_count() & 1 else 1)
               for x in range(2**d)) / math.sqrt(2**d) for z in range(2**d)]
    energy = math.sqrt(sum(abs(t)**2 for t in hat))
    return sum(abs(t) for t in hat)/energy


def normal_phi(t):
    return math.exp(-t*t/2)/math.sqrt(2*math.pi)


def H(t):
    return 2*(1+math.erf(t/math.sqrt(2)))-3-2*t*(t*t-1)*normal_phi(t)


def normal_root():
    lo, hi = 0.0, 1.0
    assert H(lo)<0<H(hi)
    for _ in range(80):
        mid = (lo+hi)/2
        if H(mid) < 0: lo=mid
        else: hi=mid
    t=(lo+hi)/2
    C=2*t*normal_phi(t)*math.sqrt((1-t*t)**2+2)
    return t,C


def main():
    ntests=0
    for d in range(2,8):
        cd, minimizers=discrete_formula(d)
        for v,j,u,_,_ in minimizers:
            a=1-float(u)
            b=2/d
            assert abs(fourier_ratio(d,a,b)/(2**(d/2))-v)<2e-12
            ntests+=1
        rng=random.Random(92116+d)
        for _ in range(80):
            a=complex(rng.uniform(-5,5),rng.uniform(-5,5))
            b=complex(rng.uniform(-5,5),rng.uniform(-5,5))
            ratio=fourier_ratio(d,a,b)/math.sqrt(2**d)
            assert ratio >= cd-5e-12
            ntests+=1
        assert (len({krawtchouk2(d,k) for k in range(d+1)})==d//2+1)
        ntests+=1
    for d in [10,20,40,80,160,320]:
        val,_=discrete_formula(d)
        assert 0.48 < val < 0.65
        ntests+=1
    t,c=normal_root()
    assert .479<t<.481 and .549 <c<.55
    assert abs(H(t))<2e-14
    assert H(math.sqrt(3))>0
    assert abs((2*t*normal_phi(t)*math.sqrt((1-t*t)**2+2))-c)<1e-14
    ntests+=4
    print('PASS',ntests,'supplementary cases; unique normal root t=',format(t,'.15f'),
          'limit c=',format(c,'.15f'))
    for d in [2,3,4,5,8,20,80,320]:
        cd, minimizers=discrete_formula(d)
        print('d=',d,'c_d=',format(cd,'.14f'),'minimizer j=',[j for _,j,_,_,_ in minimizers])

if __name__=='__main__': main()
