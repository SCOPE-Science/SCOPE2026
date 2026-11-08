#!/usr/bin/env python3
"""Reconstruct the out-neighborhood complex of the 11-vertex Paley tournament.

Enumerates all subsets, certifies an acyclic face matching, independent mod-two
homology, and the signed Lefschetz character of the affine automorphism group.
Requires only the Python standard library.
"""
from collections import Counter, defaultdict
from itertools import combinations

N = 11
Q = frozenset((x*x)%N for x in range(1,N))
assert Q == frozenset((1,3,4,5,9))

# 11 maximal out-neighborhood simplices
blocks = [sum(1 << ((v + q)%N) for q in Q) for v in range(N)]
assert len(set(blocks)) == N
for i,j in combinations(range(N),2):
    assert (blocks[i]&blocks[j]).bit_count()==2
    assert sum(((block >> i)&1) and ((block >> j)&1) for block in blocks)==2
# Independent enumeration of all 2**11 subsets: the common-predecessor predicate.
faces_a = {0}
for mask in range(1,1<<N):
    if any((mask & block)==mask for block in blocks):
        faces_a.add(mask)
faces_b = {0}
for block in blocks:
    sub = block
    while sub:
        faces_b.add(sub)
        sub = (sub-1)&block
assert faces_a == faces_b
assert all(sum((mask & block)==mask for block in blocks)==1
           for mask in faces_a if mask.bit_count()>=3)
faces=faces_a-{0}
by_dim = defaultdict(list)
for f in faces:
    by_dim[f.bit_count()-1].append(f)
for d in by_dim:by_dim[d].sort()
fvec=[len(by_dim[d]) for d in range(5)]
assert fvec == [11,55,110,55,11]

# Greedy elementary acyclic matching with fixed vertex order.
# A pair consists of an unmatched face and its one-vertex extension.
def matching(order):
    waiting=set(faces)
    pairs=[]
    for v in order:
        bit=1<<v
        for small in sorted(waiting, key=lambda f:(f.bit_count(),f)):
            large=small|bit
            if small in waiting and not small&bit and large in waiting:
                waiting.remove(small)
                waiting.remove(large)
                pairs.append((small,large))
    return waiting,pairs

def is_acyclic(pairs):
    reversed_pairs=set(pairs)
    degree=dict.fromkeys(faces,0)
    outgoing=defaultdict(list)
    incidences=0
    for big in faces:
        if big.bit_count()==1:continue
        for v in range(N):
            if big & (1<<v):
                small=big^(1<<v)
                assert small in faces
                source,target=(small,big) if (small,big) in reversed_pairs else (big,small)
                outgoing[source].append(target)
                degree[target]+=1
                incidences+=1
    zero=[v for v in degree if degree[v]==0]
    visited=0
    while zero:
        current=zero.pop();visited+=1
        for w in outgoing[current]:
            degree[w]-=1
            if degree[w]==0:zero.append(w)
    return visited==len(faces),incidences,visited

for order in (range(N),range(N-1,-1,-1)):
    critical,pairs=matching(order)
    ok,incidences,visited=is_acyclic(pairs)
    assert ok and incidences==715 and len(pairs)==110
    assert Counter(f.bit_count()-1 for f in critical)==Counter({0:1,2:21})
print('faces_by_dimension:',fvec)
print('two_independent_face_enumerations: AGREE')
print('distinct_blocks:',len(blocks),'pairwise_block_intersection:',2)
print('matching_pairs_per_order:',110,'critical_cells:',{0:1,2:21})
print('acyclicity_incidence_arcs:',incidences,'acyclicity_check: PASS (both orders)')

# Independent mod-two ranks on full simplicial chains.
def mod2_rank(bitcols):
    pivot={}
    for col in bitcols:
        while col:
            k=col.bit_length()-1
            if k in pivot:col^=pivot[k]
            else:
                pivot[k]=col
                break
    return len(pivot)

ranks={0:0,5:0}
for d in range(1,5):
    prev_index={face:i for i,face in enumerate(by_dim[d-1])}
    bitcols=[]
    for face in by_dim[d]:
        col=0
        for v in range(N):
            if face & (1<<v):
                col^=1<<prev_index[face^(1<<v)]
        bitcols.append(col)
    ranks[d]=mod2_rank(bitcols)
assert [ranks[d] for d in range(1,5)]==[10,45,44,11]
betti=[len(by_dim[d])-ranks[d]-ranks[d+1]-(d==0) for d in range(5)]
assert betti == [0,0,21,0,0]
print('mod2_boundary_ranks:',[ranks[d] for d in range(1,5)])
print('mod2_reduced_betti:',betti)

# The 55 affine maps preserve the Paley orientation and simplices.
def perm_sign(seq):
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return (-1)**(inv%2)
char_distribution=Counter()
trace_by_type={}
for a in sorted(Q):
    for b in range(N):
        mapping=[(a*v+b)%N for v in range(N)]
        assert len(set(mapping))==N
        assert {sum(1<<mapping[v] for v in range(N) if block & (1<<v)) for block in blocks}==set(blocks)
        chain_trace={}
        for d in range(5):
            contribution=0
            for face in by_dim[d]:
                vertices=[v for v in range(N) if face & (1<<v)]
                mapped=[mapping[v] for v in vertices]
                if set(vertices)==set(mapped):
                    contribution+=perm_sign(mapped)
            chain_trace[d]=contribution
        reduced_lefschetz=sum((-1)**d*chain_trace[d] for d in range(5))-1
        # Only nonzero reduced homology is in degree 2, so this is its character.
        typ='identity' if (a,b)==(1,0) else ('translation' if a==1 else 'nontranslation_affine')
        expected={'identity':21,'translation':-1,'nontranslation_affine':1}[typ]
        assert reduced_lefschetz==expected
        trace_by_type[typ]=expected
        char_distribution[(typ,expected)]+=1
assert char_distribution==Counter({('identity',21):1,('translation',-1):10,('nontranslation_affine',1):44})
print('affine_h2_character_distribution:',dict(sorted(char_distribution.items())))
print('invariant_rational_dimension:',(21+10*(-1)+44*1)//55)
print('rational_affine_module: trivial plus two copies of the rational 10-dimensional cyclotomic module')
print('ALL_CHECKS_PASS')
