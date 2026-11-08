#!/usr/bin/env python3
"""Exact finite census for two commuting idempotent unary maps.

Every structure is represented as a multiset of components. A component is
(p, q, A), where A is a nonnegative (p+1) by (q+1) matrix, with its zeroth
row and column distinguished. Rows 1..p and columns 1..q are independently
permutable. Its order is 1+p+q+sum(A).

The two functions are represented by named binary relations. Counting
refinement uses all directed two-variable atomic types, including both
relation names, their converses and the diagonal equality type.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import permutations
from math import factorial


@lru_cache(None)
def anchored_permutations(k):
    return tuple((0,) + tuple(z + 1 for z in pi)
                 for pi in permutations(range(k)))


def weak_compositions(total, slots):
    if slots == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in weak_compositions(total - a, slots - 1):
            yield (a,) + rest


def canonical_matrix(p, q, a):
    cols = q + 1
    return min(tuple(a[cols * r + c] for r in rp for c in cp)
               for rp in anchored_permutations(p)
               for cp in anchored_permutations(q))


@lru_cache(None)
def components(n):
    found = set()
    for p in range(n):
        for q in range(n - p):
            e = n - 1 - p - q
            for entries in weak_compositions(e, (p + 1) * (q + 1)):
                found.add((p, q, canonical_matrix(p, q, entries)))
    return tuple(sorted(found))


@lru_cache(None)
def structures(n):
    if n == 0:
        return ((),)
    out = []
    for size in range(1, n + 1):
        for comp in components(size):
            head = (size, comp)
            for rest in structures(n - size):
                if not rest or head <= rest[0]:
                    out.append((head,) + rest)
    assert len(out) == len(set(out)), 'duplicate canonical multiset'
    return tuple(out)


def transition_tables(struct):
    f, g = [], []
    for size, (p, q, A) in struct:
        base = len(f)
        f.extend([base] + [base + r for r in range(1, p + 1)] + [base] * q)
        g.extend([base] + [base] * p + [base + p + c for c in range(1, q + 1)])
        for r in range(p + 1):
            for c in range(q + 1):
                f.extend([base + r] * A[r * (q + 1) + c])
                g.extend([base if c == 0 else base + p + c]
                         * A[r * (q + 1) + c])
        assert len(f) - base == size
    assert len(f) == len(g)
    assert all(f[f[x]] == f[x] and g[g[x]] == g[x] and
               f[g[x]] == g[f[x]] for x in range(len(f)))
    return tuple(f), tuple(g)


def binary_type(f, g, x, y):
    return (int(x == y), int(f[x] == y), int(f[y] == x),
            int(g[x] == y), int(g[y] == x))


def c2_signatures(all_structures):
    tables = [transition_tables(S) for S in all_structures]
    offsets, total = [], 0
    for f, _ in tables:
        offsets.append(total)
        total += len(f)
    initial = [
        (int(f[x] == x), int(g[x] == x))
        for f, g in tables for x in range(len(f))
    ]
    palette = {key: i for i, key in enumerate(sorted(set(initial)))}
    colors = [palette[key] for key in initial]
    max_order = max(len(f) for f, _ in tables)
    rounds = 0
    for t in range(max_order + 1):
        keys = []
        for (f, g), offset in zip(tables, offsets):
            for x in range(len(f)):
                counts = Counter((binary_type(f, g, x, y), colors[offset + y])
                                 for y in range(len(f)))
                keys.append((colors[offset + x], tuple(sorted(counts.items()))))
        palette = {key: i for i, key in enumerate(sorted(set(keys)))}
        new = [palette[key] for key in keys]
        if new == colors:
            break
        colors = new
        rounds += 1
    else:
        raise AssertionError('refinement failed to stabilize by n+1 rounds')
    signatures = [tuple(sorted(Counter(colors[o:o + len(f)]).items()))
                  for (f, _), o in zip(tables, offsets)]
    return signatures, rounds


@lru_cache(None)
def component_automorphisms(component):
    p, q, A = component
    cols = q + 1
    stabilizer = sum(
        all(A[cols * r + c] == A[cols * rp[r] + cp[c]]
            for r in range(p + 1) for c in range(q + 1))
        for rp in anchored_permutations(p)
        for cp in anchored_permutations(q)
    )
    z = stabilizer
    for a in A:
        z *= factorial(a)
    return z


def automorphisms(struct):
    multiplicities = Counter(struct)
    z = 1
    for (size, component), count in multiplicities.items():
        z *= factorial(count) * component_automorphisms(component) ** count
    return z


def explicit_witness():
    A = ((9, (2, 2, (0, 0, 0, 0, 0, 2, 0, 2, 0))),)
    B = ((9, (2, 2, (0, 0, 0, 0, 1, 1, 0, 1, 1))),)
    fa, ga = transition_tables(A)
    fb, gb = transition_tables(B)
    assert all(fa[fa[i]] == fa[i] and ga[ga[i]] == ga[i] for i in range(9))
    assert all(fb[fb[i]] == fb[i] and gb[gb[i]] == gb[i] for i in range(9))
    sig, _ = c2_signatures((A, B))
    assert sig[0] == sig[1]
    assert not any(all(pi[fa[i]] == fb[pi[i]] and pi[ga[i]] == gb[pi[i]]
                       for i in range(9)) for pi in permutations(range(9)))
    return A, B, (fa, ga), (fb, gb)


def main():
    iso_counts = (1, 4, 12, 37, 105, 307, 861, 2432, 6752)
    logic_counts = (1, 4, 12, 37, 105, 307, 861, 2432, 6751)
    labeled_counts = (1, 7, 58, 601, 7616, 113989, 1963060, 38178193, 826879312)
    for n in range(1, 10):
        items = structures(n)
        assert len(items) == iso_counts[n - 1]
        signatures, rounds = c2_signatures(items)
        grouped = defaultdict(list)
        for obj, signature in zip(items, signatures):
            grouped[signature].append(obj)
        assert len(grouped) == logic_counts[n - 1]
        cls_sizes = Counter(len(group) for group in grouped.values())
        if n < 9:
            assert cls_sizes == {1: len(items)}
        else:
            assert cls_sizes == {1: 6750, 2: 1}
            collision = next(group for group in grouped.values() if len(group) == 2)
            A, B, _, _ = explicit_witness()
            assert set(collision) == {A, B}
        labeled = sum(factorial(n) // automorphisms(S) for S in items)
        assert labeled == labeled_counts[n - 1]
        print(f'ORDER {n}: isomorphism_types={len(items)} '
              f'C2_classes={len(grouped)} labeled_pairs={labeled} '
              f'rounds={rounds}')
    A, B, tablesA, tablesB = explicit_witness()
    print(f'WITNESS A: F={tablesA[0]} G={tablesA[1]}')
    print(f'WITNESS B: F={tablesB[0]} G={tablesB[1]}')
    print('VERIFY_OK first_collision=9 unique_doubleton_at_9=1')


if __name__ == '__main__':
    main()
