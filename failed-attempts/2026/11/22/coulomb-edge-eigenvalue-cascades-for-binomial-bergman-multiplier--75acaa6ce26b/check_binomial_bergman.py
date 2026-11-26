#!/usr/bin/env python3
"""Supplementary finite calculations for the binomial Bergman multiplier Gram spectrum.
Only standard-library Python. Finite-dimensional checks do not establish the infinite theorem.
"""
from fractions import Fraction
from math import factorial

def moment(n,alpha):
    assert isinstance(alpha,int) and alpha>=0
    w=Fraction(1)
    for j in range(1,alpha+2):
        w*=Fraction(j,n+j)
    return w

def form(m,alpha,c,r,J,L):
    # Monomial coefficient sequence: (-1)^j times a finite nonnegative tent.
    ys=[min(i+1,L-i) for i in range(L)]
    omega=[moment(r+(J+i)*m,alpha) for i in range(L)]
    omega_next=[moment(r+(J+i+1)*m,alpha) for i in range(L)]
    n2=sum((omega[i]*ys[i]*ys[i] for i in range(L)),Fraction(0))
    q=sum(((omega_next[i]+c*c*omega[i])*ys[i]*ys[i] for i in range(L)),Fraction(0))
    q-=2*c*sum((omega_next[i]*ys[i]*ys[i+1] for i in range(L-1)),Fraction(0))
    d=q-(1-c)**2*n2
    return d,n2

def run():
    tally=0
    for m in (2,3,5):
        for alpha in (0,1,2):
            for c in (Fraction(1,3),Fraction(1,2),Fraction(3,4)):
                for r in range(m):
                    d,n=form(m,alpha,c,r,400,220)
                    # Every case must be a strict spectral-edge trial vector.
                    assert n>0, (m,alpha,c,r)
                    assert d<0,(m,alpha,c,r, d/n)
                    tally+=1
    # Exact monomial case c=0; equality with diagonal spectral branch.
    for m in (2,3,5):
        for alpha in (0,1,2):
            for n in range(1,30):
                assert moment(n+m,alpha)<moment(n,alpha)
                tally+=1
    print('BERGMAN_BINOMIAL_EXACT_CHECK_OK',tally)
if __name__=='__main__':run()
