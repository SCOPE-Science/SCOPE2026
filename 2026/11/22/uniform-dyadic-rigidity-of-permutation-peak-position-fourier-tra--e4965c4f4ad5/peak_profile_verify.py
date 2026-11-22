"""Exact checks of peak-profile Fourier congruences; Python 3, standard library only.

These finite checks are independent corroboration, not the all-order proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial, gcd


def transform(a):
    a = list(a)
    step = 1
    while step < len(a):
        for i in range(0, len(a), 2 * step):
            for j in range(step):
                x, y = a[i+j], a[i+j+step]
                a[i+j], a[i+j+step] = x + y, x - y
        step *= 2
    return a


def tangent_coefficients(max_k):
    # tan(z) = sum a[k] z^(2k+1); tan'(z)=1+tan(z)^2.
    a = [Fraction(1)]
    for k in range(1, max_k + 1):
        a.append(sum((a[j] * a[k-1-j] for j in range(k)), Fraction()) / (2*k+1))
    return a


def via_peak_intersections(n):
    m = max(0, n-2)
    a = tangent_coefficients(m)
    p = [Fraction() for _ in range(1 << m)]
    p[0] = Fraction(1)
    for mask in range(1, 1 << m):
        sites = [j for j in range(m) if mask >> j & 1]
        if any(y == x+1 for x, y in zip(sites, sites[1:])):
            continue
        blocks = []
        run = 1
        for x, y in zip(sites, sites[1:]):
            if y == x+2:
                run += 1
            else:
                blocks.append(run)
                run = 1
        blocks.append(run)
        q = Fraction(1)
        for k in blocks:
            q *= a[k]
        p[mask] = q
    # Subset-zeta transform of (-2)^|T| * Pr(all peaks in T).
    w = [p[mask] * ((-2) ** mask.bit_count()) for mask in range(1 << m)]
    for b in range(m):
        for mask in range(1 << m):
            if mask >> b & 1:
                w[mask] += w[mask ^ (1 << b)]
    return [int(r * factorial(n)) if (r * factorial(n)).denominator == 1
            else (_ for _ in ()).throw(AssertionError('noninteger')) for r in w]


def via_descent_mobius(n):
    m = max(0, n-2)
    f = [0] * (1 << max(0, n-1))
    for mask in range(len(f)):
        cuts = [0] + [i for i in range(1, n) if mask >> (i-1) & 1] + [n]
        denom = 1
        for start, end in zip(cuts, cuts[1:]):
            denom *= factorial(end-start)
        f[mask] = factorial(n) // denom
    # Invert descent-subset cumulative counts.
    for b in range(n-1):
        for mask in range(len(f)):
            if mask >> b & 1:
                f[mask] -= f[mask ^ (1 << b)]
    peaks = [0] * (1 << m)
    for desc, count in enumerate(f):
        peak_mask = (desc >> 1) & (~desc) & ((1 << m) - 1)
        peaks[peak_mask] += count
    return transform(peaks)


def via_permutation_enumeration(n):
    m = max(0, n-2)
    peaks = [0] * (1 << m)
    for p in permutations(range(n)):
        mask = sum(1 << (i-1) for i in range(1, n-1)
                   if p[i-1] < p[i] > p[i+1])
        peaks[mask] += 1
    return transform(peaks)


def check():
    for n in range(3, 16):
        a = via_peak_intersections(n)
        b = via_descent_mobius(n)
        assert a == b, ('moment/descent discrepancy', n)
        if n <= 9:
            c = via_permutation_enumeration(n)
            assert a == c, ('moment/permutation discrepancy', n)
        v = 0
        t = factorial(n)
        while t % 2 == 0:
            t //= 2
            v += 1
        modulus = 2 ** (v+1)
        assert all(x % modulus == factorial(n) % modulus for x in a), n
        assert all(x != 0 for x in a), n
        # One marked peak yields the multiplier n!/3, showing sharpness.
        assert a[1] == factorial(n) // 3
        assert ((a[1] - factorial(n)) % (2 * modulus)) != 0
        print('n=%d; characters=%d; exact 2-adic valuation=%d; PASS' % (n, len(a), v))
    print('PASS: independent exact algorithms and sharp congruence')


if __name__ == '__main__':
    check()
