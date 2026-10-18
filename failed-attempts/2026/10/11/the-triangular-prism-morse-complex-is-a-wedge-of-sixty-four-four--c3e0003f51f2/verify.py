#!/usr/bin/env python3
from collections import defaultdict, deque

VERTICES = tuple(range(6))
EDGES = ((0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5))
# A primitive vector field is (tail, edge_index, head), representing (tail, edge).
PRIMITIVES = []
for ei,(a,b) in enumerate(EDGES):
    PRIMITIVES.append((a,ei,b))
    PRIMITIVES.append((b,ei,a))
N = len(PRIMITIVES)
TOGGLE_ORDER = (4,2,8,1,7,12,13,11,6,3,14,15,0,9,17,16,5,10)
PROTECTED_SINGLETON = 1  # primitive index 0

def valid(mask):
    tails=set(); used_edges=set(); out={v:[] for v in VERTICES}
    for i,(tail,ei,head) in enumerate(PRIMITIVES):
        if (mask>>i)&1:
            if tail in tails or ei in used_edges:
                return False
            tails.add(tail); used_edges.add(ei); out[tail].append(head)
    state=[0]*len(VERTICES)
    def dfs(v):
        state[v]=1
        for w in out[v]:
            if state[w]==1:
                return False
            if state[w]==0 and not dfs(w):
                return False
        state[v]=2
        return True
    return all(state[v] or dfs(v) for v in VERTICES)

def gf2_rank(columns):
    piv={}; rank=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x; rank+=1; break
    return rank

faces=[]; bydim=defaultdict(list)
for mask in range(1,1<<N):
    if valid(mask):
        faces.append(mask)
        bydim[mask.bit_count()-1].append(mask)
face_set=set(faces)
assert N==18
assert [len(bydim[d]) for d in range(5)] == [18,126,428,705,450]
assert len(faces)==1727

unmatched=set(faces); pairs=[]
for i in TOGGLE_ORDER:
    bit=1<<i
    for f in sorted(tuple(unmatched), key=lambda z:(z.bit_count(),z)):
        if f not in unmatched or (f & bit):
            continue
        g=f|bit
        if g in unmatched and g in face_set:
            if f==PROTECTED_SINGLETON or g==PROTECTED_SINGLETON:
                continue
            unmatched.remove(f); unmatched.remove(g); pairs.append((f,g))

critical=defaultdict(int)
for f in unmatched:
    critical[f.bit_count()-1]+=1
assert len(pairs)==831
assert dict(critical)=={0:1,4:64}
assert unmatched.__contains__(PROTECTED_SINGLETON)

# Full Hasse-diagram acyclicity check. Unmatched covers point upward; matched covers are reversed.
pairset=set(pairs)
adj=defaultdict(list); indeg={f:0 for f in faces}; covers=0
for hi in faces:
    if hi.bit_count()<=1: continue
    for i in range(N):
        if (hi>>i)&1:
            lo=hi^(1<<i)
            if lo in face_set:
                covers+=1
                if (lo,hi) in pairset:
                    u,v=hi,lo
                else:
                    u,v=lo,hi
                adj[u].append(v); indeg[v]+=1
q=deque(f for f,d in indeg.items() if d==0); seen=0
while q:
    u=q.popleft(); seen+=1
    for v in adj[u]:
        indeg[v]-=1
        if indeg[v]==0: q.append(v)
assert covers==6606
assert seen==len(faces)

# Independent reduced mod-2 homology check.
ranks={}
for d in range(1,5):
    lows=bydim[d-1]; low_index={f:i for i,f in enumerate(lows)}; cols=[]
    for hi in bydim[d]:
        col=0
        for i in range(N):
            if (hi>>i)&1:
                lo=hi^(1<<i)
                if lo in low_index:
                    col ^= 1<<low_index[lo]
        cols.append(col)
    ranks[d]=gf2_rank(cols)
assert ranks=={1:17,2:109,3:319,4:386}
betti=[]
for d in range(5):
    ker=(len(bydim[0])-1) if d==0 else len(bydim[d])-ranks[d]
    im=ranks.get(d+1,0)
    betti.append(ker-im)
assert betti==[0,0,0,0,64]

chi=sum(((-1)**d)*len(bydim[d]) for d in range(5))
assert chi==65
print('VERIFY_OK')
print('graph=triangular_prism')
print('vertices=6 edges=9 primitives=18')
print('faces=1727 f_vector=18,126,428,705,450')
print('hasse_covers=6606 matched_pairs=831 critical_0=1 critical_4=64')
print('directed_hasse_toposort=1727 acyclic=True')
print('gf2_boundary_ranks=d1:17,d2:109,d3:319,d4:386')
print('reduced_gf2_betti=0,0,0,0,64')
print('euler_characteristic=65')
