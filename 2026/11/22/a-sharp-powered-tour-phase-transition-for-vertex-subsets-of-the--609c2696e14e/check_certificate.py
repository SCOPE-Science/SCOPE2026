"""Exact finite certificate for the three-cube powered-tour theorem.

Requires Python 3 standard library only.  Vertex labels are binary integers 0..7,
with coordinate 0 the most significant bit. Tours on two vertices traverse
that edge twice. No floating-point arithmetic is used.
"""
from itertools import combinations, permutations, product

WITNESSES = {
    '01': '01', '03': '03', '07': '07',
    '012': '012', '016': '016', '035': '035',
    '0123': '0132', '0124': '0124', '0125': '0215',
    '0127': '0172', '0167': '0176', '0356': '0356',
    '01234': '01324', '01247': '01274', '01256': '01562',
    '012345': '023154', '012347': '012374', '012567': '015762',
    '0123456': '0132645', '01234567': '01326754',
}

vertices = list(product((0, 1), repeat=3))
permutation_maps = []
for perm in permutations(range(3)):
    for reflection in product((0, 1), repeat=3):
        permuted = tuple(vertices.index(tuple(
            vertices[v][perm[i]] ^ reflection[i] for i in range(3)
        )) for v in range(8))
        permutation_maps.append(permuted)
assert len(permutation_maps) == len(set(permutation_maps)) == 48


def canonical(subset):
    return min(tuple(sorted(mapping[v] for v in subset))
               for mapping in permutation_maps)


def hamming(a, b):
    return (a ^ b).bit_count()


def tour_steps(tour):
    return [hamming(tour[j], tour[(j + 1) % len(tour)])
            for j in range(len(tour))]


seen = set()
class_sizes = {}
for n in range(2, 9):
    for subset in combinations(range(8), n):
        rep = ''.join(map(str, canonical(subset)))
        assert rep in WITNESSES, ('uncovered subset', subset)
        seen.add(rep)
        class_sizes[rep] = class_sizes.get(rep, 0) + 1
assert seen == set(WITNESSES)
assert sum(class_sizes.values()) == 247  # all cube subsets of size >= 2
assert len(seen) == 20

for rep, tour_s in WITNESSES.items():
    tour = [int(c) for c in tour_s]
    assert sorted(tour) == [int(c) for c in rep]
    d = tour_steps(tour)
    assert all(1 <= x <= 3 for x in d)
    A = sum(d)  # squared Euclidean distance at exponent 2
    B = sum({1: 1, 2: 3, 3: 6}[x] for x in d)
    assert A <= 8 and B <= 12, (rep, A, B)
    if B == 12:
        assert rep in ('07', '0356'), (rep, 'unexpected equality witness')
    print(rep, tour_s, ''.join(map(str, d)), 'A=', A, 'B=', B,
          'orbit=', class_sizes[rep])
print('PASS: all 247 subsets, 48 symmetries, 20 complete orbits.')
