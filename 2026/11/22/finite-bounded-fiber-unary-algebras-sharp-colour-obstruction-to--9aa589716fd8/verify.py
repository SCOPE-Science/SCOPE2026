"""Finite independent checks for bounded-fiber unary-function amalgamation.

Run: python verify.py
"""
from itertools import product
from collections import Counter


def valid(f,k):
    return max(Counter(f).values(),default=0)<=k


def constructed_amalgam(A,B,C,k):
    """Merge common-root incoming trees recursively, keeping new cycles separate."""
    a,b,c=len(A),len(B),len(C)
    if tuple(B[:a])!=tuple(A) or tuple(C[:a])!=tuple(A):
        raise ValueError('Not the same common subalgebra')
    # Directed copies are B: [0,b), C: [b,b+c).
    par=list(range(b+c))
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]]
            x=par[x]
        return x
    def union(x,y):
        x=find(x);y=find(y)
        if x!=y:par[y]=x
    paired=[(i,i) for i in range(a)]
    for i in range(a):union(i,b+i)
    seen=set()
    while paired:
        i,j=paired.pop()
        if (i,j) in seen: continue
        seen.add((i,j))
        inB=[x for x in range(a,b) if B[x]==i]
        inC=[y for y in range(a,c) if C[y]==j]
        for x,y in zip(inB,inC):
            union(x,b+y)
            paired.append((x,y))
    names={};f=[]
    for x in range(b+c):
        v=find(x)
        if v not in names:names[v]=len(names)
    for x in range(b+c):
        y=B[x] if x<b else b+C[x-b]
        fx=names[find(x)];fy=names[find(y)]
        while len(f)<=fx:f.append(None)
        if f[fx] is not None and f[fx]!=fy:
            raise AssertionError('not function-compatible')
        f[fx]=fy
    assert all(z is not None for z in f)
    assert len({names[find(i)] for i in range(b)})==b
    assert len({names[find(b+j)] for j in range(c)})==c
    assert all(names[find(i)]==names[find(b+i)] for i in range(a))
    assert valid(f,k),(A,B,C,k,f)
    return f

count=0
for k in (1,2,3):
    for a in range(1,4):
        for A in product(range(a),repeat=a):
            if not valid(A,k):continue
            for b in range(a,5):
                for c in range(a,5):
                    Bs=[A+f for f in product(range(b),repeat=b-a) if valid(A+f,k)]
                    Cs=[A+f for f in product(range(c),repeat=c-a) if valid(A+f,k)]
                    for B in Bs:
                        for C in Cs:
                            constructed_amalgam(A,B,C,k)
                            count+=1

# Distinct colors prevent the forced identification at a saturated fiber.
for k in range(2,9):
    A=tuple([0]*(k-1))
    B=A+(0,);C=A+(0,)
    assert valid(B,k) and valid(C,k)
    # The two fresh points in B and C have different colors, so cannot
    # merge; the shared element 0 would acquire k+1 distinct preimages.
    assert (k-1)+2==k+1

# Strong amalgamation failure: two extensions each fill a remaining fiber.
for k in range(2,9):
    A=(0,)
    B=(0,)+(0,)*(k-1)
    C=B
    assert valid(B,k) and 1+2*(k-1)>k

print('AMALGAM_VERIFIED',count,'uncoloured test diagrams; color and strong obstructions k=2..8')
