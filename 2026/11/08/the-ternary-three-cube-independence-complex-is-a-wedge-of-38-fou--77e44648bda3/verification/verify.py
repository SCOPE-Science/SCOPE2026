"""Self-contained exact certificate for the independence complex of H(3,3).
Run: python3 verification/verify.py
"""
from collections import Counter, deque
from itertools import product

VERTICES = list(product(range(3), repeat=3))
N = len(VERTICES)
ADJ = [sum(1 << j for j, w in enumerate(VERTICES)
           if sum(x != y for x, y in zip(v, w)) == 1)
       for v in VERTICES]

# Generator A: recursive independent-set enumeration, each set appears exactly once.
faces = []
def visit(s, remaining):
    faces.append(s)
    while remaining:
        b = remaining & -remaining
        remaining ^= b
        visit(s | b, remaining & ~ADJ[b.bit_length() - 1])
visit(0, (1 << N) - 1)
face_set = set(faces)
assert len(face_set) == len(faces)

# Generator B: each 3-by-3 layer is a partial permutation matrix;
# across layers, occupancy at the same (second, third) coordinate is forbidden.
layer_faces = []
for m in range(1 << 9):
    occ = [(r, c) for r in range(3) for c in range(3)
           if (m >> (3 * r + c)) & 1]
    if (len({r for r, c in occ}) == len(occ)
            and len({c for r, c in occ}) == len(occ)):
        layer_faces.append(m)
faces_b = {(a | (b << 9) | (c << 18))
           for a in layer_faces for b in layer_faces for c in layer_faces
           if not (a & b or a & c or b & c)}
assert faces_b == face_set
assert len(face_set) == 11776
assert len(layer_faces) == 34
counts = Counter(f.bit_count() for f in faces)
assert [counts[d] for d in range(10)] == [1,27,270,1278,3078,3834,2412,756,108,12]

# A fixed complete vertex order, discovered by finite search and now part
# of the independently replayable certificate. Pair lower s with upper s+v
# at the first stage at which both remain available.
PIVOTS = [3,14,10,17,5,0,7,21,19,18,23,25,4,2,22,6,11,20,9,26,15,16,8,1,13,24,12]
assert sorted(PIVOTS) == list(range(N))
remaining = set(face_set)
match = {}
for v in PIVOTS:
    bit = 1 << v
    for s in sorted(remaining):
        if not(s & bit) and (s | bit) in remaining:
            remaining.remove(s)
            remaining.remove(s | bit)
            match[s] = s | bit
assert len(match) == 5869
assert 0 in match
assert len(remaining) == 38 and {s.bit_count() for s in remaining} == {5}

# Remove the empty-simplex pair to obtain an ordinary acyclic Morse
# matching, with one critical vertex and 38 critical dimension-four cells.
critical_vertex = match.pop(0)
nonempty = [s for s in faces if s]
idx = {s: i for i, s in enumerate(nonempty)}
indegree = [0] * len(nonempty)
out = [[] for _ in nonempty]
cover_relations = 0
for high in nonempty:
    bits = high
    while bits:
        b = bits & -bits
        bits ^= b
        low = high ^ b
        if low == 0:
            continue
        cover_relations += 1
        if match.get(low) == high:
            a, c = idx[low], idx[high]  # matched edge reversed
        else:
            a, c = idx[high], idx[low]  # unmatched edge downward
        out[a].append(c)
        indegree[c] += 1
assert cover_relations == 56592
q = deque(i for i, deg in enumerate(indegree) if deg == 0)
visited = 0
while q:
    i = q.popleft()
    visited += 1
    for j in out[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)
assert visited == len(nonempty), "The directed Hasse graph has a cycle"
assert len(match) == 5868
assert 2 * len(match) + 39 == len(nonempty)

# Independent mod-two check directly on the full simplicial chain complex.
# For each dimension d, reduce the columns of d_boundary modulo two.
by_dim = [[s for s in faces if s.bit_count() == d + 1] for d in range(9)]
ranks = [0]
for d in range(1, 9):
    previous = {s: i for i, s in enumerate(by_dim[d - 1])}
    piv = {}
    for high in by_dim[d]:
        bits = high
        column = 0
        while bits:
            b = bits & -bits
            bits ^= b
            column ^= 1 << previous[high ^ b]
        while column:
            lead = column.bit_length() - 1
            if lead in piv:
                column ^= piv[lead]
            else:
                piv[lead] = column
                break
    ranks.append(len(piv))
betti = [len(by_dim[d]) - ranks[d] - (ranks[d + 1] if d < 8 else 0)
         for d in range(9)]
assert betti == [1,0,0,0,38,0,0,0,0], (ranks, betti)
assert sum((-1) ** d * len(by_dim[d]) for d in range(9)) == 39

print('graph_vertices', N, 'graph_edges', sum(a.bit_count() for a in ADJ) // 2)
print('layer_placements', len(layer_faces))
print('all_faces_including_empty', len(face_set))
print('face_vector_nonempty', [counts[d] for d in range(1,10)])
print('full_matching_pairs_including_empty', 5869)
print('ordinary_matching_pairs', len(match))
print('critical_ordinary_cells', {0: 1, 4: 38})
print('oriented_hasse_edges', cover_relations)
print('acyclicity_toposort_visited', visited)
print('mod2_boundary_ranks', ranks)
print('mod2_betti', betti)
print('homotopy_type', 'wedge of 38 copies of S^4')
print('ALL_TERNARY_ROOK_COMPLEX_CHECKS_PASS')
