#!/usr/bin/env python3
"""Exact rational and high-precision diagnostic checks for a two-gap firing law.
This is a finite diagnostic; the supplied proof establishes the infinite theorem.
"""
from fractions import Fraction as Q
from decimal import Decimal, getcontext
from math import gcd


def floor(x):
    return x.numerator // x.denominator


def mech(i, alpha, theta):
    return floor((i + 1) * alpha + theta) - floor(i * alpha + theta)


def test(alpha, theta, a, b, start=-250, end=750):
    assert Q(0) < alpha < Q(1,2) and a < b
    digits={i:mech(i, alpha, theta) for i in range(start-1,end+1)}
    assert all(digits[i]+digits[i+1] <= 1 for i in range(start-1,end))
    event={0:Q(0)}
    for i in range(1,end+1):
        event[i]=event[i-1]+(a if digits[i-1] else b)
    for i in range(-1,start-1,-1):
        event[i]=event[i+1]-(a if digits[i] else b)
    L=1-alpha; beta=alpha/L
    for c in (a/2,a,(a+b)/2,b):
        for i0 in (-140,-99,-54,-1,0,1,33,71):
            curr=i0
            seq=[]
            for n in range(100):
                j=curr+1
                while event[j] < event[curr]+c:
                    j+=1
                seq.append((curr,j))
                curr=j
            if c <= a:
                assert all(j==i+1 for i,j in seq)
            else:
                # The canonical phase is entered after at most one firing.
                for i,j in seq[1:]:
                    assert digits[i-1] == 0
                    assert (j==i+2 if digits[i] else j==i+1)
                i=seq[1][0]
                r=(i*alpha+theta) % 1
                eta=(r-alpha)/L
                assert Q(0) <= eta < 1
                for j,(old,new) in enumerate(seq[1:]):
                    w=floor((j+1)*beta+eta)-floor(j*beta+eta)
                    assert event[new]-event[old] == b+a*w
                N=len(seq)-1
                actual=event[seq[-1][1]]-event[i]
                assert abs(actual-N*(b+a*beta)) < a
    return True


def main():
    cases=0
    for q in (5,7,8,11,13,17,19,23,29,34):
        for p in range(1,q//2+1):
            if 2*p>=q or gcd(p,q)!=1: continue
            alpha=Q(p,q)
            for theta in (Q(0),Q(1,7),Q(5,13)):
                test(alpha,theta,Q(2),Q(3))
                cases+=1
    getcontext().prec=70
    golden=(Decimal(3)-Decimal(5).sqrt())/Decimal(2)
    alpha=Q(golden)
    test(alpha,Q(1,11),Q(2),Q(3))
    # Directly inspect the first twelve factor complexities of the induced word.
    L=1-alpha; beta=alpha/L; i=next(k for k in range(1,100) if mech(k-1,alpha,Q(1,11))==0)
    eta=(((i*alpha+Q(1,11))%1)-alpha)/L
    word=[floor((j+1)*beta+eta)-floor(j*beta+eta) for j in range(2500)]
    comp={n:len({tuple(word[j:j+n]) for j in range(len(word)-n+1)}) for n in range(1,13)}
    assert all(comp[n]==n+1 for n in comp), comp
    print('PASS rational parameter/phase trials:',cases)
    print('PASS high-precision golden-slope diagnostic: n=2500, factor complexities:',comp)
    print('PASS exact rational spike-time discrepancy, finite interval recurrence, and phase synchronization')

if __name__=='__main__':
    main()
