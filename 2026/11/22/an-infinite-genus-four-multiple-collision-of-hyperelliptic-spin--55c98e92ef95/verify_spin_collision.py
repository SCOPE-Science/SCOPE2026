#!/usr/bin/env python3
"""Independent finite checks for an infinite collision of hyperelliptic spin schemes.

All calculations use exact integer arithmetic and only the Python standard library.
"""
from collections import Counter
from math import comb, gcd


def cycle_lengths_of_power(lengths, power):
    out = []
    for ell in lengths:
        d = gcd(ell, power)
        out.extend([ell // d] * d)
    return out


def fixed_spin_counts(lengths, genus):
    """Return (odd, even) fixed theta classes for branch-cycle lengths.

    Theta classes are subsets S of size congruent to g+1 modulo two, up
    to complement; parity is (g+1-|S|)//2 modulo two when |S| <= g+1.
    """
    n = 2 * genus + 2
    assert sum(lengths) == n
    half = genus + 1
    polynomial = [1] + [0] * n
    for length in lengths:
        for i in range(n - length, -1, -1):
            polynomial[i + length] += polynomial[i]
    counts = [0, 0]
    for k in range(half):
        if k % 2 == half % 2:
            counts[(half - k) // 2 % 2] += polynomial[k]
    anti = 2 ** len(lengths) if all(ell % 2 == 0 for ell in lengths) else 0
    assert (polynomial[half] + anti) % 2 == 0
    counts[0] += (polynomial[half] + anti) // 2
    return counts[1], counts[0]


def action_permutation(lengths):
    n = sum(lengths)
    perm = list(range(n))
    at = 0
    for ell in lengths:
        for i in range(ell):
            perm[at + i] = at + (i + 1) % ell
        at += ell
    return perm


def orbit_spectrum_bruteforce(lengths):
    """Construct *all* theta classes, act on bit masks, compute every orbit."""
    g = (sum(lengths) - 2) // 2
    n = sum(lengths)
    all_mask = (1 << n) - 1
    half = g + 1
    perm = action_permutation(lengths)
    def move(mask):
        out = 0
        for i, dst in enumerate(perm):
            if (mask >> i) & 1:
                out |= 1 << dst
        return min(out, out ^ all_mask)
    eligible = set()
    for mask in range(1 << n):
        if mask.bit_count() % 2 == half % 2:
            eligible.add(min(mask, mask ^ all_mask))
    assert len(eligible) == 2 ** (2 * g)
    spectra = [Counter(), Counter()]
    while eligible:
        start = eligible.pop()
        cur = move(start)
        cycle_len = 1
        while cur != start:
            assert cur in eligible
            eligible.remove(cur)
            cur = move(cur)
            cycle_len += 1
        k = min(start.bit_count(), n - start.bit_count())
        parity = ((half - k) // 2) % 2
        spectra[parity][cycle_len] += 1
    return spectra[1], spectra[0]


def fixed_from_spectrum(spectra, power):
    return sum(k * count for k, count in spectra.items() if power % k == 0)


def check(m):
    L = 8 * m
    g = 4 * m
    lengths_a = [L, 2]
    lengths_b = [L, 1, 1]
    for power in range(1, L + 1):
        a = fixed_spin_counts(cycle_lengths_of_power(lengths_a, power), g)
        b = fixed_spin_counts(cycle_lengths_of_power(lengths_b, power), g)
        assert a == b, (m, power, a, b)
        if power % 2:
            assert a == (0, 2 ** gcd(L, power)), (m, power, a)
    if m <= 2:
        pair_a = orbit_spectrum_bruteforce(lengths_a)
        pair_b = orbit_spectrum_bruteforce(lengths_b)
        assert pair_a == pair_b, (m, pair_a, pair_b)
        for power in range(1, L + 1):
            observed = (fixed_from_spectrum(pair_a[0], power),
                        fixed_from_spectrum(pair_a[1], power))
            assert observed == fixed_spin_counts(
                cycle_lengths_of_power(lengths_a, power), g)
        print('genus', g, 'odd-orbits', sorted(pair_a[0].items()),
              'even-orbits', sorted(pair_a[1].items()))
    else:
        print('genus', g, 'symbolic formula matches all', L, 'powers')


if __name__ == '__main__':
    for m in range(1, 11):
        check(m)
    print('INFINITE_HYPERELLIPTIC_SPIN_COLLISION_CHECKS_OK')
