#!/usr/bin/env python3
"""Independent exhaustive 4-element field verification (X^2+X+1)."""
from itertools import product
from collections import Counter
N=4

def add(a,b):return a^b

def times(a,b):
    x=0
    if b&1:x^=a
    if b&2:x^=(a<<1)
    if x&8:x^=0b1100 # alpha^3 = alpha+1
    if x&4:x^=0b111 # alpha^2 = alpha+1
    return x

def mul(a,b,L):
    # char two: u*v=u*w=v*w=w*w=u; v*v=u+L*v
    x=0
    for i,j in ((0,1),(1,0),(0,2),(2,0),(1,1),(1,2),(2,1),(2,2)):
        x^=times(a[i],b[j])
    return (x,times(L,times(a[1],b[1])),0)

def valid(c,L):
    basis=((1,0,0),(0,1,0),(0,0,1))
    for i in range(3):
        for j in range(i,3):
            p=mul(basis[i],basis[j],L)
            lhs=tuple(times(p[0],c[0][r])^times(p[1],c[1][r])^times(p[2],c[2][r]) for r in range(3))
            if lhs!=mul(c[i],c[j],L):return False
    return True

def rank(c):
    a=[[c[j][i] for j in range(3)] for i in range(3)]
    d=0
    for k in range(3):
        piv=next((i for i in range(d,3) if a[i][k]),None)
        if piv is None:continue
        a[d],a[piv]=a[piv],a[d]
        inverse=next(t for t in range(1,4) if times(a[d][k],t)==1)
        a[d]=[times(t,inverse) for t in a[d]]
        for i in range(3):
            if i!=d:
                f=a[i][k]
                a[i]=[a[i][j]^times(f,a[d][j]) for j in range(3)]
        d+=1
    return d

for lam in (1,2,3):
    counts=Counter()
    for x in product(range(4),repeat=9):
        c=(x[:3],x[3:6],x[6:9])
        if valid(c,lam):counts[rank(c)]+=1
    assert counts=={0:1,1:4,3:1},(lam,counts)
print('F4_EXHAUSTIVE_OK 3 parameters x 262144 matrices')
