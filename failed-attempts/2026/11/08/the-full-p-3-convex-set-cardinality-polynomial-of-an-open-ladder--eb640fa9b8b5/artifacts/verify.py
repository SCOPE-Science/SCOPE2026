#!/usr/bin/env python3
"""Exact finite certificates for the P3-convex-set enumerator of open ladders.
Uses only the Python standard library; run `python3 artifacts/verify.py`.
"""
from collections import defaultdict
from itertools import product

def pop(x):return x.bit_count()
def swap(a):return ((a&1)<<1)|((a&2)>>1)
def okay(a,b,c):
    for r in (0,1):
        if not (b>>r)&1:
            count=((a>>r)&1)+((c>>r)&1)+((b>>(1-r))&1)
            if count>1:return False
    return True

states=list(product(range(4),repeat=2))
seen=set();orbits=[]
for s in states:
    if s not in seen:
        orbit=tuple(sorted({s,(swap(s[0]),swap(s[1]))}))
        orbits.append(orbit);seen.update(orbit)
assert len(orbits)==10

def B_at(z):
    b=[[0]*10 for _ in range(10)]
    for i,oi in enumerate(orbits):
        a,c=oi[0]
        for j,oj in enumerate(orbits):
            b[i][j]=sum(z**pop(d) for (e,d) in oj if e==c and okay(a,c,d))
    return b

def determinant_bareiss(A):
    A=[list(map(int,row)) for row in A]
    n=len(A);sgn=1;prev=1
    if n==0:return 1
    for k in range(n-1):
        if A[k][k]==0:
            q=next((q for q in range(k+1,n) if A[q][k]!=0),None)
            if q is None:return 0
            A[k],A[q]=A[q],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=A[i][j]*pivot-A[i][k]*A[k][j]
                assert val%prev==0
                A[i][j]=val//prev
            A[i][k]=0
        prev=pivot
    return sgn*A[-1][-1]

def D(t,z):
    return 1-(1+z+z*z)*t+(z*z+z**3)*t*t-(z+z*z)*t**3+2*z**3*t**4+z**3*t**5

# A determinant of a 10x10 matrix whose entries are degree <= 2 in z,
# with affine t dependence, is of degree <= 10 in t, <=20 in z.
# Matching on (10+1)*(20+1) distinct integer grid points is an
# exact polynomial-identity certificate over the integers.
for z in range(21):
    B=B_at(z)
    for t in range(11):
        M=[[(int(i==j)-t*B[i][j]) for j in range(10)] for i in range(10)]
        assert determinant_bareiss(M)==D(t,z),(z,t)
print('EXACT_TEN_STATE_DETERMINANT_IDENTITY_OK 231 interpolation points')

# Polynomial arithmetic in Z[z] and exact quotient-state transfer.
def plus(p,q):
    r=p+[0]*max(0,len(q)-len(p))
    for i,v in enumerate(q):r[i]+=v
    while len(r)>1 and r[-1]==0:r.pop()
    return r

def shift(p,k):return [0]*k+p

# original 16 states permit simple coefficient-level dynamic programming
# (independent of quotient-state determinant above).
vec={(0,b):shift([1],pop(b)) for b in range(4)}
polys=[]
for n in range(1,15):
    total=[0]
    for (a,b),p in vec.items():
        if okay(a,b,0):total=plus(total,p)
    polys.append(total)
    nextv={}
    for (a,b),p in vec.items():
        for c in range(4):
            if okay(a,b,c):
                key=(b,c)
                nextv[key]=plus(nextv.get(key,[0]),shift(p,pop(c)))
    vec=nextv

def denominator():return [[1],[-1,-1,-1],[0,0,1,1],[0,-1,-1],[0,0,0,2],[0,0,0,1]]
def numerator():return [[1,2,1],[0,1,0,-3],[0,1,1,-3],[0,0,0,-3],[0,0,0,-1]]
for k in range(10):
    s=[0]
    for j,c in enumerate(denominator()):
        if j<=k:
            p=polys[k-j]
            r=[0]*(len(p)+len(c)-1)
            for i,x in enumerate(p):
                for h,y in enumerate(c):r[i+h]+=x*y
            s=plus(s,r)
    want=numerator()[k] if k<5 else [0]
    assert s==want,(k,s,want)
print('EXACT_GENERATING_FUNCTION_NUMERATOR_OK first 10 coefficient-polynomials')

# Scalar sequence checked independently against the historical public
# unweighted sequence, not used to prove the new refined formula.
expected=[4,10,21,48,113,261,601,1390,3216,7435,17190,39751]
assert [sum(p) for p in polys[:12]]==expected
print('UNWEIGHTED_BASELINE_OK first 12 values')

# Direct enumerate each vertex subset and check open-neighborhood counts;
# this does not use the transfer predicate.
for n in range(1,9):
    adj=[]
    for col in range(n):
        for row in range(2):
            nbr=[2*col+1-row]
            if col:nbr.append(2*(col-1)+row)
            if col+1<n:nbr.append(2*(col+1)+row)
            adj.append(nbr)
    counts=[0]*(2*n+1)
    for mask in range(1<<(2*n)):
        if all(((mask>>v)&1) or sum((mask>>u)&1 for u in adj[v])<=1 for v in range(2*n)):
            counts[mask.bit_count()]+=1
    assert counts==polys[n-1]+[0]*(len(counts)-len(polys[n-1])),n
print('DIRECT_ALL_VERTEX_SUBSETS_OK n=1..8')
print('VERIFY_OK')
