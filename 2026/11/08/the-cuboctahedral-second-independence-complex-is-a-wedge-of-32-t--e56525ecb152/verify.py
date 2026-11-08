#!/usr/bin/env python3
"""Finite proof certificate for the second-independence complex of L(Q3).
Only the Python standard library is required. Deterministic labels and order.
"""
from collections import Counter,deque
from itertools import combinations
from hashlib import sha256
from pathlib import Path
import json

# Canonical cube vertices are binary words encoded by 0,...,7.
CUBE_EDGES = tuple((u,v) for u in range(8) for v in range(u+1,8) if (u^v).bit_count()==1)
assert len(CUBE_EDGES)==12
# Cuboctahedral graph L(Q3) has one vertex per cube edge.
N=[]
for i,(a,b) in enumerate(CUBE_EDGES):
    N.append(sum(1<<j for j,(c,d) in enumerate(CUBE_EDGES)
                 if i!=j and (a==c or a==d or b==c or b==d)))
assert len(set(N))==12 and all(x.bit_count()==4 for x in N)
assert sum(x.bit_count() for x in N)//2==24

def face(mask):
    """Every induced component has at most two vertices iff its degree is <=1."""
    for i in range(12):
        if mask & (1<<i) and (mask & N[i]).bit_count()>1:
            return False
    return True

F={m for m in range(1,1<<12) if face(m)}
assert len(F)==455
fvec=tuple(sum(m.bit_count()==k for m in F) for k in range(1,6))
assert fvec==(12,66,164,177,36),fvec
# Complete lower cover edges, without the empty simplex.
cover=[]
for upper in sorted(F):
    for i in range(12):
        if upper & (1<<i):
            lower=upper^(1<<i)
            if lower:
                assert lower in F
                cover.append((lower,upper))
assert len(cover)==sum(k*fvec[k-1] for k in range(2,6))

# Sequential lexicographic vertex toggles form a partial matching.
TOGGLE_ORDER=(9,8,10,2,5,0,4,7,6,11,3,1)
remaining=F.copy();pairs=[]
for i in TOGGLE_ORDER:
    bit=1<<i
    for lower in sorted(remaining):
        if lower & bit: continue
        upper=lower|bit
        if upper in remaining:
            assert lower in remaining
            remaining.remove(lower);remaining.remove(upper)
            pairs.append((lower,upper))
assert len(pairs)==211,len(pairs)
assert len(remaining)==33
assert sorted(Counter(m.bit_count()-1 for m in remaining).items())==[(0,1),(3,32)]
assert len({m for p in pairs for m in p})==2*len(pairs)
assert {m for p in pairs for m in p} | remaining == F
assert not ({m for p in pairs for m in p} & remaining)
matching=set(pairs)
assert matching <= set(cover)

# Acyclic matching: reverse matched lower->upper arrows;
# orient all other cover edges upper->lower, run full Kahn elimination.
adj={m:[] for m in F}; indeg={m:0 for m in F}
for low,high in cover:
    src,dst=(low,high) if (low,high) in matching else (high,low)
    adj[src].append(dst);indeg[dst]+=1
q=deque(sorted(m for m in F if indeg[m]==0))
removed=0; topological_order=[]
while q:
    m=q.popleft();removed+=1;topological_order.append(m)
    for nxt in adj[m]:
        indeg[nxt]-=1
        if indeg[nxt]==0:q.append(nxt)
assert removed==len(F), (removed,len(F))
certificate={
 "cube_edges":list(map(list,CUBE_EDGES)),
 "toggle_order":list(TOGGLE_ORDER),
 "matched_pairs":[list(p) for p in pairs],
 "critical_faces":sorted(remaining),
 "directed_topological_order":topological_order,
}
# Validate the committed combinatorial witness, not just printed statistics.
assert json.loads(Path(__file__).with_name("certificate.json").read_text(encoding="utf-8"))==certificate
# One critical 0-cell and exactly 32 critical 3-cells establish wedge of 32 3-spheres.
print('GRAPH cube_edges=12 cuboctahedral_vertices=12 cuboctahedral_edges=24')
print('FACE_COUNTS dimensions_0_to_4='+','.join(map(str,fvec)))
print('MATCHING pairs='+str(len(pairs))+' critical_0=1 critical_3=32')
print('FACE_POSET_COVERS '+str(len(cover)))
print('ACYCLIC_TOPOLOGICAL_ELIMINATION '+str(removed)+'/'+str(len(F)))
print('MATCHING_SHA256 '+sha256((';'.join(str(a)+','+str(b) for a,b in pairs)).encode()).hexdigest())
print('ALL_CUBOCTAHEDRAL_IND2_HOMOTOPY_CHECKS_PASS')
