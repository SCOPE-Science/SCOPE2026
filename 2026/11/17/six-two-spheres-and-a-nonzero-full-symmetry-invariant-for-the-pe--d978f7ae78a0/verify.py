#!/usr/bin/env python3
"""Exact combinatorial verification for the pentagonal-antiprism perfect-matching complex."""
import collections
import hashlib
import itertools
import json
from functools import lru_cache

N=10
EDGES=sorted({tuple(sorted((i,(i+d)%N))) for i in range(N) for d in (1,2)})
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}

def perfect_matchings(remaining, selected=0):
    if not remaining:
        yield selected
        return
    a=min(remaining)
    for b in sorted(remaining-{a}):
        key=(min(a,b),max(a,b))
        if key in EDGE_INDEX:
            yield from perfect_matchings(remaining-{a,b},selected|(1<<EDGE_INDEX[key]))

FACETS=sorted(set(perfect_matchings(set(range(N)))))
FACES={0}
for facet in FACETS:
    bits=[1<<i for i in range(len(EDGES)) if facet>>i&1]
    for size in range(1,len(bits)+1):
        for sub in itertools.combinations(bits,size):
            FACES.add(sum(sub))
NONEMPTY=FACES-{0}
assert len(EDGES)==20 and len(FACETS)==22 and len(NONEMPTY)==457
# Cross-check against the ordinary (not necessarily extendible) matching complex.
ordinary_counts=collections.Counter()
for size in range(1,6):
    for indices in itertools.combinations(range(len(EDGES)),size):
        endpoints=[v for i in indices for v in EDGES[i]]
        if len(set(endpoints))==2*size:
            ordinary_counts[size-1]+=1
assert [ordinary_counts[d] for d in range(5)]==[20,130,310,225,22]
assert collections.Counter(f.bit_count()-1 for f in NONEMPTY)=={0:20,1:115,2:190,3:110,4:22}
# Pair every still-unmatched face with the face adding the present pivot edge.
UNMATCHED=set(NONEMPTY)
PAIRS=[]
for pivot in range(len(EDGES)-1,-1,-1):
    mask=1<<pivot
    for face in sorted(UNMATCHED,key=lambda f:(f.bit_count(),f)):
        if face & mask:
            continue
        larger=face|mask
        if larger in UNMATCHED:
            UNMATCHED.remove(face)
            UNMATCHED.remove(larger)
            PAIRS.append((face,larger))
CRITICAL=sorted(UNMATCHED)
assert len(PAIRS)==224 and len(CRITICAL)==9
assert collections.Counter(f.bit_count()-1 for f in CRITICAL)=={0:1,1:1,2:7}
assert len({f for p in PAIRS for f in p})==448
# Orient each Hasse cover downward except the matched covers, which point upward.
LOWER_TO_UPPER={a:b for a,b in PAIRS}
UPPER_TO_LOWER={b:a for a,b in PAIRS}
indegree={f:0 for f in NONEMPTY}
arcs={f:[] for f in NONEMPTY}
cover_count=0
for upper in NONEMPTY:
    for i in range(len(EDGES)):
        if not (upper>>i&1):
            continue
        lower=upper^(1<<i)
        if lower not in NONEMPTY:
            continue
        cover_count+=1
        a,b=(lower,upper) if UPPER_TO_LOWER.get(upper)==lower else (upper,lower)
        arcs[a].append(b)
        indegree[b]+=1
queue=collections.deque(f for f in NONEMPTY if indegree[f]==0)
removed=0
while queue:
    face=queue.popleft()
    removed+=1
    for other in arcs[face]:
        indegree[other]-=1
        if indegree[other]==0:
            queue.append(other)
assert removed==len(NONEMPTY), 'Matching is not acyclic'

def simplicial_boundary(face):
    ids=[i for i in range(len(EDGES)) if face>>i&1]
    return {face^(1<<i):(-1)**j for j,i in enumerate(ids)}

# Compute the Morse degree-2 to degree-1 boundary by following every gradient path.
@lru_cache(None)
def edge_expansion(edge):
    if edge in UNMATCHED:
        return {edge:1}
    if edge not in LOWER_TO_UPPER:
        return {} # Paired with a vertex, hence not critical in degree one.
    triangle=LOWER_TO_UPPER[edge]
    assert triangle.bit_count()==3
    boundary=simplicial_boundary(triangle)
    coefficient=boundary.pop(edge)
    out=collections.defaultdict(int)
    for other,sign in boundary.items():
        for c,v in edge_expansion(other).items():
            out[c]-=coefficient*sign*v
    return {k:v for k,v in out.items() if v}

critical_edges=[x for x in CRITICAL if x.bit_count()==2]
critical_triangles=[x for x in CRITICAL if x.bit_count()==3]
assert len(critical_edges)==1
MORSE_BOUNDARY=[]
for triangle in critical_triangles:
    out=collections.defaultdict(int)
    for edge,sign in simplicial_boundary(triangle).items():
        for c,v in edge_expansion(edge).items():
            out[c]+=sign*v
    MORSE_BOUNDARY.append(out[critical_edges[0]])
assert sorted(MORSE_BOUNDARY)==[-1,-1,-1,0,0,0,0], MORSE_BOUNDARY

# Dihedral edge permutations and signed fixed-face Lefschetz traces.
def edge_permutation(k,eps):
    perm=[]
    for u,v in EDGES:
        a,b=(eps*u+k)%N,(eps*v+k)%N
        perm.append(EDGE_INDEX[(min(a,b),max(a,b))])
    assert len(set(perm))==20
    return perm

def reduced_lefschetz(k,eps):
    perm=edge_permutation(k,eps)
    total=-1 # The augmented empty face in degree -1.
    for face in NONEMPTY:
        ids=[i for i in range(len(EDGES)) if face>>i&1]
        mapped=[perm[i] for i in ids]
        if set(ids)!=set(mapped):
            continue
        inversions=sum(mapped[i]>mapped[j] for i in range(len(ids)) for j in range(i+1,len(ids)))
        total+=(-1)**(len(ids)-1+inversions)
    return total
ROTATIONS=[reduced_lefschetz(k,1) for k in range(N)]
REFLECTIONS=[reduced_lefschetz(k,-1) for k in range(N)]
assert ROTATIONS==[6,-1,1,-1,1,4,1,-1,1,-1]
assert REFLECTIONS==[2,0,2,0,2,0,2,0,2,0]
assert sum(ROTATIONS+REFLECTIONS)==20

out={
  'graph':'C_10 squared (pentagonal antiprism)',
  'edges':len(EDGES),'perfect_matchings':len(FACETS),
  'nonempty_face_count':len(NONEMPTY),
  'ordinary_matching_face_counts':[ordinary_counts[d] for d in range(5)],
  'face_counts_by_dimension':{str(k):v for k,v in sorted(collections.Counter(f.bit_count()-1 for f in NONEMPTY).items())},
  'hasse_covers_checked':cover_count,
  'matched_pairs':len(PAIRS),
  'acyclic_hasse_nodes_visited':removed,
  'critical_face_counts':{str(k):v for k,v in sorted(collections.Counter(f.bit_count()-1 for f in CRITICAL).items())},
  'critical_edges':critical_edges,
  'critical_triangles':critical_triangles,
  'morse_degree2_to_degree1_coefficients':MORSE_BOUNDARY,
  'betti2_integral':6,'other_reduced_integral_homology':'zero',
  'dihedral_rotations':ROTATIONS,'dihedral_reflections':REFLECTIONS,
  'full_dihedral_rational_invariant_rank':sum(ROTATIONS+REFLECTIONS)//20,
}
if __name__=='__main__':
    print(json.dumps(out,sort_keys=True,indent=2))
    # Readable certificate digest from the whole pair list and critical faces.
    certificate={'edges':EDGES,'perfect_matching_masks':FACETS,'morse_pairs':PAIRS,'critical_masks':CRITICAL,'critical_boundary_2_to_1':MORSE_BOUNDARY}
    with open(__file__.replace('verify.py','MORSE_CERTIFICATE.json'),'w',encoding='utf8') as fh:
        json.dump(certificate,fh,sort_keys=True,separators=(',',':'),ensure_ascii=False)
        fh.write('\n')
    with open(__file__.replace('verify.py','SYMMETRY_TABLE.json'),'w',encoding='utf8') as fh:
        json.dump({'rotations':ROTATIONS,'reflections':REFLECTIONS,'irreducible_complex_decomposition':{'trivial':1,'rotation_sign_reflection_positive':1,'rho_2':1,'rho_4':1}},fh,sort_keys=True,separators=(',',':'))
        fh.write('\n')
