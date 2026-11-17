"""Reconstruct the Petersen matching complex and its integral Morse and rational symmetry data.

Python 3 standard library only; no precomputed topology tables or external files.
The Petersen graph is KG(5,2): two vertices are adjacent exactly when disjoint.
"""
from itertools import combinations, permutations
from collections import Counter, deque
from functools import lru_cache

POINTS = tuple(combinations(range(5), 2))
point_index = {p: i for i, p in enumerate(POINTS)}
EDGES = tuple((i, j) for i, u in enumerate(POINTS)
              for j, v in enumerate(POINTS) if i < j and set(u).isdisjoint(v))
edge_index = {e: i for i, e in enumerate(EDGES)}
FACES = {k - 1: [] for k in range(1, 6)}
for size in range(1, 6):
    for face in combinations(range(len(EDGES)), size):
        endpoints = [v for edge_id in face for v in EDGES[edge_id]]
        if len(set(endpoints)) == 2 * size:
            FACES[size - 1].append(face)
INDEX = {dimension: {f: i for i, f in enumerate(fs)}
         for dimension, fs in FACES.items()}
assert len(EDGES) == 15
assert [len(FACES[d]) for d in range(5)] == [15, 75, 145, 90, 6]

# Fixed matching on the augmented face poset; deleting its empty-face pair
# produces an ordinary discrete Morse matching with one critical vertex.
PIVOTS = (1, 11, 9, 8, 2, 7, 0, 3, 14, 5, 4, 13, 10, 6, 12)
remaining = {(): None}
remaining.update({f: None for fs in FACES.values() for f in fs})
remaining = set(remaining)
augmented_pairs = []
for v in PIVOTS:
    pairs = [(f, tuple(sorted(f + (v,)))) for f in remaining if v not in f
             and tuple(sorted(f + (v,))) in remaining]
    for lower, upper in pairs:
        assert lower in remaining and upper in remaining
        remaining.remove(lower)
        remaining.remove(upper)
    augmented_pairs.extend(pairs)
assert len(augmented_pairs) == 161
assert ((), (1,)) in augmented_pairs
pairs = [(lo, up) for lo, up in augmented_pairs if lo]
crit = remaining | {(1,)}
assert Counter(map(len, crit)) == Counter({1: 1, 3: 5, 4: 5})
crit2 = tuple(sorted(f for f in crit if len(f) == 3))
crit3 = tuple(sorted(f for f in crit if len(f) == 4))
low_up = dict(pairs)
up_low = {up: lo for lo, up in pairs}
assert len(low_up) == len(up_low) == 160

# Exhaustive Hasse-diagram cycle test: every unmatched cover is directed down,
# every matched cover is directed up. This certifies Forman acyclicity.
all_faces = set(f for fs in FACES.values() for f in fs)
assert len(all_faces) == 331
successors = {f: [] for f in all_faces}
in_degree = {f: 0 for f in all_faces}
for upper in all_faces:
    for j in range(len(upper)):
        lower = upper[:j] + upper[j + 1:]
        if not lower:
            continue
        if low_up.get(lower) == upper:
            source, target = lower, upper
        else:
            source, target = upper, lower
        successors[source].append(target)
        in_degree[target] += 1
queue = deque(f for f in all_faces if in_degree[f] == 0)
visited = 0
while queue:
    f = queue.popleft()
    visited += 1
    for g in successors[f]:
        in_degree[g] -= 1
        if in_degree[g] == 0:
            queue.append(g)
assert visited == len(all_faces)

# Exact integral gradient-path reduction of the critical degree-three boundary.
# A matched lower 2-face is replaced via the signed boundary of its upper
# 3-face; a 2-face matched down to a 1-face contributes no critical 2-cell.
def incidence(face, simplex):
    for j in range(len(simplex)):
        if simplex[:j] + simplex[j + 1:] == face:
            return (-1) ** j
    raise ValueError('not a codimension-one face')

@lru_cache(None)
def reduce_to_critical_2(face):
    if face in crit:
        return {face: 1} if len(face) == 3 else {}
    if face in low_up:
        upper = low_up[face]
        assert len(face) == 3 and len(upper) == 4
        pivot = incidence(face, upper)
        out = {}
        for j in range(4):
            child = upper[:j] + upper[j + 1:]
            if child == face:
                continue
            for c, coefficient in reduce_to_critical_2(child).items():
                out[c] = out.get(c, 0) - ((-1) ** j) * coefficient * pivot
        return {c: value for c, value in out.items() if value}
    assert face in up_low  # this 2-face is an upper partner of a 1-face
    return {}

morse_boundary = []
for top in crit3:
    out = Counter()
    for j in range(4):
        child = top[:j] + top[j + 1:]
        for c, coeff in reduce_to_critical_2(child).items():
            out[c] += ((-1) ** j) * coeff
    morse_boundary.append([out[c] for c in crit2])
assert morse_boundary == [[0] * 5 for _ in range(5)], morse_boundary

# The Morse CW model has a point, five 2-cells, five 3-cells, and zero
# integer cellular boundary. By pi_2(wedge^5 S^2)=Z^5, all 3-cell
# attaching maps are nullhomotopic, giving the claimed integral wedge.

# Rational homology characters are computed without forming dense rational
# homology matrices: the image of boundary d_3 is a rational S_5 submodule.
# Its character is the trace of the induced action on a chosen basis of image d_3.
def invert_mod(matrix, prime):
    n = len(matrix)
    a = [[x % prime for x in row] + [int(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for i in range(n):
        j = next(j for j in range(i, n) if a[j][i] % prime)
        a[i], a[j] = a[j], a[i]
        inv = pow(a[i][i], -1, prime)
        a[i] = [(x * inv) % prime for x in a[i]]
        for j in range(n):
            if j == i or not a[j][i]:
                continue
            v = a[j][i]
            a[j] = [(x - v * y) % prime for x, y in zip(a[j], a[i])]
    return [row[n:] for row in a]

def pivots_of_columns(columns, prime):
    """Indices of independent ordered columns, by exact mod-prime elimination."""
    echelon = {}
    picked = []
    for j, col in enumerate(columns):
        v = dict((i, a % prime) for i, a in enumerate(col) if a % prime)
        while v:
            r = min(v)
            if r not in echelon:
                inverse = pow(v[r], -1, prime)
                echelon[r] = {k: (a * inverse) % prime for k, a in v.items()}
                picked.append(j)
                break
            scale = v[r]
            for k, a in echelon[r].items():
                t = (v.get(k, 0) - scale * a) % prime
                if t:
                    v[k] = t
                else:
                    v.pop(k, None)
    return picked

D3_columns = []
for face in FACES[3]:
    col = [0] * len(FACES[2])
    for j in range(4):
        col[INDEX[2][face[:j] + face[j + 1:]]] = (-1) ** j
    D3_columns.append(col)

pivcols = pivots_of_columns(D3_columns, 1009)
assert len(pivcols) == 79
chosen_cols = [D3_columns[i] for i in pivcols]
pivrows = pivots_of_columns(chosen_cols and list(zip(*chosen_cols)), 1009)
assert len(pivrows) == 79
rowlookup = {r: k for k, r in enumerate(pivrows)}

def permutation_sign(values):
    return -1 if sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i + 1, len(values))) % 2 else 1

def compute_characters(prime):
    A = [[chosen_cols[j][i] for j in range(79)] for i in pivrows]
    inv = invert_mod(A, prime)
    results = {}
    counts = Counter()
    for g in permutations(range(5)):
        point_perm = [point_index[tuple(sorted(g[a] for a in pair))]
                      for pair in POINTS]
        edge_perm = [edge_index[tuple(sorted((point_perm[i], point_perm[j])))]
                     for i, j in EDGES]
        seen = set()
        lengths = []
        for i in range(5):
            if i not in seen:
                j, length = i, 0
                while j not in seen:
                    seen.add(j)
                    j = g[j]
                    length += 1
                lengths.append(length)
        cycle_type = tuple(sorted(lengths, reverse=True))
        counts[cycle_type] += 1
        chain_trace = []
        for d in range(5):
            s = 0
            for face in FACES[d]:
                image = [edge_perm[i] for i in face]
                if sorted(image) == list(face):
                    s += permutation_sign(image)
            chain_trace.append(s)
        boundary_trace = 0
        for i, j in enumerate(pivcols):
            top = FACES[3][j]
            image = [edge_perm[t] for t in top]
            ordered = tuple(sorted(image))
            assert ordered in INDEX[3]
            total_sign = permutation_sign(image)
            for t in range(4):
                boundary_face = ordered[:t] + ordered[t + 1:]
                r = INDEX[2][boundary_face]
                if r in rowlookup:
                    boundary_trace += inv[i][rowlookup[r]] * total_sign * ((-1) ** t)
        boundary_trace %= prime
        if boundary_trace > prime // 2:
            boundary_trace -= prime
        # Finite-order rational matrices have integer traces bounded by rank 79.
        assert -79 <= boundary_trace <= 79
        H2 = chain_trace[2] - boundary_trace - chain_trace[1] + chain_trace[0] - 1
        H3 = chain_trace[3] - chain_trace[4] - boundary_trace
        if cycle_type in results:
            assert results[cycle_type] == (H2, H3, boundary_trace)
        else:
            results[cycle_type] = (H2, H3, boundary_trace)
    return results, counts

char1, counts = compute_characters(1009)
char2, counts2 = compute_characters(1013)
assert counts == counts2 and char1 == char2
assert sum(counts.values()) == 120
assert counts[(1,1,1,1,1)] == 1
assert char1[(1,1,1,1,1)][:2] == (5,5)

# The degree-two module is sign times the natural five-point permutation
# representation. The degree-three module has character norm one and is
# therefore absolutely irreducible over Q; its S_5 partition is (3,2).
for cycle_type, (h2, h3, _) in char1.items():
    sign = (-1) ** (5 - len(cycle_type))
    assert h2 == sign * cycle_type.count(1)
    fixed_points = cycle_type.count(1)
    fixed_two_subsets = fixed_points * (fixed_points - 1) // 2 + cycle_type.count(2)
    assert h3 == fixed_two_subsets - fixed_points
assert sum(counts[t] * char1[t][1] ** 2 for t in counts) == 120
assert sum(counts[t] * char1[t][0] ** 2 for t in counts) == 240
assert sum(counts[t] * char1[t][0] * char1[t][1] for t in counts) == 0
assert sum(counts[t] * char1[t][0] for t in counts) == 0
assert sum(counts[t] * char1[t][1] for t in counts) == 0
assert sum(counts[t] * char1[t][0] for t in counts
           if (5 - len(t)) % 2 == 0) == 60
assert sum(counts[t] * char1[t][1] for t in counts
           if (5 - len(t)) % 2 == 0) == 0
print('FACE_COUNTS 15 75 145 90 6')
print('MORSE_CRITICAL 0:1 2:5 3:5; ACYCLIC_HASSE 331')
print('EXACT_MORSE_BOUNDARY', morse_boundary)
print('HOMOLOGY H2=Z^5 H3=Z^5; HOMOTOPY wedge(5 S2,5 S3)')
print('CHARACTER_TABLE type class_size H2 H3')
for t in sorted(counts, reverse=True):
    print(' '.join(map(str,t)), counts[t], char1[t][0], char1[t][1])
print('H2 sign-twisted five-point permutation; H3 Specht(3,2)')
print('FULL_QUOTIENT rationally acyclic; A5_QUOTIENT rational S2 cohomology')
print('PETERSEN_MATCHING_MIXED_WEDGE_CHARACTER_PASS')
