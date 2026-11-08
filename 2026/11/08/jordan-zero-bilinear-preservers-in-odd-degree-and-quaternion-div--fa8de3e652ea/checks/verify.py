#!/usr/bin/env python3
"""Exact arithmetic checks for the stated zero-Jordan theorem."""
from fractions import Fraction
from itertools import product

def rank(vectors, modulus=None):
    if not vectors: return 0
    a=[[(x%modulus if modulus else Fraction(x)) for x in v] for v in vectors]
    r=0; n=len(a);m=len(a[0])
    for c in range(m):
        pivot=next((i for i in range(r,n) if a[i][c]),None)
        if pivot is None:continue
        a[pivot],a[r]=a[r],a[pivot]
        factor=pow(int(a[r][c]),-1,modulus) if modulus else 1/a[r][c]
        a[r]=[(x*factor)%modulus if modulus else x*factor for x in a[r]]
        for i in range(r+1,n):
            factor=a[i][c]
            if factor: a[i]=[(a[i][j]-factor*a[r][j])%modulus if modulus else a[i][j]-factor*a[r][j] for j in range(m)]
        r+=1
        if r==n:break
    return r

def tensor(x,y):return [a*b for a in x for b in y]
def qmul(x,y):
    a,b,c,d=x;e,f,g,h=y
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def jordan(x,y):
    a=qmul(x,y);b=qmul(y,x)
    return tuple(a[i]+b[i] for i in range(4))
zero=(0,0,0,0);one=(1,0,0,0)
V=[(0,1,0,0),(0,0,1,0),(0,0,0,1)]
pairs=[(V[i],V[j]) for i in range(3) for j in range(3) if i!=j]
for j in (1,2):
    pairs.append((tuple(V[0][k]+V[j][k] for k in range(4)),tuple(V[0][k]-V[j][k] for k in range(4))))
assert len(pairs)==8 and all(jordan(x,y)==zero for x,y in pairs)
assert rank([tensor(x,y) for x,y in pairs])==8
E=[tuple(int(i==j) for i in range(4)) for j in range(4)]
assert rank([jordan(x,y) for x in E for y in E])==4
factor=[[jordan(x,y)[k] for x in E for y in E] for k in range(4)]
extra=[[x[0]*y[0] for x in E for y in E]]
for j in range(1,4):extra.append([x[0]*y[j]-y[0]*x[j] for x in E for y in E])
assert rank(factor+extra)==8
assert all(sum(a*b for a,b in zip(L,tensor(x,y)))==0 for L in extra for x,y in pairs)
print('QUATERNION_OK zero_span=8 jordan_rank=4 bilinear_space=8 obstruction_dim=4')
def mprod(x,y):
    return ((x[0]*y[0]+x[1]*y[2])%3,(x[0]*y[1]+x[1]*y[3])%3,(x[2]*y[0]+x[3]*y[2])%3,(x[2]*y[1]+x[3]*y[3])%3)
def mjor(x,y):
    a=mprod(x,y);b=mprod(y,x)
    return tuple((a[i]+b[i])%3 for i in range(4))
mats=list(product(range(3),repeat=4))
zeros=[tensor(x,y) for x in mats for y in mats if mjor(x,y)==zero]
assert rank([mjor(x,y) for x in E for y in E],3)==4
assert rank(zeros,3)==12
assert len(zeros)==417
print('SPLIT_OK field=F3 Jordan_zero_pairs=417 zero_span=12 obstruction_dim=0')
print('VERIFY_OK')
