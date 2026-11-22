#!/usr/bin/env python3
"""Exact checks for degree-normalized colonization fixation location on T_k.
Only standard Python libraries are required. Python 3.10+.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


def symbolic_last_far(k):
    assert isinstance(k,int) and k>=1
    a=Fraction(1,2)
    b=Fraction(1,k+1)
    L=lambda z:(a/(a+z))**3
    out=Fraction(0)
    for j in range(k+1):
        z=j*b
        if z==a:
            e=a*3/(2*a)*L(a) # E[a*T_f*exp(-a*T_f)]
        else:
            e=a/(a-z)*(L(z)-L(a))
        out+=(-1)**j*comb(k,j)*e
    return out


def markov_last_far(k):
    # State h=hub infected, j=k-short leaves infected, b=0..3 right-side path infected.
    # Infection rates follow independent rate-one vertex clocks and uniform neighbor draws.
    @lru_cache(None)
    def f(h,j,b):
        if b==3:
            return Fraction(0) # the far leaf has already been infected before completion
        if h and j==k:
            return Fraction(1) # the remaining right-chain infections culminate in the far leaf
        transitions=[]
        if not h:
            transitions.append((Fraction(1,2),f(1,0,b)))
        if b<3:
            transitions.append((Fraction(1,2),f(h,j,b+1)))
        if h and j<k:
            transitions.append((Fraction(k-j,k+1),f(1,j+1,b)))
        total=sum(x for x,_ in transitions)
        return sum(x*y for x,y in transitions)/total
    return f(0,0,0)


def main():
    for k in range(1,18):
        p=symbolic_last_far(k)
        q=markov_last_far(k)
        assert p==q,(k,p,q)
        assert 0<p<1
        if k==4:
            assert p==Fraction(40122073072,243729729243)
            near=(1-p)/4
            assert near==Fraction(203607656171,974918916972)
            assert near-p==Fraction(43119363883,974918916972)>0
            print('T_4 far:',p,'near each:',near,'near minus far:',near-p)
        # for k>=8 the elementary moment bound can be crude, and is not used as exact probability
    assert symbolic_last_far(4) < Fraction(1,5)
    for k in [10,20,30]:
        p=symbolic_last_far(k)
        bound=Fraction(factorial(k+2)*2**(k-1),(k+1)**k)
        assert p<=bound
    print('PASS: 17 independent exact Markov comparisons, rational witness, 3 moment-bound comparisons')

if __name__=='__main__':main()
