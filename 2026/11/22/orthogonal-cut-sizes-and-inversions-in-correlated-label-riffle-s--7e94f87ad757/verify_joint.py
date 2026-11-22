#!/usr/bin/env python3
"""Exact finite checks for cut/inversion identities in stationary binary Markov labels."""
from fractions import Fraction
from itertools import product

checks = 0
for n in range(2,10):
    for p in (Fraction(0),Fraction(1,3),Fraction(1,2),Fraction(3,4),Fraction(9,10)):
        q=(1-p)/2
        probabilities={}
        total=Fraction(0)
        moment_K=moment_I=moment_KI=Fraction(0)
        cond_p=[Fraction(0) for _ in range(n+1)]
        cond_i=[Fraction(0) for _ in range(n+1)]
        for x in product((0,1),repeat=n):
            changes=sum(x[i]!=x[i-1] for i in range(1,n))
            prob=Fraction(1,2)*q**changes*(1-q)**(n-1-changes)
            k=x.count(0)
            inv=sum(x[i]>x[j] for i in range(n) for j in range(i+1,n))
            z=[2*y-1 for y in x]
            W=sum(z)
            L=sum((n+1-2*(i+1))*z[i] for i in range(n))
            assert 8*inv==n*n+2*L-W*W
            checks+=1
            total+=prob
            moment_K+=prob*k
            moment_I+=prob*inv
            moment_KI+=prob*k*inv
            cond_p[k]+=prob
            cond_i[k]+=prob*inv
        assert total==1
        assert moment_K==Fraction(n,2)
        assert moment_KI==moment_K*moment_I
        checks+=3
        for k in range(n+1):
            assert 2*cond_i[k]==k*(n-k)*cond_p[k]
            checks+=1
        expected=Fraction(1,4)*sum((n-d)*(1-p**d) for d in range(1,n))
        assert moment_I==expected
        checks+=1
        assert 0<cond_p[0]<1 and moment_I>0
        checks+=1
print('PASS',checks,'exact rational assertions')
