"""Exact finite certificate for the full strong Morse matching complex of the unfilled nine-cycle.

Run: python3 verify_c9.py (standard library only). The supplied deterministic
coordinate-toggle order is tested, not assumed to be a correct Morse field.
"""
from collections import Counter, defaultdict, deque
from itertools import permutations

N = 9
# Each directed vertex-edge pair v -> predecessor has index 2*v;
# v -> successor has index 2*v+1, with graph vertices modulo N.
ORDER = (6, 2, 12, 17, 15, 14, 4, 8, 10, 11, 5, 1, 9, 3, 7, 0, 13, 16)
EXPECTED_CRITICAL = (64, 10402, 20741, 35368, 70916, 75809)
EXPECTED_FACE_VECTOR = (18, 126, 438, 810, 792, 378, 72)


def matching_from_order(order):
    visited = 0
    mask = 0
    for v in order:
        left, right = (v - 1) % N, (v + 1) % N
        old_left = bool(visited & (1 << left))
        old_right = bool(visited & (1 << right))
        if old_left != old_right:
            directed_pair = 2 * v + (0 if old_left else 1)
            mask |= 1 << directed_pair
        visited |= 1 << v
    return mask


def enumerate_faces():
    generated = {matching_from_order(p) for p in permutations(range(N))}
    faces = set()
    for x in generated:
        subset = x
        while subset:
            faces.add(subset)
            subset = (subset - 1) & x
    return generated, faces


def toggle_match(faces):
    unmatched = faces.copy()
    matched = set()
    pairing = {}
    for bit in ORDER:
        b = 1 << bit
        for low in sorted(unmatched):
            if low & b:
                continue
            high = low | b
            if high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                matched.add((low, high))
                pairing[low] = high
                pairing[high] = low
    return unmatched, matched, pairing


def hasse_acyclic(faces, matches):
    # Every cover high -> low is reversed to low -> high if matched.
    upper = defaultdict(list)
    indegree = {x: 0 for x in faces}
    edges = 0
    for high in faces:
        bits = high
        while bits:
            bit = bits & -bits
            low = high ^ bit
            bits ^= bit
            if not low:  # Ignore the empty face.
                continue
            edges += 1
            if (low, high) in matches:
                source, target = low, high
            else:
                source, target = high, low
            upper[source].append(target)
            indegree[target] += 1
    q = deque(x for x, d in indegree.items() if d == 0)
    processed = 0
    while q:
        x = q.popleft()
        processed += 1
        for y in upper[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert processed == len(faces), (processed, len(faces))
    return edges, processed


def rank_gf2(columns):
    leading = {}
    rank = 0
    for col in columns:
        while col:
            k = col.bit_length() - 1
            if k not in leading:
                leading[k] = col
                rank += 1
                break
            col ^= leading[k]
    return rank


def chain_homology(faces):
    # Independent mod-two chain matrices on the unreduced simplicial chain complex.
    levels = defaultdict(list)
    for face in faces:
        levels[face.bit_count() - 1].append(face)
    ranks = {}
    for dim in sorted(levels):
        if dim == 0:
            ranks[0] = 0
            continue
        index = {f: i for i, f in enumerate(levels[dim - 1])}
        columns = []
        for high in levels[dim]:
            val = 0
            bits = high
            while bits:
                bit = bits & -bits
                bits ^= bit
                low = high ^ bit
                val ^= 1 << index[low]
            columns.append(val)
        ranks[dim] = rank_gf2(columns)
    homology = {d: len(levels[d]) - ranks[d] - ranks.get(d + 1, 0) for d in levels}
    homology[0] -= 1  # reduced H_0, complex is nonempty
    return ranks, {d: b for d, b in homology.items() if b}


def main():
    assert len(ORDER) == 2 * N and set(ORDER) == set(range(2 * N))
    generated, faces = enumerate_faces()
    print('GENERATORS_OK', len(generated), 'distinct from', __import__('math').factorial(N), 'orders')
    fvec = tuple(sum(x.bit_count() == k for x in faces) for k in range(1, 8))
    assert fvec == EXPECTED_FACE_VECTOR, fvec
    maximal = [x for x in generated if not any(x != y and (x & y) == x for y in generated)]
    assert len(maximal) == 90
    assert Counter(x.bit_count() - 1 for x in maximal) == {6: 72, 4: 18}
    assert len(faces) == 2634
    pure = set()
    for facet in generated:
        if facet.bit_count() == 7:
            subset = facet
            while subset:
                pure.add(subset)
                subset = (subset - 1) & facet
    extra = faces - pure
    assert len(pure) == 2598
    assert Counter(x.bit_count()-1 for x in extra) == {3: 18, 4: 18}
    print('PURE_COMPARISON_OK', len(pure), 'extra', len(extra))
    print('FACES_OK', fvec, 'maximal', len(maximal))
    critical, matches, pairing = toggle_match(faces)
    assert len(matches) == 1314
    assert len(pairing) == 2628
    assert tuple(sorted(critical)) == EXPECTED_CRITICAL, sorted(critical)
    assert Counter(x.bit_count() - 1 for x in critical) == {0: 1, 4: 5}
    assert {a for a,b in matches}.isdisjoint({b for a,b in matches})  # no face in both pairing roles
    assert all((b ^ a).bit_count() == 1 and a & b == a for a,b in matches)
    print('MATCHING_OK', len(matches), 'critical', dict(Counter(x.bit_count()-1 for x in critical)))
    edges, seen = hasse_acyclic(faces, matches)
    print('ACYCLIC_OK', seen, edges)
    ranks, betti = chain_homology(faces)
    assert betti == {4: 5}, (ranks, betti)
    print('RAW_MOD2_OK', ranks, betti)
    print('HOMOTOPY_OK wedge_of_five_S4')
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
