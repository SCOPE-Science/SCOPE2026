#!/usr/bin/env python3
"""Reproducible complete isometry census for radius-one identifying codes in Q4.

This is an exact finite search with integer arithmetic and no external packages.
"""
from collections import Counter
from itertools import combinations, permutations

DIM = 4
VERTICES = tuple(range(1 << DIM))
GRAY = (0, 1, 3, 2)

# Build the closed neighborhoods in two independent ways.
CLOSED1 = [frozenset([x] + [x ^ (1 << j) for j in range(DIM)]) for x in VERTICES]
CLOSED2 = [frozenset(y for y in VERTICES if (x ^ y).bit_count() <= 1) for x in VERTICES]
assert CLOSED1 == CLOSED2


def valid_by_mask(C):
    membership = sum(1 << x for x in C)
    signatures = [membership & sum(1 << y for y in CLOSED1[x]) for x in VERTICES]
    return 0 not in signatures and len(set(signatures)) == len(VERTICES)


def valid_by_sets(C):
    selected = set(C)
    signals = [frozenset(selected.intersection(CLOSED2[x])) for x in VERTICES]
    return all(signals) and len(set(signals)) == len(VERTICES)


# Exhaust *all* potential size-six and size-seven codes with two validators.
valid_six = []
valid_seven = []
for count, target in ((6, valid_six), (7, valid_seven)):
    for C in combinations(VERTICES, count):
        lhs = valid_by_mask(C)
        rhs = valid_by_sets(C)
        assert lhs == rhs, (count, C)
        if lhs:
            target.append(C)
assert len(valid_six) == 0
assert len(valid_seven) == 960
# Superset monotonicity of identifying codes means the size-six exclusion
# proves no code of size <= six can work.
ALL_VALID = set(valid_seven)

# Generate all 4! coordinate permutations and all sixteen translations.
COORD_PERMS = list(permutations(range(DIM)))

def permute_word(x, p):
    return sum(((x >> i) & 1) << p[i] for i in range(DIM))

maps = []
for p in COORD_PERMS:
    for shift in VERTICES:
        maps.append(tuple(permute_word(v, p) ^ shift for v in VERTICES))
assert len(maps) == 384 and len(set(maps)) == 384
assert all({mapping[v] for v in VERTICES} == set(VERTICES) for mapping in maps)
assert all(all(CLOSED2[mapping[v]] == frozenset(mapping[w] for w in CLOSED2[v])
               for v in VERTICES) for mapping in maps)

def transform(C, mapping):
    return tuple(sorted(mapping[v] for v in C))

# Two independent orbit-count certificates:
#   (1) direct complete orbit partition;
#   (2) Burnside's fixed point lemma across all 384 symmetries.
unused = set(ALL_VALID)
orb = []
while unused:
    representative = min(unused)
    orbit = {transform(representative, mapping) for mapping in maps}
    assert orbit <= ALL_VALID
    unused -= orbit
    stab = sum(transform(representative, mapping) == representative for mapping in maps)
    assert len(orbit) * stab == 384
    profile = tuple(sorted(Counter((x ^ y).bit_count()
                                   for x, y in combinations(representative, 2)).items()))
    antipodal = sum(x ^ y == 15 for x, y in combinations(representative, 2))
    assert antipodal == dict(profile).get(4, 0)
    orb.append((len(orbit), stab, representative, profile, antipodal))
orb.sort()
assert [(size, stab) for size, stab, *_ in orb] == [(192, 2), (384, 1), (384, 1)]
assert len({profile for _, _, _, profile, _ in orb}) == 3
assert sum(size for size, *_ in orb) == 960

burnside = sum(sum(transform(C, mapping) == C for C in ALL_VALID) for mapping in maps)
assert burnside == len(orb) * len(maps) == 1152

# Gray isomorphism from the Lee torus Z_4^2 = C4 Cartesian C4 to Q4.
def gray_pair(a, b):
    return GRAY[a] | (GRAY[b] << 2)

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                lee = min((a - c) % 4, (c - a) % 4) + min((b - d) % 4, (d - b) % 4)
                hamming = (gray_pair(a, b) ^ gray_pair(c, d)).bit_count()
                assert lee == hamming

# The two previously printed explicit examples both produce known types.
printed_examples = (
    ('22', '00', '32', '13', '30', '33', '11'),
    ('00', '32', '10', '03', '20', '23', '02'),
)
sample_profiles = []
for example in printed_examples:
    C = tuple(sorted(gray_pair(int(word[0]), int(word[1])) for word in example))
    assert C in ALL_VALID
    sample_profiles.append(tuple(sorted(Counter((x ^ y).bit_count()
                                               for x, y in combinations(C, 2)).items())))
assert sample_profiles[0] != sample_profiles[1]
assert set(sample_profiles) <= {profile for _, _, _, profile, _ in orb}
assert len({profile for _, _, _, profile, _ in orb} - set(sample_profiles)) == 1

print('DOMAIN_OK vertices=16 checked_six=8008 checked_seven=11440 validators_agree=true')
print('GRAY_OK Lee_torus_Z4xZ4_is_Q4=true')
print('MINIMUM=7 LABELED_MINIMA=960 (previously known)')
print('BURNSIDE_OK fixed_sum=1152 automorphisms=384 orbits=3')
for i, (size, stab, rep, profile, anti) in enumerate(orb, start=1):
    print('TYPE', i, 'orbit', size, 'stabilizer', stab,
          'words', ','.join(f'{x:04b}' for x in rep),
          'hamming_profile', ','.join(f'{j}:{v}' for j, v in profile),
          'antipodal_pairs', anti)
print('LITERATURE_EXAMPLES_ONLY_TWO_TYPES=true THIRD_PROFILE_NEW_TO_EXAMPLES=true')
print('VERIFY_OK minima=960 orbits=3 orbit_sizes=192,384,384 stabilizers=2,1,1 burnside=1152')
