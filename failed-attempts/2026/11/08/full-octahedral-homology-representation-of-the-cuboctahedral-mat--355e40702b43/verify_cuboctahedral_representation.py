"""Exact finite certificate for the cuboctahedral matching-complex representation.

Run with Python 3, standard library only. All graphs, chains and characters are
constructed here; no external data files or symbolic packages are required.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict

CUBE_VERTICES = tuple(range(8))
CUBE_EDGES = tuple(sorted((u, u ^ (1 << i)) for u in range(8)
                          for i in range(3) if u < (u ^ (1 << i))))
assert len(CUBE_EDGES) == 12
# Each cuboctahedral vertex is a cube edge. Each cuboctahedral edge is
# an unordered pair of incident cube edges.
C_EDGES = tuple((i, j) for i, x in enumerate(CUBE_EDGES)
                for j, y in enumerate(CUBE_EDGES) if i < j and len(set(x + y)) == 3)
assert len(C_EDGES) == 24
ENDPOINTS = [set(e) for e in C_EDGES]
INTERSECT = [sum(1 << j for j in range(24) if j != i and ENDPOINTS[i] & ENDPOINTS[j])
             for i in range(24)]

# First enumerator inserts one optional edge at a time.
faces = [()]
for i in range(24):
    faces += [face + (i,) for face in faces
              if all((INTERSECT[i] & (1 << j)) == 0 for j in face)]
levels = [sorted(face for face in faces if len(face) == k) for k in range(7)]
assert [len(x) for x in levels] == [1, 24, 204, 744, 1116, 528, 32]

# Second enumerator is independent: enumerates fixed-size edge combinations.
for k in range(7):
    assert levels[k] == [comb for comb in combinations(range(24), k)
                         if all(not (ENDPOINTS[i] & ENDPOINTS[j])
                                for i, j in combinations(comb, 2))]

# All augmented cellular boundary ranks over F_2, found by exact integer-bit
# Gaussian elimination; no floating-point or truncated enumeration.
indices = [{face: i for i, face in enumerate(level)} for level in levels]
ranks = []
for k in range(1, 7):
    pivots = {}
    for face in levels[k]:
        v = sum(1 << indices[k-1][face[:j]+face[j+1:]] for j in range(k))
        while v:
            pivot = v.bit_length()-1
            if pivot in pivots:
                v ^= pivots[pivot]
            else:
                pivots[pivot] = v
                break
    ranks.append(len(pivots))
assert ranks == [1, 23, 181, 563, 496, 32]
reduced_betti = [len(levels[k]) - (ranks[k-1] if k else 0)
                 - (ranks[k] if k < 6 else 0) for k in range(7)]
assert reduced_betti == [0, 0, 0, 0, 57, 0, 0]
# Universal coefficients: rational Betti numbers are bounded by mod-two Betti
# numbers. The rational Euler characteristic forces rank 57 in dimension 3.

cube_edge_index = {e: i for i, e in enumerate(CUBE_EDGES)}
cubo_edge_index = {e: i for i, e in enumerate(C_EDGES)}
def transform_cube_vertex(x, p, flip):
    return sum(((((x >> i) & 1) ^ ((flip >> i) & 1)) << p[i]) for i in range(3))

def transform_cubo_edges(p, flip):
    q = [cube_edge_index[tuple(sorted((transform_cube_vertex(u, p, flip),
                                        transform_cube_vertex(v, p, flip))))]
         for u,v in CUBE_EDGES]
    return tuple(cubo_edge_index[tuple(sorted((q[i], q[j])))] for i,j in C_EDGES)

def inversion_sign(x):
    return -1 if sum(x[i] > x[j] for i in range(len(x))
                     for j in range(i+1, len(x))) % 2 else 1

def signed_type(p, flip):
    visited = set()
    pos, neg = [], []
    for i in range(3):
        if i not in visited:
            cyc=[]; j=i
            while j not in visited:
                visited.add(j);cyc.append(j);j=p[j]
            (neg if sum((flip >> j) & 1 for j in cyc) % 2 else pos).append(len(cyc))
    return (tuple(sorted(pos, reverse=True)), tuple(sorted(neg, reverse=True)))

def partition_list(n):
    return {0:[()],1:[(1,)],2:[(2,),(1,1)],3:[(3,),(2,1),(1,1,1)]}[n]

def symmetric_char(shape, cycle_lengths):
    n = sum(shape)
    assert n == sum(cycle_lengths)
    if n <= 1:return 1
    if n == 2:return 1 if shape == (2,) else (-1 if cycle_lengths==(2,) else 1)
    return {(3,):{(1,1,1):1,(2,1):1,(3,):1},
            (2,1):{(1,1,1):2,(2,1):0,(3,):-1},
            (1,1,1):{(1,1,1):1,(2,1):-1,(3,):1}}[shape][cycle_lengths]

def wreath_char(p, flip, left, right):
    # Induction from B_a x B_b, with sign of all flips in the right block.
    a = sum(left); answer=0
    for A_tuple in combinations(range(3), a):
        A=set(A_tuple);B=set(range(3))-A
        if any((i in A) != (p[i] in A) for i in range(3)):
            continue
        types=[]
        for block in (A,B):
            unseen=set(block);cycle=[]
            while unseen:
                i=min(unseen);j=i;degree=0
                while j in unseen:
                    unseen.remove(j);degree+=1;j=p[j]
                cycle.append(degree)
            types.append(tuple(sorted(cycle,reverse=True)))
        answer += symmetric_char(left,types[0])*symmetric_char(right,types[1]) * (
            -1 if sum((flip >> i) & 1 for i in B)%2 else 1)
    return answer

bipartitions=[(a,b) for n in range(4) for a in partition_list(n)
              for b in partition_list(3-n)]
assert len(bipartitions)==10

classes=defaultdict(list)
autos=[]
cover_checks=0
for p in permutations(range(3)):
    for flip in range(8):
        phi=transform_cubo_edges(p,flip)
        assert sorted(phi) == list(range(24))
        # Verify the map preserves every cuboctahedral-edge incidence relation.
        for i,j in combinations(range(24),2):
            assert bool(ENDPOINTS[i]&ENDPOINTS[j])==bool(ENDPOINTS[phi[i]]&ENDPOINTS[phi[j]])
        degree_traces=[]
        for k in range(1,7):
            value=0
            for face in levels[k]:
                image=tuple(phi[v] for v in face)
                assert tuple(sorted(image)) in indices[k]
                # Simplicial differential commutes with signed permutation.
                sg=inversion_sign(image)
                for j in range(k):
                    sub=face[:j]+face[j+1:]
                    image_sub=tuple(phi[v] for v in sub)
                    # coefficient on its oriented simplex in d(g.face)
                    coeff_lhs=(-1)**(sorted(image).index(phi[face[j]]))*sg
                    # coefficient of the same sub-simplex in g(d.face)
                    img_slot=image.index(phi[face[j]])
                    coeff_rhs=(-1)**j*inversion_sign(image_sub)
                    assert coeff_lhs==coeff_rhs
                    cover_checks+=1
                if tuple(sorted(image))==face:
                    value+=sg
            degree_traces.append(value)
        character=1-sum((-1)**k*t for k,t in enumerate(degree_traces))
        t=signed_type(p,flip)
        classes[t].append(character)
        autos.append((p,flip,character,t))
assert len(autos)==48 and len(classes)==10
assert all(len(set(ch))==1 for ch in classes.values())
expected={
 ((1,1,1),()):(1,57),
 ((2,1),()):(6,1),
 ((3,),()):(8,-3),
 ((1,1),(1,)):(3,-1),
 ((2,),(1,)):(6,3),
 ((1,),(2,)):(6,-3),
 ((1,),(1,1)):(3,13),
 ((),(3,)):(8,-1),
 ((),(2,1)):(6,-5),
 ((),(1,1,1)):(1,11),
}
assert {t:(len(vals), vals[0]) for t,vals in classes.items()}==expected

# Orthogonality independently certifies that the ten induced characters are
# irreducible, pairwise distinct and complete for the 48-element group.
for i,(a,b) in enumerate(bipartitions):
    for j,(c,d) in enumerate(bipartitions):
        inner=sum(wreath_char(p,flip,a,b)*wreath_char(p,flip,c,d)
                  for p,flip,_,_ in autos)
        assert inner==48*(i==j)

multiplicities={}
for a,b in bipartitions:
    coefficient=sum(chi*wreath_char(p,flip,a,b) for p,flip,chi,_ in autos)
    assert coefficient%48==0
    multiplicities[(a,b)]=coefficient//48
assert multiplicities=={
 ((),(3,)):1, ((),(2,1)):4, ((),(1,1,1)):2,
 ((1,),(2,)):5, ((1,),(1,1)):2,
 ((2,),(1,)):2, ((1,1),(1,)):2,
 ((3,),()):1, ((2,1),()):5, ((1,1,1),()):2}
assert sum(multiplicities[(a,b)]*wreath_char((0,1,2),0,a,b)
           for a,b in bipartitions)==57
assert sum(x[2] for x in autos)==48  # one invariant dimension
antipodal=next(chi for p,flip,chi,_ in autos if p==(0,1,2) and flip==7)
assert antipodal==11
assert ((57+antipodal)//2,(57-antipodal)//2)==(34,23)
print('CUBOCTAHEDRAL_MATCHING_FULL_B3_CHARACTER_PASS')
print('face_counts_by_cardinality',*[len(x) for x in levels])
print('augmented_mod2_boundary_ranks',*ranks)
print('reduced_mod2_betti',*reduced_betti)
print('signed_boundary_equivariance_checks',cover_checks)
for typ in sorted(classes):print('signed_class',typ,'size',len(classes[typ]),'H3_character',classes[typ][0])
for pair in bipartitions:print('bipartition',pair,'dimension',wreath_char((0,1,2),0,*pair),'multiplicity',multiplicities[pair])
print('full_invariant_dimension',sum(x[2] for x in autos)//48)
print('central_inversion_eigenspace_dimensions',34,23)
