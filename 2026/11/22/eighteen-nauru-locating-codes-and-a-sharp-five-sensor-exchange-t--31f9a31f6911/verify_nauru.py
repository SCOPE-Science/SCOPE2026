"""Self-contained exact proof checker for the minimum locating-dominating code classification on GP(12,5)."""
from itertools import combinations
from collections import Counter
from collections import deque

N=12
V=2*N
edges=set()
for i in range(N):
    edges.add(tuple(sorted((i,(i+1)%N))))
    edges.add((i,i+N))
    edges.add(tuple(sorted((i+N,((i+5)%N)+N))))
assert len(edges)==36
adj=[0]*V
for u,v in edges:
    adj[u]|=1<<v;adj[v]|=1<<u
assert all(x.bit_count()==3 for x in adj)

def ld(s):
    seen=set()
    for v in range(V):
        if s>>v & 1: continue
        signature=adj[v]&s
        if not signature or signature in seen:return False
        seen.add(signature)
    return True

def mask(seq):return sum(1<<v for v in seq)

# Secondary cross-check on the four-outer/four-inner candidate class.
# This restriction alone is not a proof of completeness; the separately
# supplied check_all_masks.cpp exhausts EVERY subset of size at most eight.
opt=set()
for outer in combinations(range(N),4):
    om=mask(outer)
    for inner in combinations(range(N,2*N),4):
        s=om|mask(inner)
        if ld(s):opt.add(s)
assert len(opt)==18, len(opt)

# Intrinsic closed-form two-orbit description.
A=set()
for i in range(N):
    A.add(mask([(i+j)%N for j in (4,6,9,11)]+[N+(i+j)%N for j in (0,1,2,3)]))
B=set()
for r in range(3):
    for t in range(3):
        if r!=t:
            B.add(mask([i for i in range(N) if i%3==r]+[N+i for i in range(N) if i%3==t]))
assert len(A)==12 and len(B)==6 and opt==A|B

# Pair-intersection spectrum and simultaneous optimum-preserving move graph.
pairs=Counter((s&t).bit_count() for s,t in combinations(opt,2))
assert pairs=={0:27,2:36,3:72,4:18},pairs
L=list(sorted(opt))
for q,expected in [(1,(18,0,1)),(2,(18,0,1)),(3,(18,0,1)),(4,(3,18,6)),(5,(1,90,18))]:
    neigh=[set() for _ in L]
    for i,j in combinations(range(len(L)),2):
        if (L[i]&L[j]).bit_count()>=8-q:
            neigh[i].add(j);neigh[j].add(i)
    unseen=set(range(18));components=[]
    while unseen:
        start=unseen.pop();que=[start];comp=[start]
        for v in que:
            for w in neigh[v]&unseen:
                unseen.remove(w);comp.append(w);que.append(w)
        components.append(comp)
    assert (len(components),sum(map(len,neigh))//2,max(map(len,components)))==expected
    if q==4:assert sorted(map(len,components))==[6,6,6] and all(len(neigh[v])==2 for v in range(18))
    if q==5:
        assert all(len(neigh[v])==10 for v in range(18))
        for src in range(18):
            dist={src:0};que=deque([src])
            while que:
                v=que.popleft()
                for w in neigh[v]:
                    if w not in dist:dist[w]=dist[v]+1;que.append(w)
            assert len(dist)==18 and max(dist.values())==2

# Every optimum is independent, and its double-covered bipartite core is two 8-cycles.
for s in opt:
    assert all(not(adj[u]&s) for u in range(V) if s>>u&1)
    signature_counts=Counter((adj[v]&s).bit_count() for v in range(V) if not(s>>v&1))
    assert signature_counts=={1:8,2:8}
    core=set(i for i in range(V) if s>>i&1)
    core|={v for v in range(V) if not (s>>v&1) and (adj[v]&s).bit_count()==2}
    assert len(core)==16
    remaining=set(core);cycle_lengths=[]
    while remaining:
        start=remaining.pop();front=[start];size=1
        for u in front:
            assert len([v for v in range(V) if v in core and adj[u]>>v&1])==2
            for v in core:
                if v in remaining and (adj[u]>>v&1):
                    remaining.remove(v);front.append(v);size+=1
        cycle_lengths.append(size)
    assert sorted(cycle_lengths)==[8,8]

# Explicit automorphism bridging the cyclic families; rotation and reflection
# separately preserve all edges and move transitively within each family.
bridge=[4,5,17,12,0,1,13,20,8,9,21,16,3,6,22,19,11,2,18,15,7,10,14,23]
assert sorted(bridge)==list(range(V))
assert all(tuple(sorted((bridge[u],bridge[v]))) in edges for u,v in edges)
def pimage(s,p):return mask(p[v] for v in range(V) if s>>v&1)
A0=mask([j for j in (4,6,9,11)]+[N+j for j in (0,1,2,3)])
B01=mask([i for i in range(N) if i%3==0]+[N+i for i in range(N) if i%3==1])
assert pimage(A0,bridge)==B01
def rotate(s,t):return mask([N*(v//N)+(v%N+t)%N for v in range(V) if s>>v&1])
def reflect(s):return mask([N*(v//N)+(-(v%N))%N for v in range(V) if s>>v&1])
assert A==set(rotate(A0,t) for t in range(N))
assert B==set(rotate(x,t) for x in [B01,reflect(B01)] for t in range(N))


print('VERIFY_OK 245025_BALANCED_CANDIDATES 18_MINIMUM_CODES 3C6_THRESHOLD4 CONNECTED_THRESHOLD5_DIAMETER2')
