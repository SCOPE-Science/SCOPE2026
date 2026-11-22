#!/usr/bin/env python3
"""Exact finite certificate for dihedral quotients of split complexes.

Only the Python standard library is required. Each cell is an orbit of a
strict chain of nonempty compatible split families. Every cell boundary is
computed by deleting one member of the chain, with its alternating sign.
"""
from itertools import combinations
from collections import defaultdict


def build(n):
    full = (1 << n) - 1
    splits = [s for s in range(1, full) if (s & 1) and
              2 <= s.bit_count() <= n - 2]
    index = {s: i for i, s in enumerate(splits)}

    def compatible(s, t):
        return not ((s & t) and (s & (full ^ t)) and
                    ((full ^ s) & t) and ((full ^ s) & (full ^ t)))

    adjacency = {
        i: {j for j, t in enumerate(splits)
            if j != i and compatible(s, t)}
        for i, s in enumerate(splits)
    }
    faces = {1: [(i,) for i in range(len(splits))]}
    for k in range(2, n-2):
        faces[k] = [face + (j,) for face in faces[k - 1]
                    for j in sorted(set.intersection(*(
                        adjacency[i] for i in face))) if j > face[-1]]
    # Expected face counts are independently prescribed by tree enumeration.
    expected_faces = {4: (3,), 5: (10, 15),
                      6: (25, 105, 105),
                      7: (56, 490, 1260, 945)}
    assert tuple(map(len, faces.values())) == expected_faces[n]

    action = []
    for sign in (1, -1):
        for shift in range(n):
            permutation = [(sign * i + shift) % n for i in range(n)]
            def image_split(s):
                t = sum(1 << permutation[i]
                        for i in range(n) if (s >> i) & 1)
                return t if t & 1 else full ^ t
            action.append(tuple(index[image_split(s)] for s in splits))
    assert len(set(action)) == (2 if n == 4 else 2 * n)

    def on_chain(chain, perm):
        return tuple((k, tuple(sorted(perm[i] for i in face)))
                     for k, face in chain)

    chains = defaultdict(set)
    for k, family in faces.items():
        for face in family:
            stack = [((k, face),)]
            while stack:
                chain = stack.pop()
                chains[len(chain)].add(chain)
                small = chain[0][1]
                for length in range(1, len(small)):
                    for subset in combinations(small, length):
                        stack.append(((length, subset),) + chain)

    def canonical(chain):
        return min(on_chain(chain, p) for p in action)

    cells = {k: sorted({canonical(chain) for chain in family})
             for k, family in chains.items()}
    enumerations = {
        4: (2,), 5: (5, 4), 6: (37, 95, 59),
        7: (232, 1660, 3072, 1656)
    }
    assert tuple(map(len, cells.values())) == enumerations[n]
    lookup = {k: {chain: i for i, chain in enumerate(family)}
              for k, family in cells.items()}
    boundaries = {}
    for k in range(2, max(cells)+1):
        columns = []
        for chain in cells[k]:
            column = defaultdict(int)
            for i in range(k):
                face = canonical(chain[:i] + chain[i+1:])
                column[lookup[k-1][face]] += (-1)**i
            assert all(abs(v) == 1 for v in column.values())
            columns.append(dict(column))
        boundaries[k] = columns
    for k in range(3, max(cells)+1):
        for col in boundaries[k]:
            composed = defaultdict(int)
            for j, a in col.items():
                for i, b in boundaries[k-1][j].items():
                    composed[i] += a*b
            assert not any(composed.values())
    return cells, boundaries


def elementary_collapses(cells, boundaries):
    active = {k: set(range(len(family))) for k, family in cells.items()}
    number = {}
    for k in range(max(cells), 1, -1):
        incidences = defaultdict(set)
        for high, boundary in enumerate(boundaries[k]):
            for low in boundary:
                incidences[low].add(high)
        count = 0
        while True:
            free = next(((low, min(incidences[low] & active[k]))
                        for low in sorted(active[k-1])
                        if len(incidences[low] & active[k]) == 1), None)
            if free is None:
                break
            low, high = free
            assert abs(boundaries[k][high][low]) == 1
            active[k-1].remove(low)
            active[k].remove(high)
            count += 1
        number[k] = count
    return number, tuple(len(active[k]) for k in sorted(active))


def rank(columns, prime):
    """Exact sparse modular column echelon rank, over the specified field."""
    basis = {}
    for column in columns:
        if prime == 2:
            current = {i for i, a in column.items() if a & 1}
            while current:
                pivot = max(current)
                if pivot not in basis:
                    basis[pivot] = current
                    break
                current.symmetric_difference_update(basis[pivot])
        else:
            current = {i: a % prime for i, a in column.items()
                       if a % prime}
            while current:
                pivot = max(current)
                scale = current[pivot]
                if pivot not in basis:
                    inv = pow(scale, -1, prime)
                    basis[pivot] = {i: a * inv % prime
                                    for i, a in current.items()}
                    break
                for i, b in basis[pivot].items():
                    a = (current.get(i, 0) - scale*b) % prime
                    if a:
                        current[i] = a
                    else:
                        current.pop(i, None)
    return len(basis)


def main():
    for n in (4, 5, 6, 7):
        cells, boundaries = build(n)
        counts = tuple(len(cells[k]) for k in sorted(cells))
        print('leaves', n, 'quotient cells', counts)
        if n in (5, 6):
            matching, remaining = elementary_collapses(cells, boundaries)
            assert remaining == tuple([1] + [0] * (n-4))
            assert matching == ({2: 4} if n == 5 else {3: 59, 2: 36})
            print('  actual elementary collapses', matching)
        if n == 7:
            for p in (2, 7):
                ranks = tuple(rank(boundaries[k], p) for k in (2,3,4))
                assert ranks == (231, 1429, 1643)
                print('  boundary ranks modulo', p, ranks)
            assert sum((-1)**(k-1)*len(cells[k]) for k in cells) == -12
    print('DIHEDRAL_PHYLOGENETIC_SPLIT_QUOTIENT_CERTIFICATE_OK')

if __name__ == '__main__':
    main()
