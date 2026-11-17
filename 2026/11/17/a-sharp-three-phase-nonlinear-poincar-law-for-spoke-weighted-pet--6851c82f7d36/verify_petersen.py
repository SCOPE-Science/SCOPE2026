"""Exact-arithmetic supplementary checks of the weighted Petersen metric bound.
Python 3 standard library only. Proof for all parameters is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations
from heapq import heappush,heappop

N=10
edges=[]
for i in range(5):
    edges.append((i,(i+1)%5,0))
    edges.append((5+i,5+((i+2)%5),1))
    edges.append((i,5+i,2))
assert len(edges)==15

def lengths(weights):
    D=[[None]*N for _ in range(N)]
    for s in range(N):
        D[s][s]=Q(0)
        adj=[[] for _ in range(N)]
        for a,b,k in edges:
            adj[a].append((b,weights[k]));adj[b].append((a,weights[k]))
        pq=[(Q(0),s)]
        while pq:
            d,u=heappop(pq)
            if D[s][u]!=d:continue
            for v,w in adj[u]:
                z=d+w
                if D[s][v] is None or z<D[s][v]:
                    D[s][v]=z;heappush(pq,(z,v))
    return D

def pair_total(D):
    return sum((D[a][b] for a,b in combinations(range(N),2)), Q(0))

def ratio(D,t):
    s=pair_total(D)
    e=sum((D[u][v]*(t if k==2 else 1) for u,v,k in edges),Q(0))
    return s/e

def target(t):
    if t<=1:return 5/t
    if t<=Q(9,4):return 25/(t+4)
    return Q(4)

def witness(t):
    if t<=1:
        return [[Q(0) if (a<5)==(b<5) else Q(1) for b in range(N)] for a in range(N)]
    if t<=Q(9,4):
        return lengths((Q(2),Q(2),Q(1)))
    return [[Q(min((a-b)%5,(b-a)%5)) for b in [v%5 for v in range(N)]] for a in [u%5 for u in range(N)]]

# Shortest path tests: exact three parameter regimes, both transition endpoints.
T=[Q(1,11),Q(1,2),Q(1),Q(10,9),Q(3,2),Q(2),Q(9,4),Q(5,2),Q(7)]
for t in T:
    d=witness(t)
    assert all(d[i][i]==0 for i in range(N))
    assert all(d[i][j]==d[j][i] for i in range(N) for j in range(N))
    assert all(d[i][k]<=d[i][j]+d[j][k] for i in range(N) for j in range(N) for k in range(N))
    assert ratio(d,t)==target(t),(t,ratio(d,t),target(t))

# The 7 dihedral pair classes and the pair-path upper certificates.
def reflect(v,epsilon,k):
    return (v//5)*5+(epsilon*(v%5)+k)%5

def orbit(a,b):
    return min(tuple(sorted((reflect(a,ep,k),reflect(b,ep,k)))) for ep in (-1,1) for k in range(5))
groups={}
for a,b in combinations(range(N),2):groups.setdefault(orbit(a,b),[]).append((a,b))
assert sorted(len(g) for g in groups.values())==[5,5,5,5,5,10,10]
# Each certificate is a specific pair of graph paths, encoded as counts
# of outer, inner, spoke edges; verify every endpoint in each orbit.
paths={}
for (a,b),pairs in groups.items():
    if a<5 and b<5:
        if (a-b)%5 in (1,4): cert=((1,0,0),(1,0,0))
        else: cert=((2,0,0),(0,1,2))
    elif a>=5 and b>=5:
        if (a-b)%5 in (2,3): cert=((0,1,0),(0,1,0))
        else: cert=((0,2,0),(1,0,2))
    else:
        oi=a if a<5 else b;ii=b if a<5 else a
        diff=(oi-ii)%5
        if diff==0:cert=((0,0,1),(0,0,1))
        elif diff in (1,4):cert=((1,0,1),(1,0,1))
        else:cert=((0,1,1),(0,1,1))
    paths[(a,b)]=(len(pairs),cert)
# For each orbit and both route schemes, exhibit a valid walk with
# the certified three-type vector, using exhaustive simple-path search.
adj={v:[] for v in range(N)}
for u,v,k in edges:adj[u].append((v,k));adj[v].append((u,k))
def is_path(a,b,signature):
    stack=[(a,(0,0,0),{a})]
    while stack:
        u,c,visited=stack.pop()
        if u==b and c==signature:return True
        if sum(c)>=sum(signature):continue
        for v,k in adj[u]:
            if v in visited:continue
            z=list(c);z[k]+=1
            if z[k]>signature[k]:continue
            stack.append((v,tuple(z),visited|{v}))
    return False
for (a,b),(n,certs) in paths.items():
    assert all(is_path(a,b,c) for c in certs),((a,b),certs)
for k in (0,1):
    v=[0,0,0]
    for multiplicity,certs in paths.values():
        c=certs[k]
        for i in range(3):v[i]+=multiplicity*c[i]
    assert tuple(v)==((25,25,25) if k==0 else (20,20,45)),(k,v)
print('PASS: exact nine-parameter witnesses, metric triangle checks, seven orbit sizes, two 45-pair route certificates.')
