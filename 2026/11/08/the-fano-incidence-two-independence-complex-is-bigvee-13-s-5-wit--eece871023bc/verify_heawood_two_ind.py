#!/usr/bin/env python3
"""Reproducible finite verification of the Fano-incidence two-independence topology.

Uses only the Python standard library. No external data files are required.
"""
from collections import Counter, defaultdict, deque
from itertools import product

POINTS = range(1, 8)                 # nonzero three-bit vectors
NV = 14                              # p_1,...,p_7, ell_1,...,ell_7

def dot(x, y):
    return (x & y).bit_count() & 1

def adjacency():
    result = [0] * NV
    for x in POINTS:
        for y in POINTS:
            if dot(x, y) == 0:
                a, b = x - 1, y + 6
                result[a] |= 1 << b
                result[b] |= 1 << a
    return result

ADJ = adjacency()
assert all(a.bit_count() == 3 for a in ADJ)
assert sum(a.bit_count() for a in ADJ) // 2 == 21

def good_degree(mask):
    return all(not (mask >> i & 1) or (ADJ[i] & mask).bit_count() <= 1
               for i in range(NV))

def good_components(mask):
    unseen = mask
    while unseen:
        first = unseen & -unseen
        component = first
        unseen ^= first
        frontier = first
        while frontier:
            start = frontier & -frontier
            frontier ^= start
            i = start.bit_length() - 1
            newly = ADJ[i] & unseen
            unseen ^= newly
            component |= newly
            frontier |= newly
        if component.bit_count() > 2:
            return False
    return True

assert all(good_degree(s) == good_components(s) for s in range(1 << NV))
faces = {s for s in range(1, 1 << NV) if good_degree(s)}
face_vector = tuple(sum(s.bit_count() == d + 1 for s in faces) for d in range(7))
assert len(faces) == 2256
assert face_vector == (14, 91, 322, 651, 728, 392, 58)

# Sequential face-poset toggling.  A face once paired is never reused.
unused = set(faces)
matching = set()
for vertex in range(NV):
    bit = 1 << vertex
    for face in sorted(unused):
        bigger = face | bit
        if face in unused and not face & bit and bigger in unused:
            matching.add((face, bigger))
            unused.remove(face)
            unused.remove(bigger)
critical = tuple(sorted(unused))
assert len(matching) == 1121
assert critical == (1, 1008, 3300, 5460, 6712, 8064, 9826, 10600,
                    12160, 12504, 14208, 15232, 15744, 16000)
assert Counter(s.bit_count() - 1 for s in unused) == {0: 1, 5: 13}

# Full Hasse graph, oriented upwards on matched covers, otherwise downwards.
indegree = {s: 0 for s in faces}
outgoing = defaultdict(list)
num_covers = 0
for upper in faces:
    remaining = upper
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        lower = upper ^ bit
        if not lower:
            continue
        start, end = ((lower, upper) if (lower, upper) in matching
                      else (upper, lower))
        outgoing[start].append(end)
        indegree[end] += 1
        num_covers += 1
ready = deque(s for s in faces if indegree[s] == 0)
seen = 0
while ready:
    face = ready.popleft()
    seen += 1
    for target in outgoing[face]:
        indegree[target] -= 1
        if not indegree[target]:
            ready.append(target)
assert num_covers == 10150
assert seen == len(faces)      # complete acyclicity certificate

# A separate exact homology calculation over F_2 for corroboration.
by_dim = [[s for s in sorted(faces) if s.bit_count() == d + 1]
          for d in range(7)]
ranks = [0] * 7
for d in range(1, 7):
    rows = {s: i for i, s in enumerate(by_dim[d-1])}
    pivots = {}
    for upper in by_dim[d]:
        column = 0
        remaining = upper
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            column ^= 1 << rows[upper ^ bit]
        while column:
            top = column.bit_length() - 1
            if top not in pivots:
                pivots[top] = column
                break
            column ^= pivots[top]
    ranks[d] = len(pivots)
mod2_reduced_betti = [face_vector[0]-ranks[1]-1] + [
    face_vector[d] - ranks[d] - ranks[d+1] for d in range(1, 6)
] + [face_vector[6]-ranks[6]]
assert mod2_reduced_betti == [0, 0, 0, 0, 0, 13, 0]

# The 168 invertible 3x3 binary matrices, and all their point/line dualities.
def action(cols, x):
    return ((cols[0] if x & 1 else 0)
            ^ (cols[1] if x & 2 else 0)
            ^ (cols[2] if x & 4 else 0))

def maps():
    for cols in product(POINTS, repeat=3):
        if len({action(cols, x) for x in POINTS}) == 7:
            yield cols

def image_mask(mask, perm):
    result = 0
    while mask:
        bit = mask & -mask
        mask ^= bit
        result |= 1 << perm[bit.bit_length()-1]
    return result

def inversion_sign(seq):
    inversions = sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i+1, len(seq)))
    return -1 if inversions & 1 else 1

def trace_by_faces(perm):
    # Reduced Lefschetz number L~, including empty face contribution -1.
    L = -1
    for face in faces:
        if image_mask(face, perm) != face:
            continue
        ordered = [i for i in range(NV) if face >> i & 1]
        sign = inversion_sign([perm[i] for i in ordered])
        L += (-1) ** (len(ordered)-1) * sign
    return -L  # only reduced homology in odd degree five

def trace_by_cycles(perm):
    # A setwise fixed face is exactly a union of cycles; orientation cancels
    # simplex cardinality signs, leaving (-1)^(number of cycles).
    cycles = []
    used = set()
    for initial in range(NV):
        if initial in used:
            continue
        cur = initial
        cycle_mask = 0
        while cur not in used:
            used.add(cur)
            cycle_mask |= 1 << cur
            cur = perm[cur]
        cycles.append(cycle_mask)
    total = 0
    for picked in range(1 << len(cycles)):
        mask = 0
        for j, cycle in enumerate(cycles):
            if picked >> j & 1:
                mask |= cycle
        if not mask or mask in faces:
            total += (-1) ** picked.bit_count()
    return total

matrices = tuple(maps())
assert len(matrices) == 168
perms = []
traces = []
counts = Counter()
for cols in matrices:
    point = {x: action(cols, x) for x in POINTS}
    dual = {y: next(z for z in POINTS if all(
        dot(z, point[x]) == dot(y, x) for x in POINTS)) for y in POINTS}
    preserving = tuple([point[x]-1 for x in POINTS]
                       + [dual[y]+6 for y in POINTS])
    swapping = tuple([preserving[i+7] if i < 7 else preserving[i-7]
                      for i in range(NV)])
    fixed_nonzero = sum(point[x] == x for x in POINTS)
    for exchange, perm in ((False, preserving), (True, swapping)):
        assert sorted(perm) == list(range(NV))
        assert all(image_mask(ADJ[i], perm) == ADJ[perm[i]]
                   for i in range(NV))
        c = trace_by_faces(perm)
        assert c == trace_by_cycles(perm)
        assert c == (-1 if exchange else 2*fixed_nonzero-1)
        counts[c] += 1
        perms.append(perm)
        traces.append(c)
assert len(set(perms)) == 336
assert dict(sorted(counts.items())) == {-1: 216, 1: 98, 5: 21, 13: 1}
assert sum(traces) == 0
assert sum(c*c for c in traces) == 3*336
assert sum(c*(1 if i % 2 == 0 else -1)
           for i, c in enumerate(traces)) == 336

print('vertices=14 edges=21')
print('face_vector=', face_vector, 'nonempty=', len(faces))
print('morse_pairs=', len(matching), 'critical={0:1,5:13}')
print('hasse_covers=', num_covers, 'acyclic_vertices=', seen)
print('mod2_boundary_ranks=', tuple(ranks[1:]))
print('mod2_reduced_betti=', tuple(mod2_reduced_betti))
print('aut_group=336, preserving=168, exchanging=168')
print('top_homology_character=', dict(sorted(counts.items())))
print('character_norm=3, trivial_multiplicity=0, swap_sign_multiplicity=1')
print('ALL_CHECKS_PASS')
