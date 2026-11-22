"""Exact finite cross-checks for cyclic triangles under fair independent edge orientations.

Uses only Python's standard library. This checks small graphs; the general
statements require the proof, not extrapolation from these tests.
"""
from itertools import combinations
from math import comb


def inspect_graph(n, selected_edges):
    edges = list(selected_edges)
    m = len(edges)
    edge_index = {e: j for j, e in enumerate(edges)}
    triangles = [v for v in combinations(range(n), 3)
                 if all(e in edge_index for e in combinations(v, 2))]
    t = len(triangles)
    fours = [v for v in combinations(range(n), 4)
             if all(e in edge_index for e in combinations(v, 2))]
    q = len(fours)
    n_cases = 1 << m
    active = [0] * t  # Bitset of orientation outcomes realizing each directed triangle.
    total = total2 = total3 = 0
    weights = [(-1 if j % 2 else 1) * (j + 1) for j in range(t)]
    wtotal = wtotal2 = wtotal3 = 0
    for orientation in range(n_cases):
        count = weighted = 0
        for j, (a, b, c) in enumerate(triangles):
            ab = (orientation >> edge_index[(a, b)]) & 1
            ac = (orientation >> edge_index[(a, c)]) & 1
            bc = (orientation >> edge_index[(b, c)]) & 1
            # For a<b<c, a directed 3-cycle has ab=bc != ac.
            cycle = (ab == bc and ac != ab)
            if cycle:
                active[j] |= 1 << orientation
                count += 1
                weighted += weights[j]
        total += count
        total2 += count * count
        total3 += count * count * count
        wtotal += weighted
        wtotal2 += weighted * weighted
        wtotal3 += weighted * weighted * weighted
    assert total * 4 == n_cases * t
    assert 16 * (n_cases * total2 - total ** 2) == 3 * t * n_cases ** 2
    assert 32 * (n_cases ** 2 * total3 - 3 * n_cases * total * total2
                 + 2 * total ** 3) == (3 * t - 12 * q) * n_cases ** 3
    w1 = sum(weights)
    w2 = sum(w*w for w in weights)
    w3 = sum(w*w*w for w in weights)
    wfaces = 0
    triangle_index = {v: i for i,v in enumerate(triangles)}
    for four in fours:
        faces = [triangle_index[v] for v in combinations(four, 3)]
        for triple in combinations(faces, 3):
            p = 1
            for j in triple:
                p *= weights[j]
            wfaces += p
    assert 4 * wtotal == n_cases * w1
    assert 16 * (n_cases * wtotal2 - wtotal ** 2) == 3 * w2 * n_cases ** 2
    assert 32 * (n_cases ** 2 * wtotal3 - 3 * n_cases * wtotal * wtotal2
                 + 2 * wtotal ** 3) == (3 * w3 - 3 * wfaces) * n_cases ** 3
    assert all(bits.bit_count() * 4 == n_cases for bits in active)
    for i,j in combinations(range(t), 2):
        assert (active[i] & active[j]).bit_count() * 16 == n_cases
    for triple in combinations(range(t), 3):
        selected = [set(triangles[i]) for i in triple]
        is_tetrahedron = len(set.union(*selected)) == 4
        actual = (active[triple[0]] & active[triple[1]] & active[triple[2]]).bit_count()
        assert actual * 64 == (0 if is_tetrahedron else n_cases)
    return len(list(combinations(range(t), 3)))


def main():
    checked = 0
    triple_checks = 0
    for n in (2,3,4,5):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            selected = [edge for j,edge in enumerate(possible) if (mask >> j) & 1]
            triple_checks += inspect_graph(n,selected)
            checked += 1
    print('PASS: %s labelled graphs (n=2..5), %s distinct-triangle triples' %
          (checked, triple_checks))
    print('All orientation states checked exactly; tested moment/cumulant and weighted identities.')


if __name__ == '__main__':
    main()
