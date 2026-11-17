#!/usr/bin/env python3
"""Exact finite verification for Desargues independence-homology characters.

Python 3 standard library only. All simplicial and group actions are constructed
from the definitions, rather than read from serialized certificates.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations

labels = tuple(range(5))
vertices = tuple(combinations(labels, 2)) + tuple(combinations(labels, 3))
lookup = {s: i for i, s in enumerate(vertices)}
n = len(vertices)
edge_pairs = {(i, j) for i, a in enumerate(vertices) for j, b in enumerate(vertices)
              if len(a) == 2 and len(b) == 3 and set(a) < set(b)}
assert n == 20 and len(edge_pairs) == 30
adj = [0] * n
for i, j in edge_pairs:
    adj[i] |= 1 << j
    adj[j] |= 1 << i

# Independent simplices, including the augmentation simplex with mask zero.
faces = [0]
def walk(mask, available):
    while available:
        bit = available & -available
        available -= bit
        vertex = bit.bit_length() - 1
        new_mask = mask | bit
        faces.append(new_mask)
        walk(new_mask, available & ~adj[vertex])
walk(0, (1 << n) - 1)
face_set = set(faces)
assert len(face_set) == len(faces) == 6212
vector = tuple(Counter(m.bit_count() for m in faces)[size] for size in range(1, 11))
assert vector == (20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2)

# Greedy element matching, including the empty simplex (reduced chains).
remaining = set(faces)
matching = {}
for v in range(n):
    b = 1 << v
    for lo in tuple(sorted(remaining)):
        if lo not in remaining or lo & b:
            continue
        hi = lo | b
        if hi in remaining:
            remaining.remove(lo)
            remaining.remove(hi)
            matching[lo] = hi
assert len(matching) == 3103 and len(remaining) == 6
counts = Counter(m.bit_count()-1 for m in remaining)
assert counts == {4: 1, 5: 5}

# Complete acyclicity test of the reversed matched Hasse orientations.
indegree = {m: 0 for m in faces}
directed = defaultdict(list)
cover_count = 0
for hi in faces:
    if not hi:
        continue
    tmp = hi
    while tmp:
        b = tmp & -tmp
        tmp -= b
        lo = hi ^ b
        u, w = (lo, hi) if matching.get(lo) == hi else (hi, lo)
        directed[u].append(w)
        indegree[w] += 1
        cover_count += 1
queue = deque(m for m, degree in indegree.items() if degree == 0)
visited = 0
while queue:
    u = queue.popleft()
    visited += 1
    for w in directed[u]:
        indegree[w] -= 1
        if indegree[w] == 0:
            queue.append(w)
assert visited == len(faces)

# Exact integral signed Morse differential from critical 5-faces to 4-faces.
def incidence(mask, bit):
    return (-1) ** ((mask & (bit - 1)).bit_count())
critical4 = tuple(sorted(x for x in remaining if x.bit_count() == 5))
critical5 = tuple(sorted(x for x in remaining if x.bit_count() == 6))
upper_to_lower = {hi: lo for lo, hi in matching.items()}
@lru_cache(None)
def reduce_face(sigma):
    if sigma in remaining:
        return {sigma: 1}
    if sigma in upper_to_lower:
        return {}
    tau = matching[sigma]
    pivot = tau ^ sigma
    coeff_pivot = incidence(tau, pivot)
    answer = defaultdict(int)
    tmp = tau ^ pivot
    while tmp:
        b = tmp & -tmp
        tmp -= b
        coeff = -incidence(tau, b) * coeff_pivot
        for z, c in reduce_face(tau ^ b).items():
            answer[z] += coeff * c
    return {z: c for z, c in answer.items() if c}
mdiff = []
for c5 in critical5:
    out = defaultdict(int)
    tmp = c5
    while tmp:
        b = tmp & -tmp
        tmp -= b
        for z, a in reduce_face(c5 ^ b).items():
            out[z] += incidence(c5, b) * a
    mdiff.append(tuple(out[x] for x in critical4))
assert mdiff == [(0,)] * 5

# Natural S_5 x C_2: complement exchanges the two bipartition classes.
def action(p, exchange):
    return tuple(lookup[tuple(sorted(set(labels) - {p[i] for i in s}))
                        if exchange else tuple(sorted(p[i] for i in s))]
                 for s in vertices)
def parity(p):
    return -1 if sum(p[i] > p[j] for i in labels for j in labels if i < j) % 2 else 1
def cycle_type(p):
    done = set()
    lengths = []
    for v in labels:
        if v not in done:
            cur = v
            count = 0
            while cur not in done:
                done.add(cur)
                count += 1
                cur = p[cur]
            lengths.append(count)
    return tuple(sorted(lengths, reverse=True))

def orbit_lefschetz(g):
    unseen = set(range(n))
    valid = []
    while unseen:
        start = min(unseen)
        x = start
        mask = 0
        while x in unseen:
            unseen.remove(x)
            mask |= 1 << x
            x = g[x]
        # Only orbits that are themselves independent can be selected.
        if all((adj[i] & (mask ^ (1 << i))) == 0 for i in range(n) if mask >> i & 1):
            valid.append(mask)
    incompatible = [0] * len(valid)
    for i, mask in enumerate(valid):
        for j, other in enumerate(valid):
            if i == j:
                continue
            if any((adj[v] & other) for v in range(n) if mask >> v & 1):
                incompatible[i] |= 1 << j
    @lru_cache(None)
    def partition_sum(active):
        if active == 0:
            return 1
        bit = active & -active
        i = bit.bit_length() - 1
        rest = active ^ bit
        return partition_sum(rest) - partition_sum(rest & ~incompatible[i])
    # Reduced signed Lefschetz = minus independence polynomial at -1.
    return -partition_sum((1 << len(valid)) - 1)

def direct_lefschetz(g):
    # Independent check: signs on every fixed oriented nonempty simplex.
    total = -1  # reduced empty face contribution
    for mask in faces:
        if mask == 0:
            continue
        order = [i for i in range(n) if mask >> i & 1]
        moved = [g[i] for i in order]
        if set(moved) != set(order):
            continue
        inv = sum(a > b for i, a in enumerate(moved) for b in moved[i + 1:])
        total += (-1) ** (mask.bit_count() - 1 + inv)
    return total

class_les = {}
all_actions = set()
class_counts = Counter()
all_perms = tuple(permutations(labels))
for p in all_perms:
    cl = cycle_type(p)
    for swap in (0, 1):
        g = action(p, swap)
        all_actions.add(g)
        lefschetz = orbit_lefschetz(g)
        expected = (-1 if swap else 1) * (parity(p) - sum(p[i] == i for i in labels))
        assert lefschetz == expected, (p, swap, lefschetz, expected)
        assert direct_lefschetz(g) == lefschetz
        if (cl, swap) in class_les:
            assert class_les[cl, swap] == lefschetz
        class_les[cl, swap] = lefschetz
        class_counts[cl, swap] += 1
assert len(all_actions) == 240 and len(class_les) == 14

# Confirm no additional graph automorphisms by independent constraint backtracking.
def count_all_automorphisms():
    mapping = {}
    free_images = set(range(n))
    total = 0
    tested_nodes = 0
    def extend():
        nonlocal total, tested_nodes
        tested_nodes += 1
        if len(mapping) == n:
            total += 1
            return
        assigned_mask = sum(1 << x for x in mapping)
        v = max((x for x in range(n) if x not in mapping),
                key=lambda x: ((adj[x] & assigned_mask).bit_count(), -x))
        for w in sorted(free_images):
            if all(bool(adj[v] & (1 << u)) == bool(adj[w] & (1 << mapping[u]))
                   for u in mapping):
                mapping[v] = w
                free_images.remove(w)
                extend()
                free_images.add(w)
                del mapping[v]
    extend()
    return total, tested_nodes
full_order, backtrack_nodes = count_all_automorphisms()
assert full_order == 240

# H_4 is one-dimensional, hence one of the four S_5 x C_2 linear characters.
# H_5 = H_4 - L. For three choices H_5 has a negative irreducible
# multiplicity against the linear character sign(S_5) tensor sign(C_2).
for sign5 in (0, 1):
    for sign2 in (0, 1):
        def candidate4(p, swap):
            return (parity(p) if sign5 else 1) * ((-1) ** (swap * sign2))
        numerator = sum((candidate4(p, swap) - class_les[cycle_type(p), swap])
                        * parity(p) * (-1) ** swap
                        for p in all_perms for swap in (0, 1))
        assert numerator % 240 == 0
        coeff = numerator // 240
        assert coeff == (0 if (sign5, sign2) == (1, 1) else -1)

print('DESARGUES_IND_FACE_VECTOR', vector)
print('MATCHED_PAIRS', len(matching), 'CRITICAL_4_5', len(critical4), len(critical5), 'HASSE_COVERS', cover_count)
print('REDUCED_MORSE_BOUNDARY', mdiff)
print('CLASS_VALUES', [(cl, sw, class_counts[cl, sw], class_les[cl, sw])
                       for cl in sorted({c for c, sw in class_les}, reverse=True)
                       for sw in (0, 1)])
print('FULL_GRAPH_AUTOMORPHISMS', full_order, 'SEARCH_NODES', backtrack_nodes)
print('H4', 'S5_sign_times_complement_sign', 'rank=1')
print('H5', 'five_point_permutation_times_complement_sign', 'rank=5')
print('DESARGUES_240_SYMMETRIES_EXACT_CHARACTER_PASS')
