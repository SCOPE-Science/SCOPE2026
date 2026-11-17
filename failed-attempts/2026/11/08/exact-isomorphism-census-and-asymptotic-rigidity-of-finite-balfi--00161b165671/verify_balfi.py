"""Reproduce finite BALFI isomorphism spectra and check direct small exhaustive cases.
Requires Python >=3.9 only. No data files or dependencies.
"""
from itertools import permutations, product
from collections import defaultdict
from math import factorial


def act(mask, perm):
    out = 0
    for i, j in enumerate(perm):
        if mask & (1 << i):
            out |= 1 << j
    return out


def cycle_count_on_invariant_set(mask, perm):
    count = 0
    remaining = mask
    while remaining:
        i = (remaining & -remaining).bit_length() - 1
        count += 1
        j = i
        while remaining & (1 << j):
            remaining &= ~(1 << j)
            j = perm[j]
    return count


def fixed_counts(perm):
    """(all BALFIs, those with Boolean-complement negation) fixed by perm."""
    k = len(perm)
    universe = (1 << k) - 1
    seen = set()
    total, explosive = 1, 1
    for a in range(1 << k):
        if a in seen:
            continue
        d = 0
        b = a
        while b not in seen:
            seen.add(b)
            b = act(b, perm)
            d += 1
        power = tuple(range(k))
        for _ in range(d):
            power = tuple(perm[power[i]] for i in range(k))
        ci = cycle_count_on_invariant_set(a, power)
        co = cycle_count_on_invariant_set(universe ^ a, power)
        c = cycle_count_on_invariant_set(universe, power)
        assert ci + co == c
        total *= 3**ci * 2**co
        explosive *= 2**c
    return total, explosive


def orbit_counts(k):
    s_all = s_ex = 0
    for p in permutations(range(k)):
        all_fixed, ex_fixed = fixed_counts(p)
        s_all += all_fixed
        s_ex += ex_fixed
    assert s_all % factorial(k) == 0
    assert s_ex % factorial(k) == 0
    return s_all // factorial(k), s_ex // factorial(k)


def allowed_pairs(k, a):
    u = (1 << k) - 1
    return [(neg, con) for neg in range(1 << k) for con in range(1 << k)
            if (a | neg) == u and (a & neg & con) == 0]


def brute_orbits(k):
    """Independent direct enumeration, feasible at k <= 2 only."""
    local = [allowed_pairs(k, a) for a in range(1 << k)]
    all_records = set(product(*local))
    assert len(all_records) == 6**(k * 2**(k-1))
    identity = tuple(range(k))
    excluded = set()
    n_orbits = n_ex = 0
    for record in all_records:
        if record in excluded:
            continue
        n_orbits += 1
        if all(neg == ((1 << k) - 1) ^ a for a, (neg, con) in enumerate(record)):
            n_ex += 1
        for perm in permutations(range(k)):
            image = [None] * (1 << k)
            for a, (neg, con) in enumerate(record):
                image[act(a, perm)] = (act(neg, perm), act(con, perm))
            assert tuple(image) in all_records
            excluded.add(tuple(image))
    assert len(excluded) == len(all_records)
    return n_orbits, n_ex


def main():
    expected = [(6, 4), (666, 136), (362937456, None)]
    for k in range(1, 6):
        number = 6**(k * 2**(k-1))
        explosive = 2**(k * 2**k)
        total_classes, ex_classes = orbit_counts(k)
        assert number > explosive
        if k <= 2:
            direct = brute_orbits(k)
            assert direct == (total_classes, ex_classes)
        if k <= 3:
            assert total_classes == expected[k-1][0]
            if expected[k-1][1] is not None:
                assert ex_classes == expected[k-1][1]
        print(f'k={k}; labeled={number}; complement-negation={explosive}; '
              f'isomorphism={total_classes}; complement-isomorphism={ex_classes}; '
              f'nonclassical-isomorphism={total_classes-ex_classes}')
    print('BALFI_VERIFY_OK')

if __name__ == '__main__':
    main()
