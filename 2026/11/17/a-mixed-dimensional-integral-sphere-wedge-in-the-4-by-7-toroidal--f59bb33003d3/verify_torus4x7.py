"""Exact, standalone certificate for the toroidal 4-by-7 hard-square complex.

Only Python 3 standard-library modules are required. No external data is read.
"""
from collections import Counter, deque
from functools import lru_cache

ROWS, COLS = 4, 7
N = ROWS * COLS
ORDER_A = (20, 1, 14, 12, 18, 5, 0, 16, 27, 9, 22, 10, 26, 13,
           7, 24, 19, 15, 23, 17, 21, 8, 6, 4, 2, 25, 11, 3)
ORDER_B = (15, 17, 6, 20, 19, 21, 23, 7, 10, 25, 14, 24, 4, 2,
           12, 1, 26, 11, 16, 27, 5, 9, 18, 0, 13, 22, 8, 3)

# The vertex (a,b) is encoded by bit a*COLS+b.
adjacency = [0] * N
for a in range(ROWS):
    for b in range(COLS):
        i = a * COLS + b
        for aa, bb in (((a + 1) % ROWS, b), ((a - 1) % ROWS, b),
                       (a, (b + 1) % COLS), (a, (b - 1) % COLS)):
            adjacency[i] |= 1 << (aa * COLS + bb)
assert all(x.bit_count() == 4 for x in adjacency)
assert sum(x.bit_count() for x in adjacency) // 2 == 56

# Complete face enumeration, including the empty face; never a sample.
faces = [0]
for i in range(N):
    v = 1 << i
    faces += [mask | v for mask in faces if not (mask & adjacency[i])]
face_set = set(faces)
assert len(face_set) == len(faces) == 96433
face_vector = Counter(mask.bit_count() - 1 for mask in faces)
expected_vector = {-1: 1, 0: 28, 1: 322, 2: 1988, 3: 7266,
                   4: 16464, 5: 23786, 6: 22540, 7: 14602,
                   8: 6748, 9: 2198, 10: 448, 11: 42}
assert face_vector == expected_vector
assert sum((-1 if (k % 2) else 1) * v for k,v in face_vector.items()) == -1


def greedy_matching(order):
    assert sorted(order) == list(range(N))
    unpaired = face_set.copy()
    pairs = []
    for i in order:
        bit = 1 << i
        current = [(x, x | bit) for x in unpaired
                   if x != 0 and not (x & bit) and (x | bit) in unpaired]
        for lower, upper in current:
            assert lower in unpaired and upper in unpaired
            unpaired.remove(lower)
            unpaired.remove(upper)
        pairs.extend(current)
    assert len(pairs) * 2 + len(unpaired) == len(faces)
    assert 0 in unpaired
    assert all(y.bit_count() == x.bit_count() + 1 and x & y == x
               for x, y in pairs)
    return unpaired, pairs


def check_acyclic(pairs):
    # Orient every unmatched cover upward, every paired cover downward.
    # Kahn elimination exhausts the *entire* Hasse digraph, not a sample.
    matched = set(pairs)
    ids = {x: i for i, x in enumerate(faces)}
    indegree = [0] * len(faces)
    outgoing = [[] for _ in faces]
    covers = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            lower = upper ^ bit
            if (lower, upper) in matched:
                src, dst = ids[upper], ids[lower]
            else:
                src, dst = ids[lower], ids[upper]
            outgoing[src].append(dst)
            indegree[dst] += 1
            covers += 1
    queue = deque(i for i, d in enumerate(indegree) if d == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in outgoing[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert visited == len(faces), (visited, len(faces))
    return covers


def boundary(x):
    bits = x
    parity = 1
    while bits:
        bit = bits & -bits
        bits -= bit
        yield x ^ bit, parity
        parity = -parity


def morse_boundary(critical, pairs):
    """Signed gradient paths from critical 6-cells to critical 5-cells."""
    uppair = dict(pairs)
    downpair = {y: x for x, y in pairs}
    critical5 = sorted(c for c in critical if c.bit_count() == 6)
    critical6 = sorted(c for c in critical if c.bit_count() == 7)
    assert all(x not in uppair and x not in downpair for x in critical5)

    @lru_cache(None)
    def project_five(x):
        if x in critical:
            assert x in critical5
            return {x: 1}
        if x in downpair:  # not the lower element of a 5--6 pair
            return {}
        y = uppair[x]
        assert x.bit_count() == 6 and y.bit_count() == 7
        edges = list(boundary(y))
        incidence = next(s for w, s in edges if w == x)
        ans = Counter()
        for w, s in edges:
            if w == x:
                continue
            for z, coefficient in project_five(w).items():
                ans[z] -= incidence * s * coefficient
        return {z: coefficient for z, coefficient in ans.items() if coefficient}

    rows = []
    for cell in critical6:
        ans = Counter()
        for face, sign in boundary(cell):
            for z, coefficient in project_five(face).items():
                ans[z] += sign * coefficient
        rows.append([ans[c] for c in critical5])
    return critical5, critical6, rows, project_five.cache_info().currsize


def determinant3(a):
    return (a[0][0] * (a[1][1]*a[2][2]-a[1][2]*a[2][1])
          - a[0][1] * (a[1][0]*a[2][2]-a[1][2]*a[2][0])
          + a[0][2] * (a[1][0]*a[2][1]-a[1][1]*a[2][0]))


for name, order in [('A', ORDER_A), ('B', ORDER_B)]:
    critical, pairs = greedy_matching(order)
    covers = check_acyclic(pairs)
    crit5, crit6, matrix, explored = morse_boundary(critical, pairs)
    crit_counts = dict(sorted(Counter(x.bit_count() - 1 for x in critical).items()))
    print(name, 'simplices', len(faces), 'pairs', len(pairs),
          'critical_by_dimension', crit_counts, 'covers', covers)
    print(name, 'critical_5_cells', crit5, 'critical_6_cells', crit6,
          'morse_boundary_6_to_5', matrix, 'gradient_faces', explored)
    if name == 'A':
        assert crit_counts == {-1:1, 0:1, 5:2, 6:1}
        assert crit5 == [41960481, 67127817]
        assert crit6 == [36307268]
        assert matrix == [[0,0]]
    else:
        assert crit_counts == {-1:1, 0:1, 5:5, 6:4}
        assert matrix == [[0,-1,0,0,1],[-1,0,0,-1,0],
                          [1,0,-1,0,0],[0,0,1,1,0]]
        # The first three rows and first three columns have unit determinant;
        # last row = - (second row + third row). Thus exact rank three.
        assert abs(determinant3([row[:3] for row in matrix[:3]])) == 1
        assert all(matrix[1][j]+matrix[2][j]+matrix[3][j]==0
                   for j in range(5))
print('TORUS_4X7_TWO_FIVE_SPHERES_ONE_SIX_SPHERE_PASS')
