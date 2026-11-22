"""Independent Coxeter line-graph certificate for Heawood optimal edge domination.
Run with Python 3 standard library: python3 verify_coxeter.py
"""
from collections import Counter, deque
from itertools import combinations

lines=[{j,(j+1)%7,(j+3)%7} for j in range(7)]
flags=[(p,j) for p in range(7) for j in range(7) if p in lines[j]]
assert len(flags)==21

def valid(M):
    usedpoints={flags[i][0] for i in M}
    usedlines={flags[i][1] for i in M}
    return all(p in usedpoints or j in usedlines for p,j in flags)

def matching(M):
    return len({flags[i][0] for i in M}) == len(M) == len({flags[i][1] for i in M})

# The Fano argument shows every optimum is a five-edge matching.
# Enumerate all (21 choose 5) five-edge choices directly, rather than relying
# on the full-subset bitmask dynamic program of the other certificate.
opt=[sum(1<<i for i in M) for M in combinations(range(21),5)
     if matching(M) and valid(M)]
opt.sort()
assert len(opt)==42
assert all(valid([i for i in range(21) if (s>>i)&1]) for s in opt)
A=[{j for j,t in enumerate(opt) if i!=j and (s^t).bit_count()==4}
   for i,s in enumerate(opt)]
assert all(len(N)==4 for N in A)
triangles=[t for t in combinations(range(42),3)
           if all(b in A[a] for a,b in combinations(t,2))]
assert len(triangles)==28
assert all(sum(i in t for t in triangles)==2 for i in range(42))
# Every exchange edge occurs in one of the 28 triangles.
for i in range(42):
    for j in A[i]:
        assert sum(i in t and j in t for t in triangles)==1

# Triangle-intersection quotient: vertices are the 28 triangles,
# edges are the optimum five-matchings contained in two triangles.
Q=[{j for j,u in enumerate(triangles) if j!=i and set(t)&set(u)}
   for i,t in enumerate(triangles)]
assert all(len(row)==3 for row in Q)
assert sum(map(len,Q))//2==42

# Canonical Coxeter graph = disjointness graph of Fano nonline triples.
triples=[set(t) for t in combinations(range(7),3) if set(t) not in lines]
assert len(triples)==28
C=[{j for j,u in enumerate(triples) if j!=i and not (t&u)}
   for i,t in enumerate(triples)]
assert all(len(row)==3 for row in C)
# Explicit permutation is a complete finite isomorphism certificate. It maps
# the lexicographically sorted triangle IDs to sorted nonline-triple IDs.
permutation=[0,25,6,15,17,27,19,26,13,10,7,2,23,20,
             21,9,3,24,22,1,16,5,18,4,14,11,12,8]
assert sorted(permutation)==list(range(28))
for i in range(28):
    for j in range(28):
        assert (j in Q[i]) == (permutation[j] in C[permutation[i]])
# Consequently the 42-state exchange graph equals the line graph of C:
# each five-edge optimum corresponds to its two containing triangles,
# and two optimum states exchange two edges exactly when their C-edges meet.
which=[tuple(i for i,t in enumerate(triangles) if j in t) for j in range(42)]
assert all(len(x)==2 for x in which)
assert len(set(which))==42
for i in range(42):
    for j in range(42):
        if i!=j:
            assert (j in A[i]) == bool(set(which[i])&set(which[j]))

# Distances (the line graph diameter is 5 while the Coxeter diameter is 4).
def distprofile(G,root):
    d={root:0};q=deque([root])
    while q:
        u=q.popleft()
        for v in G[u]:
            if v not in d:d[v]=d[u]+1;q.append(v)
    assert len(d)==len(G)
    return Counter(d.values())
assert all(tuple(distprofile(A,i)[j] for j in range(6))==(1,4,8,16,12,1)
           for i in range(42))
assert all(max(distprofile(C,i))==4 for i in range(28))
assert all(max(distprofile(Q,i))==4 for i in range(28))
# Coxeter graph girth seven, independently checked by deletion-and-BFS.
def girth(G):
    g=len(G)+1
    for a in range(len(G)):
        for b in G[a]:
            if b<a:continue
            d={a:0};q=deque([a])
            while q:
                u=q.popleft()
                for v in G[u]:
                    if {u,v}=={a,b}: continue
                    if v not in d:d[v]=d[u]+1;q.append(v)
            assert b in d
            g=min(g,d[b]+1)
    return g
assert girth(C)==7 and girth(Q)==7
print('OPTIMAL_MATCHINGS',len(opt))
print('EXCHANGE 42 vertices, 84 edges, 28 edge-disjoint triangles')
print('TRIANGLE_QUOTIENT',len(Q),'vertices',sum(map(len,Q))//2,'edges')
print('COXETER_IDENTIFICATION: triangle quotient = disjointness of nonline Fano triples')
print('EXCHANGE_GRAPH = LINE_GRAPH(COXETER_GRAPH)')
print('EXCHANGE_DISTANCE_PROFILE (1,4,8,16,12,1)')
print('VERIFY_COXETER_OK')
