"""Independent finite checks for geometric fixed simplices of binary Hamming Rips complexes.
Run: python verify_weight3.py
Only standard Python modules are required.
"""
from itertools import combinations
from math import comb


def hamming(u, v):
    return (u ^ v).bit_count()


def orbits(n, v):
    remaining = set(range(1 << n))
    result = []
    while remaining:
        a = min(remaining)
        pair = frozenset((a, a ^ v))
        result.append(pair)
        remaining.difference_update(pair)
    return result


def orbit_edges(orbits, cutoff=3):
    result = set()
    for i, j in combinations(range(len(orbits)), 2):
        if all(hamming(u, w) <= cutoff for u in orbits[i] for w in orbits[j]):
            result.add((i, j))
    return result


def model_label(o, m):
    x = min(o)
    mask = (1 << 3) - 1
    low = x & mask
    # v=7 and each low-bit coset has two elements
    return (x >> 3, min(low, low ^ mask))


def expected_edge(a, b):
    w, c = a
    z, d = b
    q = hamming(w, z)
    return (q == 0 and c != d) or (q == 1 and c != d)


def enumerate_faces(labels, edges):
    # Generate all cliques inside one column or two neighboring columns.
    adj = {i: set() for i in range(len(labels))}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    out = {frozenset()}
    def extend(prefix, candidates):
        for k, v in enumerate(candidates):
            new = prefix + (v,)
            out.add(frozenset(new))
            extend(new, [x for x in candidates[k+1:] if x in adj[v]])
    extend((), list(range(len(labels))))
    return out


def gf2_rank(vectors):
    pivots = {}
    for x in vectors:
        while x:
            h = x.bit_length() - 1
            if h not in pivots:
                pivots[h] = x
                break
            x ^= pivots[h]
    return len(pivots)


def reduced_betti(faces):
    dims = {}
    for s in faces:
        if s:
            dims.setdefault(len(s)-1, []).append(tuple(sorted(s)))
    for d in dims:
        dims[d].sort()
    ranks = {}
    for d in range(1, max(dims)+1):
        basis = {f:i for i,f in enumerate(dims[d-1])}
        columns = []
        for s in dims.get(d, []):
            col = 0
            for t in combinations(s, len(s)-1):
                col ^= 1 << basis[t]
            columns.append(col)
        ranks[d] = gf2_rank(columns)
    betti = {}
    for d in dims:
        v = len(dims[d]) - ranks.get(d, 0) - ranks.get(d+1, 0)
        if d == 0:
            v -= 1
        if v:
            betti[d] = v
    return betti, {d:len(faces_d) for d, faces_d in dims.items()}


def main():
    total = 0
    for n in range(3, 8):
        m = n - 3
        v = 7
        os = orbits(n, v)
        labels = [model_label(o, m) for o in os]
        assert len(set(labels)) == len(labels) == (1 << (n-1))
        edges = orbit_edges(os)
        for i, j in combinations(range(len(os)), 2):
            assert ((i, j) in edges) == expected_edge(labels[i], labels[j])
            total += 1
        faces = enumerate_faces(labels, edges)
        beta, count = reduced_betti(faces)
        if n == 3:
            predicted = {}
            expected_facets = 1
        else:
            e = m * (1 << (m-1))
            c = e - (1 << m) + 1
            predicted = {3:e}
            if c:
                predicted[1] = c
            expected_facets = 16*e - (m-1)*(1 << m)
        assert beta == predicted, (n, beta, predicted)
        if n >= 4:
            facets = [s for s in faces if len(s) == 4]
            assert len(facets) == expected_facets, (n,len(facets),expected_facets)
            assert max(count) == 3
        else:
            assert len(faces)==16
        print(f'n={n} orbit_vertices={len(os)} edges={len(edges)} faces={len(faces)} f_by_dimension={count} reduced_F2_betti={beta}')
    # All weight-three generators in representative low-dimensional cubes.
    for n in range(3, 7):
        for support in combinations(range(n), 3):
            v = sum(1 << j for j in support)
            os = orbits(n, v)
            actual = orbit_edges(os)
            e = (n-3) * (1 << (n-4)) * 12 + 6*(1 << (n-3)) if n>=4 else 6
            assert len(actual)==e, (n,support,len(actual),e)
            total += len(os)*(len(os)-1)//2
    print(f'ORBIT_EDGE_AND_HOMOLOGY_CHECKS_OK pair_comparisons={total}')


if __name__ == '__main__':
    main()
