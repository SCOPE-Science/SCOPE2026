#!/usr/bin/env python3
"""Independent finite checks for signed-cycle singleton-type bounds."""
from itertools import product
from collections import Counter

STATES = (0, 1, -1)


def allowed(a, b, e):
    # e=+1 is old arc i -> i+1; the sole allowed nonzero pair is (+,-).
    return a == 0 or b == 0 or (a == e and b == -e)


def direct(eps):
    n = len(eps)
    p = [0] * (n + 1)
    for a in product(STATES, repeat=n):
        if all(allowed(a[i], a[(i+1) % n], eps[i]) for i in range(n)):
            p[sum(x != 0 for x in a)] += 1
    return tuple(p)


def defect_set(eps):
    n = len(eps)
    return {i for i in range(n) if eps[(i-1) % n] == eps[i]}


def by_defects(eps):
    n = len(eps)
    bad = defect_set(eps)
    p = [0] * (n + 1)
    for mask in range(1 << n):
        if any(all(mask & (1 << ((i+j) % n)) for j in (-1, 0, 1)) for i in bad):
            continue
        s = 0
        for i in range(n):
            if mask & (1 << i) and not mask & (1 << ((i-1) % n)) and not mask & (1 << ((i+1) % n)):
                s += 1
        p[mask.bit_count()] += 1 << s
    return tuple(p)


def by_transfer(eps):
    n = len(eps)
    p = [0] * (n + 1)
    # A separate finite-state recurrence with the weight assigned upon arrival.
    for initial in STATES:
        dp = {(initial, 0): 1}
        for edge in eps:
            ndp = {}
            for (last, k), count in dp.items():
                for new in STATES:
                    if allowed(last, new, edge):
                        q = (new, k + (new != 0))
                        ndp[q] = ndp.get(q, 0) + count
            dp = ndp
        for (last, k), count in dp.items():
            if last == initial:
                p[k] += count
    return tuple(p)


def expected_cubic(n, d):
    return n + 2 * n * (n - 4) + 8 * (n * (n - 4) * (n - 5) // 6) - d


def candidate_max(n):
    return tuple(1 if i % 2 == 0 else -1 for i in range(n))


def coherent(n):
    return (1,) * n


def main():
    direct_checked = transfer_checked = 0
    rows = []
    for n in range(4, 12):
        pmin = by_defects(coherent(n))
        pmax = by_defects(candidate_max(n))
        assert pmin == by_transfer(coherent(n))
        assert pmax == by_transfer(candidate_max(n))
        minimizers = maximizers = 0
        for eps in product((1, -1), repeat=n):
            pd = by_defects(eps)
            pt = by_transfer(eps)
            transfer_checked += 1
            assert pd == pt, (n, eps, pd, pt)
            if n <= 8:
                assert direct(eps) == pd
                direct_checked += 1
            d = len(defect_set(eps))
            assert d % 2 == n % 2
            assert pd[3] == expected_cubic(n, d), (n, eps, pd[3], d)
            assert all(a <= b <= c for a, b, c in zip(pmin, pd, pmax))
            if pd == pmin:
                minimizers += 1
                assert d == n
            if pd == pmax:
                maximizers += 1
                assert d == n % 2
        assert minimizers == 2, (n, minimizers)
        assert maximizers == (2 if n % 2 == 0 else 2 * n), (n, maximizers)
        rows.append((n, sum(pmin), sum(pmax), minimizers, maximizers, pmin[3], pmax[3]))
    for n in (9, 10, 11):
        assert direct(coherent(n)) == by_defects(coherent(n))
        assert direct(candidate_max(n)) == by_defects(candidate_max(n))
        direct_checked += 2
    print('VERIFY_OK')
    print('Exhaustive independent direct ternary-word tests:', direct_checked)
    print('Exhaustive independent transfer/defect tests:', transfer_checked)
    print('n min_total max_total n_minimizers n_maximizers cubic_min cubic_max')
    for row in rows:
        print(*row)


if __name__ == '__main__':
    main()
