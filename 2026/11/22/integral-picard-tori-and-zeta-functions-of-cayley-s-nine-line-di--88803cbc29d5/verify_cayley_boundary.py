#!/usr/bin/env python3
"""Exact combinatorial and finite-field checks for the Cayley nine-line divisor."""
from itertools import combinations, product
from collections import Counter, deque

I=tuple(range(4))
E=list(combinations(I,2))
Q=sorted({tuple(sorted((e,tuple(i for i in I if i not in e)))) for e in E})
lines=[('E',e) for e in E]+[('Q',u) for u in Q]
points=[('N',i) for i in I]+[('P',e) for e in E]+[('R',u) for u in Q]
branches=[]
for e in E:
    branches.extend([(('E',e),('N',i)) for i in e])
    branches.append((('E',e),('P',e)))
for u in Q:
    for e in u: branches.append((('Q',u),('P',e)))
    for v in Q:
        if u!=v:
            r=next(w for w in Q if w not in (u,v))
            branches.append((('Q',u),('R',r)))
branches=list(dict.fromkeys(branches))
vertices=lines+points
assert len(E)==6 and len(Q)==3 and len(lines)==9 and len(points)==13 and len(branches)==30
assert len(set(branches))==30

def apply(p,x):
    t,v=x
    if t=='N':return ('N',p[v])
    if t in ('E','P'): return (t,tuple(sorted(p[i] for i in v)))
    if t in ('Q','R'):return (t,tuple(sorted(tuple(sorted(p[i] for i in e)) for e in v)))
    raise ValueError(x)

def orbit_counts(objects,p,transform):
    left=set(objects); cnt=Counter()
    while left:
        x=next(iter(left));y=x;n=0
        while y in left:
            left.remove(y);n+=1;y=transform(p,y)
        assert y==x
        cnt[n]+=1
    return dict(sorted(cnt.items()))

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def trace(A):return sum(A[i][i] for i in range(len(A)))

def charpoly(A):
    n=len(A);P=identity(n);tr=[]
    for k in range(1,n+1):
        P=matmul(P,A);tr.append(trace(P))
    c=[1]
    for k in range(1,n+1):
        x=-sum(c[k-j]*tr[j-1] for j in range(1,k+1))
        assert x%k==0
        c.append(x//k)
    return c

def poly_mul(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):r[i+j]+=u*v
    return r

def target_poly(factors):
    poly=[1]
    for base,power in factors:
        for _ in range(power):poly=poly_mul(poly,base)
    return poly

# Each column of cycles has coefficient +1 on its own chord.
# The path from the singular endpoint of a chord to its line endpoint is completed inside the tree.
parent={v:v for v in vertices}
def root(v):
    while parent[v]!=v:v=parent[v]
    return v
tree=[]; chords=[]
for a,b in branches:
    if root(a)!=root(b):parent[root(a)]=root(b);tree.append((a,b))
    else:chords.append((a,b))
assert len(tree)==21 and len(chords)==9
adj={v:[] for v in vertices}
for e in tree:
    a,b=e;adj[a].append((b,e));adj[b].append((a,e))

def fundamental_cycle(chord):
    a,b=chord;prev={b:None};queue=deque([b])
    while queue and a not in prev:
        v=queue.popleft()
        for w,e in adj[v]:
            if w not in prev:prev[w]=(v,e);queue.append(w)
    assert a in prev
    coef={chord:1};v=a
    while v!=b:
        u,e=prev[v]
        coef[e]=1 if e==(u,v) else -1
        v=u
    assert len(coef)>=2
    divergence={v:0 for v in vertices}
    for (l,s),w in coef.items(): divergence[l]-=w;divergence[s]+=w
    assert all(z==0 for z in divergence.values())
    return coef
cycles=[fundamental_cycle(ch) for ch in chords]

def frob_matrix(p):
    M=[[0]*9 for _ in range(9)]
    for j,c in enumerate(cycles):
        moved={(apply(p,a),apply(p,b)):v for (a,b),v in c.items()}
        for i,ch in enumerate(chords):M[i][j]=moved.get(ch,0)
        reconstructed=Counter()
        for i,col in enumerate(cycles):
            for e,v in col.items():reconstructed[e]+=M[i][j]*v
        assert all(reconstructed[e]==moved.get(e,0) for e in branches)
    return M

cases={
'identity':((0,1,2,3),{1:9},{1:13},{1:30},[( [1,-1],9)]),
'transposition':((1,0,2,3),{1:3,2:3},{1:5,2:4},{1:6,2:12},[([1,-1],4),([1,1],5)]),
'double_transposition':((1,0,3,2),{1:5,2:2},{1:5,2:4},{1:10,2:10},[([1,-1],5),([1,1],4)]),
'3_cycle':((1,2,0,3),{3:3},{1:1,3:4},{3:10},[([1,-1],3),([1,1,1],3)]),
'4_cycle':((1,2,3,0),{1:1,2:2,4:1},{1:1,2:2,4:2},{2:5,4:5},[([1,-1],2),([1,1],3),([1,0,1],2)])}

for name,(p,L,S,B,factors) in cases.items():
    assert orbit_counts(lines,p,apply)==L,(name,'L')
    assert orbit_counts(points,p,apply)==S,(name,'S')
    assert orbit_counts(branches,p,lambda p,e:(apply(p,e[0]),apply(p,e[1])))==B,(name,'B')
    assert sum(k*v for k,v in L.items())==9
    assert sum(k*v for k,v in S.items())==13
    assert sum(k*v for k,v in B.items())==30
    M=frob_matrix(p)
    assert charpoly(M)==target_poly(factors),(name,charpoly(M),target_poly(factors))
    P=identity(9)
    for m in range(1,13):
        P=matmul(P,M)
        if P==identity(9):break
    assert m in (1,2,3,4)
    print(name,'line_orbits',L,'node_orbits',S,'branch_orbits',B,'charpoly',charpoly(M))

# Actual projective F_p points and their line multiplicities in the split model.
for p in (5,7,11):
    multiples=Counter()
    for x in product(range(p),repeat=4):
        if all(t==0 for t in x):continue
        if next(t for t in x if t)!=1:continue
        mult=0
        for e in E:
            if all(x[i]==0 for i in I if i not in e):mult+=1
        for u in Q:
            if all(sum(x[i] for i in e)%p==0 for e in u):mult+=1
        if mult:
            assert (sum(x[a]*x[b]*x[c] for a,b,c in combinations(I,3))%p)==0
            multiples[mult]+=1
    assert multiples[3]==4 and multiples[2]==9 and multiples[1]==9*p-21,(p,multiples)
    assert sum(multiples.values())==9*p-8
    print('split F_',p, 'line union',sum(multiples.values()),'triple',multiples[3],'double',multiples[2])
print('CAYLEY_BOUNDARY_INTEGRAL_FROBENIUS_AND_ZETA_OK')
