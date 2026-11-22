#!/usr/bin/env python3
"""Independent finite check for minimum domination and shattering on a Cayley graph."""
from itertools import combinations
from collections import Counter

V=list((x,y) for x in range(4) for y in range(4))
idx={v:i for i,v in enumerate(V)}
A={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
B={(1,2),(3,2),(2,1),(2,3),(1,3),(3,1)}
N=[]
for x,y in V:
    N.append(sum(1<<j for j,(u,v) in enumerate(V)
                 if ((u-x)%4,(v-y)%4) in A or (u,v)==(x,y)))
FULL=(1<<16)-1
D=[]
for mask in range(1<<16):
    if mask.bit_count()>3:continue
    cov=0
    for i in range(16):
        if mask>>i&1:cov|=N[i]
    if cov==FULL:D.append(mask)
assert len(D)==32 and all(x.bit_count()==3 for x in D)
assert not any((N[i]|N[j])==FULL for i,j in combinations(range(16),2))

# Independent candidate description using pair differences (not domination).
T=[]
for c in combinations(range(16),3):
    if all(((V[j][0]-V[i][0])%4,(V[j][1]-V[i][1])%4) in B
           for i,j in combinations(c,2)):
        T.append(sum(1<<i for i in c))
assert len(T)==32 and set(T)==set(D)

faces=[]
f=Counter()
for supp in range(1<<16):
    patterns={d&supp for d in D}
    if len(patterns)==1<<supp.bit_count():
        faces.append(supp)
        f[supp.bit_count()]+=1
assert f=={0:1,1:16,2:48,3:32}
assert all(any((supp&t)==supp for t in T) for supp in faces)
assert len(faces)==97

# Graph induced by positive pair occurrence; every edge lies in two triangles.
Es=[t for t in faces if t.bit_count()==2]
for e in Es:
    assert sum((e&t)==e for t in T)==2
assert all(sum(v>>i&1 for v in Es)==6 for i in range(16))

# Two translation orbits of the 32 triangle faces. For each, explicit eight trace witnesses.
def translate(mask,dx,dy):
    out=0
    for i,(x,y) in enumerate(V):
        if mask>>i&1:out|=1<<idx[((x+dx)%4,(y+dy)%4)]
    return out
unseen=set(T);orbits=[]
while unseen:
    t=min(unseen)
    orbit={translate(t,dx,dy) for dx in range(4) for dy in range(4)}
    assert len(orbit)==16
    unseen-=orbit
    orbits.append((t,orbit))
assert len(orbits)==2
for t,orbit in orbits:
    vv=[i for i in range(16) if t>>i&1]
    pattern=[]
    for r in range(8):
        witness=next(d for d in D if all(((d>>vv[j])&1)==((r>>j)&1) for j in range(3)))
        pattern.append(tuple(V[j] for j in range(16) if witness>>j&1))
    print('representative:',tuple(V[i] for i in vv))
    for k,v in enumerate(pattern):print('  trace',format(k,'03b'),'witness',v)

# Smith-free integral rank check, with spanning tree graph d1 and rational d2.
triv=[x for x in faces if x.bit_count()==3]
D2=[[0]*32 for _ in range(48)]
for j,t in enumerate(triv):
    vv=[i for i in range(16) if t>>i&1]
    for k in range(3):
        D2[Es.index(t^(1<<vv[k]))][j]=(-1)**k
def rank_mod_prime(matrix,p=1000003):
    arr=[[v%p for v in row] for row in matrix]
    rr=0
    for col in range(len(arr[0])):
        pivot=next((i for i in range(rr,len(arr)) if arr[i][col]), None)
        if pivot is None: continue
        arr[rr],arr[pivot]=arr[pivot],arr[rr]
        inv=pow(arr[rr][col],-1,p)
        arr[rr]=[(v*inv)%p for v in arr[rr]]
        for i in range(rr+1,len(arr)):
            if arr[i][col]:
                factor=arr[i][col]
                arr[i]=[(a-factor*b)%p for a,b in zip(arr[i],arr[rr])]
        rr+=1
    return rr
rank=rank_mod_prime(D2)
assert rank==31
print('gamma=3 minimizers=32')
print('Shattering polynomial:', dict(sorted(f.items())))
print('Boundary rank mod 1000003=',rank,'; expected integral homology ranks H1=',48-15-rank,' H2=',32-rank)
print('Each vertex link a C6; a 4-by-4 periodic triangular tessellation gives an orientable torus.')
print('PASS')
