#!/usr/bin/env python3
"""Finite checks for the dihedral character of ordinary three-cut complexes of Möbius ladders.

Run with Python 3. No external dependencies. The all-parameter proof is in RESULT.md.
"""
from itertools import combinations
from math import comb


def graph(n):
    N = 2 * n
    edges = {tuple(sorted((i, (i + 1) % N))) for i in range(N)}
    edges.update((i, i + n) for i in range(n))
    return N, edges


def dual(n):
    N, edges = graph(n)
    tri = []
    for x in combinations(range(N), 3):
        if sum(e in edges for e in combinations(x, 2)) >= 2:
            tri.append(x)
    tetra = [tuple(sorted({i, (i + 1) % N, i + n, (i + n + 1) % N}))
             for i in range(n)]
    assert len(set(tetra)) == n
    return [[(i,) for i in range(N)], list(combinations(range(N), 2)), tri, tetra]


def signed_fixed(simplex, perm):
    image = [perm(x) for x in simplex]
    if sorted(image) != list(simplex):
        return 0
    inv = sum(image[i] > image[j]
              for i in range(len(image)) for j in range(i + 1, len(image)))
    return (-1) ** inv


def sign_perm(N, perm):
    seen = set()
    cycles = 0
    for i in range(N):
        if i in seen:
            continue
        cycles += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = perm(j)
    return (-1) ** (N - cycles)


def predicted(n, kind, a):
    N = 2 * n
    B = 2 * n * n - 8 * n + 1
    if kind == 'r':
        return B if a == 0 else (-1) ** a
    if n % 2:
        return 4 - n if a % 2 == 0 else n - 2
    return n - 3 if a % 2 == 0 else 3 - n


def trace_from_dual(n, faces, kind, a):
    N = 2 * n
    perm = (lambda i: (i + a) % N) if kind == 'r' else (lambda i: (a - i) % N)
    chains = [sum(signed_fixed(f, perm) for f in level) for level in faces]
    h1 = 1 - chains[0] + chains[1] - chains[2] + chains[3]
    return sign_perm(N, perm) * h1, chains


def collapse_dual(n, faces):
    living = set(f for level in faces for f in level)
    pairs = 0
    for big_size in (4, 3):
        while True:
            upper = {}
            for large in living:
                if len(large) != big_size:
                    continue
                for small in combinations(large, big_size - 1):
                    upper.setdefault(small, []).append(large)
            free = [(small, cofaces[0]) for small, cofaces in upper.items()
                    if len(cofaces) == 1]
            if not free:
                break
            small, big = min(free)
            assert small in living and big in living
            assert sum(small in list(combinations(s, len(small))) for s in living
                       if len(s) == big_size) == 1
            living.remove(small)
            living.remove(big)
            pairs += 1
    assert all(len(f) <= 2 for f in living)
    V = {s[0] for s in living if len(s) == 1}
    E = {s for s in living if len(s) == 2}
    assert V == set(range(2 * n))
    assert len(E) == 2 * n * (n - 3)
    reached = {0}
    changed = True
    while changed:
        changed = False
        for u, v in E:
            if (u in reached) != (v in reached):
                reached.update((u, v))
                changed = True
    assert reached == V
    assert pairs == 6 * n
    return pairs


def direct_cut_complex_trace(n, kind, a):
    N, E = graph(n)
    disconnected = [sum(1 << i for i in t) for t in combinations(range(N), 3)
                    if sum(e in E for e in combinations(t, 2)) < 2]
    perm = (lambda i: (i + a) % N) if kind == 'r' else (lambda i: (a - i) % N)
    total = -1  # augmented empty simplex, dimension -1
    for mask in range(1, 1 << N):
        if not any((mask & triple) == 0 for triple in disconnected):
            continue
        simplex = [i for i in range(N) if mask & (1 << i)]
        total += (-1) ** (len(simplex) - 1) * signed_fixed(simplex, perm)
    return total  # the unique reduced homology degree 2n-4 is even


def main():
    dual_cases = 0
    group_elements = 0
    collapses = 0
    for n in range(5, 21):
        faces = dual(n)
        N = 2 * n
        assert list(map(len, faces)) == [N, comb(N, 2), 6 * n, n]
        # Validate all higher dual faces by the defining 'every triple connected' condition.
        if n <= 10:
            E = graph(n)[1]
            tset = set(faces[2])
            constructed = [q for q in combinations(range(N), 4)
                           if all(t in tset for t in combinations(q, 3))]
            assert set(constructed) == set(faces[3])
        collapses += collapse_dual(n, faces)
        values = {}
        for kind in ('r', 's'):
            for a in range(N):
                actual, chains = trace_from_dual(n, faces, kind, a)
                assert actual == predicted(n, kind, a), (n, kind, a, actual)
                group_elements += 1
                values[kind, a] = actual
        invariant = sum(values.values()) // (4 * n)
        assert invariant == (n - 3) // 2
        dual_cases += 1
    direct_checks = 0
    for n in (5, 6, 7):
        for kind in ('r', 's'):
            for a in range(2 * n):
                actual = direct_cut_complex_trace(n, kind, a)
                assert actual == predicted(n, kind, a), (n, kind, a, actual)
                direct_checks += 1
    print('Dual cases:', dual_cases)
    print('Elementary collapse pairs checked:', collapses)
    print('Dihedral character comparisons:', group_elements)
    print('Direct cut-complex Lefschetz checks:', direct_checks)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
