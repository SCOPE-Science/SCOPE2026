#!/usr/bin/env python3
"""Reproduce dihedral traces of even Möbius-ladder perfect-matching complexes.
Uses only the Python 3 standard library; no external input files.
"""
from functools import lru_cache


def instance(n):
    assert n >= 4 and n % 2 == 0
    N = 2 * n
    edges = [((i, (i + 1) % N)) for i in range(N)] + [(i, i + n) for i in range(n)]
    assert len(set(tuple(sorted(e)) for e in edges)) == 3 * n
    edge_index = {tuple(sorted(e)): i for i, e in enumerate(edges)}
    incidence = [[] for _ in range(N)]
    for i, (u, v) in enumerate(edges):
        incidence[u].append((v, i))
        incidence[v].append((u, i))

    @lru_cache(None)
    def matchings(vertices):
        if vertices == 0:
            return (0,)
        u = (vertices & -vertices).bit_length() - 1
        out = []
        for v, i in incidence[u]:
            if (vertices >> v) & 1:
                for rest in matchings(vertices ^ (1 << u) ^ (1 << v)):
                    out.append(rest | (1 << i))
        return tuple(out)

    perfect = matchings((1 << N) - 1)
    assert len(set(perfect)) == len(perfect)
    bad = [0] * len(edges)
    for i, (u, v) in enumerate(edges):
        for j in range(i):
            w, x = edges[j]
            conflict = len({u, v, w, x}) < 4
            if i < 2 * n and j < 2 * n:
                conflict |= (i - j) % N in (n - 1, n + 1)
            if conflict:
                bad[i] |= 1 << j
                bad[j] |= 1 << i

    def permutation(a, b):
        # Vertex map v -> a*v + b, with a in {-1,+1}.
        return [edge_index[tuple(sorted(((a * u + b) % N,
                                         (a * v + b) % N)))]
                for u, v in edges]

    def quotient(a, b):
        perm = permutation(a, b)
        used = set()
        orbits = []
        for e in range(len(edges)):
            if e in used:
                continue
            orbit = []
            cur = e
            while cur not in used:
                orbit.append(cur)
                used.add(cur)
                cur = perm[cur]
            # A fixed simplex cannot contain an orbit with internally incompatible edges.
            if any((bad[u] >> v) & 1 for i, u in enumerate(orbit)
                   for v in orbit[i + 1:]):
                continue
            orbits.append(tuple(orbit))
        neighbors = [0] * len(orbits)
        for i, orbit in enumerate(orbits):
            for j in range(i):
                other = orbits[j]
                if any((bad[u] >> v) & 1 for u in orbit for v in other):
                    neighbors[i] |= 1 << j
                    neighbors[j] |= 1 << i

        @lru_cache(None)
        def independent_polynomial_minus_one(vertices):
            if not vertices:
                return 1
            v = (vertices & -vertices).bit_length() - 1
            without = vertices ^ (1 << v)
            return (independent_polynomial_minus_one(without)
                    - independent_polynomial_minus_one(without & ~neighbors[v]))

        value = independent_polynomial_minus_one((1 << len(orbits)) - 1)
        return value, orbits, neighbors

    def predicted(a, b):
        k = n // 2
        if a == 1:
            return 0 if b % 2 else 2 * ((-1) ** ((k - 1) * (b // 2)))
        if b % 2 == 0 or k % 2 == 0:
            return 0
        return 2 * ((-1) ** ((k - 1) // 2))

    for a, b in [(1, 1), (1, 2), (-1, 0), (-1, 1)]:
        poly, orbits, graph = quotient(a, b)
        assert (-1) ** (n // 2) * poly == predicted(a, b), (n, a, b, poly)
        if a == -1 and b == 0:
            # The spoke {0,n} is a fixed orbit isolated after forbidden rim orbits vanish.
            fixed_spoke = next(i for i, o in enumerate(orbits) if o == (2 * n,))
            assert graph[fixed_spoke] == 0
        if a == -1 and b == 1:
            # Vertex-orbit graph reduces by false-twin deletions to a chain of triangles.
            k = n // 2
            ei = {}
            for idx, orb in enumerate(orbits):
                for e in orb:
                    if e < 2 * n:
                        ei[e] = idx
            rim = [ei[j] for j in range(k + 1)]
            tips = []
            for j in range(k):
                tip = next(i for i, o in enumerate(orbits)
                           if set(o) == {2 * n + (j + 1), 2 * n + ((-j) % n)})
                tips.append(tip)
            assert len(set(rim + tips)) == 2 * k + 1
            # Every other rim orbit is a false twin of one selected orbit.
            remaining = set(rim + tips)
            for i in range(len(orbits)):
                if i not in remaining:
                    assert any(graph[i] == graph[j] and not (graph[i] >> j) & 1
                               for j in rim)
            for j, v in enumerate(rim):
                expected = set()
                if j: expected.add(rim[j - 1]); expected.add(tips[j - 1])
                if j < k: expected.add(rim[j + 1]); expected.add(tips[j])
                assert {w for w in remaining if (graph[v] >> w) & 1} == expected
            for j, v in enumerate(tips):
                assert {w for w in remaining if (graph[v] >> w) & 1} == {
                    rim[j], rim[j + 1]}

    faces = None
    if n <= 10:
        faces = set()
        for matching in perfect:
            subset = [0]
            bits = matching
            while bits:
                low = bits & -bits
                subset.extend(x | low for x in list(subset))
                bits ^= low
            faces.update(subset)
        # Independent-set enumeration on the forbidden-pair graph, not on perfect matchings.
        independent = {0}
        for i in range(3 * n):
            independent |= {x | (1 << i) for x in independent if not (bad[i] & x)}
        assert faces == independent
        # Direct signed chain traces, with simplex orientation explicitly computed.
        for a in (-1, 1):
            for b in range(2 * n):
                perm = permutation(a, b)
                reduced_lefschetz = -1  # augmented empty simplex
                for mask in faces:
                    if not mask:
                        continue
                    verts = [i for i in range(3 * n) if mask >> i & 1]
                    translated = [perm[i] for i in verts]
                    if set(translated) != set(verts):
                        continue
                    inversion = sum(translated[i] > translated[j]
                                    for i in range(len(verts))
                                    for j in range(i + 1, len(verts)))
                    reduced_lefschetz += (-1) ** (len(verts) - 1 + inversion)
                trace = ((-1) ** (n // 2 - 1)) * reduced_lefschetz
                assert trace == predicted(a, b), (n, a, b, trace)
    print('VERIFY', n, 'perfect_matchings', len(perfect), 'faces',
          (len(faces) if faces is not None else 'not_enumerated'),
          'reflection_traces', predicted(-1, 0), predicted(-1, 1))


if __name__ == '__main__':
    for n in (4, 6, 8, 10, 12, 14):
        instance(n)
    print('ALL_VERIFY_OK')
