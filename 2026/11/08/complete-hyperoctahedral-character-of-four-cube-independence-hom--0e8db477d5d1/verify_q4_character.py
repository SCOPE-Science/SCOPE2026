#!/usr/bin/env python3
"""Exact finite verification of four-cube independence homology symmetries.

Uses only Python's standard library. Every face, cover and symmetry is generated
from the graph definition; no precomputed data file or external certificate is needed.
"""
from itertools import permutations
from collections import Counter, deque

D = 4
V = 1 << D
neighbors = [sum(1 << (v ^ (1 << j)) for j in range(D)) for v in range(V)]
faces = [mask for mask in range(1, 1 << V)
         if all((neighbors[v] & mask) == 0
                for v in range(V) if mask & (1 << v))]
face_set = set(faces)
assert len(face_set) == 742
assert [sum(m.bit_count() == k for m in faces) for k in range(1, 9)] == [16,88,208,228,128,56,16,2]

# The fixed-order vertex toggle is a matching on a partition of the face poset.
# Acyclicity is checked independently below on the entire oriented Hasse diagram.
unused = set(faces)
match = set()
pivot_counts = []
for pivot in range(V):
    pairs = [(m, m | (1 << pivot)) for m in sorted(unused)
             if not (m & (1 << pivot)) and (m | (1 << pivot)) in unused]
    assert len({x for a,b in pairs for x in (a,b)}) == 2*len(pairs)
    for a, b in pairs:
        assert a in unused and b in unused and a.bit_count()+1 == b.bit_count()
        unused.remove(a); unused.remove(b)
        match.add((a,b))
    pivot_counts.append(len(pairs))
assert len(match) == 367
assert Counter(m.bit_count()-1 for m in unused) == {0:1,3:7}
assert sorted(unused) == [1,1680,2400,10370,17028,24600,33064,33096]
assert pivot_counts == [176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1]

# For each cover (lower, upper), orient upper -> lower except matched
# incidences, which are reversed. A successful full topological sort
# certifies absence of directed cycles.
out = {m: [] for m in faces}
indeg = {m: 0 for m in faces}
covers = 0
for upper in faces:
    for v in range(V):
        if upper & (1 << v):
            lower = upper & ~(1 << v)
            if not lower: continue
            assert lower in face_set
            src,dst = (lower,upper) if (lower,upper) in match else (upper,lower)
            out[src].append(dst)
            indeg[dst]+=1
            covers+=1
assert covers == 2816
queue = deque(sorted(m for m in faces if indeg[m] == 0))
visited = 0
while queue:
    m = queue.popleft();visited+=1
    for v in out[m]:
        indeg[v]-=1
        if indeg[v]==0: queue.append(v)
assert visited==len(faces), 'Morse matching is cyclic'

# Complete signed reduced Lefschetz trace. A simplex is fixed setwise,
# but contributes the sign of the induced permutation on its vertices.
# Since Morse shows Htilde is concentrated in dimension 3, character = -Ltilde.
perms=list(permutations(range(D)))
all_chars={}
for p in perms:
    parity_p = (-1)**sum(p[i]>p[j] for i in range(D) for j in range(i+1,D))
    fixed = [i for i in range(D) if p[i] == i]
    for shift in range(V):
        action = tuple((sum(((v >> i) & 1) << p[i] for i in range(D)) ^ shift)
                       for v in range(V))
        reduced_lefs = -1  # empty simplex, dimension -1
        for face in faces:
            inds = [v for v in range(V) if (face >> v) & 1]
            image = [action[v] for v in inds]
            if sum(1<<v for v in image) != face:
                continue
            inversions = sum(image[i] > image[j] for i in range(len(image))
                             for j in range(i+1,len(image)))
            reduced_lefs += (-1)**(len(inds)-1 + inversions)
        trace = -reduced_lefs
        predicted = parity_p * (len(fixed)-1 + sum(
            (-1)**((shift & (15 ^ (1<<i))).bit_count()) for i in fixed))
        assert trace == predicted, (p,shift,trace,predicted)
        all_chars[(p,shift)] = trace
assert len(all_chars)==384
assert Counter(all_chars.values())=={1:188,-1:161,-3:24,3:6,5:4,7:1}

# Restriction to the normal translation subgroup: Fourier multiplicities
# m_a=1/16 sum_t chi(t)(-1)^{a.t}. This detects a three-dimensional
# zero-weight summand and one copy of each weight-3 character.
idp=tuple(range(D))
mult={a:sum(all_chars[idp,s] * (-1)**((a&s).bit_count())
            for s in range(V)) // V for a in range(V)}
assert mult == {a: (3 if a==0 else 1 if a.bit_count()==3 else 0)
                for a in range(V)}

# Averaging over translations projects onto the inflated sign-twisted
# standard S4 module; the complementary weight-three orbit has the
# sign-twisted signed-permutation character on four coordinates.
for p in perms:
    signp=(-1)**sum(p[i]>p[j] for i in range(D) for j in range(i+1,D))
    fixed=sum(i==p[i] for i in range(D))
    invariant_trace=sum(all_chars[p,s] for s in range(V))
    assert invariant_trace == 16 * signp*(fixed-1)
assert sum(all_chars.values()) == 0  # no full automorphism invariants
print('FOUR_CUBE_INDEPENDENCE_B4_CHARACTER_PASS')
print('faces=742 hasse_covers=2816 matched_pairs=367 critical=1x0+7x3')
print('automorphisms=384 character_multiplicities='+str(sorted(Counter(all_chars.values()).items())))
print('translation_Fourier_weights=3xtrivial+4xweight3 each once')
print('rational_modules=sign_S4_tensor_standard3 + sign_S4_tensor_weight3_monimial4')
print('full_symmetry_invariant_dimension=0')
