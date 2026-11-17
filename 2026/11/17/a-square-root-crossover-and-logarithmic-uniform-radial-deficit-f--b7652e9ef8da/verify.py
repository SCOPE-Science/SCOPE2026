#!/usr/bin/env python3
"""Exact/independent checks for the harmonic-polytope radial-deficit theorem.
No network or external packages required.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial, comb, log


def shell_counts(n):
    # Integer evaluation of all shell multiplicities.
    return [factorial(n)//factorial(b)*sum(factorial(a+b)*factorial(n-1-a)
                    for a in range(n-b)) for b in range(n)]


def fine_triples(n):
    # Source fine-harmonic-triple criterion: no label is after k in both orders.
    for k in range(n):
        for p in permutations(range(n)):
            left = p.index(k)
            beforep = set(p[:left]); afterp = set(p[left+1:])
            for q in permutations(range(n)):
                right = q.index(k)
                afterq = set(q[right+1:])
                if afterp.isdisjoint(afterq):
                    b = len(beforep.intersection(q[:right]))
                    yield k,p,q,b


def exact_small_checks():
    cases=0
    for n in range(2,6):
        hist=[0]*n
        mu_num=n*(n+1)//2+1
        const=Fraction(n*(n*n-1),6)+Fraction(2*(n-1),n)
        for k,p,q,b in fine_triples(n):
            hist[b]+=1; cases+=1
            ix=[0]*n; iy=[0]*n
            for pos,label in enumerate(p): ix[label]=pos+1
            for pos,label in enumerate(q): iy[label]=pos+1
            ix[k]+=1; iy[k]+=1
            n2_r2=sum((n*v-mu_num)**2 for v in ix+iy)
            assert n2_r2==n*n*(const+2*b),(n,k,p,q,b,n2_r2)
        target=shell_counts(n)
        assert hist==target,(n,hist,target)
        H=sum(Fraction(1,i) for i in range(1,n+1))
        assert sum(hist)==factorial(n)**2*H
        # Reindex b -> d and evaluate exact ratio via factorials.
        for d in range(n):
            b=n-1-d
            lhs=Fraction(target[b],factorial(n)**2)
            rhs=sum((Fraction(factorial(n-1-d+a)*factorial(n-1-a),
                                  factorial(n-1-d)*factorial(n-1))
                     for a in range(d+1)),Fraction(0))/n
            assert lhs==rhs,(n,d,lhs,rhs)
    return cases


def weight_profile(n):
    # R_a=R_{d-a}; sum only to halfway, avoiding instability for large n.
    ws=[]
    for d in range(n):
        b=n-1-d
        total= 1.0 + (1.0 if d>0 else 0.0) # endpoints R_0,R_d
        r=1.0
        for a in range(1, d//2+1):
            r *= (b+a)/(n-a)
            total += (1.0 if 2*a==d else 2.0)*r
        ws.append(total/n)
    return ws


def numeric_checks():
    for n in (100, 400, 1200):
        w=weight_profile(n)
        H=sum(1/i for i in range(1,n+1))
        assert abs(sum(w)-H)<5.e-10, (n, sum(w),H)
        assert abs(w[0]-1/n)<1.e-14
        for d in range(1,n):
            assert w[d]>0
            assert w[d] <= (d+1)/n + 1e-11
            assert w[d] <= 2/n+4/d+1e-11
        # The logarithmic law has slow convergence; check robust qualitative approach.
        mean=sum(a*log(max(d,1))/log(n) for d,a in enumerate(w))/H
        assert 0.68<mean<0.78,(n,mean)
    return 3

if __name__=='__main__':
    a=exact_small_checks()
    b=numeric_checks()
    print(f'HARMONIC_RADIAL_LOG_PASS exact_triples={a} numerical_profiles={b} exact_shells=14')
