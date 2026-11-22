#!/usr/bin/env python3
"""Exact length law for loop-erased walks on the twelve-vertex icosahedral graph.

Requires Python 3 standard library only. The rooted-forest determinant formula is
proved in the accompanying manuscript; this code checks every finite instance.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import prod

N=12
adj=[set() for _ in range(N)]
def edge(u,v):
    adj[u].add(v);adj[v].add(u)
# Poles 0 and 11, two staggered five-cycles 1,...,5 and 6,...,10.
for i in range(5):
    u=1+i; v=6+i
    edge(0,u);edge(11,v)
    edge(u,1+(i+1)%5)
    edge(v,6+(i+1)%5)
    edge(u,v);edge(u,6+(i-1)%5)
adj=tuple(tuple(sorted(x)) for x in adj)
assert all(len(x)==5 for x in adj) and sum(map(len,adj))==60
L=[[ (5 if i==j else (-1 if j in adj[i] else 0)) for j in range(N)] for i in range(N)]

def det_bareiss(matrix):
    A=[list(row) for row in matrix]
    n=len(A)
    if not n:return 1
    sign=1;old=1
    for k in range(n-1):
        if A[k][k]==0:
            t=next((i for i in range(k+1,n) if A[i][k]!=0),None)
            if t is None:return 0
            A[t],A[k]=A[k],A[t]; sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*p-A[i][k]*A[k][j]
                assert numerator%old==0
                A[i][j]=numerator//old
        for i in range(k+1,n): A[i][k]=0
        old=p
    return sign*A[-1][-1]

@lru_cache(None)
def principal(mask):
    ix=[i for i in range(N) if mask & 1<<i]
    return det_bareiss([[L[i][j] for j in ix] for i in ix])

full=(1<<N)-1
T=principal(full^(1<<11))
assert T==5184000

def distances(root):
    d={root:0};front=[root]
    for u in front:
        for v in adj[u]:
            if v not in d:
                d[v]=d[u]+1;front.append(v)
    return d
D=distances(0)
assert Counter(D.values())==Counter({0:1,1:5,2:5,3:1})

expected={
1:{1:1900800,2:1045440,3:561792,4:448920,5:469148,6:398776,7:232224,8:93888,9:27220,10:5280,11:512},
2:{2:1209600,3:1260384,4:1086696,5:788576,6:463488,7:236756,8:100416,9:31236,10:6240,11:608},
3:{3:1797120,4:1707360,5:903660,6:425240,7:209340,8:98360,9:34800,10:7400,11:720},
}
expected_geodesics={1:Fraction(11,30),2:Fraction(7,30),3:Fraction(26,75)}
expected_mean={1:Fraction(930701,324000),2:Fraction(1255111,324000),3:Fraction(5713,1350)}

# First exact method: contract each simple path and use its principal Laplacian
# minor to count spanning trees containing the path.
def path_spectrum(s,t):
    bylength=Counter(); ordinary=Counter(); geodesic_pathweights=[]
    def visit(u,used,steps):
        if u==t:
            z=principal(full^used)
            bylength[steps]+=z
            ordinary[steps]+=1
            if steps==D[t]:geodesic_pathweights.append(z)
            return
        for v in adj[u]:
            if not used & (1<<v): visit(v,used|(1<<v),steps+1)
    visit(s,1<<s,0)
    return dict(sorted(bylength.items())),dict(sorted(ordinary.items())),geodesic_pathweights

# Second exact method: Wilson's path law via the diagonal Green function of
# the random walk killed at the target and earlier loop-erased vertices.
# Exact inverse element is formed using Fraction Gaussian elimination rather
# than determinant arithmetic. Telescoping gives the forest minor identity.
def green_diag(vertices,v):
    order=sorted(vertices);ind=order.index(v)
    A=[[Fraction(L[x][y]) for y in order] for x in order]
    b=[Fraction(int(i==ind)) for i in range(len(order))]
    for j in range(len(order)):
        q=next(i for i in range(j,len(order)) if A[i][j])
        if q!=j:A[j],A[q]=A[q],A[j];b[j],b[q]=b[q],b[j]
        p=A[j][j]
        for k in range(j,len(order)):A[j][k]/=p
        b[j]/=p
        for i in range(j+1,len(order)):
            c=A[i][j]
            if c:
                for k in range(j,len(order)):A[i][k]-=c*A[j][k]
                b[i]-=c*b[j]
    for i in range(len(order)-1,-1,-1):
        for j in range(i+1,len(order)):b[i]-=A[i][j]*b[j]
    return b[ind]

# Keep this independent check bounded: path representatives for all three
# distance classes, including direct geodesics, long and Hamiltonian paths.
for d in (1,2,3):
    t=next(k for k in range(N) if D[k]==d)
    counts,paths,gw=path_spectrum(0,t)
    assert counts==expected[d]
    assert sum(counts.values())==T
    assert Fraction(counts[d],T)==expected_geodesics[d]
    assert Fraction(sum(k*v for k,v in counts.items()),T)==expected_mean[d]
    assert len(gw)==paths[d]
    for z in range(N):
        if D[z]==d:
            pz,_,_=path_spectrum(0,z)
            assert pz==counts
    print(f'd={d} path_count={sum(paths.values())} lengths={counts}')
    print(f'd={d} geodesic={expected_geodesics[d]} mean={expected_mean[d]}')

# Exhaustively check all 66 unordered vertex pairs, not merely a presumed
# distance-transitivity reduction.
for s in range(N):
    ds=distances(s)
    for t in range(s+1,N):
        spectrum,_,_=path_spectrum(s,t)
        assert spectrum==expected[ds[t]], (s,t,ds[t],spectrum)

# Sample all 3 geodesic classes and one each of the extremal path lengths;
# verify the Green-function formula through an independent rational solve.
for d in (1,2,3):
    t=next(k for k in range(N) if D[k]==d)
    samples={}
    def collect(u,used,P):
        if u==t:
            k=len(P)-1
            if k in (d,d+1,11) and len(samples.get(k,[]))<2:
                samples.setdefault(k,[]).append(tuple(P))
            return
        for w in adj[u]:
            if not used>>w&1:collect(w,used|(1<<w),P+[w])
    collect(0,1,[0])
    for k,Ps in samples.items():
        for P in Ps:
            remainder=set(range(N))-{t}
            weight=Fraction(1)
            for v in P[:-1]:
                weight*=green_diag(remainder,v)
                remainder.remove(v)
            minor=Fraction(principal(full^sum(1<<v for v in P)),T)
            assert weight==minor,(d,P,weight,minor)
print('PASS: all 66 vertex pairs, exact distributions, matrix-tree normalization, and Green-function spot checks')
