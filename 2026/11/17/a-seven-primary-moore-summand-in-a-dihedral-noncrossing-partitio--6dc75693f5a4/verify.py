#!/usr/bin/env python3
"""Exact integral verification for a dihedral orbit of the seven-point noncrossing partition complex.

Run: python3 verify.py [certificate.json]
Only the Python standard library is required.
"""
import collections
import hashlib
import itertools
import json
import pathlib
import sys

N = 7

def all_set_partitions(n):
    def walk(labels, last):
        if len(labels) == n:
            blocks = tuple(sorted(tuple(i for i, c in enumerate(labels) if c == b)
                                  for b in range(last + 1)))
            yield blocks
        else:
            for k in range(last + 2):
                yield from walk(labels + (k,), max(last, k))
    yield from walk((0,), 0)

def is_noncrossing(p, n):
    b = {v: j for j, block in enumerate(p) for v in block}
    for a, c, e, f in itertools.combinations(range(n), 4):
        if b[a] == b[e] and b[c] == b[f] and b[a] != b[c]:
            return False
    return True

def refines(p, q):
    by = {x: j for j, b in enumerate(q) for x in b}
    return all(len({by[x] for x in b}) == 1 for b in p)

def image(p, offset, sign, n):
    return tuple(sorted(tuple(sorted((sign * a + offset) % n for a in b))
                        for b in p))

def construct():
    allp = tuple(all_set_partitions(N))
    assert len(allp) == 877  # Bell number B_7
    nc = tuple(p for p in allp if is_noncrossing(p, N))
    assert len(nc) == 429  # Catalan number C_7
    proper = tuple(p for p in nc if 1 < len(p) < N)
    assert len(proper) == 427
    idx = {p: k for k, p in enumerate(proper)}
    assert len(idx) == len(proper)
    group = [tuple(idx[image(p, k, s, N)] for p in proper)
             for s in (1, -1) for k in range(N)]
    assert len(group) == 14 and all(set(g) == set(range(427)) for g in group)
    above = [tuple(j for j, q in enumerate(proper)
                   if len(q) < len(p) and refines(p, q)) for p in proper]
    # Original strict chains have increasing coarseness, so group elements
    # preserve each chain's vertex order and every simplex orientation.
    def orbit(ch):
        return min(tuple(g[i] for i in ch) for g in group)
    cells = [set() for _ in range(N - 2)]
    all_chains = [[] for _ in range(N - 2)]
    def extend(ch):
        d = len(ch) - 1
        all_chains[d].append(ch)
        cells[d].add(orbit(ch))
        if d < N - 3:
            for j in above[ch[-1]]:
                extend(ch + (j,))
    for i in range(427):
        extend((i,))
    tab = [sorted(x) for x in cells]
    loci = [{ch: i for i, ch in enumerate(dim)} for dim in tab]
    fixed = [[sum(all(g[i] == i for i in ch) for ch in all_chains[d])
              for g in group] for d in range(len(tab))]
    # A second enumeration counts orbit cells via Burnside without canonicalizing.
    assert all(sum(f) == 14 * len(tab[d]) for d, f in enumerate(fixed))
    dims = [len(x) for x in tab]
    assert dims == [47, 542, 1954, 2680, 1231]
    bd = [{}]
    for d in range(1, len(tab)):
        cols = {}
        for j, ch in enumerate(tab[d]):
            c = collections.Counter()
            for k in range(d + 1):
                face = orbit(ch[:k] + ch[k+1:])
                c[loci[d-1][face]] += -1 if k % 2 else 1
            cols[j] = {i: a for i, a in c.items() if a}
        bd.append(cols)
    assert_complex(bd)
    return dims, fixed, bd

def assert_complex(bd):
    for d in range(2, len(bd)):
        for c in bd[d].values():
            comp = collections.Counter()
            for r, a in c.items():
                for s, b in bd[d - 1][r].items():
                    comp[s] += a * b
            assert all(not v for v in comp.values()), (d, c)

def cancel(bd, dims):
    """Elementary algebraic chain contraction with integral unit pivots.

    For a pivot a = +/-1 at (row i, column j) of boundary degree d,
    replace every other column k by column k - (entry_i,k/a)*column_j.
    Then delete column j and row i. Restrict adjacent boundary maps to
    the surviving modules. This is the standard chain homotopy cancellation.
    """
    steps = []
    dims = dims[:]
    for d in range(len(bd)-1, 0, -1):
        while True:
            pivot = next(((i, j, a) for j, c in bd[d].items()
                          for i, a in c.items() if abs(a) == 1), None)
            if pivot is None:
                break
            i, j, a = pivot
            chosen = bd[d][j]
            for k, c in list(bd[d].items()):
                if k == j or i not in c:
                    continue
                alpha = c[i] * a
                for r, v in chosen.items():
                    c[r] = c.get(r, 0) - alpha*v
                    if c[r] == 0:
                        del c[r]
            del bd[d][j]
            for c in bd[d].values():
                c.pop(i, None)
            bd[d-1].pop(i, None)
            if d+1 < len(bd):
                for c in bd[d+1].values():
                    c.pop(j, None)
            dims[d] -= 1
            dims[d-1] -= 1
            steps.append([d, i, j, a])
        assert_complex(bd)
    return dims, steps

def compute():
    dims, fixed, boundaries = construct()
    entries = [sum(map(len, boundaries[d].values())) for d in range(len(boundaries))]
    dims2, steps = cancel(boundaries, dims)
    assert dims2 == [1, 0, 0, 1, 10]
    assert len(steps) == 3221
    assert_complex(boundaries)
    lower = {str(d): {str(j): sorted((int(i), int(a)) for i, a in c.items())
                      for j, c in boundaries[d].items() if c}
             for d in range(1, len(boundaries))}
    # After cancellation, the sole nonzero matrix maps Z^10 -> Z.
    assert not lower['1'] and not lower['2'] and not lower['3']
    vals = list(next(iter(c))[1] for c in lower['4'].values())
    assert len(vals) == 10
    from math import gcd
    from functools import reduce
    invariant = reduce(gcd, (abs(v) for v in vals), 0)
    assert invariant == 7
    assert len([c for c in boundaries[4].values() if c]) == 10
    assert [x for x in dims2 if x] == [1, 1, 10]
    return {'object':'proper_non_crossing_partitions_7_dihedral_orbit',
            'count_set_partitions':877,'count_nc_partitions':429,
            'count_proper_partitions':427,
            'group_order':14,
            'orbit_cells_by_dimension':dims,
            'boundary_nonzero_entries_by_degree':entries,
            'burnside_fixed_flags':fixed,
            'cancellation_count':len(steps),
            'cancellations':steps,
            'remaining_generators_by_dimension':dims2,
            'remaining_boundaries':lower,
            'unique_nonunit_smith_invariant':invariant,
            'homology':{'H0':'Z','H1':'0','H2':'0','H3':'Z/7','H4':'Z^9'}}

def main():
    result = compute()
    cert = json.dumps(result, sort_keys=True, separators=(',',':'))+'\n'
    if len(sys.argv) > 1:
        target = pathlib.Path(sys.argv[1])
        if target.exists():
            assert target.read_bytes() == cert.encode('utf-8'), 'certificate differs'
        else:
            target.write_bytes(cert.encode('utf-8'))
    print('VERIFY_OK', 'orbit_cells', result['orbit_cells_by_dimension'],
          'cancellations', result['cancellation_count'],
          'residual', result['remaining_generators_by_dimension'],
          'smith', result['unique_nonunit_smith_invariant'],
          'sha256', hashlib.sha256(cert.encode()).hexdigest())
if __name__ == '__main__':
    main()
