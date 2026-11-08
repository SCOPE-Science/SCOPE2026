"""Standalone finite certificate for the diagonal-deleted five-by-five chessboard complex."""
import collections
import itertools
from sympy import MutableSparseMatrix
from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix

N = 5
EDGES = tuple((i, j) for i in range(N) for j in range(N) if i != j)
ORDER = (19, 9, 10, 17, 16, 3, 11, 14, 4, 8, 0, 7, 2, 6, 1, 15, 18, 5, 13, 12)
FACES = []
for k in range(N + 1):
    fs = []
    for ids in itertools.combinations(range(len(EDGES)), k):
        if len({EDGES[i][0] for i in ids}) == k and len({EDGES[i][1] for i in ids}) == k:
            fs.append(ids)
    FACES.append(fs)
INDEX = [{f: i for i, f in enumerate(fs)} for fs in FACES]
MASKS = {sum(1 << v for v in fs) for fs in sum(FACES, [])}
assert [len(a) for a in FACES] == [1, 20, 130, 320, 265, 44]

# Greedy consecutive toggle matching on all faces, including empty.
remaining = set(MASKS)
matched = set()
for v in ORDER:
    bit = 1 << v
    for mask in tuple(remaining):
        if mask & bit:
            continue
        upper = mask | bit
        if upper in remaining:
            remaining.remove(mask)
            remaining.remove(upper)
            matched.add((mask, upper))
assert len(matched) == 383 and (0, 1 << ORDER[0]) in matched
# Replace the empty-face matching by a critical vertex in the ordinary complex.
matched.remove((0, 1 << ORDER[0]))
critical = remaining | {1 << ORDER[0]}
assert collections.Counter(m.bit_count() - 1 for m in critical) == {0: 1, 2: 1, 3: 13}

# Exhaustive Forman acyclicity test: reverse each matched Hasse cover.
faces = MASKS - {0}
out = {m: [] for m in faces}
indeg = {m: 0 for m in faces}
cover_count = 0
for low in faces:
    for v in range(len(EDGES)):
        bit = 1 << v
        if low & bit:
            continue
        high = low | bit
        if high not in faces:
            continue
        cover_count += 1
        a, b = (low, high) if (low, high) in matched else (high, low)
        out[a].append(b)
        indeg[b] += 1
queue = collections.deque(v for v, d in indeg.items() if d == 0)
visited = 0
while queue:
    v = queue.popleft()
    visited += 1
    for w in out[v]:
        indeg[w] -= 1
        if indeg[w] == 0:
            queue.append(w)
assert visited == len(faces) == 779
print('ACYCLIC_MORSE_MATCHING_PASS faces=779 pairs=382 covers=%d critical=(1,0,1,13,0)' % cover_count)

# Exact characteristic-zero augmented boundary ranks, independently of the matching.
ranks = [0]
for k in range(1, N + 1):
    row_index = INDEX[k - 1]
    entries = {}
    for j, simplex in enumerate(FACES[k]):
        for t in range(k):
            entries[row_index[simplex[:t] + simplex[t+1:]], j] = (-1) ** t
    boundary = MutableSparseMatrix(len(FACES[k-1]), len(FACES[k]), entries)
    ranks.append(DomainMatrix.from_Matrix(boundary).convert_to(QQ).rank())
assert ranks == [0, 1, 19, 111, 208, 44]
assert [len(FACES[k]) - ranks[k] - ranks[k+1] for k in range(1, 5)] == [0, 0, 1, 13]
print('EXACT_Q_CHAIN_RANKS_PASS ranks_d1_to_d5=(1,19,111,208,44) betti=(0,0,1,13,0)')

# H_2 nonzero witness: octahedral 2-sphere as join of three 0-spheres.
# Each of these two-element groups consists of incompatible board squares;
# squares chosen from distinct groups are pairwise compatible.
OCTAHEDRAL_PAIRS = ((0, 1), (4, 6), (11, 15))
def inversion_sign(seq):
    return (-1) ** sum(x > y for i, x in enumerate(seq) for y in seq[i+1:])

sphere = collections.defaultdict(int)
for choices in itertools.product((0, 1), repeat=3):
    verts = tuple(OCTAHEDRAL_PAIRS[k][choices[k]] for k in range(3))
    sphere[INDEX[3][tuple(sorted(verts))]] += inversion_sign(verts) * (-1) ** sum(choices)
assert len(sphere) == 8 and set(abs(x) for x in sphere.values()) == {1}
boundary_z = collections.defaultdict(int)
for col, coeff in sphere.items():
    tri = FACES[3][col]
    for i in range(3):
        boundary_z[INDEX[2][tri[:i] + tri[i+1:]]] += (-1) ** i * coeff
assert not any(boundary_z.values())

# Mod-three column reduction for im(d_3): this tests nontriviality of the
# specific integral sphere and its images, not rational rank or integral torsion.
B = {}
def mod_reduce(vec):
    v = {i: a % 3 for i, a in vec.items() if a % 3}
    while v:
        lead = max(v)
        if lead not in B:
            break
        factor = v[lead]
        for i, a in B[lead].items():
            z = (v.get(i, 0) - factor * a) % 3
            if z:
                v[i] = z
            else:
                v.pop(i, None)
    return v
for tetrahedron in FACES[4]:
    vec = {INDEX[3][tetrahedron[:i] + tetrahedron[i+1:]]: (-1) ** i for i in range(4)}
    res = mod_reduce(vec)
    if res:
        top = max(res)
        inv = pow(res[top], -1, 3)
        B[top] = {i: (a*inv)%3 for i, a in res.items()}
assert len(B) == 208 and mod_reduce(sphere)

def cycle_transform(z, p, transpose):
    action = {i: EDGES.index((p[b], p[a]) if transpose else (p[a], p[b]))
              for i, (a, b) in enumerate(EDGES)}
    w = collections.defaultdict(int)
    for index, coeff in z.items():
        images = [action[i] for i in FACES[3][index]]
        w[INDEX[3][tuple(sorted(images))]] += inversion_sign(images) * coeff
    return w
identity = tuple(range(5))
transposition = (1, 0, 2, 3, 4)
for transformation, transpose, expected in ((transposition, False, 1), (identity, True, -1)):
    mapped = cycle_transform(sphere, transformation, transpose)
    assert not mod_reduce({i: mapped.get(i, 0)-expected*sphere.get(i, 0)
                           for i in set(mapped)|set(sphere)})
    assert mod_reduce({i: mapped.get(i, 0)+expected*sphere.get(i, 0)
                       for i in set(mapped)|set(sphere)})
print('INTEGRAL_SPHERE_MOD3_SYMMETRY_PASS sphere_triangles=8 H2_transposition=+1 H2_transpose=-1')

# Full 240-element signed simplicial Hopf traces.  H_2 is the trivial
# S_5 line, with transpose acting by -1, as established above.
def count_fixed_and_twocycles(p):
    f = sum(p[i] == i for i in range(5))
    two = sum(i < j and p[i] == j and p[j] == i for i in range(5) for j in range(5))
    return f, two

def trace_reduced_chain_action(p, transpose):
    mapping = [EDGES.index((p[b], p[a]) if transpose else (p[a], p[b]))
               for a, b in EDGES]
    traces = []
    for layer in FACES[1:]:
        traces.append(sum(inversion_sign([mapping[i] for i in simplex])
                          for simplex in layer if set(map(mapping.__getitem__, simplex)) == set(simplex)))
    return -1 + sum((-1) ** k * tr for k, tr in enumerate(traces))

class_results = {}
for p in itertools.permutations(range(5)):
    f, t = count_fixed_and_twocycles(p)
    parity = inversion_sign(p)
    for transpose in (False, True):
        standard = f - 1
        twisted_standard = parity * (f - 1)
        two_row = f * (f-1)//2 + t - f
        h3 = standard + (-twisted_standard if transpose else twisted_standard) + two_row
        h2 = -1 if transpose else 1
        lef = trace_reduced_chain_action(p, transpose)
        assert lef == h2 - h3, (p, transpose, lef, h2, h3)
        # A class label is the multiset of permutation cycle lengths.
        seen = set()
        cycles = []
        for i in range(5):
            if i not in seen:
                j, length = i, 0
                while j not in seen:
                    seen.add(j)
                    j = p[j]
                    length += 1
                cycles.append(length)
        label = (tuple(sorted(cycles, reverse=True)), int(transpose))
        if label in class_results:
            assert class_results[label] == (h2, h3)
        class_results[label] = (h2, h3)
assert len(class_results) == 14
print('ALL_GROUP_ACTIONS_PASS elements=240 classes=14')
for (cycle_type, transpose), (h2,h3) in sorted(class_results.items()):
    print('class %s transpose=%d H2=%d H3=%d' % (cycle_type, transpose,h2,h3))
print('DIAGONAL_DELETION_HOMOTOPY_AND_SYMMETRY_PASS')
