"""Exact integral H_1 of pentagon graph-Hom complexes of two (16,6,2,2) graphs.

Requires Python 3.10+ standard library only. No external data files.
The cell complex is the ordinary product-of-simplices graph Hom complex.
"""
from collections import Counter, defaultdict
from heapq import heappush, heappop
from itertools import combinations
from math import gcd
import json

NVERT = 16
FULL = (1 << NVERT) - 1


def neighbours(graph):
    out = []
    for a in range(NVERT):
        x, y = divmod(a, 4)
        mask = 0
        for b in range(NVERT):
            if a == b:
                continue
            u, v = divmod(b, 4)
            dx, dy = (u - x) % 4, (v - y) % 4
            if graph == 'rook':
                adjacent = x == u or y == v
            else:
                assert graph == 'shrikhande'
                adjacent = (dx, dy) in {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
            if adjacent:
                mask |= 1 << b
        out.append(mask)
    assert all(m.bit_count() == 6 for m in out)
    # This directly verifies the (16,6,2,2) strongly regular property.
    for a in range(NVERT):
        for b in range(a + 1, NVERT):
            assert (out[a] & out[b]).bit_count() == 2
    return out


def singletons(neighbor):
    choices = [[i for i in range(NVERT) if neighbor[v] & (1 << i)] for v in range(NVERT)]
    cells = set()
    for a in range(NVERT):
        for b in choices[a]:
            for c in choices[b]:
                for d in choices[c]:
                    for e in choices[d]:
                        if neighbor[e] & (1 << a):
                            cells.add(tuple(1 << i for i in (a, b, c, d, e)))
    return cells


def all_cells(neighbor):
    current = singletons(neighbor)
    layers = [current]
    cache = {0: FULL}

    def common_neighbours(mask):
        if mask not in cache:
            result = FULL
            for i in range(NVERT):
                if mask & (1 << i):
                    result &= neighbor[i]
            cache[mask] = result
        return cache[mask]

    while True:
        upper = set()
        for f in current:
            for j in range(5):
                extra = common_neighbours(f[(j - 1) % 5]) & common_neighbours(f[(j + 1) % 5]) & ~f[j]
                while extra:
                    bit = extra & -extra
                    extra -= bit
                    lifted = list(f)
                    lifted[j] |= bit
                    upper.add(tuple(lifted))
        if not upper:
            break
        current = upper
        layers.append(current)
    return layers


class Forest:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True


def boundary_matrix(layers):
    verts = sorted(layers[0]); edges = sorted(layers[1]); two = sorted(layers[2])
    vi = {v: i for i, v in enumerate(verts)}
    ei = {f: i for i, f in enumerate(edges)}
    forest = Forest(len(verts))
    chord = {}
    for f in edges:
        j = next(i for i, m in enumerate(f) if m.bit_count() == 2)
        low = f[j] & -f[j]
        high = f[j] - low
        x = list(f); x[j] = low
        y = list(f); y[j] = high
        if not forest.join(vi[tuple(x)], vi[tuple(y)]):
            chord[ei[f]] = len(chord)
    components = Counter(forest.root(i) for i in range(len(verts)))
    assert sum(components.values()) == len(verts)
    num_chords = len(chord)
    assert num_chords == len(edges) - len(verts) + len(components)

    # Column presentation: im(partial_2) inside the integer cycle lattice,
    # using the chord coefficients of the canonical fundamental-cycle basis.
    matrix = {}
    incidence = defaultdict(set)
    for c, f in enumerate(two):
        col = {}
        prior_dimension = 0
        term_count = 0
        for j, mask in enumerate(f):
            bits = [1 << v for v in range(NVERT) if mask & (1 << v)]
            if len(bits) >= 2:
                for k, bit in enumerate(bits):
                    boundary = list(f)
                    boundary[j] = mask ^ bit
                    term_count += 1
                    edge_id = ei[tuple(boundary)]
                    if edge_id in chord:
                        r = chord[edge_id]
                        col[r] = col.get(r, 0) + (-1) ** (prior_dimension + k)
                prior_dimension += len(bits) - 1
        assert term_count in (3, 4)
        col = {r: value for r, value in col.items() if value != 0}
        if col:
            matrix[c] = col
            for r in col:
                incidence[r].add(c)
    return matrix, incidence, num_chords, sorted(components.values())


def integral_unit_cancellation(matrix, incidence, num_chords):
    # Every cancellation is an integer-unimodular pivot, hence preserves the
    # presented abelian group. A priority queue reduces intermediate fill-in.
    queue = []

    def push(c, r):
        if matrix[c].get(r) in (-1, 1):
            cost = (len(matrix[c]) - 1) * (len(incidence[r]) - 1)
            heappush(queue, (cost, c, r))

    for c, col in matrix.items():
        for r, a in col.items():
            if abs(a) == 1:
                push(c, r)

    cancelled = 0
    while queue:
        cost, c, r = heappop(queue)
        if c not in matrix or r not in incidence or matrix[c].get(r) not in (-1, 1):
            continue
        newcost = (len(matrix[c]) - 1) * (len(incidence[r]) - 1)
        if cost != newcost:
            heappush(queue, (newcost, c, r))
            continue
        pivot = matrix[c]
        a = pivot[r]
        for other in list(incidence[r] - {c}):
            col = matrix[other]
            factor = col[r] * a
            for rr, value in pivot.items():
                updated = col.get(rr, 0) - factor * value
                if updated:
                    if rr not in col:
                        incidence[rr].add(other)
                    col[rr] = updated
                elif rr in col:
                    del col[rr]
                    incidence[rr].discard(other)
                    if not incidence[rr]:
                        del incidence[rr]
            if not col:
                del matrix[other]
            else:
                for rr, value in col.items():
                    if abs(value) == 1:
                        push(other, rr)
        for rr in pivot:
            incidence[rr].discard(c)
            if not incidence[rr]:
                del incidence[rr]
        del matrix[c]
        cancelled += 1

    remaining_rows = sorted(incidence)
    assert all(abs(a) != 1 for col in matrix.values() for a in col.values())
    if not remaining_rows:
        assert not matrix
        invariants = []
        gcd_entries = 0
        gcd_minors = 0
    else:
        assert len(remaining_rows) == 2
        vectors = [tuple(col.get(r, 0) for r in remaining_rows) for col in matrix.values()]
        gcd_entries = 0
        gcd_minors = 0
        for a, b in vectors:
            gcd_entries = gcd(gcd_entries, a, b)
        for i, (a, b) in enumerate(vectors):
            for c, d in vectors[i + 1:]:
                gcd_minors = gcd(gcd_minors, a * d - b * c)
                if gcd_minors == gcd_entries * gcd_entries:
                    break
            if gcd_minors == gcd_entries * gcd_entries:
                break
        assert gcd_minors > 0 and gcd_minors % gcd_entries == 0
        invariants = [gcd_entries, gcd_minors // gcd_entries]
        assert all(x > 1 for x in invariants)
    free_rank = num_chords - cancelled - len(invariants)
    return {'unit_pivots': cancelled, 'residual_rows': len(remaining_rows),
            'residual_nonzero_columns': len(matrix), 'residual_gcd_entries': gcd_entries,
            'residual_gcd_2minors': gcd_minors, 'smith_nonunit_invariants': invariants,
            'H1_free_rank': free_rank}


def run_one(kind):
    neighbor = neighbours(kind)
    layers = all_cells(neighbor)
    assert len(layers) == 7
    counts = [len(s) for s in layers]
    assert counts == [7680, 30720, 45120, 36480, 20160, 6720, 960]
    m, inc, num_chords, components = boundary_matrix(layers)
    outcome = integral_unit_cancellation(m, inc, num_chords)
    return {'graph': kind, 'cells_by_dimension': counts,
            'number_of_components': len(components), 'component_vertices': components,
            'fundamental_cycle_rank': num_chords, **outcome}


def main():
    results = [run_one(kind) for kind in ('rook', 'shrikhande')]
    a, b = results
    assert a['unit_pivots'] == 22950
    assert a['H1_free_rank'] == 90 and a['smith_nonunit_invariants'] == [2, 2]
    assert b['unit_pivots'] == 22982
    assert b['H1_free_rank'] == 60 and b['smith_nonunit_invariants'] == []
    assert a['number_of_components'] == b['number_of_components'] == 2
    print(json.dumps({'verification': 'passed', 'results': results}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
