#!/usr/bin/env python3
"""Exact integral orbit-chain certificate for signed-partition rank five."""
from itertools import permutations, product
from collections import Counter


def set_partitions(xs):
    xs = tuple(xs)
    if not xs:
        yield ()
        return
    x = xs[0]
    for p in set_partitions(xs[1:]):
        yield ((x,),) + p
        for i in range(len(p)):
            yield p[:i] + ((x,) + p[i],) + p[i + 1:]


def canon(p):
    return tuple(sorted(tuple(sorted(b)) for b in p))


def partitions(n):
    res = []
    xs = range(1, n + 1)
    for zbits in range(1 << n):
        zeros = {x for x in xs if zbits >> (x - 1) & 1}
        remaining = [x for x in xs if x not in zeros]
        for pp in set_partitions(remaining):
            specs = [
                [tuple(zip(p, (1,) + s)) for s in product((-1, 1), repeat=len(p) - 1)]
                for p in pp
            ]
            for choice in product(*specs):
                blocks = [tuple(sorted([0] + [a for x in zeros for a in (-x, x)]))]
                for block in choice:
                    blocks.append(tuple(sorted(x * s for x, s in block)))
                    blocks.append(tuple(sorted(-x * s for x, s in block)))
                res.append(canon(blocks))
    assert len(res) == len(set(res))
    return res


def refines(a, b):
    block_idx = {x: i for i, block in enumerate(b) for x in block}
    return all(len({block_idx[x] for x in block}) == 1 for block in a)


def transform(p, perm):
    def relabel(x):
        return 0 if x == 0 else (1 if x > 0 else -1) * perm[abs(x) - 1]
    return canon(tuple(tuple(relabel(x) for x in block) for block in p))


def matrix_rank_mod(cols, prime):
    pivots = {}
    for col in cols:
        v = {k: a % prime for k, a in col.items() if a % prime}
        while v:
            k = min(v)
            if k in pivots:
                fac = v[k] * pow(pivots[k][k], -1, prime) % prime
                for j, a in pivots[k].items():
                    v[j] = (v.get(j, 0) - fac * a) % prime
                    if not v[j]:
                        del v[j]
            else:
                pivots[k] = v
                break
    return len(pivots)


def run():
    n = 5
    all_p = partitions(n)
    degree = lambda p: n - (len(p) - 1) // 2
    assert len(all_p) == 648
    assert dict(sorted(Counter(map(degree, all_p)).items())) == {0: 1, 1: 25, 2: 170, 3: 330, 4: 121, 5: 1}
    proper = sorted(p for p in all_p if 1 <= degree(p) < n)
    m = len(proper)
    assert m == 646
    vid = {p: i for i, p in enumerate(proper)}
    ranks = [degree(p) for p in proper]
    bigger = {
        i: [j for j in range(m) if ranks[i] < ranks[j] and refines(proper[i], proper[j])]
        for i in range(m)
    }
    flags = [[(i,) for i in range(m)]]
    for _ in range(2, n):
        flags.append([c + (j,) for c in flags[-1] for j in bigger[c[-1]]])
    ordinary_counts = [len(x) for x in flags]
    assert ordinary_counts == [646, 7910, 20720, 14400], ordinary_counts
    actions = [tuple(vid[transform(p, s)] for p in proper) for s in permutations(range(1, n + 1))]
    assert len(actions) == 120
    orbit_index, orbit_counts = [], []
    for fs in flags:
        seen = {}
        for c in fs:
            if c in seen:
                continue
            # The first member of each orbit receives the next integer index.
            j = max(seen.values(), default=-1) + 1
            for act in actions:
                seen[tuple(act[k] for k in c)] = j
        assert len(seen) == len(fs)
        orbit_index.append(seen)
        orbit_counts.append(max(seen.values(), default=-1) + 1)
    assert orbit_counts == [37, 242, 471, 274], orbit_counts
    # Representative is needed only for determining each signed boundary column.
    representatives = []
    for oi in orbit_index:
        reps = [None] * (max(oi.values()) + 1)
        for f, i in oi.items():
            if reps[i] is None:
                reps[i] = f
        representatives.append(reps)
    boundaries = {}
    for d in range(1, 4):
        B = {}
        for col, simplex in enumerate(representatives[d]):
            v = {}
            for i in range(len(simplex)):
                face = simplex[:i] + simplex[i + 1:]
                key = orbit_index[d - 1][face]
                v[key] = v.get(key, 0) + (-1) ** i
            B[col] = {k: a for k, a in v.items() if a}
        boundaries[d] = B
    for d in (2, 3):
        for col in boundaries[d].values():
            v = {}
            for j, a in col.items():
                for k, b in boundaries[d - 1][j].items():
                    v[k] = v.get(k, 0) + a * b
            assert not any(v.values()), ('boundary_squared', d)
    print('rank counts', dict(sorted(Counter(map(degree, all_p)).items())))
    print('unquotiented flag counts', ordinary_counts)
    print('quotient cell counts', orbit_counts)
    for p in (2, 3, 5):
        rr = [matrix_rank_mod(list(boundaries[d].values()), p) for d in (1, 2, 3)]
        assert rr == [36, 206, 265], (p, rr)
        print('modular ranks', p, rr)
    # Integral elementary-pair cancellation: every pivot is a unit; no division except +/-1.
    alive = {d: set(range(orbit_counts[d])) for d in range(4)}
    pairs = []
    for d in (1, 2, 3):
        n_pivots = 0
        while True:
            pivot = next(((j, i, a) for j, col in boundaries[d].items()
                          for i, a in col.items() if abs(a) == 1), None)
            if pivot is None:
                break
            j, i, a = pivot
            src = boundaries[d][j]
            for k, col in boundaries[d].items():
                if k == j:
                    continue
                scale = col.get(i, 0)
                if not scale:
                    continue
                for t, v in src.items():
                    col[t] = col.get(t, 0) - scale * a * v
                    if not col[t]:
                        del col[t]
            del boundaries[d][j]
            if d > 1:
                del boundaries[d - 1][i]
            if d < 3:
                for col in boundaries[d + 1].values():
                    col.pop(j, None)
            alive[d].remove(j)
            alive[d - 1].remove(i)
            n_pivots += 1
        pairs.append(n_pivots)
    assert pairs == [36, 206, 265], pairs
    rem = [len(alive[d]) for d in range(4)]
    assert rem == [1, 0, 0, 9], rem
    assert all(not col for d in boundaries for col in boundaries[d].values())
    print('integral unit cancellations', pairs)
    print('critical cells', rem)
    print('exact integral homology [H0,H1,H2,H3] = [Z,0,0,Z^9]')
    print('PASS')

if __name__ == '__main__':
    run()
