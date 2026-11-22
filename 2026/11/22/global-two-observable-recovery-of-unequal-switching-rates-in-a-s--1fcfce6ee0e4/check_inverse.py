#!/usr/bin/env python3
"""Reproduce finite exact moment checks and numerical inversion for a switching harmonic diffusion.

Requires only Python 3 standard library. The theorem's continuum uniqueness proof is analytic;
these computations test independent formulas and inversion algorithms, not the proof itself.
"""
from fractions import Fraction as F
from math import isclose


def mixture_moments(a, b, A, B):
    # a>b>0; r1=2*a*A, r2=2*b*B
    t, d = A + B, a - b
    den = b*t+d*A
    mean = A*(b*(t+1)+d*(A+1))/((t+1)*den)
    second = A*(A+1)*(b*(t+2)+d*(A+2))/((t+1)*(t+2)*den)
    return mean, second


def solve2(p, q, r, s, h, k):
    det = p*s-q*r
    assert det > 0
    return (h*s-q*k)/det, (p*k-r*h)/det


def generator_moments(a, b, D, A, B):
    r1, r2 = 2*a*A, 2*b*B
    p1, p2 = r2/(r1+r2), r1/(r1+r2)
    s1, s2 = solve2(2*a+r1, -r2, -r1, 2*b+r2, 2*D*p1, 2*D*p2)
    t1, t2 = solve2(4*a+r1, -r2, -r1, 4*b+r2, 4*D*s1, 4*D*s2)
    return s1+s2, t1+t2


def observed(a, b, D, A, B):
    m, e2 = mixture_moments(a, b, A, B)
    vmin, delta = D/a, D/b-D/a
    S = vmin+delta*m
    K = delta*delta*(e2-m*m)
    return S, K


def numeric_moments(a,b,t,z):
    A=t*z; B=t*(1-z)
    return mixture_moments(a,b,A,B)


def invert(a,b,D,S,K):
    vmin, delta = D/a, D/b-D/a
    m=(S-vmin)/delta
    k=K/(delta*delta)
    assert 0<m<1 and 0<k<m*(1-m)

    def at_t(t):
        low, high=0., 1.
        for _ in range(66):
            z=(low+high)/2
            mean, _ = numeric_moments(a,b,t,z)
            if mean < m: low=z
            else: high=z
        z=(low+high)/2
        mean, second=numeric_moments(a,b,t,z)
        return z, second-mean*mean

    low=0.; high=1.
    while at_t(high)[1]>k: high*=2
    for _ in range(72):
        t=(low+high)/2
        if at_t(t)[1]>k: low=t
        else: high=t
    t=(low+high)/2
    z,_=at_t(t)
    return 2*a*t*z, 2*b*t*(1-z)


def run():
    tests=0
    for a in (F(2),F(3),F(7,2),F(9)):
        for b in (F(1,3),F(1),F(3,2)):
            if a<=b: continue
            for D in (F(1,2),F(1),F(5,3)):
                for A in (F(1,3),F(1),F(7,4),F(3)):
                    for B in (F(1,4),F(2,3),F(2),F(11,3)):
                        m,e2=mixture_moments(a,b,A,B)
                        vmin,delta=D/a,D/b-D/a
                        S,K=observed(a,b,D,A,B)
                        genS,genV2=generator_moments(a,b,D,A,B)
                        assert S==genS
                        assert genV2==vmin*vmin+2*vmin*delta*m+delta*delta*e2
                        assert vmin<S<D/b
                        assert 0<K<(S-vmin)*(D/b-S)
                        tests+=4
    assert observed(F(2), F(1), F(1), F(1), F(3)) == (F(16,25),F(13,1250))
    tests+=1
    for a,b,D in ((2,1,1),(3.5,.6,2),(5,3,1.5)):
        for A in (.15,.5,1,3,9):
            for B in (.2,.7,2.5,6):
                S,K=observed(a,b,D,A,B)
                r1,r2=invert(a,b,D,S,K)
                assert isclose(r1,2*a*A, rel_tol=2e-9,abs_tol=1e-8),(a,b,D,A,B,r1)
                assert isclose(r2,2*b*B, rel_tol=2e-9,abs_tol=1e-8),(a,b,D,A,B,r2)
                tests+=2
    for a,b,m in ((2,1,.25),(3,.5,.5),(8,1,.75)):
        last=float('inf')
        for t in (.001,.005,.01,.05,.1,.5,1,3,8,30,100):
            # Fixed mean; increasing t tightens the common-variance distribution.
            lo,hi=0.,1.
            for _ in range(70):
                z=(lo+hi)/2
                mean,_=numeric_moments(a,b,t,z)
                if mean<m: lo=z
                else: hi=z
            mean,second=numeric_moments(a,b,t,(lo+hi)/2)
            variance=second-mean*mean
            assert 0<variance<last
            last=variance
            tests+=1
    print('PASS:',tests,'independent exact equalities, inequalities, inverse and monotonicity assertions')
    print('Exact asymmetric example a=2,b=1,D=1,r1=4,r2=6: S=16/25, K=13/1250')

if __name__=='__main__': run()
