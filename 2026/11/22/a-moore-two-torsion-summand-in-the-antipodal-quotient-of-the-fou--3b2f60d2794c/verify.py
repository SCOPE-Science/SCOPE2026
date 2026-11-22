#!/usr/bin/env python3
"""Exact integral certificate for the antipodal quotient of Ind(Q_4).

Requires only Python 3 standard library. All chain operations use integers.
All enumerations are exhaustive over the sixteen vertices of Q_4.
"""
from collections import Counter, defaultdict
from itertools import combinations
import heapq

N = 16
neighbors = [sum(1 << j for j in range(N) if (i ^ j).bit_count() == 1)
             for i in range(N)]
original = {s for s in range(1, 1 << N)
            if all(not (s & neighbors[i]) for i in range(N) if s & (1 << i))}
assert len(original) == 742
assert [sum(s.bit_count() == k for s in original) for k in range(1,9)] == [16,88,208,228,128,56,16,2]

def opposite(face):
    return sum(1 << (i ^ 15) for i in range(N) if face & (1 << i))

fixed = sorted((s for s in original if opposite(s) == s),
               key=lambda s: (-s.bit_count(),s))
assert len(fixed) == 30
# Each invariant face is an entire collection of opposite pairs, with all pairs
# in one of the two parity classes. The fixed-point space is two 3-simplices.
assert sorted(Counter(s.bit_count() for s in fixed).items()) == [(2,8),(4,12),(6,8),(8,2)]

# Simultaneous involution-equivariant stellar subdivisions of every invariant
# face, ordered by descending cardinality. Subdividing a face replaces every
# containing facet by cones from its new barycenter over all proper subsets.
facets = {s for s in original if all(s | (1 << j) not in original
                                     for j in range(N) if not (s & (1 << j)))}
permutation = {i:i^15 for i in range(N)}
for j, face in enumerate(fixed):
    assert any((facet & face)==face for facet in facets), "missing invariant face"
    fresh = set()
    for facet in facets:
        if facet & face != face:
            fresh.add(facet)
            continue
        rest = facet ^ face
        subset = (face-1) & face
        fresh.add(rest | (1 << (N+j)))
        while subset:
            fresh.add(rest | subset | (1 << (N+j)))
            subset = (subset-1) & face
    facets = fresh
    permutation[N+j] = N+j

all_faces = set()
for facet in facets:
    sub = facet
    while sub:
        all_faces.add(sub)
        sub = (sub-1) & facet
assert len(all_faces) == 24530
assert [sum(s.bit_count()==k for s in all_faces) for k in range(1,9)] == [46,420,1800,4488,6960,6592,3456,768]

def flip(face):
    ans = 0
    while face:
        b = face & -face
        ans |= 1 << permutation[b.bit_length()-1]
        face ^= b
    return ans

def orientation_flip(face):
    ordered = [permutation[i] for i in sorted(permutation) if face & (1 << i)]
    inversions = sum(ordered[i] > ordered[j]
                     for i in range(len(ordered)) for j in range(i+1,len(ordered)))
    return -1 if inversions & 1 else 1

assert all(flip(face) in all_faces for face in all_faces)
assert all(not (flip(face) == face and
                any(permutation[i] != i for i in permutation if face & (1 << i)))
           for face in all_faces), 'action has an inverted simplex'

# Since the refined action has no inversions, each face orbit is an honest
# quotient Delta-complex cell with signed cellular boundary obtained below.
cells = {min(face,flip(face)) for face in all_faces}
assert len(cells)==12414
assert [sum(s.bit_count()==k for s in cells) for k in range(1,9)]==[38,260,960,2268,3480,3296,1728,384]

boundaries = {}
occurrences = {}
cofaces = defaultdict(set)
for cell in cells:
    vertices = [i for i in permutation if cell & (1 << i)]
    counts = Counter()
    chain = Counter()
    for j,i in enumerate(vertices):
        face = cell ^ (1 << i)
        if not face:
            continue
        representative = min(face,flip(face))
        counts[representative] += 1
        sign = (-1 if j & 1 else 1) * (1 if representative==face
                                        else orientation_flip(face))
        chain[representative] += sign
        cofaces[representative].add(cell)
    occurrences[cell]=counts
    boundaries[cell]={face:c for face,c in chain.items() if c}

def assert_complex(d):
    for y, col in d.items():
        check=Counter()
        for x, coef in col.items():
            for w, c in d[x].items():
                check[w] += coef*c
        assert not any(check.values()), ('boundary squared', y, check)
assert_complex(boundaries)

# Genuine topological collapses: a lower cell is incident to a single higher
# cell and occurs exactly once in its attaching boundary. Store no external logs.
active=set(cells)
incidence={x:set(t) for x,t in cofaces.items()}
queue=[]
for x, higher in incidence.items():
    if len(higher)==1:
        y=next(iter(higher))
        if occurrences[y][x]==1:
            heapq.heappush(queue,(-x.bit_count(),x))
num_collapses=0
while queue:
    _, x = heapq.heappop(queue)
    if x not in active or len(incidence.get(x,()))!=1:
        continue
    y = next(iter(incidence[x]))
    if y not in active or occurrences[y][x]!=1:
        continue
    assert not incidence.get(y,set()), "free coface must be maximal"
    active.remove(x);active.remove(y)
    num_collapses+=1
    for z in (x,y):
        for lower in occurrences[z]:
            incidence[lower].discard(z)
            if lower in active and len(incidence[lower])==1:
                higher=next(iter(incidence[lower]))
                if occurrences[higher][lower]==1:
                    heapq.heappush(queue,(-lower.bit_count(),lower))
assert num_collapses==6100
assert len(active)==214
assert [sum(s.bit_count()==k for s in active) for k in range(1,5)]==[10,48,96,60]
D={cell:{f:c for f,c in boundaries[cell].items() if f in active} for cell in active}
assert_complex(D)

# Independent finite-field rank comparison on the 214-cell topological core.
def rank_mod(d, k, p):
    pivot={}
    for y in sorted(x for x in d if x.bit_count()==k+1):
        v={r:c%p for r,c in d[y].items() if c%p}
        while v:
            r=min(v)
            if r in pivot:
                b=pivot[r]; f=v[r]
                for a,c in b.items():
                    t=(v.get(a,0)-f*c)%p
                    if t:v[a]=t
                    else:v.pop(a,None)
            else:
                inv=pow(v[r],-1,p)
                pivot[r]={a:(c*inv)%p for a,c in v.items()}
                break
    return len(pivot)
assert [rank_mod(D,k,2) for k in (1,2,3)]==[9,39,56]
assert [rank_mod(D,k,3) for k in (1,2,3)]==[9,39,57]
assert [rank_mod(D,k,5) for k in (1,2,3)]==[9,39,57]

# Exact integer chain contractions. Pivots are ±1; no floating point and no
# modular inference is used for the integral Smith invariant.
current=set(active)
D={x:dict(v) for x,v in D.items()}
num_units=0
while True:
    co=defaultdict(list)
    for y in current:
        for x in D[y]:co[x].append(y)
    choices=[]
    for y in current:
        for x,u in D[y].items():
            if abs(u)==1:
                choices.append(((len(D[y])-1)*(len(co[x])-1),y,x,u))
    if not choices:
        break
    _,y,x,u=min(choices)
    for z in co[x]:
        if z==y:continue
        f=D[z][x]//u
        for a,c in D[y].items():
            new=D[z].get(a,0)-f*c
            if new:D[z][a]=new
            else:D[z].pop(a,None)
    for z in current:
        D[z].pop(y,None)
    current.remove(x);current.remove(y)
    D.pop(x);D.pop(y)
    num_units+=1
assert num_units==104 and len(current)==6
assert_complex(D)
assert [sum(c.bit_count()==k for c in current) for k in range(1,5)]==[1,0,1,4]
nonzero=[D[y] for y in current if D[y]]
assert len(nonzero)==2 and all(len(d)==1 and list(d.values())==[2] for d in nonzero)
# The final differential is [2,2,0,0] from C_3=Z^4 to C_2=Z.
# Its Smith factor is 2. Therefore H_2=Z/2, H_3=Z^3, H_0=Z.

# Independently certify simply connected original space by a Tietze reduction
# of the full presentation of pi_1 of the original 2-skeleton.
edges=sorted(tuple(i for i in range(N) if s & (1<<i)) for s in original if s.bit_count()==2)
triangles=sorted(tuple(i for i in range(N) if s & (1<<i)) for s in original if s.bit_count()==3)
parent=list(range(N))
def root(i):
    while parent[i]!=i:i=parent[i]
    return i
spanning=set()
for a,b in edges:
    if root(a)!=root(b):
        parent[root(a)]=root(b)
        spanning.add((a,b))
assert len(spanning)==15 and len(edges)==88
variables={e:i+1 for i,e in enumerate(e for e in edges if e not in spanning)}
def letter(a,b):
    if a<b:return variables.get((a,b),0)
    return -variables.get((b,a),0)
def freely_reduce(word):
    stack=[]
    for x in word:
        if stack and stack[-1]==-x:stack.pop()
        else:stack.append(x)
    while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
    return tuple(stack)
rels=[]
for a,b,c in triangles:
    w=freely_reduce(x for x in (letter(a,b),letter(b,c),letter(c,a)) if x)
    if w:rels.append(w)
remaining=set(variables.values())
num_tietze=0
while True:
    frequency=Counter(abs(x) for w in rels for x in w)
    options=[]
    for j,w in enumerate(rels):
        per=Counter(abs(x) for x in w)
        for g,c in per.items():
            if c==1:
                options.append(((len(w)-1)*(frequency[g]-1),len(w),j,g))
    if not options:break
    _,_,j,g=min(options)
    w=rels[j]
    pos=next(t for t,x in enumerate(w) if abs(x)==g)
    before=w[:pos];after=w[pos+1:]
    # Eliminate a generator occurring exactly once in one relator.
    substitute=tuple(-x for x in reversed(before))+tuple(-x for x in reversed(after)) if w[pos]>0 else after+before
    updated=[]
    for k,r in enumerate(rels):
        if k==j:continue
        out=[]
        for x in r:
            if abs(x)==g:
                out.extend(substitute if x>0 else [-z for z in reversed(substitute)])
            else:out.append(x)
        rr=freely_reduce(out)
        if rr:updated.append(rr)
    rels=updated
    remaining.remove(g)
    num_tietze+=1
assert num_tietze==73 and not remaining and not rels
# Since antipodal complementation fixes barycenters of invariant faces,
# Armstrong's orbit-space theorem applies: its normal fixed-point subgroup
# equals the full group C_2, hence pi_1 of the geometric quotient is trivial.

print('Q4_ANTIPODAL_INTEGRAL_QUOTIENT_VERIFIED')
print('original_faces=742 invariant_faces=30 refined_faces=24530')
print('orbit_cells=12414 genuine_collapses=6100 integral_unit_cancellations=104')
print('smith_factor=2 free_H3_rank=3 original_pi1_relator_eliminations=73')
print('homotopy_type=M(Z/2,2) wedge 3 S^3')
