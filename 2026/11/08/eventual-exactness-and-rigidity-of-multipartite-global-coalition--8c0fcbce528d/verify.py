#!/usr/bin/env python3
"""Exact small-instance checks for global coalitions of multipartite graphs.

Requires only Python 3 standard library. The all-order theorems are proved
mathematically, not by the finite checks in this script.
"""
from itertools import permutations, product
from math import prod, factorial


def vertices(sizes):
    return tuple((i, j) for i, n in enumerate(sizes) for j in range(n))


def support(block):
    return frozenset(i for i, _ in block)


def global_dominating_direct(sizes, chosen):
    allv = vertices(sizes)
    chosen = set(chosen)
    for u in allv:
        if u in chosen:
            continue
        if not any(v[0] != u[0] for v in chosen):
            return False
        if not any(v[0] == u[0] for v in chosen):
            return False
    return True


def valid_support_partition(partition, r):
    full = frozenset(range(r))
    types = [support(b) for b in partition]
    return all(t != full and any(t | types[j] == full
                                  for j in range(len(types)) if j != i)
               for i, t in enumerate(types))


def valid_direct_partition(partition, sizes):
    return all(not global_dominating_direct(sizes, b) and
               any(global_dominating_direct(sizes, set(b) | set(partition[j]))
                   for j in range(len(partition)) if j != i)
               for i, b in enumerate(partition))


def partitions(seq):
    # Every unlabeled set partition is generated exactly once.
    blocks = []
    def rec(i):
        if i == len(seq):
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(seq[i])
            yield from rec(i + 1)
            b.pop()
        blocks.append([seq[i]])
        yield from rec(i + 1)
        blocks.pop()
    yield from rec(0)


def exhaustive(sizes):
    r = len(sizes)
    best = 0
    counts = 0
    visited = 0
    for part in partitions(vertices(sizes)):
        visited += 1
        good = valid_support_partition(part, r)
        if good and len(part) >= best:
            if len(part) > best:
                best, counts = len(part), 0
            counts += 1
    return visited, best, counts


def canonical(sizes):
    r = len(sizes)
    assert all(n >= r-1 for n in sizes)
    chosen = {(i, j): (j if i > j else j-1) for i in range(r) for j in range(r) if i != j}
    hub = []
    for omit in range(r):
        hub.append(tuple((i, chosen[i, omit]) for i in range(r) if i != omit))
    used = set(x for b in hub for x in b)
    return tuple(hub) + tuple((v,) for v in vertices(sizes) if v not in used)


def canonical_count_by_injections(sizes):
    r = len(sizes)
    d = prod(factorial(n) // factorial(n-r+1) for n in sizes)
    return d


def test_injection_bijection(sizes):
    r = len(sizes)
    options = [list(permutations(range(n), r-1)) for n in sizes]
    seen = set()
    for selection in product(*options):
        hub = []
        for missing in range(r):
            b = tuple(sorted((i, selection[i][missing - (missing > i)])
                             for i in range(r) if i != missing))
            hub.append(b)
        included = set(x for b in hub for x in b)
        all_blocks = hub + [(v,) for v in vertices(sizes) if v not in included]
        key = tuple(sorted(all_blocks))
        assert key not in seen
        seen.add(key)
    assert len(seen) == canonical_count_by_injections(sizes)
    return len(seen)


def bound_check():
    for r in range(4, 25):
        q = r*(r-2)
        m = 3*r-6
        for s in range(r):
            twice_bound = 2*s*(r-2)+(r-s)*(m-s)
            # The deficit is integral; a half-integer bound rounds up.
            assert (twice_bound+1)//2 >= q
        m = 3*r-4
        for s in range(r):
            twice_bound = 2*s*(r-2)+(r-s)*(m-s)
            assert twice_bound > 2*q
    print('DEFICIT_THRESHOLD_ARITHMETIC_OK r=4..24')


def run():
    bound_check()
    for sizes in [(2,2,2), (2,2,2,2), (3,2,2,2),
                  (3,3,2,2), (2,2,2,2,2)]:
        v = vertices(sizes)
        # Independent graph-level test of support criterion on every subset.
        if len(v) <= 9:
            full = frozenset(range(len(sizes)))
            for bits in range(1 << len(v)):
                chosen = {v[j] for j in range(len(v)) if bits & (1 << j)}
                assert global_dominating_direct(sizes, chosen) == (support(chosen) == full)
        visited, best, number = exhaustive(sizes)
        print('EXHAUSTIVE_PARTITIONS_OK', sizes, 'visited',visited,
              'maximum',best,'maximizers',number)
        assert best >= 2
    for sizes in [(15,16,17,18), (17,17,20,23),
                  (29,30,31,32,33), (47,48,49,50,51,52)]:
        r = len(sizes)
        Q = r * (r-2)
        assert min(sizes) >= 2*Q-1
        p = canonical(sizes)
        assert valid_support_partition(p, r)
        assert len(p) == sum(sizes)-Q
        assert all(len(b) in (1,r-1) for b in p)
        assert sum(len(b)-1 for b in p) == Q
        if min(sizes) >= 2*Q+1:
            assert canonical_count_by_injections(sizes) > 0
        print('LARGE_PART_CONSTRUCTION_OK', sizes,'classes',len(p),'excess',Q)
    for sizes in [(3,3,3), (3,3,3,3)]:
        n=test_injection_bijection(sizes)
        print('INJECTION_COUNT_BIJECTION_OK', sizes, n)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
