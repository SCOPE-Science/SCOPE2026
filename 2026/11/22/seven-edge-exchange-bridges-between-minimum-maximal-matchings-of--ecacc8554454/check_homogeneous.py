"""Independent exhaustive check via homogeneous GF(4) coordinates and vectorized bit arithmetic.
Run with Python 3 and NumPy. The C++ checker uses unrelated affine slope coordinates.
"""
from itertools import combinations
from collections import Counter, deque
import numpy as np


def times(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        if a & 4:
            a ^= 0b111
        b >>= 1
    return out


def normalize(v):
    c = next(t for t in v if t)
    inv = next(t for t in (1, 2, 3) if times(c, t) == 1)
    return tuple(times(t, inv) for t in v)


points = sorted({normalize((a,b,c)) for a in range(4)
                 for b in range(4) for c in range(4) if a or b or c})
forms = points
assert len(points) == len(forms) == 21
inc = [[int(times(x[0], y[0]) ^ times(x[1], y[1]) ^ times(x[2], y[2]) == 0)
        for y in forms] for x in points]
assert all(sum(row) == 5 for row in inc)
assert all(sum(inc[i][j] for i in range(21)) == 5 for j in range(21))
line_bitsets = [sum(inc[i][j] << i for i in range(21)) for j in range(21)]
edge_idx = {(i,j):k for k,(i,j) in enumerate((i,j) for i in range(21) for j in range(21) if inc[i][j])}
assert len(edge_idx) == 105

hyperovals = []
for combo in combinations(range(21), 6):
    mask = sum(1 << t for t in combo)
    if any((mask & line).bit_count() > 2 for line in line_bitsets):
        continue
    dual = tuple(j for j, line in enumerate(line_bitsets) if mask & line == 0)
    assert len(dual) == 6
    hyperovals.append((combo, dual))
assert len(hyperovals) == 168

fibers = []
for xx, yy in hyperovals:
    remaining_points = [i for i in range(21) if i not in xx]
    remaining_lines = [j for j in range(21) if j not in yy]
    assert all(sum(inc[p][j] for j in remaining_lines) == 3 for p in remaining_points)
    solutions = []
    def visit(k, used, mask):
        if k == 15:
            solutions.append(mask)
            return
        p = remaining_points[k]
        for l in remaining_lines:
            if inc[p][l] and not (used >> l) & 1:
                visit(k+1, used | (1 << l), mask | (1 << edge_idx[p,l]))
    visit(0, 0, 0)
    assert len(solutions) == 288
    fibers.append(solutions)

# Distinct incidence model and direct complete enumeration of the edge subset in each fiber.
# The 105-bit edge set is split into two uint64 lanes for vectorized pairwise intersections.
lanes = []
for solutions in fibers:
    lanes.append((np.array([s & ((1 << 64)-1) for s in solutions], dtype=np.uint64),
                  np.array([s >> 64 for s in solutions], dtype=np.uint64)))

within_edges = 0
within_four = 0
in_degree_hist = Counter()
for lo, hi in lanes:
    cnt = np.bitwise_count(lo[:,None] & lo[None,:]) + np.bitwise_count(hi[:,None] & hi[None,:])
    assert np.all(np.diag(cnt) == 15)
    eq_four = cnt == 11
    all_seven = (cnt >= 8) & (cnt < 15)
    deg4 = eq_four.sum(axis=1)
    deg7 = all_seven.sum(axis=1)
    assert np.all(deg4 == 10)
    assert np.all((cnt <= 11) | np.eye(288, dtype=bool))
    seen = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in np.flatnonzero(eq_four[u]):
            v = int(v)
            if v not in seen:
                seen.add(v)
                queue.append(v)
    assert len(seen) == 288
    assert sorted(Counter(map(int,deg7)).items()) == [(37,144),(41,144)]
    within_four += int(eq_four.sum())//2
    within_edges += int(all_seven.sum())//2
    in_degree_hist.update(map(int,deg7))
assert within_four == 241920 and within_edges == 943488

edges_between = 0
pair_counts = Counter()
cross_degree = np.zeros((168,288), dtype=np.uint16)
quotient = [[] for _ in range(168)]
for i in range(168):
    x, y = hyperovals[i]
    for j in range(i+1, 168):
        a, b = hyperovals[j]
        r = len(set(x) & set(a))
        s = len(set(y) & set(b))
        pair_counts[(r,s)] += 1
        assert r == s and r <= 3
        if r < 3:
            continue
        a0,a1 = lanes[i]
        b0,b1 = lanes[j]
        intersection = np.bitwise_count(a0[:,None] & b0[None,:]) + np.bitwise_count(a1[:,None] & b1[None,:])
        assert np.all(intersection <= 8), 'No cross-fiber exchanges of size six or smaller'
        moves = (intersection == 8)
        assert int(moves.sum()) == 216
        cross_degree[i] += moves.sum(axis=1, dtype=np.uint16)
        cross_degree[j] += moves.sum(axis=0, dtype=np.uint16)
        quotient[i].append(j)
        quotient[j].append(i)
        edges_between += int(moves.sum())
assert pair_counts == Counter({(0,0):840,(1,1):6048,(2,2):3780,(3,3):3360})
assert edges_between == 725760
assert np.all(cross_degree == 30)
assert all(len(v) == 40 for v in quotient)
for start in range(168):
    d = [-1]*168
    d[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in quotient[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                queue.append(v)
    assert min(d) == 0 and max(d) == 2
assert edges_between + within_edges == 1669248
assert dict(sorted(in_degree_hist.items())) == {37:24192,41:24192}
print('PASS: 168 hyperovals; 288 perfect matchings per fiber; 48384 size-15 minima')
print('PASS: all 3360 triple-intersection hyperoval pairs: exactly 216 seven-edge bridges each, zero six-edge bridges')
print('PASS: 4-edge within-fiber connected, cross-fiber seven-edge quotient connected of diameter 2')
print('PASS: 725760 cross edges; 943488 internal edges; 1669248 total seven-exchange edges')
print('PASS: global degrees 67 and 71: 24192 vertices of each; all cross degrees 30')
