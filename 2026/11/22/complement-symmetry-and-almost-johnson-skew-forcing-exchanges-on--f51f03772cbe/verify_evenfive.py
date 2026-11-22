"""Independent coordinate and forcing verifier for the five-folded cube.

Run: python3 verify_evenfive.py
Uses even-parity five-bit vertices; adjacency is Hamming distance four.
"""
from collections import Counter, deque
from itertools import combinations, permutations

vectors = tuple(v for v in range(32) if v.bit_count() % 2 == 0)
assert len(vectors) == 16
index = {v: i for i, v in enumerate(vectors)}
adjacency = [set() for _ in vectors]
for i, x in enumerate(vectors):
    for j, y in enumerate(vectors):
        if (x ^ y).bit_count() == 4:
            adjacency[i].add(j)
assert all(len(a) == 5 for a in adjacency)
assert sum(map(len, adjacency)) // 2 == 40

# Deliberately use mutable vertex sets, sequential applications, and the
# five-coordinate geometry, independently of the other bit-mask verifier.
def forces_all(seeds):
    painted = set(seeds)
    while True:
        found = None
        for neighbors in adjacency:
            remaining = neighbors - painted
            if len(remaining) == 1:
                found = next(iter(remaining))
                break
        if found is None:
            return len(painted) == len(vectors)
        painted.add(found)

forced_by_cardinality = Counter()
min_sets = []
for k in range(17):
    for s in combinations(range(16), k):
        if forces_all(s):
            forced_by_cardinality[k] += 1
            if k == 8:
                min_sets.append(frozenset(s))
assert dict(forced_by_cardinality) == {
    8: 6490, 9: 9760, 10: 7752, 11: 4352, 12: 1820,
    13: 560, 14: 120, 15: 16, 16: 1,
}
min_set_index = {s: i for i, s in enumerate(min_sets)}
assert len(min_set_index) == 6490
assert all(frozenset(set(range(16)) - s) in min_set_index for s in min_sets)

# A five-coordinate permutation followed by addition of an even word is
# an automorphism. These 16*120 maps give the full automorphism group.
def permute_bits(word, perm):
    return sum(1 << perm[j] for j in range(5) if (word >> j) & 1)

automorphisms = []
for perm in permutations(range(5)):
    for translation in vectors:
        mapping = tuple(index[permute_bits(x, perm) ^ translation] for x in vectors)
        assert len(set(mapping)) == 16
        automorphisms.append(mapping)
assert len(automorphisms) == 1920

unseen = set(min_sets)
orbit_records = []
while unseen:
    chosen = min(unseen, key=lambda x: tuple(sorted(x)))
    orbit = {frozenset(mapping[i] for i in chosen) for mapping in automorphisms}
    assert orbit.issubset(min_set_index)
    unseen -= orbit
    orbit_records.append((len(orbit), chosen))
assert sorted(size for size, _ in orbit_records) == [10, 160, 240, 320, 480, 480, 960, 1920, 1920]

# One-token jumps preserving the skew-forcing property.
reconfigure = []
for s in min_sets:
    neighbors = set()
    for selected in s:
        for free in (set(range(16)) - s):
            moved = frozenset((s - {selected}) | {free})
            if moved in min_set_index:
                neighbors.add(min_set_index[moved])
    reconfigure.append(neighbors)
assert sum(map(len, reconfigure)) // 2 == 116320
assert Counter(map(len, reconfigure)) == {32: 10, 35: 3200, 36: 2160, 38: 1120}
assert all(i in reconfigure[j] for i, a in enumerate(reconfigure) for j in a)

exception_sum = 0
exception_orbits = Counter()
for size, representative in orbit_records:
    start = min_set_index[representative]
    distance = [-1] * len(min_sets)
    distance[start] = 0
    pending = deque([start])
    while pending:
        i = pending.popleft()
        for j in reconfigure[i]:
            if distance[j] == -1:
                distance[j] = distance[i] + 1
                pending.append(j)
    assert min(distance) == 0 and max(distance) == 8
    exception = 0
    for j, target in enumerate(min_sets):
        lower = 8 - len(representative & target)
        assert distance[j] in (lower, lower + 1)
        exception += (distance[j] == lower + 1)
    exception_orbits[(size, exception)] += 1
    exception_sum += size * exception
assert exception_sum // 2 == 9120 and exception_sum % 2 == 0
assert exception_orbits == {
    (10, 0): 1, (160, 0): 1, (240, 0): 1, (320, 0): 1,
    (480, 0): 2, (960, 9): 1, (1920, 0): 1, (1920, 5): 1,
}
# Independent witness search for the matroid basis-exchange axiom failure.
violation = None
for _, base in orbit_records:
    for other in min_sets:
        if base == other:
            continue
        missing = other - base
        for deleted in base - other:
            if not any(frozenset((base - {deleted}) | {added}) in min_set_index
                       for added in missing):
                violation = (base, other, deleted, missing)
                break
        if violation is not None:
            break
    if violation is not None:
        break
assert violation is not None
print('basis-exchange counterexample verified')
print('even-five independent verification PASS')
print('forcing-cardinality-polynomial', sorted(forced_by_cardinality.items()))
print('optimal', len(min_sets), 'orbits', sorted((size, exc) for (size, exc), mult in exception_orbits.items() for _ in range(mult)))
print('degrees', sorted(Counter(map(len, reconfigure)).items()))
print('exchange-edges', sum(map(len, reconfigure)) // 2, 'radius 8 diameter 8',
      'pairs exceeding Johnson distance', exception_sum // 2)
