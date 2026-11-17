#!/usr/bin/env python3
"""Independent GF(9) verification of the first arithmetic derivation stratum."""
from itertools import product
from collections import Counter

# GF(9)=GF(3)[a]/(a*a+1); encode c+d*a as c+3*d.
def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def neg(x):return (-x%3)+3*((-(x//3))%3)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    a,b=x%3,x//3;c,d=y%3,y//3
    return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
def inv(x):
    assert x
    for y in range(1,9):
        if mul(x,y)==1:return y
    raise AssertionError(x)
def rank(a):
    a=[row[:] for row in a];nr=len(a);nc=len(a[0]);r=0
    for c in range(nc):
        z=next((k for k in range(r,nr) if a[k][c]),None)
        if z is None:continue
        a[r],a[z]=a[z],a[r]
        scale=inv(a[r][c]);a[r]=[mul(scale,x) for x in a[r]]
        for j in range(nr):
            if j==r:continue
            t=a[j][c]
            if t:a[j]=[sub(x,mul(t,y)) for x,y in zip(a[j],a[r])]
        r+=1
        if r==nr:break
    return r

def derdim(M):
    n=2;eq=[]
    for i in range(n):
        for j in range(i,n):
            for v in range(n):
                row=[0]*4
                if i!=j:
                    row[2*j+i]=sub(row[2*j+i],M[j][v]);row[2*i+j]=sub(row[2*i+j],M[i][v])
                else:
                    for a in range(n):row[2*v+a]=add(row[2*v+a],M[i][a])
                    row[2*i+i]=sub(row[2*i+i],add(M[i][v],M[i][v]))
                eq.append(row)
    return 4-rank(eq)

d=Counter()
for a,b,c,e in product(range(9),repeat=4):
    M=[[a,b],[c,e]]
    if rank(M)==2:d[derdim(M)]+=1
assert d==Counter({0:5696,1:64}),d
print('PASS GF9 n2 dimension distribution',dict(d))
print('VERIFY_EXTENSION_OK')
