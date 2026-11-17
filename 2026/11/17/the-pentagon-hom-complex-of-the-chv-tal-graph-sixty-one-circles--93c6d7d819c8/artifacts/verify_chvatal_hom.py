#!/usr/bin/env python3
"""Exhaustive polyhedral graph-Hom collapse and equivariant character check.

Requires only the Python 3 standard library. Run in the same directory as
collapse_pairs.json. The target graph is specified completely by EDGES.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
import json

EDGES = [(0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),
         (3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),
         (7,8),(7,11),(8,10),(9,10),(9,11)]
N = 12
adj = [0]*N
for u,v in EDGES:
    assert u!=v
    adj[u] |= (1<<v)
    adj[v] |= (1<<u)
assert all(x.bit_count()==4 for x in adj)

def elements(b):
    while b:
        low = b & -b
        yield low.bit_length()-1
        b ^= low

def allsubsets(b):
    sub=b
    while sub:
        yield sub
        sub=(sub-1)&b

def complete(A,B):
    return all((adj[u]&B)==B for u in elements(A))

def direct_cells():
    # Any set of colors appearing at one C5 vertex must lie within the
    # neighborhood of some color assigned at either source neighbor.
    states=sorted({a for n in adj for a in allsubsets(n)})
    nexts={a:[b for b in states if complete(a,b)] for a in states}
    out=set()
    def dfs(seq):
        if len(seq)==5:
            if complete(seq[-1],seq[0]):out.add(tuple(seq))
            return
        for b in (states if not seq else nexts[seq[-1]]):
            if len(seq)==4 and not complete(b,seq[0]):
                continue
            dfs(seq+[b])
    dfs([])
    return out, len(states)

def zero_cells():
    out=[]
    def dfs(seq):
        if len(seq)==5:
            if seq[0] in elements(adj[seq[-1]]):
                out.append(tuple(1<<x for x in seq))
            return
        options=range(N) if not seq else elements(adj[seq[-1]])
        for v in options:
            dfs(seq+[v])
    dfs([])
    return set(out)

def bfs_cells():
    starts=zero_cells()
    seen=set(starts)
    queue=deque(starts)
    while queue:
        a=queue.popleft()
        for i in range(5):
            nbs=(1<<N)-1
            for j in ((i-1)%5,(i+1)%5):
                for col in elements(a[j]):
                    nbs &= adj[col]
            for col in elements(nbs & ~a[i]):
                b=list(a)
                b[i] |= 1<<col
                b=tuple(b)
                if b not in seen:
                    seen.add(b)
                    queue.append(b)
    return seen

def d(c):return sum(a.bit_count()-1 for a in c)

def boundaries(c):
    for i,b in enumerate(c):
        if b.bit_count()>=2:
            for x in elements(b):
                a=list(c)
                a[i]&=~(1<<x)
                yield tuple(a)

def orientation(c,p):
    # Orient each product simplex by increasing target vertex indices.
    mapped=tuple(sum(1<<p[u] for u in elements(A)) for A in c)
    if mapped!=c:return 0
    sign=1
    for A in c:
        lst=[p[u] for u in elements(A)]
        inversions=sum(lst[i]>lst[j] for i in range(len(lst)) for j in range(i+1,len(lst)))
        if inversions%2:sign=-sign
    return sign

R=(1,5,11,6,0,4,7,10,9,2,3,8)
S=(0,4,3,2,1,5,9,8,7,6,11,10)
IDENTITY=tuple(range(12))
def compose(p,q):return tuple(p[q[u]] for u in range(N))
def permutation_group():
    group={IDENTITY}
    pending=[IDENTITY]
    while pending:
        p=pending.pop()
        for g in (R,S):
            q=compose(g,p)
            if q not in group:
                group.add(q);pending.append(q)
    assert len(group)==8
    assert compose(R,compose(R,compose(R,R)))==IDENTITY
    assert compose(S,S)==IDENTITY
    rinverse=compose(R,compose(R,R))
    assert compose(S,compose(R,S))==rinverse
    for p in group:
        assert set(tuple(sorted((p[a],p[b]))) for a,b in EDGES)==set(EDGES)
    return group

def all_automorphisms():
    # Exhaustive backtracking preserving adjacency and nonadjacency,
    # assigning each source vertex to a unique target vertex.
    def rec(mapping, used):
        if len(mapping)==N:
            yield tuple(mapping[i] for i in range(N))
            return
        choices=[]
        for u in range(N):
            if u in mapping:continue
            vals=[v for v in range(N) if v not in used and all(
                bool(adj[u]&(1<<x))==bool(adj[v]&(1<<mapping[x]))
                for x in mapping)]
            choices.append((len(vals),-sum(bool(adj[u]&(1<<x)) for x in mapping),u,vals))
        _,_,u,vals=min(choices)
        for v in vals:
            mapping[u]=v
            yield from rec(mapping,used|{v})
            del mapping[u]
    return set(rec({},set()))

def check():
    assert all(not (adj[a]&adj[b]) for a,b in EDGES)  # triangle-free
    assert all(adj[u]&(1<<v) for u,v in [(5,10),(10,6),(6,11),(11,5)])
    cells,state_count=direct_cells()
    assert cells==bfs_cells(), 'independent CW enumerators disagree'
    counts=Counter(d(c) for c in cells)
    assert dict(sorted(counts.items()))=={0:440,1:760,2:280,3:20}
    assert len(zero_cells())==440
    assert len(cells)==1500
    face={c:set(boundaries(c)) for c in cells}
    cover=defaultdict(set)
    for c, fs in face.items():
        for f in fs:
            assert f in cells
            cover[f].add(c)
    cert=json.loads(Path(__file__).with_name('collapse_pairs.json').read_text(encoding='utf-8'))
    assert len(cert)==280
    alive=set(cells)
    phase=Counter()
    for k,item in enumerate(cert):
        f=tuple(item[0]);g=tuple(item[1])
        assert f in alive and g in alive, ('repeat',k)
        assert f in face[g] and d(g)==d(f)+1, ('not facet',k)
        assert cover[f]&alive=={g}, ('not free',k)
        assert not cover[g]&alive, ('not maximal',k)
        phase[d(g)]+=1
        alive.remove(f);alive.remove(g)
    assert dict(phase)=={3:20,2:260}
    assert Counter(d(c) for c in alive)=={0:440,1:500}
    verts={c for c in alive if d(c)==0}
    edges={c for c in alive if d(c)==1}
    neighbors=defaultdict(set)
    for e in edges:
        v=[x for x in face[e] if d(x)==0]
        assert len(v)==2
        neighbors[v[0]].add(v[1]); neighbors[v[1]].add(v[0])
    start=next(iter(verts)); reached={start};queue=deque([start])
    while queue:
        v=queue.popleft()
        for u in neighbors[v]:
            if u not in reached:
                reached.add(u);queue.append(u)
    assert reached==verts
    rank=len(edges)-len(verts)+1
    assert rank==61
    group=permutation_group()
    assert group==all_automorphisms(), "dihedral action is not the full group"
    characters={}
    for p in group:
        tr=[sum(orientation(c,p) for c in cells if d(c)==j) for j in range(4)]
        chi=1-sum((-1)**j*tr[j] for j in range(4))
        characters[p]=chi
    # r^2 is the central involution. s and rs represent the two
    # reflection conjugacy classes.
    r2=compose(R,R);rs=compose(R,S)
    assert characters[IDENTITY]==61
    assert characters[R]==characters[compose(R,r2)]==characters[r2]==1
    assert characters[S]==characters[compose(r2,S)]==-9
    assert characters[rs]==characters[compose(r2,rs)]==1
    assert Counter(characters.values())=={61:1,1:5,-9:2}
    # D4 standard rational irreducible multiplicities:
    # A1, A2, B1, B2, E (s acts +1 on B1, -1 on B2)
    classes=(61,1,1,-9,1) # e,r^2,r and r^3,s and r^2s,rs and r^3s
    v=classes
    a1=(v[0]+v[1]+2*v[2]+2*v[3]+2*v[4])//8
    a2=(v[0]+v[1]+2*v[2]-2*v[3]-2*v[4])//8
    b1=(v[0]+v[1]-2*v[2]+2*v[3]-2*v[4])//8
    b2=(v[0]+v[1]-2*v[2]-2*v[3]+2*v[4])//8
    e=(2*v[0]-2*v[1])//8
    assert (a1,a2,b1,b2,e)==(6,10,5,10,15)
    assert a1+a2+b1+b2+2*e==61
    print(json.dumps({'status':'PASS','target_vertices':12,'target_edges':24,'target_automorphisms':len(group),'transfer_states':state_count,
       'homomorphisms':len(zero_cells()),'cw_cells':dict(sorted(counts.items())),
       'collapse_pairs':dict(sorted(phase.items())),'spine_vertices':len(verts),
       'spine_edges':len(edges),'spine_components':1,'spine_first_betti':rank,
       'dihedral_character_conjugacy_classes':classes,
       'dihedral_multiplicities':[a1,a2,b1,b2,e]},sort_keys=True))

if __name__=='__main__':check()
