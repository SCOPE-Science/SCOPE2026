"""Finite transfer certificate and exact tests for circular-ladder UST leaf correlations.

Python 3, standard library only. No random sampling or external data.
The matrix polynomial certificate plus the displayed analytic inequalities
provide all-size verification; finite determinant checks are diagnostics.
"""
from fractions import Fraction
from itertools import combinations
from math import prod

T = ((1,1,2,1,1),(0,1,0,1,0),(1,1,3,1,1),(0,1,0,3,1),(0,0,0,1,1))
v1=(5,2,6,4,1)
v2=(2,1,2,1,0)
c=(0,0,1,1,1)

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def ident(n):
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def add(A,B,k=1):
    return tuple(tuple(A[i][j]+k*B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def matpow(A,k):
    R=ident(len(A))
    while k:
        if k&1:R=mm(R,A)
        A=mm(A,A);k//=2
    return R

def poly_matrix(M):
    # (x-1)(x^2-4x+1)^2 = x^5 -9x^4 +26x^3 -26x^2+9x -1
    P=ident(len(M))
    for coeff in (-9,26,-26,9,-1):
        P=add(mm(P,M),ident(len(M)),coeff)
    return P

assert all(x==0 for row in poly_matrix(T) for x in row)

def transfer(m,v):
    R=matpow(T,m-3)
    return sum(c[i]*sum(R[i][j]*v[j] for j in range(5)) for i in range(5))

def cheb(m):
    a0,a1=1,2
    if m==0:return 1,0
    b0,b1=0,1
    for k in range(1,m):
        a0,a1=a1,4*a1-a0
        b0,b1=b1,4*b1-b0
    return a1,b1

def counts(m):
    A,B=cheb(m)
    _,Bm1=cheb(m-1)
    F=m*(A-1)
    H=(A-B-m*A+2*m*B-1)//2
    C=(-A+2*B-4*m*A+7*m*B-1)//2
    R=Bm1
    return F,H,C,R

assert [counts(m) for m in range(3,8)] == [(75,11,3,4),(384,50,15,15),(1805,216,65,56),(8100,912,272,209),(35287,3795,1121,780)]
for m in range(3,51):
    f,h,side,rung=counts(m)
    assert transfer(m,v1)==h
    assert transfer(m,v2)==side
    assert f>0 and h>0 and side>0 and rung>0
    cov_h=Fraction(4*side*f-9*h*h,f*f)
    cov_r=Fraction(4*rung*f-9*h*h,f*f)
    assert (cov_h>0)==(m>=4)
    assert (cov_r>0)==(m<=4)
assert Fraction(4*3*75-9*11**2,75**2)==-Fraction(21,625)
assert Fraction(4*4*75-9*11**2,75**2)==Fraction(37,1875)
assert Fraction(4*15*384-9*50**2,384**2)==Fraction(15,4096)

# Verify 5-state transfer matrix by independent local edge-subset enumeration.
states=((('a',),('b',),('p1',)),(('a',),('b','p1')), (('a','b'),('p1',)), (('a','b','p1'),), (('a','p1'),('b',)))
def canonical(groups):
    return tuple(sorted((tuple(sorted(q)) for q in groups),key=lambda v:v[0]))
def push(groups, vertices, edges, keep):
    par={x:x for x in vertices}
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]];x=par[x]
        return x
    def uni(x,y):
        x=find(x);y=find(y)
        if x==y:return False
        par[y]=x;return True
    for group in groups:
        for x in group[1:]:
            if not uni(group[0],x):return None
    for x,y in edges:
        if not uni(x,y):return None
    for x in vertices:
        if x not in keep and all(find(x)!=find(z) for z in keep):return None
    buckets={}
    for x in keep:buckets.setdefault(find(x),[]).append(x)
    return canonical(buckets.values())

def every_subset(edges):
    for mask in range(1<<len(edges)):
        yield tuple(edges[i] for i in range(len(edges)) if mask>>i&1)

M=[[0]*5 for _ in range(5)]
for j,s in enumerate(states):
    for edges in every_subset((('a','c'),('b','d'),('c','d'))):
        p=push(s,['p1','a','b','c','d'],edges,['p1','c','d'])
        if p is None:continue
        p=canonical(tuple(tuple({'c':'a','d':'b'}.get(x,x) for x in g) for g in p))
        M[states.index(p)][j]+=1
assert tuple(map(tuple,M))==T
for present,target in [(True,v1),(False,v2)]:
    vertices=['p1','y','a','b']+(['x'] if present else [])
    edges=[('p1','y'),('y','b'),('a','b')]+([('x','y'),('x','a')] if present else [])
    vec=[0]*5
    for e in every_subset(edges):
        p=push(tuple((v,) for v in vertices),vertices,e,['p1','a','b'])
        if p is not None:vec[states.index(p)]+=1
    assert tuple(vec)==target
end=[]
for s in states:
    end.append(sum(1 for e in ((),(('b','p1'),)) if (p:=push(s,['p1','a','b'],e,['p1','a','b'])) is not None and len(p)==1))
assert tuple(end)==c

# Independent exact Matrix–Tree minors on the first eight prisms.
def determinant(A):
    A=[[Fraction(t) for t in row] for row in A]
    n=len(A);out=Fraction(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:A[k],A[pivot]=A[pivot],A[k];out=-out
        z=A[k][k];out*=z
        for i in range(k+1,n):
            fac=A[i][k]/z
            for j in range(k+1,n):A[i][j]-=fac*A[k][j]
            A[i][k]=0
    assert out.denominator==1
    return int(out)

def treecount(m,removed):
    N=2*m
    edge=set()
    for j in range(m):
        edge.add(tuple(sorted((j,(j+1)%m))))
        edge.add(tuple(sorted((m+j,m+(j+1)%m))))
        edge.add((j,m+j))
    remaining=[v for v in range(N) if v not in removed]
    if len(remaining)==1:return 1
    loc={v:i for i,v in enumerate(remaining)}
    L=[[0]*len(remaining) for _ in remaining]
    for a,b in edge:
        if a not in loc or b not in loc:continue
        i=loc[a];j=loc[b]
        L[i][i]+=1;L[j][j]+=1
        L[i][j]-=1;L[j][i]-=1
    return determinant([row[:-1] for row in L[:-1]])

for m in range(3,11):
    f,h,side,rung=counts(m)
    assert (treecount(m,set()),treecount(m,{0}),treecount(m,{0,1}),treecount(m,{0,m}))==(f,h,side,rung)
print('PASS: transfer characteristic identity, local-state enumeration, exact formulas/signs, determinant diagnostics (m=3..10).')
print('All-size signs follow from the separate explicit Laurent-coefficient inequalities in the proof.')
