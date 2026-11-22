#!/usr/bin/env python3
"""Exact finite certificate for temporal three-periodic Toom histories.
Standard-library Python only. No external data or dependencies.
"""
from itertools import permutations

N = 512

def step_column(a,b):
    z=0
    for r in range(3):
        x=(a>>r)&1; north=(a>>((r+1)%3))&1; east=(b>>r)&1
        z |= (int(x+north+east >= 2)<<r)
    return z

# The t-th three-bit block of a history is the column at time t.
def edge(a,b):
    for t in range(3):
        x=(a>>(3*t))&7
        y=(b>>(3*t))&7
        wanted=(a>>(3*((t+1)%3)))&7
        if step_column(x,y)!=wanted:
            return False
    return True

adj=[[] for _ in range(N)]
radj=[[] for _ in range(N)]
for a in range(N):
    for b in range(N):
        if edge(a,b):
            adj[a].append(b);radj[b].append(a)
assert sum(map(len,adj))==1120

# Fully independent pure-Python two-pass strong-component decomposition.
seen=[False]*N;order=[]
def dfs1(v):
    seen[v]=True
    for w in adj[v]:
        if not seen[w]:dfs1(w)
    order.append(v)
for a in range(N):
    if not seen[a]:dfs1(a)
seen=[False]*N

def dfs2(v,component):
    seen[v]=True;component.append(v)
    for w in radj[v]:
        if not seen[w]:dfs2(w,component)
components=[]
for v in reversed(order):
    if not seen[v]:
        c=[];dfs2(v,c);components.append(sorted(c))
cyclic=sorted([c for c in components if len(c)>1 or (c[0] in adj[c[0]])],key=lambda c:(len(c),c))
EXPECTED=[[0,511],[73,146,219,292,365,438],[84,161,245,266,350,427]]
assert sorted(cyclic)==sorted(EXPECTED),(len(cyclic),cyclic)
assert sum(len(c) for c in cyclic)==14
assert len(components)==501   # 498 transient singletons plus 3 cyclic SCCs
# Independent return-reachability check for every history vertex.
returning=set()
for a in range(N):
    stack=list(adj[a]);reached=set()
    while stack:
        b=stack.pop()
        if b in reached:continue
        reached.add(b)
        stack.extend(adj[b])
    if a in reached:returning.add(a)
assert returning==set(x for c in EXPECTED for x in c)

# Nonconstant three-bit columns and the temporal-rotating histories.
colnames=['001','010','100','011','101','110']
def encode_word(s):return sum(int(b)<<i for i,b in enumerate(s))
def north_shift(a):return sum(((a>>((r+1)%3))&1)<<r for r in range(3))
def triple(a):
    b=north_shift(a);c=north_shift(b)
    return a | (b<<3) | (c<<6)
cols=[encode_word(s) for s in colnames]
assert set(triple(c) for c in cols)==set(EXPECTED[2])
B=[[int(step_column(a,b)==north_shift(a)) for b in cols]for a in cols]
assert all(sum(row)==2 for row in B)
assert all(adj[triple(a)].count(triple(b))==B[i][j] for i,a in enumerate(cols) for j,b in enumerate(cols))

# Exact det(z I - B) using six-factor Leibniz formula with polynomial arrays.
# Lists are ascending coefficients in z, with Python arbitrary-precision integers.
def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def det_char(M):
    n=len(M);v=[0]*(n+1)
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        p=[1]
        for i,j in enumerate(perm):
            p=mul(p,[-M[i][j],1] if i==j else [-M[i][j]])
        for k,coef in enumerate(p):v[k]+=sign*coef
    return v
poly=det_char(B)
expected=mul(mul([0,1],[-2,1]),mul([1,-1,1],[3,3,1]))
assert poly==expected,(poly,expected)

def matmul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

def trace(M):return sum(M[i][i] for i in range(len(M)))
P=[[int(i==j) for j in range(6)] for i in range(6)]
counts={}
for n in range(1,21):
    P=matmul(P,B)
    counts[n]=trace(P)
    if n>=3:assert counts[n]%3==0
assert [(n,counts[n]//3) for n in range(3,7)]==[(3,2),(4,2),(5,20),(6,4)]
print('edge_pairs=262144, accepted_edges=1120, temporal_histories=512')
print('cyclic_sccs='+repr(cyclic))
print('rotating_matrix='+repr(B))
print('characteristic_polynomial_ascending='+repr(poly))
print('primitive_three_orbits_n3_to_n12='+repr([(n,counts[n]//3) for n in range(3,13)]))
print('all transfer assertions passed')
