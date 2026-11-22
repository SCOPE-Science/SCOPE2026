#!/usr/bin/env python3
"""Independent finite checks for the genus-conditioned embedding-dimension formulas."""
from itertools import combinations
from fractions import Fraction
from math import comb

def check_semigroup(m,c,A):
    F=2*m-c
    N=m-c-1
    cutoff=F+m+3
    S={0,m}|{m+i for i in A}|set(range(F+1,cutoff+1))
    assert m==min(S-{0}) and F not in S
    assert all(x+y in S for x in S for y in S if x+y<=cutoff)
    true_g=len(set(range(F+1))-S)
    irreducibles={x for x in S if x>0 and x<=F+m and not any(0<y<x and y in S and x-y in S for y in range(1,x))}
    B={0}|set(A)
    sums={a+b for a in B for b in B}
    predicted=c+len(A)+sum(j not in sums for j in range(1,N+2))
    assert true_g==2*m-c-1-len(A)
    assert len(irreducibles)==predicted,(m,c,A,irreducibles,predicted)
    return len(irreducibles)

def conditional_numerators(N,r):
    actual=0
    for subset in combinations(range(1,N+1),r):
        B={0,*subset}
        BB={a+b for a in B for b in B}
        actual+=sum(j not in BB for j in range(1,N+2))
    coefficient=0
    for j in range(1,N+2):
        t=(j-1)//2
        h=N-2*t-int(j%2==0)-int(j<=N)
        assert h>=0
        coefficient+=sum(comb(t,a)*2**a*comb(h,r-a) for a in range(max(0,r-h),min(t,r)+1))
    assert actual==coefficient,(N,r,actual,coefficient)
    return actual

tested_semigroups=0
for m in range(2,11):
    for c in range(1,m):
        N=m-c-1
        values=[]
        for r in range(N+1):
            for A in combinations(range(1,N+1),r):
                values.append(check_semigroup(m,c,A))
                tested_semigroups+=1
        expected=Fraction(sum(values),len(values))
        formula=Fraction(2*c+N,2)+3-2*Fraction(3,4)**(N//2)
        assert expected==formula,(m,c,expected,formula)

tested_conditionals=0
for N in range(13):
    for r in range(N+1):
        conditional_numerators(N,r)
        tested_conditionals+=1
print('VERIFY_OK: {} semigroups, {} finite hypergeometric conditions'.format(tested_semigroups,tested_conditionals))
