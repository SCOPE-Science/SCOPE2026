#!/usr/bin/env python3
"""Finite brute-force verification for zero forcing in powers of paths.

All graph adjacency and the iterative color-change closure are evaluated
from scratch.  The formula family uses the natural labels 1,...,n.
"""
from collections import Counter


def adjacency(n, k):
    return [sum(1 << j for j in range(n) if i != j and abs(i-j) <= k)
            for i in range(n)]


def first_move_possible(nbs, mask):
    for i, neighbors in enumerate(nbs):
        if (mask >> i) & 1:
            whites = neighbors & ~mask
            if whites and not (whites & (whites - 1)):
                return True
    return False


def zero_forcing(nbs, mask):
    full = (1 << len(nbs)) - 1
    while mask != full:
        forced = 0
        for i, neighbors in enumerate(nbs):
            if (mask >> i) & 1:
                whites = neighbors & ~mask
                if whites and not (whites & (whites - 1)):
                    forced |= whites
        if not forced:
            return False
        mask |= forced
    return True


def predicted_minimal(n):
    assert n >= 3
    if n == 3:
        return {sum(1 << (x-1) for x in vertices)
                for vertices in [(1, 2), (1, 3), (2, 3)]}
    groups = [(1,2), (1,3), (n-2,n), (n-1,n)]
    if n >= 5:
        groups.extend([(2,3,4), (n-3,n-2,n-1)])
    for k in range(3, n-4):
        groups.append((k,k+1,k+2,k+3))
    for k in range(2, n-5):
        groups.append((k,k+2,k+3,k+4))
    for k in range(3, n-4):
        groups.append((k,k+1,k+2,k+4))
    return {sum(1 << (x-1) for x in vertices) for vertices in groups}


def triggers(nbs):
    t = set()
    for v, nb in enumerate(nbs):
        for w in range(len(nbs)):
            if (nb >> w) & 1:
                t.add((1 << v) | (nb & ~(1 << w)))
    return t


def antichain_minima(family):
    sorted_masks = sorted(family, key=lambda m: (m.bit_count(), m))
    out = []
    for mask in sorted_masks:
        if not any((m & mask) == m for m in out):
            out.append(mask)
    return set(out)


def main():
    tests = masks = minimum = 0
    for k in range(1,6):
        for n in range(k+1,15):
            nb = adjacency(n, k)
            for mask in range(1 << n):
                actual = zero_forcing(nb, mask)
                predicted = first_move_possible(nb, mask) or mask == (1 << n)-1
                assert actual == predicted, (n,k,mask,actual,predicted)
                masks += 1
            tests += 1
    for n in range(3,19):
        nb = adjacency(n,2)
        minimum_sets = antichain_minima(triggers(nb))
        expected = predicted_minimal(n)
        assert minimum_sets == expected, ('triggers',n,minimum_sets^expected)
        for mask in range(1<<n):
            expected_zf = any((mask & m) == m for m in minimum_sets)
            actual_zf = zero_forcing(nb, mask)
            assert expected_zf == actual_zf, ('zf',n,mask)
            if expected_zf and not any((mask & m) == m for m in minimum_sets if m!=mask):
                # For a minimum trigger the only contained trigger is itself.
                if mask in minimum_sets: minimum+=1
        a = Counter(m.bit_count() for m in minimum_sets)
        exp = {2: 3 if n==3 else 4}
        if n>=5:exp[3]=1 if n==5 else 2
        if n>=8:exp[4]=3*(n-7)
        assert dict(a)==exp,(n,a,exp)
    print(f'VERIFY_OK first_move_cases={tests} first_move_subsets={masks} '
          f'square_orders=3..18 square_full_subsets={sum(1<<n for n in range(3,19))} '
          f'square_minimal_sets={minimum} exact_polynomial=PASS '
          f'all_minimal_triggers=PASS standard_zero_forcing=PASS')

if __name__ == '__main__':
    main()
