#!/usr/bin/env python3
"""Self-contained exact certificate for a conjugation-orbit subgroup complex."""
import collections
import itertools
import json
from pathlib import Path


def act(matrix, vector):
    """Evaluate a binary 3-by-3 matrix on a binary column vector."""
    return sum((sum(((matrix >> (3*i+j)) & 1) * ((vector >> j) & 1)
                    for j in range(3)) % 2) << i for i in range(3))


def main():
    matrices = sorted(a for a in range(512)
                      if len({act(a, v) for v in range(8)}) == 8)
    assert len(matrices) == 168
    lookup = {a: i for i, a in enumerate(matrices)}
    identity = lookup[0b100010001]
    product = []
    for a in matrices:
        row = []
        for b in matrices:
            binary_product = sum(((act(a, act(b, 1 << j)) >> i) & 1)
                                 << (3*i+j) for i in range(3) for j in range(3))
            row.append(lookup[binary_product])
        product.append(row)
    assert all(product[identity][g] == product[g][identity] == g for g in range(168))
    inverse = [next(b for b in range(168)
                    if product[a][b] == product[b][a] == identity)
               for a in range(168)]

    def subgroup(gens):
        generators = sorted(set(gens) | {inverse[g] for g in gens})
        reached, fifo = {identity}, [identity]
        for x in fifo:
            for generator in generators:
                y = product[x][generator]
                if y not in reached:
                    reached.add(y)
                    fifo.append(y)
        return sum(1 << i for i in reached)

    subgroups = {1 << identity: ()}
    fifo = [1 << identity]
    for mask in fifo:
        gens = subgroups[mask]
        for x in range(168):
            if (mask >> x) & 1:
                continue
            new = subgroup(gens + (x,))
            if new not in subgroups:
                subgroups[new] = gens + (x,)
                fifo.append(new)
    assert len(subgroups) == 179
    assert collections.Counter(h.bit_count() for h in subgroups) == {
        1: 1, 2: 21, 3: 28, 4: 35, 6: 28, 7: 8, 8: 21,
        12: 14, 21: 8, 24: 14, 168: 1}

    proper = sorted((h for h in subgroups if 1 < h.bit_count() < 168),
                    key=lambda h: (h.bit_count(), h))
    assert len(proper) == 177
    index = {h: i for i, h in enumerate(proper)}
    elements = [[i for i in range(168) if (mask >> i) & 1] for mask in proper]
    conjugations = [[product[product[g][x]][inverse[g]] for x in range(168)]
                    for g in range(168)]
    action = [[index[sum(1 << conjugations[g][x] for x in elems)]
               for elems in elements] for g in range(168)]
    assert all(sorted(p) == list(range(177)) for p in action)
    sizes = [m.bit_count() for m in proper]
    overgroups = [[j for j, bigger in enumerate(proper)
                   if sizes[i] < sizes[j] and (smaller & bigger) == smaller]
                  for i, smaller in enumerate(proper)]

    all_chains = []
    def grow(chain):
        all_chains.append(chain)
        for j in overgroups[chain[-1]]:
            grow(chain + (j,))
    for i in range(177):
        grow((i,))
    assert collections.Counter(len(c)-1 for c in all_chains) == {
        0: 177, 1: 911, 2: 1071, 3: 336}

    def representative(chain):
        return min(tuple(g[x] for x in chain) for g in action)

    orbit_cells = {d: sorted({representative(chain)
                              for chain in all_chains if len(chain) == d+1})
                   for d in range(4)}
    assert [len(orbit_cells[d]) for d in range(4)] == [13, 37, 37, 12]
    # The 13 vertex orbits correspond to exactly 15 conjugacy classes
    # of subgroups including the two excluded endpoints.
    lookup_cell = {d: {chain: j for j, chain in enumerate(orbit_cells[d])}
                   for d in range(4)}
    facets = {d: [[lookup_cell[d-1][representative(c[:k]+c[k+1:])]
                   for k in range(d+1)] for c in orbit_cells[d]]
              for d in (1, 2, 3)}
    certificate = json.loads((Path(__file__).parent/'collapse_certificate.json').read_text())
    assert certificate['cell_counts'] == [13, 37, 37, 12]
    assert len(certificate['pairs']) == 49
    present = {d: set(range(len(orbit_cells[d]))) for d in range(4)}
    for d, upper, face in certificate['pairs']:
        assert d in (1, 2, 3) and upper in present[d] and face in present[d-1]
        assert facets[d][upper].count(face) == 1
        incidence = sum(facets[d][j].count(face) for j in present[d])
        assert incidence == 1, (d, upper, face, incidence)
        # The face must not have an extant higher-dimensional coface.
        for higher in range(d+1, 4):
            for j in present[higher]:
                # Distinct rank-ordered chain positions prohibit inversions.
                low = orbit_cells[d-1][face]
                high = orbit_cells[higher][j]
                assert not any(representative(tuple(high[k] for k in comb)) == low
                               for comb in itertools.combinations(range(len(high)), d))
        present[d].remove(upper)
        present[d-1].remove(face)
    assert {d: len(present[d]) for d in range(4)} == {0: 1, 1: 0, 2: 0, 3: 0}
    print('PSL27_ORBIT_SUBGROUP_COMPLEX_COLLAPSE_OK')
    print('group=168 subgroups=179 proper=177 chains=2495')
    print('orbit_cells=(13,37,37,12) certified_collapses=49 residual_vertex=1')

if __name__ == '__main__':
    main()
