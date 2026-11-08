#!/usr/bin/env python3
"""Self-contained checks for the total 3-cut complex of the truncated tetrahedral graph."""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations

PAIRS = tuple((i,j) for i in range(4) for j in range(4) if i != j)
N = len(PAIRS)
FULL = (1 << N) - 1
EDGES = frozenset((i,j) for i,j in combinations(range(N),2)
                  if PAIRS[i][0] == PAIRS[j][0] or PAIRS[i] == PAIRS[j][::-1])
ADJ = tuple(sum(1 << j for j in range(N) if (min(i,j),max(i,j)) in EDGES and i!=j)
            for i in range(N))
independent_triples = tuple(sum(1 << i for i in S)
                            for S in combinations(range(N),3)
                            if all(not ((i,j) in EDGES) for i,j in combinations(S,2)))
facets = tuple(FULL ^ t for t in independent_triples)
# Two logically distinct face tests: contained in a generating facet; complement independence >= 3
faces_a = frozenset(m for m in range(1 << N) if any(m & f == m for f in facets))
def is_face_b(m):
    remaining = FULL ^ m
    for i,j,k in combinations([i for i in range(N) if remaining & (1 << i)],3):
        if not ((ADJ[i] & (1 << j)) or (ADJ[i] & (1 << k)) or (ADJ[j] & (1 << k))):
            return True
    return False
faces_b = frozenset(m for m in range(1 << N) if is_face_b(m))
assert len(EDGES)==18 and len(independent_triples)==72 and faces_a == faces_b
FACES = faces_a
DIM_COUNTS = dict(sorted(Counter(m.bit_count()-1 for m in FACES).items()))

def match(order):
    unpaired = set(FACES)
    paired = {}
    pairs = 0
    for v in order:
        bit = 1 << v
        for lower in sorted(unpaired, key=lambda t:(t.bit_count(),t)):
            upper = lower | bit
            if not lower & bit and lower in unpaired and upper in unpaired:
                paired[lower]=upper
                unpaired.remove(lower)
                unpaired.remove(upper)
                pairs+=1
    # Directed covering relation: unmatched upper->lower, matched lower->upper.
    indegree={s:0 for s in FACES}
    adj=defaultdict(list)
    arrows=0
    for upper in FACES:
        for i in range(N):
            bit=1<<i
            if not upper & bit:continue
            lower=upper ^ bit
            if paired.get(lower)==upper: src,dst=lower,upper
            else:src,dst=upper,lower
            adj[src].append(dst)
            indegree[dst]+=1
            arrows+=1
    queue=deque(x for x,d in indegree.items() if d==0)
    visited=0
    while queue:
        a=queue.popleft();visited+=1
        for b in adj[a]:
            indegree[b]-=1
            if indegree[b]==0:queue.append(b)
    assert visited==len(FACES), (visited,len(FACES))
    critical=Counter(s.bit_count()-1 for s in unpaired)
    assert critical=={6:6} and (pairs,arrows)==(1834, sum(m.bit_count() for m in FACES))
    assert 0 not in unpaired
    return pairs,arrows,critical,visited

fwd=match(range(N))
rev=match(range(N-1,-1,-1))
# Full S_4 symmetry: a permutation of four triangle labels induces vertex permutation.
classes=defaultdict(list)
def partition(p):
    seen=set(); out=[]
    for i in range(4):
        if i in seen:continue
        j=i;k=0
        while j not in seen:
            seen.add(j);j=p[j];k+=1
        out.append(k)
    return tuple(sorted(out, reverse=True))

def sign_of_permutation(indices):
    return (-1) ** sum(indices[i] > indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))

def fixed_face_reduced_lefschetz(p):
    induced=[PAIRS.index((p[i],p[j])) for i,j in PAIRS]
    s=0
    for mask in FACES:
        ix=[i for i in range(N) if mask & (1<<i)]
        transformed=[induced[i] for i in ix]
        if all(mask & (1<<j) for j in transformed):
            sign=sign_of_permutation(transformed)
            s+=(-1 if len(ix)%2==0 else 1)*sign
    return s
for p in permutations(range(4)):
    classes[partition(p)].append(fixed_face_reduced_lefschetz(p))
assert {c:len(set(v)) for c,v in classes.items()}=={c:1 for c in classes}
chars={c:v[0] for c,v in classes.items()}
assert chars=={(1,1,1,1):6,(2,1,1):-2,(2,2):2,(3,1):0,(4,):0},chars
# Character rows of the five irreducible S_4 modules, by cycle type.
char_table={
    'trivial':{(1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1},
    'sign':{(1,1,1,1):1,(2,1,1):-1,(2,2):1,(3,1):1,(4,):-1},
    'standard':{(1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1},
    'standard_sign':{(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1},
    'two_two':{(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0},
}
mult={name:sum(len(classes[c])*chars[c]*row[c] for c in classes)//24 for name,row in char_table.items()}
assert mult=={'trivial':0,'sign':1,'standard':0,'standard_sign':1,'two_two':1},mult
assert sum((-1)**d * num for d,num in DIM_COUNTS.items())==6
print('TRUNCATED_TETRAHEDRON_TOTAL_THREE_CUT_VERIFIED')
print('vertex_labels:', PAIRS)
print('undirected_edges:',len(EDGES),'independent_triples:',len(independent_triples))
print('face_count_including_empty:',len(FACES),'by_dimension:',DIM_COUNTS)
print('forward:',fwd,'reverse:',rev)
print('reduced_Lefschetz_traces:',{str(c):chars[c] for c in sorted(chars)})
print('S4_irreducible_multiplicities:',mult)
print('reduced_homotopy_type: wedge of 6 copies of S^6')
