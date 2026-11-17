#!/usr/bin/env python3
"""Finite exhaustive checks for minimal ordinary domination in KG(n,2).
Only Python standard library is required. No external data or code.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb


def edge_graph(edges):
    vertices = sorted({v for e in edges for v in e})
    lookup = {v: i for i, v in enumerate(vertices)}
    mat = [[0] * len(vertices) for _ in vertices]
    for a, b in edges:
        u, v = lookup[a], lookup[b]
        mat[u][v] = mat[v][u] = 1
    return mat


def isomorphic(a, b):
    if len(a) != len(b):
        return False
    n = len(a)
    da = [sum(row) for row in a]
    db = [sum(row) for row in b]
    sig_a = [(da[i], tuple(sorted(da[j] for j in range(n) if a[i][j]))) for i in range(n)]
    sig_b = [(db[i], tuple(sorted(db[j] for j in range(n) if b[i][j]))) for i in range(n)]
    if sorted(sig_a) != sorted(sig_b):
        return False
    possibilities = {i: [j for j in range(n) if sig_a[i] == sig_b[j]] for i in range(n)}
    order = sorted(range(n), key=lambda i: (len(possibilities[i]), -da[i]))
    mapping, used = {}, set()

    def search(k):
        if k == n:
            return True
        i = order[k]
        for j in possibilities[i]:
            if j in used or any(a[i][old] != b[j][new] for old, new in mapping.items()):
                continue
            mapping[i] = j
            used.add(j)
            if search(k + 1):
                return True
            used.remove(j)
            del mapping[i]
        return False

    return search(0)


def all_graph_types_up_to_six():
    """All isolate-free unlabeled simple graphs with m=1,...,6 edges.
    Any isolate-free m-edge graph is reached from an (m-1)-edge graph by
    deleting an edge and its newly isolated endpoints, then reversing this
    deletion. We add an edge with zero, one, or two new endpoints.
    """
    previous = [tuple()]
    families = {}
    for m in range(1, 7):
        reps = []
        mats = []
        for old in previous:
            n = max((max(e) for e in old), default=-1) + 1
            candidates = list(combinations(range(n), 2)) + [(v, n) for v in range(n)] + [(n, n + 1)]
            for e in candidates:
                if e in old:
                    continue
                new = tuple(sorted(old + (e,)))
                mat = edge_graph(new)
                if not any(isomorphic(mat, former) for former in mats):
                    reps.append(new)
                    mats.append(mat)
        families[m] = reps
        previous = reps
    assert [len(families[m]) for m in range(1, 7)] == [1, 2, 5, 11, 26, 68]
    return families


def vertex_cover_number(edges):
    vertices = sorted({v for e in edges for v in e})
    for k in range(4):
        for subset in combinations(vertices, k):
            S = set(subset)
            if all(a in S or b in S for a, b in edges):
                return k
    return 4


def ordinary_domination(edges):
    # Add two unused original labels to detect every possible 2-cover,
    # even one that uses an otherwise isolated vertex.
    n = max((max(e) for e in edges), default=-1) + 3
    chosen = set(edges)
    for a, b in combinations(range(n), 2):
        if (a, b) not in chosen and not any(a not in e and b not in e for e in edges):
            return False
    return True


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        for rest in matchings(vertices[1:j] + vertices[j+1:]):
            yield ((a, b),) + rest


def predicted(n):
    E = list(combinations(range(n), 2))
    id_of = {e: i for i, e in enumerate(E)}
    found = set()
    def insert(edges):
        seq = tuple(sorted(tuple(sorted(e)) for e in edges))
        found.add(sum(1 << id_of[e] for e in seq))
    # Three-vertex cliques in the root, and complete root stars.
    for triple in combinations(range(n), 3):
        insert(combinations(triple, 2))
    for center in range(n):
        insert((center, x) for x in range(n) if x != center)
    # Root five-cycles; first label fixed and orientations identified.
    for five in combinations(range(n), 5):
        for p in permutations(five[1:]):
            if p[0] > p[-1]:
                continue
            tour = (five[0],) + p
            insert((tour[i], tour[(i+1) % 5]) for i in range(5))
    # Three disjoint root edges and proper double stars with 2+2 leaves.
    for six in combinations(range(n), 6):
        for matching in matchings(six):
            insert(matching)
        for a, b in combinations(six, 2):
            leaves = tuple(v for v in six if v != a and v != b)
            for left in combinations(leaves, 2):
                right = tuple(v for v in leaves if v not in left)
                insert([(a,b)] + [(a,v) for v in left] + [(b,v) for v in right])
    return found


def direct_check(n):
    pairs = list(combinations(range(n), 2))
    size = len(pairs)
    full = (1 << size) - 1
    closed = []
    for i, (a,b) in enumerate(pairs):
        mask = 1 << i
        for j, (c,d) in enumerate(pairs):
            if a != c and a != d and b != c and b != d:
                mask |= 1 << j
        closed.append(mask)
    covers = [0] * (1 << size)
    matches = set()
    for mask in range(1, 1 << size):
        bit = mask & -mask
        j = bit.bit_length() - 1
        rem = mask ^ bit
        covers[mask] = covers[rem] | closed[j]
        if covers[mask] != full:
            continue
        if any(covers[mask ^ (1 << i)] == full for i in range(size) if mask & (1 << i)):
            continue
        matches.add(mask)
    expected = predicted(n)
    assert matches == expected, (n, len(matches),len(expected),len(matches^expected))
    formula = comb(n,3) + n + (12*comb(n,5) if n >= 5 else 0) + (105*comb(n,6) if n >= 6 else 0)
    assert len(matches) == formula
    return len(matches), 1 << size


def main():
    families = all_graph_types_up_to_six()
    critical=[]
    minimal=[]
    for group in families.values():
        for edges in group:
            if vertex_cover_number(edges) != 3:
                continue
            if not all(vertex_cover_number(tuple(f for f in edges if f != e)) <= 2 for e in edges):
                continue
            critical.append(edges)
            if ordinary_domination(edges) and all(not ordinary_domination(tuple(f for f in edges if f != e)) for e in edges):
                minimal.append(edges)
    # Check classifications up to isomorphism, not just counts.
    three_matching = ((0,1),(2,3),(4,5))
    five_cycle = ((0,1),(1,2),(2,3),(3,4),(0,4))
    triangle_plus_edge = ((0,1),(0,2),(1,2),(3,4))
    complete_four = tuple(combinations(range(4),2))
    expected_critical = (three_matching, triangle_plus_edge, five_cycle, complete_four)
    assert len(critical) == 4
    assert all(any(isomorphic(edge_graph(g),edge_graph(t)) for t in expected_critical) for g in critical)
    assert len(minimal) == 2
    assert all(any(isomorphic(edge_graph(g),edge_graph(t)) for t in (three_matching,five_cycle)) for g in minimal)
    counts={}
    tested=0
    for n in range(4,8):
        counts[n], subsets = direct_check(n)
        tested += subsets - 1
    print('VERIFY_OK isolate_free_type_counts=1,2,5,11,26,68 tau3_edgecritical=4 ordinary_minimal_tau3=2 full_orders=4..7 examined_nonempty_subsets=%d minimal_counts=%s all_coefficients_and_structures=PASS' % (tested,','.join(str(counts[n]) for n in range(4,8))))


if __name__=='__main__':
    main()
