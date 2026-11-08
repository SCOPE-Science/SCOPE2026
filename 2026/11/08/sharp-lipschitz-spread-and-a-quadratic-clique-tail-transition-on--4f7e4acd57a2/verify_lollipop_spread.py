#!/usr/bin/env python3
"""Exact-rational independent tests for lollipop Lipschitz spread.

Run: python verify_lollipop_spread.py
No nonstandard dependencies. Finite tests are corroboration, not universal proof.
"""
from fractions import Fraction
from itertools import product


def var(vals):
    n=len(vals)
    return Fraction(sum(x*x for x in vals)*n-sum(vals)**2,n*n)

def formula(m,l):
    n=m+l
    a=l*(l+1)//2
    b=l*(l+1)*(2*l+1)//6
    nums=[n*(b+k)-(a-k)**2 for k in range(m)]
    M=max(nums)
    return Fraction(M,n*n),tuple(i for i,x in enumerate(nums) if x==M)

def direct(m,l):
    best=Fraction(-1)
    count=0
    # Every core simplex vertex occurs here (root=0); every tail cube
    # vertex has successive unit jumps. Both signs must be checked.
    for sign in (-1,1):
        for core in product((0,sign),repeat=m-1):
            for tail_steps in product((-1,1),repeat=l):
                path=[0]
                for step in tail_steps:
                    path.append(path[-1]+step)
                values=[0,*core,*path[1:]]
                v=var(values)
                if v>best:best=v;count=1
                elif v==best:count+=1
    return best,count

def check():
    exhaustive=0
    for m in range(2,10):
        for l in range(1,7):
            if m+l>14: continue
            d,c=direct(m,l)
            f,ks=formula(m,l)
            assert d==f,(m,l,d,f)
            assert c>=1
            exhaustive+=1
    print('INDEPENDENT_EXACT_ALL_POLYTOPE_VERTEX_ENUMERATION_OK',exhaustive)
    tests=0
    for l in range(1,41):
        for m in range(2,900):
            n=m+l
            c=Fraction(m+l*(l+2),2)
            ks=tuple(k for k in range(m) if abs(Fraction(k)-c)==min(abs(Fraction(j)-c) for j in (0,m-1))) if False else ()
            nearest=min(range(m),key=lambda k:abs(Fraction(k)-c))
            f,opt=formula(m,l)
            assert nearest in opt
            assert all(abs(Fraction(k)-c)==abs(Fraction(nearest)-c) for k in opt)
            assert (m<=l*(l+2)+3)==(m-1 in opt)
            assert (m>=l*(l+2)+4)==(m-1 not in opt)
            tests+=1
    print('EXACT_QUADRATIC_THRESHOLD_AND_ALL_INTEGER_OPTIMIZERS_OK',tests)
    for l in range(1,18):
        m=l*(l+2)+3
        f,opts=formula(m,l)
        assert opts==(m-2,m-1),(m,l,opts)
        ff,opts2=formula(m+1,l)
        assert m not in opts2
    print('EXACT_FIRST_COEXISTENCE_AND_STRICT_INTERIOR_TRANSITION_OK',17)
    print('ALL_LOLLIPOP_SPREAD_CHECKS_OK')

if __name__=='__main__':check()
