#!/usr/bin/env python3
"""Exact-rational finite checks for the sharp power-pullback coefficient criterion.
No finite test substitutes for the all-order proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb


def convolution(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def data(m,p):
    # Coefficients of ((w+p)^m-p^m)/w.
    first=[Q(comb(m,k+1))*p**(m-k-1) for k in range(m)]
    # Coefficients of ((p+1)^m-(w+p)^m)/(1-w).
    second=[sum(Q(comb(m,j))*p**(m-j) for j in range(k+1,m+1)) for k in range(m)]
    unscaled=convolution([p*p,2*p,Q(1)],convolution(first,second))
    scale=unscaled[0]
    assert scale==m*p**(m+1)*((p+1)**m-p**m)
    return [u/scale for u in unscaled],first,second


def sign(q): return (q>0)-(q<0)


checks=0
for m in range(2,19):
    for numer,denom in [(1,4),(1,2),(1,1),(2,1),(3,1),(4,1),(7,2),(5,1),(2*m,1),(3*m,1),(10*m,1)]:
        p=Q(numer,denom)
        coeffs,A1,A2=data(m,p)
        assert len(coeffs)==2*m+1 and coeffs[0]==1
        checks+=2
        for seq in (A1,A2,coeffs):
            assert all(c>0 for c in seq)
            for i in range(1,len(seq)-1):
                assert seq[i]*seq[i]>seq[i-1]*seq[i+1], (m,p,i,'strict logconcavity')
                checks+=1
        d1=1+Q(m+3,2)/p-Q(m)*p**(m-1)/((p+1)**m-p**m)
        assert coeffs[1]==d1
        checks+=1
        sign_threshold=sign(Q(3*(m+1),m+3)-(1+1/p)**m)
        assert sign(1-d1)==sign_threshold
        checks+=1
        # At positive linear stiffness, every coefficient is positive.
        if sign_threshold>0:
            assert all(coeffs[i]>coeffs[i+1] for i in range(2*m))
            checks+=2*m
        else:
            assert coeffs[1]>coeffs[0]
            checks+=1
# Recover the author's m=2 threshold: p=(5+3sqrt(5))/4,
# equivalent to (p+1)^2/p^2=9/5.
# Its defining polynomial is 4*p^2-10*p-5=0; positive root = (5+3sqrt(5))/4.
m=2
assert Q(3*(m+1),m+3)==Q(9,5)
checks+=1
print('VERIFY_OK exact_rational_checks='+str(checks)+' m_range=2..18 positive_p_samples=11')
