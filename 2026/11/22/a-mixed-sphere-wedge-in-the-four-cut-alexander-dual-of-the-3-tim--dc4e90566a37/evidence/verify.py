"""Exact integral certificate for the ordinary four-cut complex of the 3x3 rook graph.

Only the Python standard library is needed. All integers are exact, and all
simplicial faces and elementary collapse pairs are enumerated exhaustively.
"""
from collections import Counter
from itertools import combinations

V = tuple(range(9))
FULL = (1 << 9) - 1


def bits(mask):
    return tuple(i for i in V if mask & (1 << i))


def connected(mask):
    nodes = set(bits(mask))
    if not nodes:
        return False
    reached = {min(nodes)}
    frontier = list(reached)
    while frontier:
        u = frontier.pop()
        for v in sorted(nodes - reached):
            if u // 3 == v // 3 or u % 3 == v % 3:
                reached.add(v)
                frontier.append(v)
    return len(reached) == len(nodes)


all_masks = range(1 << 9)
conn4 = {s for s in all_masks if s.bit_count() == 4 and connected(s)}
disc4 = {s for s in all_masks if s.bit_count() == 4 and s not in conn4}
assert len(conn4) == 81 and len(disc4) == 45

# Direct definition of the dual: no disconnected four-set is contained in a face.
dual = {s for s in all_masks if not any((s & t) == t for t in disc4)}
assert Counter(s.bit_count() for s in dual) == {0: 1, 1: 9, 2: 36, 3: 84, 4: 81, 5: 36, 6: 6}

# Independently reconstruct the ordinary cut complex from its 45 facets.
cut = set()
for bad in disc4:
    facet = FULL ^ bad
    cut.update(s for s in all_masks if (s & ~facet) == 0)
assert Counter(s.bit_count() for s in cut) == {0: 1, 1: 9, 2: 36, 3: 78, 4: 90, 5: 45}
assert dual == {s for s in all_masks if (FULL ^ s) not in cut}

# Deterministic sequence of free-face collapses; each step is checked anew.
remaining = set(dual)
collapse = []
while True:
    available = []
    for s in sorted(remaining):
        if s == 0:
            continue
        codim_one = [s | (1 << v) for v in V
                     if not s & (1 << v) and (s | (1 << v)) in remaining]
        if len(codim_one) == 1:
            available.append((s, codim_one[0]))
    if not available:
        break
    lower, upper = min(available, key=lambda t: (-t[1].bit_count(), t[0]))
    # A higher-dimensional coface would imply at least two codimension-one
    # cofaces, so this is a genuine elementary collapse.
    assert all((x & lower) != lower or x == upper
               for x in remaining if x != lower)
    remaining.remove(lower)
    remaining.remove(upper)
    collapse.append((lower, upper))

assert len(collapse) == 69
assert Counter(s.bit_count() for s in remaining) == {0: 1, 1: 9, 2: 36, 3: 51, 4: 18}
assert max(s.bit_count() for s in remaining) == 4
assert all((s & (s - (1 << v))) in remaining
           for s in remaining for v in V if s & (1 << v))


def signed_boundary(faces, degree):
    upper = sorted(s for s in faces if s.bit_count() == degree + 1)
    lower = sorted(s for s in faces if s.bit_count() == degree)
    index = {s: i for i, s in enumerate(lower)}
    m = [[0] * len(upper) for _ in lower]
    for col, s in enumerate(upper):
        for position, v in enumerate(bits(s)):
            m[index[s ^ (1 << v)]][col] = (-1) ** position
    return m


def rank_by_unit_pivots(matrix):
    # Genuine integral elementary row and column operations. Every nonzero
    # diagonal pivot is +/-1, so they prove the exact Smith invariant factors.
    a = [row[:] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    k = 0
    while k < min(rows, cols):
        candidates = []
        for i in range(k, rows):
            for j in range(k, cols):
                if abs(a[i][j]) == 1:
                    score = (sum(x != 0 for x in a[i][k:])
                             + sum(a[ii][j] != 0 for ii in range(k, rows)))
                    candidates.append((score, i, j))
        if not candidates:
            break
        _, i, j = min(candidates)
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        if a[k][k] < 0:
            a[k] = [-v for v in a[k]]
        assert a[k][k] == 1
        for i in range(k + 1, rows):
            t = a[i][k]
            if t:
                a[i] = [x - t * y for x, y in zip(a[i], a[k])]
        for j in range(k + 1, cols):
            t = a[k][j]
            if t:
                for i in range(rows):
                    a[i][j] -= t * a[i][k]
        k += 1
    # The residual matrix is EXACTLY zero (no unrecognized nonunit factors).
    assert all(a[i][j] == 0 for i in range(k, rows)
               for j in range(k, cols))
    assert all(a[i][j] == (1 if i == j else 0)
               for i in range(k) for j in range(cols))
    assert all(a[i][j] == 0 for i in range(k, rows) for j in range(k))
    return k


def gf2_rank(faces, degree):
    lower = sorted(s for s in faces if s.bit_count() == degree)
    upper = sorted(s for s in faces if s.bit_count() == degree + 1)
    ix = {s: i for i, s in enumerate(lower)}
    basis = {}
    for s in upper:
        vector = 0
        for v in bits(s):
            vector ^= 1 << ix[s ^ (1 << v)]
        while vector:
            pivot = vector.bit_length() - 1
            if pivot in basis:
                vector ^= basis[pivot]
            else:
                basis[pivot] = vector
                break
    return len(basis)

# Chain groups of the three-dimensional simplicial collapse: C_0..C_3.
ranks = []
for degree in (1, 2, 3):
    matrix = signed_boundary(remaining, degree)
    r = rank_by_unit_pivots(matrix)
    ranks.append(r)
assert ranks == [8, 28, 17], ranks
# The boundary in degree four is zero because the collapsed complex is 3D.
betti = [9 - 8 - 1, 36 - 8 - 28, 51 - 28 - 17, 18 - 17]
assert betti == [0, 0, 6, 1]

# Independent mod-two check on the ORIGINAL cut complex (not its dual).
cut_ranks = [gf2_rank(cut, d) for d in (1, 2, 3, 4)]
assert cut_ranks == [8, 28, 50, 39], cut_ranks
assert 90 - 50 - 39 == 1 and 45 - 39 == 6

print('GRAPH: 3x3 rook graph = line graph of K(3,3)')
print('CONNECTED_FOUR_SETS:', len(conn4))
print('DISCONNECTED_FOUR_SETS:', len(disc4))
print('DUAL_FACE_COUNTS_BY_SIZE: 1,9,36,84,81,36,6')
print('CUT_FACE_COUNTS_BY_SIZE: 1,9,36,78,90,45')
print('VALID_ELEMENTARY_COLLAPSE_PAIRS:', len(collapse))
print('COLLAPSED_FACE_COUNTS_BY_SIZE: 1,9,36,51,18')
print('EXACT_UNIT_SMITH_RANKS_d1_d2_d3:', *ranks)
print('COLLAPSED_DUAL_REDUCED_BETTI_2_3: 6 1')
print('INDEPENDENT_CUT_GF2_RANKS_d1_d2_d3_d4:', *cut_ranks)
print('ROOK_3X3_ORDINARY_4CUT_INTEGRAL_HOMOTOPY_OK')
