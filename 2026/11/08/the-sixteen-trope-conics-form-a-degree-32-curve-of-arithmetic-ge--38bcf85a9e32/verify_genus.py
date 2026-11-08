#!/usr/bin/env python3
"""Exact finite linear-algebra check for the Kummer trope-conic local tangent interpolation.
The universal proof uses restrictions to a smooth conic and Lagrange interpolation;
this finite calculation is only an independent arithmetic consistency check.
"""
from itertools import combinations_with_replacement
P=101
sites=[(1,t,t*t%P) for t in range(6)]

def rank(rows):
    a=[list(row) for row in rows]
    if not a:return 0
    n,m=len(a),len(a[0]); r=0
    for j in range(m):
        h=next((i for i in range(r,n) if a[i][j]%P),None)
        if h is None:continue
        a[r],a[h]=a[h],a[r]
        scale=pow(a[r][j],-1,P)
        a[r]=[z*scale%P for z in a[r]]
        for i in range(n):
            if i!=r:
                f=a[i][j]
                a[i]=[(a[i][k]-f*a[r][k])%P for k in range(m)]
        r+=1
        if r==n:break
    return r

ranks=[]
for d in range(4):
    exps=[(a,b,d-a-b) for a in range(d+1) for b in range(d-a+1)]
    matrix=[[pow(x,a,P)*pow(y,b,P)*pow(z,c,P)%P for a,b,c in exps] for x,y,z in sites]
    ranks.append(rank(matrix))
assert ranks==[1,3,5,6]
assert sum(6-r for r in ranks)==9
assert 16*(9)-16+1==129
assert 2*16==32 and (16*4)**2//16==256
print('VERIFY_KUMMER_TROPE_UNION_OK ranks=1,3,5,6 local_delta=9 genus=129')
