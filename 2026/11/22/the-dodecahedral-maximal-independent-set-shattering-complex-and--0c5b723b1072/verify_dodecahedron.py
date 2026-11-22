"""Independent standard-library check via maximal cliques of the complement.
The data are the twenty vertices 0..9 (outer), 10..19 (inner) of GP(10,2).
"""
from collections import Counter
from itertools import combinations, permutations

N=20
adj=[0]*N
for i in range(10):
    for a,b in ((i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)):
        adj[a] |= 1<<b
        adj[b] |= 1<<a
ALL=(1<<N)-1
comp=[ALL^(adj[v]|(1<<v)) for v in range(N)]

# Bron--Kerbosch in the complement, not a brute-force maximality filter.
maximal=[]
def bk(R,P,X):
    if not P and not X:
        maximal.append(R)
        return
    U=P|X
    pivot=max((v for v in range(N) if U>>v&1),key=lambda v:(P&comp[v]).bit_count()) if U else 0
    choices=P&~comp[pivot]
    while choices:
        b=choices&-choices;v=b.bit_length()-1;choices-=b
        bk(R|b,P&comp[v],X&comp[v]);P-=b;X|=b
bk(0,ALL,0)
assert len(maximal)==295, len(maximal)
assert Counter(m.bit_count() for m in maximal)=={6:10,7:280,8:5}

# Enumerate every independent support via induced-subgraph recursion.
independent=[False]*(1<<N)
independent[0]=True
for s in range(1,1<<N):
    bit=s&-s;v=bit.bit_length()-1;t=s-bit
    independent[s]=independent[t] and not (t&adj[v])
assert [sum(1 for s in range(1<<N) if independent[s] and s.bit_count()==k) for k in range(9)] == [1,20,160,660,1510,1912,1240,320,5]
faces=[[] for _ in range(7)]
shattered=set()
for s in range(1<<N):
    k=s.bit_count()
    if k>8 or not independent[s]:
        continue
    if len({s&m for m in maximal}) == (1<<k):
        assert k<=6
        faces[k].append(s)
        shattered.add(s)
assert list(map(len,faces)) == [1,20,160,660,1470,1572,310]
facets=[s for s in shattered if not any((s|1<<i) in shattered for i in range(N) if not s>>i&1)]
assert Counter(s.bit_count() for s in facets) == {4:10,5:672,6:310}

# The four-vertex facets are exactly equidistant (distance three) tetrads.
dist=[[99]*N for _ in range(N)]
for v in range(N):
    dist[v][v]=0; Q=[v]
    for u in Q:
        for w in range(N):
            if adj[u]>>w&1 and dist[v][w]==99:
                dist[v][w]=dist[v][u]+1
                Q.append(w)
tetrads={sum(1<<v for v in c) for c in combinations(range(N),4)
        if all(dist[u][v]==3 for u,v in combinations(c,2))}
assert tetrads == {s for s in facets if s.bit_count()==4}
assert len(tetrads)==10

# Exact mod-2 linear algebra, with integer-bitset columns.
rank={0:0,7:0}
for k in range(1,7):
    index={s:i for i,s in enumerate(faces[k-1])}
    basis={}
    for s in faces[k]:
        col=0
        whileBits=s
        while whileBits:
            b=whileBits&-whileBits;whileBits-=b
            col ^= 1<<index[s^b]
        while col:
            h=col.bit_length()-1
            if h not in basis:
                basis[h]=col
                break
            col ^= basis[h]
    rank[k]=len(basis)
assert [rank[k] for k in range(1,7)] == [1,19,141,519,941,305]
betti=[len(faces[k])-rank[k]-rank[k+1] for k in range(7)]
assert betti == [0,0,0,0,10,326,5]
print("PASS independent Python verification; facets 10/672/310; tetrads are the ten distance-three tetrahedra; Betti (10,326,5)")
