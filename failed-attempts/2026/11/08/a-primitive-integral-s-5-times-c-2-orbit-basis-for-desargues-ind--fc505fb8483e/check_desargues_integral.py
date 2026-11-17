#!/usr/bin/env python3
"""Exact finite chain certificate for the integral homology lattice of an incidence-graph independence complex.
Standard Python 3 only; no network, no external packages.
"""
from itertools import combinations, permutations, product
from collections import Counter, deque

labels=range(5)
vertices=list(combinations(labels,2))+list(combinations(labels,3))
n=len(vertices)
by_vertex={v:i for i,v in enumerate(vertices)}
adj=[0]*n
for i,A in enumerate(vertices):
    for j,B in enumerate(vertices):
        if len(A)!=len(B) and (set(A)<set(B) or set(B)<set(A)):
            adj[i]|=1<<j
edges={(i,j) for i in range(n) for j in range(i+1,n) if adj[i]&(1<<j)}
assert n==20 and len(edges)==30

def bits(mask):
    while mask:
        b=mask&-mask
        yield b.bit_length()-1
        mask-=b

faces_by_size=[[] for _ in range(11)]
def gen(face,allowed):
    faces_by_size[face.bit_count()].append(face)
    while allowed:
        b=allowed&-allowed
        allowed-=b
        gen(face|b,allowed&~adj[b.bit_length()-1])
gen(0,(1<<n)-1)
counts=[len(x) for x in faces_by_size]
assert counts==[1,20,160,660,1510,1924,1320,480,115,20,2], counts
faces=set().union(*map(set,faces_by_size))
assert len(faces)==sum(counts)==6212

# A sequential vertex-toggle matching on the AUGMENTED face poset.
# Its acyclicity is checked directly on every oriented incidence, not assumed.
free=faces.copy()
pairs=[]
for v in range(n):
    for low in sorted(free):
        high=low|(1<<v)
        if not (low&(1<<v)) and high in free:
            free.remove(low)
            free.remove(high)
            pairs.append((low,high))
assert len(pairs)==3103
critical=Counter(m.bit_count()-1 for m in free)
assert critical=={-1:0, 4:1, 5:5} or critical=={4:1,5:5},critical
assert len(free)==6

# Orient each Hasse edge from higher to lower, except matched ones from lower to higher.
match=set(pairs)
face_order=sorted(faces)
face_index={a:i for i,a in enumerate(face_order)}
out=[[] for _ in face_order]
indeg=[0]*len(face_order)
nhasse=0
for high in face_order:
    for v in bits(high):
        low=high^(1<<v)
        if (low,high) in match: u,w=low,high
        else: u,w=high,low
        out[face_index[u]].append(face_index[w])
        indeg[face_index[w]]+=1
        nhasse+=1
q=deque(i for i,d in enumerate(indeg) if d==0)
visited=0
while q:
    k=q.popleft(); visited+=1
    for j in out[k]:
        indeg[j]-=1
        if indeg[j]==0:q.append(j)
assert visited==len(face_order), ('matching not acyclic', visited)

# Each fixed label i determines an induced disjoint union of six graph edges,
# joining A to A+{i} for all two-subsets A of the other four letters.
def pairs_for(i):
    return [(by_vertex[A],by_vertex[tuple(sorted(A+(i,)))])
            for A in combinations([j for j in labels if j!=i],2)]

def upper_or_lower_cycle(i):
    # An oriented cross-polytope fundamental cycle in reduced C_5.
    pairs_i=pairs_for(i)
    assert len(pairs_i)==6 and len({x for pair in pairs_i for x in pair})==12
    occupied=set(x for pair in pairs_i for x in pair)
    sub_edges={(a,b) for a in occupied for b in occupied if a<b and adj[a]&(1<<b)}
    assert sub_edges==set(pairs_i)
    chain={}
    for select in product((0,1),repeat=6):
        image=[pairs_i[k][select[k]] for k in range(6)]
        face=sum(1<<j for j in image)
        assert face in faces
        inversions=sum(image[a]>image[b] for a in range(6) for b in range(a+1,6))
        coefficient=(-1)**(sum(select)+inversions)
        chain[face]=coefficient
    assert len(chain)==64
    return chain
cycles=[upper_or_lower_cycle(i) for i in labels]

def boundary(chain):
    result={}
    for face,coefficient in chain.items():
        for k,v in enumerate(bits(face)):
            b=face^(1<<v)
            result[b]=result.get(b,0)+coefficient*(-1)**k
    return {k:v for k,v in result.items() if v}
for cycle in cycles:assert boundary(cycle)=={}

# Five primitive dual cocycles: a maximal 5-simplex supported on each octahedron
# and absent from all the other four octahedra.
facets=[]
for i in labels:
    a,b,c,d=[j for j in labels if j!=i]
    lower=[(a,b),(b,c),(c,d),(a,d)]
    upper=[tuple(sorted((a,c,i))),tuple(sorted((b,d,i)))]
    mask=sum(1<<by_vertex[tuple(sorted(A))] for A in lower+upper)
    assert mask in faces and mask.bit_count()==6
    assert not any(mask|(1<<j) in faces for j in range(n) if not mask&(1<<j))
    facets.append(mask)
assert len(set(facets))==5
pairing=[[cycle.get(facet,0) for cycle in cycles] for facet in facets]
assert all(pairing[i][j]==0 for i in range(5) for j in range(5) if i!=j)
assert all(abs(pairing[i][i])==1 for i in range(5))

# Every one of 120 label permutations acts on these integer chains WITHOUT a sign.
# Complementation acts by minus identity. These are exact chain equalities.
def send_chain(chain, vertex_image):
    new={}
    for face,coeff in chain.items():
        image=[vertex_image[v] for v in bits(face)]
        mm=sum(1<<v for v in image)
        inversions=sum(image[a]>image[b] for a in range(len(image)) for b in range(a+1,len(image)))
        new[mm]=new.get(mm,0)+((-1)**inversions)*coeff
    return {k:v for k,v in new.items() if v}
for sigma in permutations(labels):
    vmap=[by_vertex[tuple(sorted(sigma[j] for j in A))] for A in vertices]
    assert {tuple(sorted((vmap[a],vmap[b]))) for a,b in edges}==edges
    for i in labels:
        assert send_chain(cycles[i],vmap)==cycles[sigma[i]], (sigma,i)
complement=[by_vertex[tuple(j for j in labels if j not in A)] for A in vertices]
assert {tuple(sorted((complement[a],complement[b]))) for a,b in edges}==edges
for i in labels:
    assert send_chain(cycles[i],complement)=={mask:-v for mask,v in cycles[i].items()}

# The Morse bound gives at most five free generators in reduced degree five.
# The integral cocycle pairing is diagonal with units; hence these five cycles
# form a primitive integral basis of all of reduced H_5 (not just over Q).
print('DESARGUES_PRIMITIVE_INTEGRAL_ORBIT_PASS')
print('faces_by_cardinality=',counts)
print('graph_vertices_edges=',n,len(edges))
print('matched_pairs=',len(pairs),'critical_dimensions=',dict(critical))
print('oriented_hasse_arcs=',nhasse,'acyclic_topological_sort_visited=',visited)
print('induced_six_edge_matchings=',5,'sphere_cycle_terms_each=',64)
print('dual_facet_masks=',facets)
print('integral_pairing_matrix=',pairing)
print('permutation_actions_verified=',120*5,'complement_actions_verified=',5)
print('conclusion_H5_integral_S5_perm_5_times_C2_sign=True')
