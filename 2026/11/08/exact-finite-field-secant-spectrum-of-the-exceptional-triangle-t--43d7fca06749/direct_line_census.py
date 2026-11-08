#!/usr/bin/env python3
"""Independently enumerate every projective line in PG(3,q) for small fields."""
from collections import Counter
from itertools import combinations,product
from verify_toric_trisecants import Field

def census(p,poly):
    F=Field(p,poly);q=F.q;freq=Counter();count=0
    for i,j in combinations(range(4),2):
        free_a=[c for c in range(i+1,4) if c!=j]
        free_b=[c for c in range(j+1,4)]
        for seq in product(range(q),repeat=len(free_a)+len(free_b)):
            a=[0]*4;b=[0]*4;a[i]=1;b[j]=1
            for idx,c in enumerate(free_a):a[c]=seq[idx]
            for idx,c in enumerate(free_b):b[c]=seq[idx+len(free_a)]
            k=0
            for t in range(q):
                pt=tuple(F.add(a[z],F.mul(t,b[z])) for z in range(4))
                if pt[0] and F.mul(F.mul(pt[1],pt[2]),pt[3])==F.pow(pt[0],3):k+=1
            if b[0] and F.mul(F.mul(b[1],b[2]),b[3])==F.pow(b[0],3):k+=1
            assert k<=3,(q,a,b,k)
            freq[k]+=1;count+=1
    rho=sum(1 for t in range(q) if F.add(F.add(F.mul(t,t),t),1)==0)
    N=(q-1)**2;T=(q-2)*(q-5)+2*rho
    expect3=N*T//6
    expect2=N*(N-1-T)//2
    expect1=N*(q*q+q+1)-2*expect2-3*expect3
    G=(q*q+1)*(q*q+q+1)
    assert count==G,(q,count,G)
    expected={0:G-expect1-expect2-expect3,1:expect1,2:expect2,3:expect3}
    assert dict(freq)=={k:v for k,v in expected.items() if v},(q,freq,expected)
    print('DIRECT_PG3',q,[freq[k] for k in range(4)],'MATCHED')

for p,mod in [(3,[0,1]),(2,[1,1,1]),(5,[0,1]),(7,[0,1]),(2,[1,1,0,1]),(3,[1,0,1])]:
    census(p,mod)
print('DIRECT_LINES_PASS')
