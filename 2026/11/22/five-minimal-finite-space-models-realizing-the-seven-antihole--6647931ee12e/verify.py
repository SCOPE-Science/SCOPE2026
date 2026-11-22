#!/usr/bin/env python3
"""Exact finite combinatorial checks for seven-antihole inseparability witnesses.
Run using only Python 3 standard library: python3 verify.py
"""
from itertools import combinations
from collections import Counter, deque
import json
N=7
V=range(N)
H={frozenset((i,j)) for i,j in combinations(V,2) if (i-j)%N not in (1,N-1)}
triangles={frozenset(t) for t in combinations(V,3) if all(frozenset(e) in H for e in combinations(t,2))}
assert len(H)==14 and len(triangles)==7
T={j:frozenset((j,(j+2)%N,(j+4)%N)) for j in V}
assert set(T.values())==triangles
long={j:frozenset((j,(j+4)%N)) for j in V}
for j in V:
    assert [t for t in triangles if long[j]<=t]==[T[j]]
    assert all(sum(long[k]<=t for k in V)<=1 for t in triangles)
for i in V:
    e=frozenset((i,(i+2)%N))
    assert {j for j in V if e<=T[j]}=={i,(i-2)%N}
closed={i:{i}|{j for j in V if frozenset((i,j)) in H} for i in V}
assert all(len(closed[i])==5 for i in V)
assert len({frozenset(x) for x in closed.values()})==N
assert all(not(closed[i]<=closed[j]) for i,j in combinations(V,2))
valid=[]
for mask in range(1<<N):
    S=frozenset(i for i in V if mask>>i&1)
    cover=all(i in S or (i-2)%N in S for i in V)
    minima={j:{j,(j+4)%N}|({(j+2)%N} if j in S else set()) for j in V}
    edges={frozenset((i,k)) for i,k in combinations(V,2) if any({i,k}<=upper for upper in minima.values())}
    assert (edges==H)==cover
    if not cover: continue
    valid.append(S)
    assert all(2<=len(u)<=3 for u in minima.values())
    incidence_edges={(j,i) for j,u in minima.items() for i in u}
    assert len(incidence_edges)==14+len(S)
    adj={('m',j):[] for j in V}|{('x',i):[] for i in V}
    for j,i in incidence_edges:
        adj['m',j].append(('x',i));adj['x',i].append(('m',j))
    seen={('m',0)};q=deque(seen)
    while q:
        for t in adj[q.popleft()]:
            if t not in seen:seen.add(t);q.append(t)
    assert len(seen)==14
    assert len(incidence_edges)-14+1==len(S)+1
cnt=Counter(map(len,valid)); assert dict(cnt)=={4:7,5:14,6:7,7:1}
def act(S,a,b):
    return frozenset((a*i+b)%N for i in S)
# The dihedral permutations of the seven long-edge positions have affine forms.
# Compute induced maps directly from automorphisms on the x-vertex C7 to avoid mistaken indices.
group=[]
for sign in (1,-1):
    for shift in V:
        trans={j: next(k for k in V if long[k]==frozenset(((sign*i+shift)%N for i in long[j]))) for j in V}
        assert {frozenset(((sign*i+shift)%N for i in T[j])) for j in V}==triangles
        assert frozenset(((sign*i+shift)%N for i in T[j])) == T[trans[j]]
        group.append(trans)
assert len(group)==14
unseen=set(valid);orbits=[]
while unseen:
    S=min(unseen,key=lambda z:tuple(sorted(z)))
    orb={frozenset(g[i] for i in S) for g in group}
    assert orb<=unseen or not orb.isdisjoint(unseen)
    assert orb<=set(valid)
    unseen-=orb
    orbits.append((S,orb))
assert sorted((len(s),len(o)) for s,o in orbits)==[(4,7),(5,7),(5,7),(6,7),(7,1)]
results={
  'graph_vertices':7, 'graph_edges':len(H),'triangles':[sorted(t) for t in sorted(triangles,key=lambda a:sorted(a))],
  'forced_long_edges':{str(j):sorted(v) for j,v in long.items()},
  'valid_labeled_relations':len(valid), 'count_by_optional_incidence_count':dict(sorted(cnt.items())),
  'dihedral_isomorphism_types':len(orbits),
  'orbit_representatives':[{'optional_indices':sorted(S),'orbit_size':len(orb),'total_incidence_edges':14+len(S), 'circle_wedge_rank':len(S)+1} for S,orb in sorted(orbits,key=lambda so:(len(so[0]),sorted(so[0])))],
  'checks':['unique triangle per distance-three edge','distance-two edges covered exactly by neighboring triangles','closed-neighborhood incomparability','all 128 optional subsets checked','29 valid cases connected','dihedral orbit partition']
}
print(json.dumps(results,sort_keys=True,indent=2))
