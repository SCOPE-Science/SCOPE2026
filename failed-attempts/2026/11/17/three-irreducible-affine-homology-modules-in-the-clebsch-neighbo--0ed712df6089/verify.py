#!/usr/bin/env python3
"""Exact finite verification for the rational homology character of the Clebsch open-neighborhood complex.

Python 3 standard library only. All arithmetic is integral.
"""
from itertools import combinations, permutations
from collections import Counter, defaultdict
from fractions import Fraction

V = tuple(x for x in range(32) if x.bit_count() % 2 == 0)
S = tuple(31 ^ (1 << j) for j in range(5))
neighbor = {x: frozenset(x ^ a for a in S) for x in V}
assert len(V) == 16 and len(set(S)) == 5
assert all(x not in neighbor[x] and len(neighbor[x]) == 5 for x in V)
assert all((y in neighbor[x]) == (x in neighbor[y]) for x in V for y in V)
assert sum(len(v) for v in neighbor.values()) == 80

# Strongly regular parameters, checked without specialized graph libraries.
for i, x in enumerate(V):
    for y in V[i+1:]:
        common = len(neighbor[x] & neighbor[y])
        assert common == (0 if y in neighbor[x] else 2)

face_set = set()
for x in V:
    q = sorted(neighbor[x])
    for size in range(1, 6):
        face_set.update(combinations(q, size))
faces = {d: tuple(sorted(f for f in face_set if len(f) == d+1)) for d in range(5)}
fvector = tuple(len(faces[d]) for d in range(5))
assert fvector == (16, 80, 160, 80, 16)
assert sum((-1) ** d * fvector[d] for d in range(5)) == 32

# Boundary over F2; lower bounds also certify characteristic-zero ranks.
def rank_binary(columns):
    pivot = {}
    for col in columns:
        while col:
            bit = col.bit_length() - 1
            if bit in pivot:
                col ^= pivot[bit]
            else:
                pivot[bit] = col
                break
    return len(pivot)

ranks = [1]  # augmented d0: C0 -> Z
for d in range(1, 5):
    locations = {f: j for j, f in enumerate(faces[d-1])}
    columns = []
    for sigma in faces[d]:
        v = 0
        for j in range(d+1):
            v ^= 1 << locations[sigma[:j]+sigma[j+1:]]
        columns.append(v)
    ranks.append(rank_binary(columns))
assert ranks == [1, 15, 65, 64, 16]
# Upper bounds from chain identities: d1<=16-1; d2<=80-15;
# d4<=16; d3<=80-16. Thus these F2 lower bounds force the
# corresponding ranks over Q, and yield only H_2(Q)=Q^31.
assert (16 - ranks[0] - ranks[1], 80 - ranks[1] - ranks[2],
        160 - ranks[2] - ranks[3], 80 - ranks[3] - ranks[4],
        16 - ranks[4]) == (0, 0, 31, 0, 0)

perm5 = tuple(permutations(range(5)))
def permute_vertex(v, p):
    return sum(((v >> i) & 1) << p[i] for i in range(5))

def gmap(v, t, p):
    return t ^ permute_vertex(v, p)

def parity(a):
    return (-1) ** sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1, len(a)))

def direct_character(t, p):
    """Lefschetz trace via alternating signed diagonal simplices."""
    ans = -1   # subtract H_0 = the trivial one-dimensional module
    for d in range(5):
        for sigma in faces[d]:
            image = [gmap(x, t, p) for x in sigma]
            if set(image) != set(sigma):
                continue
            indices = [sigma.index(x) for x in image]
            ans += (-1)**d * parity(indices)
    return ans

def orbit_character(t, p):
    """Independent formula: stabilized faces as unions of vertex orbits."""
    unseen = set(V)
    cycles = []
    while unseen:
        root = min(unseen)
        orbit = []
        x = root
        while x not in orbit:
            orbit.append(x)
            x = gmap(x, t, p)
        assert x == root
        unseen.difference_update(orbit)
        cycles.append(frozenset(orbit))
    ans = -1
    for sigma in face_set:
        fs = frozenset(sigma)
        count = 0
        for orbit in cycles:
            overlap = fs & orbit
            if overlap:
                if len(overlap) != len(orbit):
                    break
                count += 1
        else:
            ans += (-1)**(count+1)
    return ans

def cycle_type(p):
    unseen = set(range(5))
    lengths = []
    while unseen:
        start = min(unseen)
        x = start
        length = 0
        while x in unseen:
            unseen.remove(x)
            length += 1
            x = p[x]
        assert x == start
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))

# The full affine-permutation group has 1920 distinct transformations.
all_maps = set()
character = {}
class_table = defaultdict(list)
for p in perm5:
    for t in V:
        mapping = tuple(gmap(x, t, p) for x in V)
        assert len(set(mapping)) == 16
        assert all((gmap(y, t, p) in neighbor[gmap(x, t, p)]) ==
                   (y in neighbor[x]) for x in V for y in V)
        all_maps.add(mapping)
        a = direct_character(t, p)
        b = orbit_character(t, p)
        assert a == b, (t, p, a, b)
        character[t, p] = a
        if t == 0:
            class_table[cycle_type(p)].append(a)
assert len(all_maps) == 1920
assert len(character) == 1920
assert Counter(character.values()) == {1: 944, -1: 825, -5: 80, 3: 60, 7: 10, 31: 1}
assert sum(v*v for v in character.values()) == 3*1920
assert sum(character.values()) == 0

# The translation subgroup is V=F2^4, characters indexed by subsets
# A of [5] of size at most two, using t's even coordinate parity.
translation = {t: character[t, tuple(range(5))] for t in V}
assert Counter((t.bit_count(), chi) for t, chi in translation.items()) == {
    (0,31): 1, (2,7): 10, (4,-1): 5}

fourier = {}
for size in range(3):
    for A in combinations(range(5), size):
        mask = sum(1 << a for a in A)
        weighted = sum(translation[t] * (-1)**((t & mask).bit_count() % 2) for t in V)
        assert weighted % 16 == 0
        fourier[A] = weighted // 16
assert Counter((len(A), m) for A, m in fourier.items()) == {
    (0,6): 1, (1,3): 5, (2,1): 10}
assert sum(m for m in fourier.values()) == 31

# S5 character on V-invariant homology: average over translations.
invariant_character = defaultdict(list)
for p in perm5:
    total = sum(character[t,p] for t in V)
    assert total % 16 == 0
    invariant_character[cycle_type(p)].append(total // 16)
expected = {
    (1,1,1,1,1): (1,6),
    (2,1,1,1): (10,0),
    (2,2,1): (15,-2),
    (3,1,1): (20,0),
    (3,2): (20,0),
    (4,1): (30,0),
    (5,): (24,1),
}
assert set(invariant_character) == set(expected)
for typ, (amount, trace) in expected.items():
    assert len(invariant_character[typ]) == amount
    assert set(invariant_character[typ]) == {trace}
# This class character equals Lambda^2 of the standard S5 module.
def fixed_points(p): return sum(p[i] == i for i in range(5))
for p in perm5:
    std_trace = fixed_points(p) - 1
    p2 = tuple(p[p[i]] for i in range(5))
    ext2 = (std_trace**2 - (fixed_points(p2)-1))//2
    assert invariant_character[cycle_type(p)][0] == ext2
assert sum(amount * trace**2 for amount, trace in expected.values()) == 120
assert sum(amount * trace for amount, trace in expected.values()) == 0

print('graph_parameters 16 5 0 2; full_symmetry_order 1920')
print('face_vector', fvector)
print('mod2_augmented_boundary_ranks', tuple(ranks))
print('reduced_rational_homology H2=31 only')
print('translation_H2_character', {0:31, 2:7, 4:-1})
print('translation_Fourier_multiplicities', {0:6, 1:3, 2:1})
print('translation_invariant_S5_character', sorted((k, v) for k, v in expected.items()))
print('full_character_distribution', sorted(Counter(character.values()).items()))
print('full_character_norm', Fraction(sum(v*v for v in character.values()),1920))
print('absolutely_irreducible_summand_dimensions', (6, 15, 10))
print('affine_quotient_rational_Betti2', 6, 'full_quotient_rationally_acyclic', True)
print('CLEBSCH_AFFINE_FOURIER_HOMOLOGY_PASS')
