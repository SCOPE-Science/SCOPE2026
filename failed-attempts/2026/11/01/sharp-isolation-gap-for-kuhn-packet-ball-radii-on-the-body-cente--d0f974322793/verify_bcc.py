"""Exact-rational checks of the stated BCC prefix-simplex radius gap.
Finite verification only; the global result is established by the proof.
Run: python verify_bcc.py
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product

Z = (F(0), F(0), F(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)

def det3(v):
    a,b,c=v
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def solve(A,b):
    n=len(b)
    A=[list(row)+[b[i]] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        if pivot is None: return None
        A[j],A[pivot]=A[pivot],A[j]
        f=A[j][j]
        A[j]=[x/f for x in A[j]]
        for i in range(n):
            if i!=j:
                f=A[i][j]
                if f: A[i]=[x-f*y for x,y in zip(A[i],A[j])]
    return tuple(A[i][-1] for i in range(n))

def circumcenter(subset):
    p=subset[0]; v=[sub(x,p) for x in subset[1:]]
    if not v: return p
    G=[[dot(x,y) for y in v] for x in v]
    lam=solve(G,[norm2(x)/2 for x in v])
    if lam is None: return None
    return add(p,tuple(sum(lam[j]*v[j][i] for j in range(len(v))) for i in range(3)))

def meb2(points):
    best=None
    for k in range(1,len(points)+1):
        for S in combinations(points,k):
            center=circumcenter(S)
            if center is None: continue
            r2=norm2(sub(center,S[0]))
            if all(norm2(sub(center,p))<=r2 for p in points):
                if best is None or r2<best: best=r2
    assert best is not None
    return best

def radius2(B):
    ans=F(0)
    for Q in permutations(B):
        points=[Z]
        for q in Q: points.append(add(points[-1],q))
        ans=max(ans,meb2(points))
    return ans

unit=[tuple(F(s) if i==j else F(0) for i in range(3)) for j in range(3) for s in (-1,1)]
short=sorted(unit+[tuple(F(s,2) for s in signs) for signs in product((-1,1),repeat=3)])
assert len(short)==14
counts={'independent':0,'isolated':0,'second_level':0}
second_example=((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(-1,2),F(-1,2),F(1,2)))
assert radius2(second_example)==F(1,2)
for B in combinations(short,3):
    if not det3(B): continue
    counts['independent']+=1
    d=radius2(B)
    sign_class=(all(all(abs(x)==F(1,2) for x in v) for v in B) and
                len(set((1 if v[0]*v[1]*v[2]>0 else -1) for v in B))==1)
    if sign_class:
        assert d==F(5,16),(B,d)
        counts['isolated']+=1
    else:
        assert d>=F(1,2),(B,d)
        if d==F(1,2): counts['second_level']+=1
assert counts['isolated']==8,counts
print('PASS exact BCC short-vector frames:',counts)
print('PASS first squared radius 5/16; next minimum squared radius 1/2 (attained)')
