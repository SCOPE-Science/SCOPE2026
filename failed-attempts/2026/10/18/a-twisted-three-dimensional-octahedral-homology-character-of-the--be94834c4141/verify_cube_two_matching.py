#!/usr/bin/env python3
"""Finite integral Morse certificate and rational symmetry character for a cube graph complex."""
from collections import Counter, deque
from itertools import permutations

VERTICES = range(8)
EDGES = tuple((u, u ^ (1 << k)) for u in VERTICES for k in range(3)
              if u < (u ^ (1 << k)))
assert len(EDGES) == 12
STARS = tuple(sum(1 << i for i, (u, v) in enumerate(EDGES) if x in (u, v))
              for x in VERTICES)
assert all(a.bit_count() == 3 for a in STARS)


def allowed_degree(face):
    degree = [0] * 8
    for i, (u, v) in enumerate(EDGES):
        if face & (1 << i):
            degree[u] += 1
            degree[v] += 1
    return max(degree) <= 2


def allowed_stars(face):
    return all((face & star) != star for star in STARS)


for mask in range(1 << len(EDGES)):
    assert allowed_degree(mask) == allowed_stars(mask)
FACES = set(mask for mask in range(1, 1 << len(EDGES)) if allowed_degree(mask))
assert len(FACES) == 1698
assert Counter(m.bit_count() - 1 for m in FACES) == {
    0: 12, 1: 66, 2: 212, 3: 423, 4: 516, 5: 352, 6: 108, 7: 9}

# Pair along edge coordinates in succession in the augmented face poset.
# Discard the empty-face pair to obtain a matching on nonempty faces.
remaining = set(FACES) | {0}
matched_augmented = set()
for bit in (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6):
    for face in range(1 << 12):
        bigger = face | (1 << bit)
        if (face & (1 << bit)) == 0 and face in remaining and bigger in remaining:
            remaining.remove(face)
            remaining.remove(bigger)
            matched_augmented.add((face, bigger))
assert 0 not in remaining
assert len(remaining) == 3
assert all(face.bit_count() == 6 for face in remaining)
empty_pair = next(pair for pair in matched_augmented if pair[0] == 0)
matched = matched_augmented - {empty_pair}
remaining.add(empty_pair[1])
assert len(matched) == 847
assert len(remaining) == 4
assert Counter(m.bit_count() - 1 for m in remaining) == {0: 1, 5: 3}

# Explicitly check acyclicity of the discrete vector field: all unmatched
# Hasse arrows go from larger to smaller cells, and matched arrows are reversed.
indeg = {face: 0 for face in FACES}
adj = {face: [] for face in FACES}
incidences = 0
for higher in FACES:
    for bit in (1, 9, 8, 5, 10, 2, 3, 7, 4, 0, 11, 6):
        if not (higher & (1 << bit)):
            continue
        lower = higher ^ (1 << bit)
        if lower == 0:
            continue
        incidences += 1
        if (lower, higher) in matched:
            source, target = lower, higher
        else:
            source, target = higher, lower
        adj[source].append(target)
        indeg[target] += 1
queue = deque(face for face, k in indeg.items() if k == 0)
visited = 0
while queue:
    face = queue.popleft()
    visited += 1
    for child in adj[face]:
        indeg[child] -= 1
        if indeg[child] == 0:
            queue.append(child)
assert visited == len(FACES)

# Independently compute the ordinary mod-two Betti numbers by sparse bitset
# boundary elimination, without using the discrete-Morse matching.
by_dim = {d: sorted(face for face in FACES if face.bit_count() == d + 1)
          for d in range(8)}
boundary_ranks = {0: 0, 8: 0}
for d in range(1, 8):
    row = {face: j for j, face in enumerate(by_dim[d - 1])}
    pivots = {}
    for face in by_dim[d]:
        bits = 0
        for j in range(12):
            if face & (1 << j):
                bits ^= 1 << row[face ^ (1 << j)]
        while bits:
            high = bits.bit_length() - 1
            if high not in pivots:
                pivots[high] = bits
                break
            bits ^= pivots[high]
    boundary_ranks[d] = len(pivots)
betti = [len(by_dim[d]) - boundary_ranks[d] - boundary_ranks[d + 1]
         for d in range(8)]
assert betti == [1, 0, 0, 0, 0, 3, 0, 0]

# Since the Morse CW model has one 0-cell, three 5-cells, and no others,
# its homotopy type is a wedge of three 5-spheres.
edge_index = {frozenset(edge): j for j, edge in enumerate(EDGES)}

def vertex_action(x, t, permutation):
    result = t
    for j in range(3):
        if x & (1 << j):
            result ^= 1 << permutation[j]
    return result


def sign_of_sequence(sequence):
    count = sum(sequence[i] > sequence[j]
                for i in range(len(sequence)) for j in range(i + 1, len(sequence)))
    return 1 if count % 2 == 0 else -1


def lefschetz_trace(edge_permutation):
    unreduced = 0
    stable_count = 0
    for face in FACES:
        indices = [j for j in range(12) if face & (1 << j)]
        image = sum(1 << edge_permutation[j] for j in indices)
        if image != face:
            continue
        stable_count += 1
        orientation = sign_of_sequence([edge_permutation[j] for j in indices])
        unreduced += (-1 if (len(indices) - 1) % 2 else 1) * orientation
    # Connected, with sole reduced homology in odd degree five.
    return 1 - unreduced, stable_count

character = {}
fixed_counts = {}
for t in range(8):
    for permutation in permutations(range(3)):
        edge_permutation = tuple(edge_index[frozenset((
            vertex_action(u, t, permutation), vertex_action(v, t, permutation)))]
            for u, v in EDGES)
        assert len(set(edge_permutation)) == 12
        observed, nstable = lefschetz_trace(edge_permutation)
        expected = sign_of_sequence(permutation) * sum(
            (-1 if t & (1 << j) else 1)
            for j in range(3) if permutation[j] == j)
        assert observed == expected, (t, permutation, observed, expected)
        # Independent fixed-orbit evaluation: an invariant face is a union
        # of edge-permutation orbits, and its signed Lefschetz contribution
        # depends only on the number of chosen orbits.
        cycles = []
        seen = set()
        for start in range(12):
            if start in seen:
                continue
            cycle_mask = 0
            x = start
            while x not in seen:
                seen.add(x)
                cycle_mask |= 1 << x
                x = edge_permutation[x]
            cycles.append(cycle_mask)
        orbit_sum = 0
        for selection in range(1 << len(cycles)):
            chosen = 0
            for k, orbit_mask in enumerate(cycles):
                if selection & (1 << k):
                    chosen |= orbit_mask
            if allowed_stars(chosen):
                orbit_sum += (-1 if selection.bit_count() % 2 else 1)
        assert orbit_sum == observed, (t, permutation, orbit_sum, observed)
        character[t, permutation] = observed
        fixed_counts[t, permutation] = nstable
assert len(character) == 48
assert character[0, (0, 1, 2)] == 3
assert character[7, (0, 1, 2)] == -3
assert sum(character.values()) == 0
assert Counter(character.values()) == {-3: 1, -1: 15, 0: 16, 1: 15, 3: 1}
print('Q3_TWO_MATCHING_EQUIVARIANT_VERIFIED')
print('faces', len(FACES), 'matched_pairs', len(matched), 'incidences', incidences)
print('mod_two_betti', betti, 'boundary_ranks', boundary_ranks)
print('critical_cell_dimensions', sorted(m.bit_count() - 1 for m in remaining))
print('all_48_character_traces_match_signed_permutation_and_independent_orbit_sum')
print('character_histogram', sorted(Counter(character.values()).items()))
print('invariant_rank', sum(character.values()) // 48)
