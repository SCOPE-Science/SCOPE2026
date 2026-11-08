#!/usr/bin/env python3
"""Exact polynomial and full-state Markov verification of the five-vertex seed-placement theorem.

Run with: python3 verify.py
No third-party dependencies are required.
"""
from fractions import Fraction

# Coefficients in descending order, including the two absorbing states.
N_DESC = {
    (0,0): [0],
    (0,1): [320,2120,4190,2000,350,20,0,0],
    (0,2): [400,2860,6700,5560,2140,340,0,0],
    (0,3): [432,3180,7980,8136,4854,1920,450,48],
    (1,0): [360,2535,5670,3975,900,60,0,0],
    (1,1): [480,3500,8405,7190,2525,380,20,0],
    (1,2): [480,3640,9580,10375,5710,1555,160,0],
    (1,3): [480,3660,9900,12000,8925,4290,1125,120],
    (2,0): [432,3210,8040,8046,4764,1980,480,48],
    (2,1): [480,3660,9620,10760,7340,3260,800,80],
    (2,2): [480,3660,9940,12550,10900,5770,1540,160],
    (2,3): [480,3660,9960,12900,12900,9960,3660,480],
}


def clean(a):
    while len(a)>1 and a[-1] == 0: a.pop()
    return a

def add(*polys):
    out=[0]*max(map(len,polys))
    for p in polys:
        for i,x in enumerate(p):out[i]+=x
    return clean(out)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return clean(c)

def scale(a,c): return clean([v*c for v in a])

def sub(a,b): return add(a,scale(b,-1))

def evalpoly(a,x):
    s=0
    for c in reversed(a):s=s*x+c
    return s

N={state:clean(list(reversed(coeffs))) for state,coeffs in N_DESC.items()}
Q=list(reversed([8,53,113,102,113,53,8]))
DEN=scale(mul([1,1],Q),60)
assert N[(0,0)] == [0] and N[(2,3)] == DEN
assert all(len(p)<=8 for p in N.values())
checks=0

# Complete polynomial verification of all backward equations, without sampling.
# Rates are written after multiplying by the two positive local normalization factors.
for i in range(3):
    for j in range(4):
        if (i,j) in ((0,0),(2,3)):continue
        db=[3-j,j]                  # 3-j + r*j
        da=[2-i,i]                  # 2-i + r*i
        p=N[(i,j)]
        x=add(scale(mul([0,1],sub(N[(i+1,j)],p)),(2-i)*j) if i<2 else [0],
              scale(sub(N[(i-1,j)],p),i*(3-j)) if i>0 else [0])
        y=add(scale(mul([0,1],sub(N[(i,j+1)],p)),(3-j)*i) if j<3 else [0],
              scale(sub(N[(i,j-1)],p),j*(2-i)) if j>0 else [0])
        assert add(mul(da,x),mul(db,y)) == [0], (i,j)
        checks+=1

H=list(reversed([48,290,365,-856,-2239,-1600,-460,-48]))
assert sub(N[(1,1)],N[(2,0)])==H
assert sub(N[(2,0)],N[(0,2)])==scale(list(reversed([16,175,670,1243,1312,820,240,24])),2)
assert sub(N[(1,1)],N[(0,2)])==scale(mul([0,1],list(reversed([16,128,341,326,77,8,4]))),5)
checks+=3
assert evalpoly(H,1)==-4500 and evalpoly(H,2)<0 and evalpoly(H,3)>0
checks+=1

# Independently reconstitute the full 2^5-configuration chain from individual node updates.
# Vertices 0,1 form one part; vertices 2,3,4 form the other.
def brute_fix(r):
    vertices=range(5)
    neighbors={v:tuple(range(2,5)) if v<2 else (0,1) for v in vertices}
    states=list(range(1,31));index={s:k for k,s in enumerate(states)}
    A=[[Fraction(0) for _ in states] for _ in states]
    b=[Fraction(0) for _ in states]
    for ix,s in enumerate(states):
        for v in vertices:
            nb=neighbors[v]
            total=sum(r if s&(1<<u) else 1 for u in nb)
            p=Fraction(0) + sum((r for u in nb if s&(1<<u)),Fraction(0)); p=p/total
            if not s&(1<<v) and p:
                z=s|(1<<v);A[ix][ix]+=p
                if z==31:b[ix]+=p
                else:A[ix][index[z]]-=p
            elif s&(1<<v) and p<1:
                z=s&~(1<<v);A[ix][ix]+=1-p
                if z:A[ix][index[z]]-=1-p
    # Fraction-valued Gauss-Jordan elimination
    n=len(states)
    for c in range(n):
        pivot=next(t for t in range(c,n) if A[t][c])
        A[c],A[pivot]=A[pivot],A[c]
        b[c],b[pivot]=b[pivot],b[c]
        k=A[c][c]
        for q in range(c,n): A[c][q]/=k
        b[c]/=k
        for t in range(n):
            if t==c or not A[t][c]:continue
            k=A[t][c]
            for q in range(c,n): A[t][q]-=k*A[c][q]
            b[t]-=k*b[c]
    return {s:b[index[s]] for s in states}

for r in (Fraction(1,5),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(5,2),Fraction(4),Fraction(9)):
    values=brute_fix(r)
    for s,f in values.items():
        ij=(sum(bool(s&(1<<v)) for v in (0,1)), sum(bool(s&(1<<v)) for v in (2,3,4)))
        expected=Fraction(evalpoly(N[ij],r),evalpoly(DEN,r))
        assert f==expected,(s,ij,r,f,expected)
        checks+=1
print(f'PASS: {checks} exact identities / full-state comparisons')
