#!/usr/bin/env python3
"""Finite diagnostic checks for a logarithmic Lorentz quasi-norm identity.
The analytic proof is in RESULT.md; these tests are not a certificate of infinity.
"""
from itertools import product
from math import log, isclose


def phi(k, m):
    return sum(1.0 + log(j)**k for j in range(1,m+1))


def balanced(k,n,S):
    m,r=divmod(S,n)
    return phi(k,S)/((n-r)*phi(k,m)+r*phi(k,m+1))


def q(k, seq):
    return sum((1+log(j)**k)*v for j,v in enumerate(sorted(map(abs,seq),reverse=True),1))


def run():
    count=0
    for k in (0.5,1.0,2.0,3.0):
        for n in range(2,6):
            for S in range(1,14):
                ratios=[]
                for counts in product(range(S+1),repeat=n):
                    if sum(counts)!=S:
                        continue
                    ratios.append(phi(k,S)/sum(phi(k,m) for m in counts))
                assert ratios and isclose(max(ratios),balanced(k,n,S),abs_tol=1e-10)
                count+=1
    k=2.0
    x=[1]*5+[0]*5
    y=[0]*5+[1]*5
    c=q(k,[a+b for a,b in zip(x,y)])/(q(k,x)+q(k,y))
    assert isclose(c,phi(k,10)/(2*phi(k,5)),abs_tol=1e-12)
    assert c>phi(k,2)/2
    count+=2
    print('PASS:',count,'finite diagnostic assertions')


if __name__ == '__main__':
    run()
