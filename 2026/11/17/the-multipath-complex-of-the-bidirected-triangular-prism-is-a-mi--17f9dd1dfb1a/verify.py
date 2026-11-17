#!/usr/bin/env python3
"""Exact finite topology checks for the multipath complex of a bidirected triangular prism.

Requires only the Python standard library. All integral incidences and all
rational arithmetic are exact; this program does not use floating point.
"""
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache

N = 6
edges = {(i, (i + 1) % 3) for i in range(3)}
edges |= {(i + 3, (i + 1) % 3 + 3) for i in range(3)}
edges |= {(i, i + 3) for i in range(3)}
assert len(edges) == 9
arcs = sorted((u, v) for x, y in edges for (u, v) in ((x, y), (y, x)))
assert len(arcs) == 18 and len(set(arcs)) == 18


def valid(mask):
    incoming, outgoing = {}, {}
    while mask:
        bit = mask & -mask
        u, v = arcs[bit.bit_length() - 1]
        mask ^= bit
        if u in outgoing or v in incoming:
            return False
        outgoing[u] = v
        incoming[v] = u
    for start in outgoing:
        seen = set()
        v = start
        while v in outgoing:
            if v in seen:
                return False
            seen.add(v)
            v = outgoing[v]
    return True


faces = {mask for mask in range(1 << len(arcs)) if valid(mask)}
assert len(faces) == 687 and 0 in faces
for x in faces:
    for i in range(18):
        if x & (1 << i):
            assert (x ^ (1 << i)) in faces
f_vector = Counter(x.bit_count() - 1 for x in faces if x)
assert tuple(f_vector[i] for i in range(5)) == (18, 108, 260, 240, 60)

# Sequential pivot-element matching, including the empty face initially.
unmatched = set(faces)
pairs = []
for i in range(18):
    bit = 1 << i
    current = [(x, x | bit) for x in unmatched
               if not x & bit and (x | bit) in unmatched]
    for lo, hi in current:
        assert lo in unmatched and hi in unmatched
        unmatched.remove(lo)
        unmatched.remove(hi)
    pairs.extend(current)

empty_pair = [(a, b) for a, b in pairs if a == 0]
assert len(empty_pair) == 1
critical = set(unmatched) | {empty_pair[0][1]}
ordinary_pairs = [(a, b) for a, b in pairs if a]
assert len(ordinary_pairs) == 326
assert Counter(x.bit_count() - 1 for x in critical) == {0: 1, 2: 5, 3: 22, 4: 6}
assert 2 * len(ordinary_pairs) + len(critical) == len(faces) - 1

# Verify an acyclic directed Hasse diagram: matched covers point upward,
# and all other codimension-one incidences point downward.
matched = set(ordinary_pairs)
vertices = faces - {0}
indegree = {x: 0 for x in vertices}
adjacency = {x: [] for x in vertices}
cover_count = 0
for hi in vertices:
    for i in range(18):
        if not hi & (1 << i):
            continue
        lo = hi ^ (1 << i)
        if not lo:
            continue
        src, dst = (lo, hi) if (lo, hi) in matched else (hi, lo)
        adjacency[src].append(dst)
        indegree[dst] += 1
        cover_count += 1
queue = deque(x for x in vertices if indegree[x] == 0)
visited = 0
while queue:
    x = queue.popleft()
    visited += 1
    for y in adjacency[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            queue.append(y)
assert visited == len(vertices) == 686 and cover_count == 2256


def signed_boundary(face):
    indices = [i for i in range(18) if face & (1 << i)]
    return [(face ^ (1 << i), 1 if j % 2 == 0 else -1)
            for j, i in enumerate(indices)]


def linear_add(dst, src, scale):
    for key, val in src.items():
        new = dst.get(key, 0) + scale * val
        if new:
            dst[key] = new
        else:
            dst.pop(key, None)

lower_to_upper = {lo: hi for lo, hi in ordinary_pairs}
upper_to_lower = {hi: lo for lo, hi in ordinary_pairs}


@lru_cache(None)
def project(face):
    """Exact algebraic-Morse projection on critical cells of this dimension."""
    if face in critical:
        return {face: 1}
    if face in upper_to_lower:
        return {}
    if face in lower_to_upper:
        mate = lower_to_upper[face]
        boundary = signed_boundary(mate)
        pivot = dict(boundary)[face]
        ans = {}
        for subface, coeff in boundary:
            if subface != face:
                linear_add(ans, project(subface), -pivot * coeff)
        return ans
    raise AssertionError(('not in matching', face))


# The signed Morse differentials vanish over Z in every critical dimension.
for face in critical:
    if face.bit_count() == 1:
        continue
    boundary = {}
    for subface, coeff in signed_boundary(face):
        linear_add(boundary, project(subface), coeff)
    assert not boundary, (face, boundary)

by_dimension = {
    k: sorted(x for x in faces if x.bit_count() == k + 1)
    for k in range(5)
}
critical_twos = sorted(x for x in critical if x.bit_count() == 3)
alpha = []
for cell in critical_twos:
    cocycle = {x: project(x)[cell] for x in by_dimension[2]
               if cell in project(x)}
    assert cocycle[cell] == 1
    for tetrahedron in by_dimension[3]:
        assert sum(sign * cocycle.get(triangle, 0)
                   for triangle, sign in signed_boundary(tetrahedron)) == 0
    alpha.append(cocycle)

# Independently compute signed incidence ranks modulo 2, including the
# dimension of degree-two coboundaries.
def gf2_add(value, basis):
    while value:
        pivot = value.bit_length() - 1
        if pivot in basis:
            value ^= basis[pivot]
        else:
            basis[pivot] = value
            return True
    return False

ranks = {}
for k in range(1, 5):
    index = {x: i for i, x in enumerate(by_dimension[k - 1])}
    basis = {}
    for cell in by_dimension[k]:
        column = 0
        for face, _ in signed_boundary(cell):
            column ^= 1 << index[face]
        gf2_add(column, basis)
    ranks[k] = len(basis)
assert ranks == {1: 17, 2: 91, 3: 164, 4: 54}
idx_2 = {x: i for i, x in enumerate(by_dimension[2])}
B2 = {}
for edge in by_dimension[1]:
    col = sum(1 << idx_2[t] for t in by_dimension[2] if (t & edge) == edge)
    gf2_add(col, B2)
assert len(B2) == 91
for cochain in alpha:
    vec = sum(1 << idx_2[t] for t, c in cochain.items() if c & 1)
    assert gf2_add(vec, B2)
assert len(B2) == 96  # five independent cohomology classes modulo 2

# Rational row reduction in dimension 4.  A cup product is a coboundary
# precisely when its 60-coordinate column lies in this exact rational span.
def add_over_Q(column, basis):
    v = {k: Fraction(x) for k, x in column.items() if x}
    while v:
        k = max(v)
        if k in basis:
            coeff = v[k]
            for j, value in basis[k].items():
                new = v.get(j, 0) - coeff * value
                if new:
                    v[j] = new
                else:
                    v.pop(j, None)
        else:
            lead = v[k]
            basis[k] = {j: x / lead for j, x in v.items()}
            return True
    return False

coboundary_image = {}
for tetrahedron in by_dimension[3]:
    column = {}
    for j, pentagon in enumerate(by_dimension[4]):
        entry = dict(signed_boundary(pentagon)).get(tetrahedron, 0)
        if entry:
            column[j] = entry
    add_over_Q(column, coboundary_image)
assert len(coboundary_image) == 54

nonzero_raw_cups = 0
for a in alpha:
    for b in alpha:
        cup = {}
        for j, pentagon in enumerate(by_dimension[4]):
            v = [i for i in range(18) if pentagon & (1 << i)]
            first = (1 << v[0]) | (1 << v[1]) | (1 << v[2])
            last = (1 << v[2]) | (1 << v[3]) | (1 << v[4])
            value = a.get(first, 0) * b.get(last, 0)
            if value:
                cup[j] = value
        nonzero_raw_cups += bool(cup)
        comparison_basis = coboundary_image.copy()
        assert not add_over_Q(cup, comparison_basis), 'nonzero cup class'

assert tuple(f_vector[i] for i in range(5)) == (18, 108, 260, 240, 60)
assert sum((-1)**i * f_vector[i] for i in range(5)) == -10
print('TRIANGULAR_PRISM_MULTIPATH_EXACT_CHECKS_PASS')
print('directed_arcs=18 nonempty_faces=686 face_vector=(18,108,260,240,60)')
print('matching_pairs=326 hasse_covers=2256 acyclic=True')
print('critical_cells=(1 dimension-0,5 dimension-2,22 dimension-3,6 dimension-4)')
print('integral_morse_differentials=0')
print('boundary_ranks_mod_2=(17,91,164,54)')
print('independent_degree_2_cocycles=5 rational_degree_4_coboundary_rank=54')
print('all_25_ordered_degree_2_cup_products=zero_in_rational_cohomology')
print('nonzero_raw_cup_cochains=%d' % nonzero_raw_cups)
print('homotopy_type=5*S^2 vee 22*S^3 vee 6*S^4')
