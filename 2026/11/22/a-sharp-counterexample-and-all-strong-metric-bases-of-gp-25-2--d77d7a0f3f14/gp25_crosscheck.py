"""Independent verification of GP(25,2) strong metric bases using small orbit searches."""
from collections import deque
from itertools import combinations, product
N=25
adj=[set() for _ in range(2*N)]
def add(a,b): adj[a].add(b); adj[b].add(a)
for i in range(N):
    add(i,(i+1)%N)
    add(i,N+i)
    add(N+i,N+(i+2)%N)

def bfs(s):
    ds=[-1]*(2*N);ds[s]=0;q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if ds[v]<0:ds[v]=ds[u]+1;q.append(v)
    return ds
D=[bfs(v) for v in range(2*N)]
M={(a,b) for a in range(2*N) for b in range(a+1,2*N)
  if max(D[w][b] for w in adj[a])<=D[a][b]
  and max(D[a][w] for w in adj[b])<=D[a][b]}
assert len(M)==175

def independent(vals,off):
    return all((min(a,b)+off,max(a,b)+off) not in M for a,b in combinations(vals,2))
# Translation fixes one vertex at 0. The possible other independent vertices
# are exactly those not MMD with 0.
allowed=[i for i in range(1,N) if independent((0,i),0)]
assert allowed == [1,2,3,4,6,8,10,15,17,19,21,22,23,24]
anchored6=[(0,)+t for t in combinations(allowed,5) if independent((0,)+t,0)]
anchored7=[(0,)+t for t in combinations(allowed,6) if independent((0,)+t,0)]
assert len(anchored6)==6 and not anchored7
U={frozenset((a+2*j)%N for j in range(6)) for a in range(N)}
assert len(U)==25
assert all(independent(u,0) for u in U)
assert {frozenset(t) for t in anchored6}=={u for u in U if 0 in u}
# Five vertex-disjoint 5-cycles for the inner MMD graph.
cycles=[[(x+5*j)%N for x in (0,9,18,2,11)] for j in range(5)]
assert sorted(v for c in cycles for v in c)==list(range(N))
choices=[]
for c in cycles:
    assert all((min(c[i],c[(i+1)%5])+N,max(c[i],c[(i+1)%5])+N) in M for i in range(5))
    opts=[p for p in combinations(c,2) if independent(p,N)]
    assert len(opts)==5
    choices.append(opts)
V={frozenset(v for p in parts for v in p) for parts in product(*choices)
  if independent([v for p in parts for v in p],N)}
assert len(V)==5
assert V=={frozenset(i for i in range(N) if i%5 in (b,(b+2)%5)) for b in range(5)}
# A direct all-pairs strong-resolution test, not relying on a reduction theorem.
for u in U:
    for v in V:
        S=set(range(2*N))-{*u,*[N+j for j in v]}
        assert len(S)==34
        for a in range(2*N):
            for b in range(a+1,2*N):
                assert any(D[w][a]==D[w][b]+D[a][b]
                           or D[w][b]==D[w][a]+D[a][b] for w in S)
print('MMD edges',len(M),'anchored outer six',len(anchored6),
      'anchored outer seven',len(anchored7),'outer maxima',len(U),
      'inner maxima',len(V),'strong metric bases',len(U)*len(V))
