#!/usr/bin/env python3
"""Independent literal 4x4 multiplication check of commuting-pair count."""
from itertools import product
from collections import Counter

def matrix(t):
    a,b,c,d,e,f=t
    return ((1,a,d,f),(0,1,b,e),(0,0,1,c),(0,0,0,1))

def commute(A,B,q):
    # Directly compare all nine upper-triangular entries of A*B and B*A.
    for i in range(4):
        for j in range(i,4):
            left=sum(A[i][k]*B[k][j] for k in range(i,j+1))%q
            right=sum(B[i][k]*A[k][j] for k in range(i,j+1))%q
            if left != right: return False
    return True

for q in (2,3):
    group=[matrix(t) for t in product(range(q),repeat=6)]
    c=Counter()
    for A in group:
        cent=sum(commute(A,B,q) for B in group)
        c[cent]+=1
    total=sum(n*f for n,f in c.items())
    expected=q**7*(2*q*q+q-2)
    assert total==expected,(q,total,expected)
    assert sum(f*s//q**6 for s,f in c.items())==total//q**6
    print(f'q={q}: group={q**6}, centralizers={dict(sorted(c.items()))}, ordered_commuting={total}, conjugacy_classes={total//q**6}: PASS')
print('ALL_LITERAL_MATRIX_CROSSCHECKS_PASS')
