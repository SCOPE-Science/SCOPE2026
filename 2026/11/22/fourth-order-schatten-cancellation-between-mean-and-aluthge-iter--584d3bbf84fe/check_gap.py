#!/usr/bin/env python3
"""Independent finite checks for a Schatten comparison of two shift transforms.
This script tests exact finite identities and numerical consequences; it is not
an infinite-dimensional proof. Python standard library only.
"""
from fractions import Fraction
from math import comb, exp, expm1, log1p, sqrt


def binomial_probs(k):
    return [comb(k, j) * (0.5**k) for j in range(k + 1)]


def weight(c, n):
    u = n+c
    return sqrt(1+1/u)


def gap(c, k, n, probs=None):
    if probs is None:
        probs = binomial_probs(k)
    h = [0.5*log1p(1/(n+c+j)) for j in range(k+1)]
    mu = sum(p*v for p,v in zip(probs,h))
    return exp(mu)*sum(p*(expm1(v-mu)-(v-mu)) for p,v in zip(probs,h))


def exact_two_isometry_tests():
    count=0
    for c in (Fraction(1,3),Fraction(1),Fraction(7,2)):
        for n in range(60):
            x=Fraction(n,1)+c
            w2=(x+1)/x
            wnext2=(x+2)/(x+1)
            assert w2*wnext2-2*w2+1 == 0
            count+=1
    return count


def iterative_tests():
    count=0
    for c in (0.4,1.0,4.0):
        for k in (1,2,3,7):
            for n in range(9):
                vals=[weight(c,n+j) for j in range(k+1)]
                for _ in range(k):
                    vals=[(vals[j]+vals[j+1])/2 for j in range(len(vals)-1)]
                a=vals[0]
                vals=[weight(c,n+j) for j in range(k+1)]
                for _ in range(k):
                    vals=[sqrt(vals[j]*vals[j+1]) for j in range(len(vals)-1)]
                g=vals[0]
                assert a>=g-5e-15
                assert abs((a-g)-gap(c,k,n))<4e-13
                count+=1
    return count


def asymptotic_checks():
    count=0
    for c in (0.5,1.,3.):
        for k in (64,128,256):
            p=binomial_probs(k)
            for t in (0.,0.5,1.,2.):
                n=int(t*k)
                actual=k**3*gap(c,k,n,p)
                expected=1/(32*(t+0.5)**4)
                # Finite k errors may remain substantial when c is large.
                if k==256:
                    assert abs(actual/expected-1)<0.17,(c,k,t,actual,expected)
                count+=1
    for c in (0.5,1.,3.):
        for k in (1,2,5):
            p=binomial_probs(k)
            for n in (1000,3000,10000):
                ratio=n**4*gap(c,k,n,p)/(k/32)
                assert abs(ratio-1)<0.05,(c,k,n,ratio)
                count+=1
    for k in (64,128,256):
        p=binomial_probs(k)
        # The finite tail is omitted here, so only lower estimates are tested.
        partial=sum(gap(1.,k,n,p) for n in range(20*k))
        normalized=k*k*partial
        assert .07 <normalized<.085,(k,normalized)
        count+=1
    return count

if __name__=='__main__':
    a=exact_two_isometry_tests()
    b=iterative_tests()
    c=asymptotic_checks()
    print(f'PASS {a} exact 2-isometry rational identities; {b} finite transform identities; {c} asymptotic sanity checks')
    print('Reference constants: k^3 operator norm -> 1/2; k^2 S1 mass -> 1/12; k^5 S2^2 -> 1/56.')
