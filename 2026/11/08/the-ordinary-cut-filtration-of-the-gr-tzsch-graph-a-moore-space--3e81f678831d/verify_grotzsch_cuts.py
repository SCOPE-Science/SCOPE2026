#!/usr/bin/env python3
"""Exact finite verification of the ordinary cut-complex filtration of Mycielski(C5).

Only Python 3 standard-library modules are used. Every face, every Hasse incidence,
every gradient path and every integral Morse-boundary coefficient is reconstructed.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from fractions import Fraction
from math import comb

N = 11
ALL = (1 << N) - 1


def edges():
    # The five originals are 0..4, their shadows 5..9, and the apex is 10.
    out = set()
    for i in range(5):
        out.add(tuple(sorted((i, (i+1) % 5))))
        for j in ((i-1) % 5, (i+1) % 5):
            out.add(tuple(sorted((i, 5+j))))
        out.add((5+i, 10))
    return out

E = edges()
assert len(E) == 20
NEIGH = [0] * N
for a, b in E:
    NEIGH[a] |= 1 << b
    NEIGH[b] |= 1 << a
assert all(not (NEIGH[a] & NEIGH[b]) for a, b in E)  # triangle-free


def is_connected(mask):
    if not mask:
        return False
    reached = mask & -mask
    while True:
        old = reached
        bits = reached
        while bits:
            b = bits & -bits
            v = b.bit_length() - 1
            reached |= NEIGH[v] & mask
            bits ^= b
        if reached == old:
            return reached == mask


def generate(k):
    # Independent construction 1: enumerate the disconnected k-sets and
    # downward-close their complements.
    disconnected = []
    faces = set()
    for vertices in combinations(range(N), k):
        mask = sum(1 << v for v in vertices)
        if not is_connected(mask):
            facet = ALL ^ mask
            disconnected.append(mask)
            sub = facet
            while sub:
                faces.add(sub)
                sub = (sub-1) & facet
    # Independent construction 2: for every candidate face, search its
    # complement for a disconnected k-set, not using the facet enumeration.
    adj_faces = set()
    for f in range(1, 1 << N):
        missing = [v for v in range(N) if not (f >> v & 1)]
        if len(missing) < k:
            continue
        for subset in combinations(missing, k):
            if not is_connected(sum(1 << v for v in subset)):
                adj_faces.add(f)
                break
    assert faces == adj_faces
    return faces, disconnected


def boundary(face):
    bits = [v for v in range(N) if face >> v & 1]
    for i, v in enumerate(bits):
        yield face ^ (1 << v), 1 if i % 2 == 0 else -1


def matching(faces):
    # Iterated element matchings: at each stage toggle the lowest remaining
    # vertex whenever both faces are still unmatched.
    left = set(faces)
    pairs = []
    for v in range(N):
        bit = 1 << v
        for f in sorted(left):
            if f & bit:
                continue
            up = f | bit
            if up in left:
                left.remove(f)
                left.remove(up)
                pairs.append((f, up))
    return left, pairs


def acyclic(faces, pairs):
    # Reverse matched Hasse arrows, and check the full resulting digraph by
    # Kahn's algorithm. No assumption about staged matching is substituted
    # for this finite directed-acyclicity verification.
    match = dict(pairs)
    successor = defaultdict(list)
    indegree = {f: 0 for f in faces}
    incidences = 0
    for high in faces:
        if high.bit_count() < 2:
            continue
        for low, _ in boundary(high):
            assert low in faces
            a, b = (low, high) if match.get(low) == high else (high, low)
            successor[a].append(b)
            indegree[b] += 1
            incidences += 1
    q = deque(f for f in faces if not indegree[f])
    reached = 0
    while q:
        f = q.popleft()
        reached += 1
        for g in successor[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    assert reached == len(faces), 'cyclic matching'
    return incidences


def morse_boundary(crit, pairs):
    # Exact signed gradient-path recursion, with no division other than by
    # the incidence ±1. A paired high cell projects to zero. If a low cell
    # f is paired to u, use ∂u=0 to remove f from the Morse chain.
    critical = set(crit)
    lower = dict(pairs)
    high = {u for _, u in pairs}
    @lru_cache(None)
    def reduce_face(f):
        if f in critical:
            return {f: 1}
        if f in high:
            return {}
        upper = lower[f]
        signed = dict(boundary(upper))
        sign = signed[f]
        out = defaultdict(int)
        for g, c in boundary(upper):
            if g == f:
                continue
            for h, z in reduce_face(g).items():
                out[h] -= c * sign * z
        return {x: z for x, z in out.items() if z}
    dimensions = sorted(set(f.bit_count()-1 for f in critical if f.bit_count() > 1))
    if not dimensions or len(dimensions) == 1:
        return [], dimensions, 0
    assert len(dimensions) == 2 and dimensions[1] == dimensions[0] + 1
    lower_crit = sorted(f for f in crit if f.bit_count()-1 == dimensions[0])
    upper_crit = sorted(f for f in crit if f.bit_count()-1 == dimensions[1])
    matrix = [[0] * len(upper_crit) for _ in lower_crit]
    ids = {f:i for i,f in enumerate(lower_crit)}
    for j, upper in enumerate(upper_crit):
        accum = defaultdict(int)
        for f, c in boundary(upper):
            for h, z in reduce_face(f).items():
                accum[h] += c*z
        for h, z in accum.items():
            assert h in ids
            matrix[ids[h]][j] = z
    return matrix, dimensions, reduce_face.cache_info().currsize


def rational_rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(z) for z in row] for row in matrix]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][j]
        a[r] = [x/z for x in a[r]]
        for i in range(r+1, len(a)):
            if a[i][j]:
                q = a[i][j]
                a[i] = [u-q*v for u,v in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def det(a):
    if len(a) == 0:
        return 1
    if len(a) == 1:
        return a[0][0]
    return sum((-1)**j * v * det([row[:j]+row[j+1:] for row in a[1:]])
               for j, v in enumerate(a[0]))


def unit_minor(matrix, r):
    if r == 0:
        return ()
    for rs in combinations(range(len(matrix)), r):
        for cs in combinations(range(len(matrix[0])), r):
            d = det([[matrix[i][j] for j in cs] for i in rs])
            if abs(d) == 1:
                return (list(rs), list(cs), d)
    return None


def mod2_homology(faces):
    # Independent simplicial boundary ranks on all cells, with no Morse data.
    bydim = {d: sorted(f for f in faces if f.bit_count()-1 == d)
             for d in range(N)}
    ranks = {}
    for d in range(1, N):
        index = {f:i for i,f in enumerate(bydim[d-1])}
        basis = {}
        for f in bydim[d]:
            c = 0
            for s, _ in boundary(f):
                c ^= 1 << index[s]
            while c:
                pivot = c.bit_length()-1
                if pivot in basis:
                    c ^= basis[pivot]
                else:
                    basis[pivot] = c
                    break
        ranks[d] = len(basis)
    betti = {}
    for d in range(N):
        count = len(bydim[d])
        b = count - ranks.get(d, 0) - ranks.get(d+1, 0)
        if d == 0 and faces:
            b -= 1  # reduced H_0
        assert b >= 0
        if b:
            betti[d] = b
    return betti

# For each level, an exact expected rank and a unimodular full-rank minor,
# except k=3, which has the determinant ±2 obstruction.
EXPECT = {
 2: ({0:1, 7:10}, 0, None, {7:10}),
 3: ({0:1, 6:3, 7:3}, 3, 2, {6:1, 7:1}),
 4: ({0:1, 5:7, 6:8}, 3, 1, {5:4, 6:5}),
 5: ({0:1, 4:8, 5:7}, 2, 1, {4:6, 5:5}),
 6: ({0:1, 3:15, 4:1}, 1, 1, {3:14}),
 7: ({0:1}, 0, None, {}),
 8: ({0:1}, 0, None, {}),
}

def main():
    assert not generate(9)[0] and not generate(10)[0] and not generate(11)[0]
    squares = []
    for verts in combinations(range(N), 4):
        vv = set(verts)
        local = [e for e in E if e[0] in vv and e[1] in vv]
        if len(local) == 4 and all(sum(v in e for e in local) == 2 for v in vv):
            squares.append(vv)
    assert len(squares) == 10
    assert all(sum(set(e).issubset(sq) for sq in squares) == 2 for e in E)
    print('GRAPH vertices=11 edges=20 triangle_free=True')
    print('FOUR_CYCLES count=10 each_edge_in_exactly_two=True')
    for k in range(2,9):
        fs, nonconnected = generate(k)
        crit, pairs = matching(fs)
        incident = acyclic(fs, pairs)
        assert 2*len(pairs) + len(crit) == len(fs)
        histogram = dict(sorted(Counter(f.bit_count()-1 for f in crit).items()))
        target, expected_rank, torsion, expected_f2 = EXPECT[k]
        assert histogram == target
        matrix, dims, paths = morse_boundary(crit, pairs)
        rk = rational_rank(matrix)
        assert rk == expected_rank
        if k == 3:
            assert len(matrix) == 3 and len(matrix[0]) == 3
            assert abs(det(matrix)) == 2
            # At least one unit 2x2 minor forces Smith invariants 1,1,2.
            assert unit_minor(matrix, 2) is not None
            evidence = 'det_abs=2; unit_2_minor=True; smith=1,1,2'
        elif k in (4,5,6):
            witness = unit_minor(matrix, rk)
            assert witness is not None
            evidence = f'unit_rank_minor={witness}'
        else:
            evidence = 'no adjacent positive-dimensional critical cells'
        f2 = mod2_homology(fs)
        assert f2 == expected_f2
        print(f'k={k} disconnected_sets={len(nonconnected)} nonempty_faces={len(fs)} '
              f'pairs={len(pairs)} incidences={incident} critical={histogram} '
              f'morse_matrix={matrix} rank={rk} {evidence} reduced_F2={f2}')
    print('k=1,9,10,11: void; ALL CHECKS PASS')

if __name__ == '__main__':
    main()
