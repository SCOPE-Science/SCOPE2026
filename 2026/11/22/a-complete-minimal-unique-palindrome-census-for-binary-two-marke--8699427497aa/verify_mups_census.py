#!/usr/bin/env python3
"""Independent census of minimal unique palindromic factors using an
occurrence-index map, plus exact rational generating-function identities.
"""
from fractions import Fraction
from collections import defaultdict
from math import comb

def indexed_count(text):
    positions=defaultdict(list)
    n=len(text)
    for size in range(1,n+1):
        for i in range(n-size+1):
            p=text[i:i+size]
            if p==p[::-1]:positions[p].append((i,i+size))
    answer=[]
    for p,intervals in positions.items():
        if len(intervals)!=1:continue
        if len(p)<=2 or len(positions[p[1:-1]]) >= 2:
            answer.append((p,intervals[0]))
    return len(answer)

def expected(n):
    s=n-2
    total=comb(s-1,2)
    k1=(s-1)//2
    # Strictly increasing a<b<c: a>=1,b=a+u,c=b+v, u,v>=1
    k3=2*sum(1 for a in range(1,s+1)
             for u in range(1,s+1)
             if s-3*a-2*u >=1)
    return (k1, total-k1-k3, k3)

cases=0
for n in range(5,51):
    census=[0,0,0]
    s=n-2
    for a in range(1,s-1):
        for b in range(1,s-a):
            c=s-a-b
            k=indexed_count('0'*a+'1'+'0'*b+'1'+'0'*c)
            assert 1<=k<=3
            census[k-1]+=1
            cases+=1
    assert tuple(census)==expected(n),(n,census,expected(n))
    if n in (5,8,12,25,50):print('n',n,'(K=1,K=2,K=3)',census)
print('PASS independent occurrence-index census:',cases,'triples')
print('Exact ordinary generating functions in word length n:')
print('G1=z^5/((1-z)(1-z^2))')
print('G2=z^5/(1-z)^3-G1-G3')
print('G3=2*z^8/((1-z)(1-z^2)(1-z^3))')
print('Limiting probabilities: (0, 2/3, 1/3); limiting mean: 7/3')
