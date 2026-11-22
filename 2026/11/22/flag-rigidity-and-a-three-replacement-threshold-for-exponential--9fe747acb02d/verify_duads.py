"""Finite, exact check of exponential domination of the Tutte-Coxeter Levi graph.
Run: python3 verify_duads.py ; standard library only.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, permutations

SYMBOLS=tuple(range(6))
DUADS=list(combinations(SYMBOLS,2))
DID={d:i for i,d in enumerate(DUADS)}
def partitions(rest):
    if not rest:
        yield ()
        return
    a=rest[0]
    for b in rest[1:]:
        for t in partitions(tuple(x for x in rest[1:] if x!=b)):
            yield ((a,b),)+t
SYNTHEMES=list(partitions(SYMBOLS))
SID={frozenset(m):j for j,m in enumerate(SYNTHEMES)}
N=30
adj=[set() for _ in range(N)]
for j,m in enumerate(SYNTHEMES):
    for d in m:
        i=DID[d]
        adj[i].add(15+j);adj[15+j].add(i)
assert len(DUADS)==len(SYNTHEMES)==15
assert all(len(x)==3 for x in adj)
assert sum(map(len,adj))//2==45

def bfs(root,ignored=frozenset()):
    if root in ignored:return {}
    dist={root:0};q=deque([root])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if w not in ignored and w not in dist:
                dist[w]=dist[v]+1;q.append(w)
    return dist
D=[bfs(i) for i in range(N)]
assert set(map(len,D))=={N}
assert max(max(d.values()) for d in D)==4
assert all(Counter(d.values())=={0:1,1:3,2:6,3:12,4:8} for d in D)

def porous(S):
    T=set(S)
    return all(sum(1<<(4-D[u][s]) for s in S)>=8 for u in range(N) if u not in T)

counts={};minima=[]
for k in range(5):
    feasible=[tuple(S) for S in combinations(range(N),k) if porous(S)]
    counts[k]=len(feasible)
    if k==4:minima=feasible
assert counts=={0:0,1:0,2:0,3:0,4:45},counts

# Every flag (incident duad i, syntheme j) gives a 4-set:
# the other two points on j, and the other two lines through i.
flags={}
for i in range(15):
    for j in sorted(adj[i]):
        S=tuple(sorted((adj[j]-{i})|(adj[i]-{j})))
        assert len(S)==4 and sum(x<15 for x in S)==2
        flags[S]=(i,j)
assert len(flags)==45
assert set(minima)==set(flags)

def weight(u,S):
    val=Fraction(0)
    for s in S:
        dist=bfs(u,frozenset(S)-{s}).get(s)
        if dist is not None:val+=Fraction(2,2**dist)
    return val
histograms=[]
for S in minima:
    w=Counter(weight(u,S) for u in range(N) if u not in S)
    assert sum(w.values())==26
    assert min(w)>=1
    histograms.append(w)
assert all(w==Counter({Fraction(9,8):16,Fraction(21,16):8,Fraction(3):2}) for w in histograms)

# Under symbol permutations, the 45 flags form a single orbit.
representative=minima[0]
images=set()
for p in permutations(SYMBOLS):
    pm=[]
    for d in DUADS:pm.append(DID[tuple(sorted((p[d[0]],p[d[1]])))])
    for m in SYNTHEMES:
        pm.append(15+SID[frozenset(tuple(sorted((p[a],p[b]))) for a,b in m)])
    images.add(tuple(sorted(pm[v] for v in representative)))
assert images==set(minima)

# k simultaneous exchanges means replacing at most k of the four selected vertices.
M=len(minima)
shared=[[len(set(minima[i])&set(minima[j])) for j in range(M)] for i in range(M)]
assert max(shared[i][j] for i in range(M) for j in range(M) if i!=j)==1
edges3=[(i,j) for i in range(M) for j in range(i+1,M) if shared[i][j]>=1]
assert len(edges3)==450
R=[set() for _ in range(M)]
for i,j in edges3:R[i].add(j);R[j].add(i)
assert set(map(len,R))=={20}
rd=[]
for i in range(M):
    dist={i:0};q=deque([i])
    while q:
        v=q.popleft()
        for w in R[v]:
            if w not in dist:dist[w]=dist[v]+1;q.append(w)
    assert len(dist)==M
    rd.append(max(dist.values()))
assert set(rd)=={2}
print('PASS: n=30, cubic, diameter 4; porous cardinalities',counts)
print('PASS: exactly 45 nonporous optimal 4-sets, all indexed by point-line flags')
print('PASS: weight histogram: 16*9/8, 8*21/16, 2*3 on every four-set')
print('PASS: one symbol-permutation orbit; no exchanges of <=2, 450 edges for 3, 20-regular, diameter 2')
