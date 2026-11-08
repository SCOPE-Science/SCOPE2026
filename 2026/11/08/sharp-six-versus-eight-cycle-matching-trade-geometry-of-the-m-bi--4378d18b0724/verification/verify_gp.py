"""Exhaustive independent vertex-subset and cycle enumeration for GP(8,3).
Run: python3 verify_gp.py. Requires Python 3.9+, standard library only.
"""
from collections import Counter, deque
from itertools import combinations

def edge(a,b): return (min(a,b),max(a,b))
V=tuple(range(16)); A={v:set() for v in V}
E=set()
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        E.add(edge(a,b));A[a].add(b);A[b].add(a)
assert len(E)==24 and all(len(A[v])==3 for v in V)

# First enumerator: recursively saturate the least remaining vertex.
matching_set=set()
def extend(remaining,m):
    if not remaining:
        matching_set.add(frozenset(m));return
    a=min(remaining)
    for b in sorted(A[a]&remaining):
        extend(remaining-{a,b},m+(edge(a,b),))
extend(frozenset(V),())
M=sorted(matching_set,key=lambda s:tuple(sorted(s)))
assert len(M)==33
idx={m:i for i,m in enumerate(M)}

def cycles(n):
    found=set()
    def dfs(p):
        if len(p)==n:
            if p[0] in A[p[-1]]:
                found.add(frozenset(edge(a,b) for a,b in zip(p,p[1:]+p[:1])))
            return
        for b in sorted(A[p[-1]]-set(p)):
            if b>p[0]: dfs(p+[b])
    for a in V:
        for b in sorted(A[a]):
            if b>a: dfs([a,b])
    return found
C6=cycles(6);C8=cycles(8)
assert len(C6)==24 and len(C8)==30

def adj_from_flips(C):
    out=[set() for _ in M]
    for i,m in enumerate(M):
        for c in C:
            if len(m&c)*2!=len(c):continue
            new=m^c
            assert new in idx and len(new)==8
            out[i].add(idx[new])
    assert all(i in out[j] for i,neigh in enumerate(out) for j in neigh)
    return out

def components(adj):
    parts=[];left=set(range(len(adj)))
    while left:
        start=min(left); seen={start};q=[start]
        while q:
            for v in adj[q.pop()]-seen:seen.add(v);q.append(v)
        parts.append(seen);left-=seen
    return sorted(parts,key=lambda s:(-len(s),min(s)))

def metric(adj,expected_parts):
    comps=components(adj)
    assert tuple(sorted(map(len,comps)))==expected_parts
    pair_dist=Counter(); ecc=Counter()
    for comp in comps:
        if len(comp)==1: continue
        for u in sorted(comp):
            ds={u:0};q=deque([u])
            while q:
                x=q.popleft()
                for v in adj[x]:
                    if v not in ds:ds[v]=ds[x]+1;q.append(v)
            assert set(ds)==comp
            ecc[max(ds.values())]+=1
            pair_dist.update({k:sum(1 for v,d in ds.items() if u<v and d==k) for k in set(ds.values())})
    return pair_dist,ecc

S=adj_from_flips(C6);O=adj_from_flips(C8)
B=[S[i]|O[i] for i in range(len(M))]
assert sum(map(len,S))//2==96 and sum(map(len,O))//2==36
assert all(not(S[i]&O[i]) for i in range(33))
assert sum(map(len,B))//2==132
assert Counter(map(len,S))=={0:3,6:24,8:6}
assert Counter(map(len,O))=={1:24,2:6,12:3}
assert Counter(map(len,B))=={7:24,10:6,12:3}

# Complementary 2-factor cycle types distinguish the three intrinsic classes.
def complement_type(m):
    H={v:set(A[v]) for v in V}
    for a,b in m:H[a].remove(b);H[b].remove(a)
    unseen=set(V);lengths=[]
    while unseen:
        u=min(unseen);q=[u];comp={u}
        while q:
            for w in H[q.pop()]-comp:comp.add(w);q.append(w)
        assert all(len(H[v])==2 for v in comp)
        lengths.append(len(comp));unseen-=comp
    return tuple(sorted(lengths))
types=Counter(complement_type(m) for m in M)
assert types=={(6,10):24,(16,):6,(8,8):3}
for i,m in enumerate(M):
    t=complement_type(m)
    assert (len(S[i]),len(O[i]))=={(6,10):(6,1),(16,):(8,2),(8,8):(0,12)}[t]

# Octagon-only graph: each leaf attaches to exactly one of 3 hubs; each of 6
# degree-2 vertices subdivides an edge of the doubled triangle on these hubs.
hubs={i for i in range(33) if len(O[i])==12}
mids={i for i in range(33) if len(O[i])==2}
leaves={i for i in range(33) if len(O[i])==1}
assert (len(hubs),len(mids),len(leaves))==(3,6,24)
assert all(O[v]<=hubs for v in mids|leaves)
assert all(len(O[h]&leaves)==8 and len(O[h]&mids)==4 for h in hubs)
assert Counter(frozenset(O[v]) for v in mids)=={frozenset(p):2 for p in combinations(sorted(hubs),2)}

assert metric(S,(1,1,1,30))==(Counter({1:96,2:216,3:120,4:3}),Counter({3:24,4:6}))
assert metric(O,(33,))==(Counter({1:36,2:198,3:54,4:240}),Counter({3:3,4:30}))
assert metric(B,(33,))==(Counter({1:132,2:342,3:54}),Counter({3:33}))
print('PASS_GP_VERTEX_RECURSION_33_MATCHINGS')
print('PASS_ALL_24_HEXAGONS_AND_30_OCTAGONS')
print('PASS_6_CYCLE_3_ISOLATES_PLUS_30_COMPONENT_RADIUS3_DIAMETER4')
print('PASS_8_CYCLE_DOUBLED_TRIANGLE_SUBDIVISION_AND_24_LEAVES')
print('PASS_BOTH_132_EDGES_SELF_CENTERED_DIAMETER3')
print('PASS_COMPLEMENT_TYPES_3_6_24_AND_EXACT_PAIR_DISTRIBUTIONS')
