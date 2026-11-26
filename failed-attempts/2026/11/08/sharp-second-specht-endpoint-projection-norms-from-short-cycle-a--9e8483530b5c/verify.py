#!/usr/bin/env python3
"""Exact independent finite checks for the two-subset Specht Fourier projector."""
from itertools import permutations
from math import factorial
from fractions import Fraction


def cycle_counts(p):
    n=len(p); seen=[False]*n; one=two=0
    for j in range(n):
        if seen[j]:continue
        k=j; r=0
        while not seen[k]:
            seen[k]=True; r+=1; k=p[k]
        if r==1:one+=1
        if r==2:two+=1
    return one,two


def admissible(m):
    # Independent recurrence: permutations whose cycle lengths are all >=3.
    vals=[0]*(m+1); vals[0]=1
    for j in range(1,m+1):
        vals[j]=sum(factorial(j-1)//factorial(j-k)*vals[j-k] for k in range(3,j+1))
    return vals[m]


def q_formula(m):
    return sum((Fraction((-1)**(a+b),factorial(a)*2**b*factorial(b))
                for b in range(m//2+1) for a in range(m-2*b+1)),Fraction(0))

for m in range(0,15):
    assert q_formula(m)==Fraction(admissible(m),factorial(m)),(m, q_formula(m))
print('EXACT_FORBIDDEN_CYCLE_EGF_CHECKS_PASSED 15')

for n in range(4,9):
    dim=n*(n-3)//2
    distribution={}
    total_abs=0;sum_chi=0;sum_chi_sq=0;negative=0
    for p in permutations(range(n)):
        f,t=cycle_counts(p)
        chi=f*(f-3)//2+t
        distribution[(f,t)]=distribution.get((f,t),0)+1
        total_abs+=abs(chi); sum_chi+=chi;sum_chi_sq+=chi**2
        negative+=chi<0
        assert (chi<0)==(f in (1,2) and t==0)
    assert sum_chi==0
    assert sum_chi_sq==factorial(n)
    expected_negative=n*admissible(n-1)+n*(n-1)//2*admissible(n-2)
    assert negative==expected_negative,(n,negative,expected_negative)
    assert total_abs==2*negative
    observed=Fraction(dim*total_abs,factorial(n))
    formula=n*(n-3)*(q_formula(n-1)+q_formula(n-2)/2)
    assert observed==formula,(n,observed,formula)
    # Standard constituent is known to be fixed points minus 1; two-subset total character.
    for (f,t), count in distribution.items():
        assert (f*(f-1)//2+t)== 1+(f-1)+(f*(f-3)//2+t)
    print('S_N_EXACT_CHARACTER_L1_AND_PROJECTION_NORM',n,str(observed),'negative_count',negative)
print('ALL_SECOND_SPECHT_PROJECTION_CHECKS_PASSED')
