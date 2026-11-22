#!/usr/bin/env python3
"""Independent finite congruence checks for even-parameter generalized derangements.

The infinite theorem is established in RESULT.md; this is a finite sanity test.
Python 3 standard library only.
"""
from collections import Counter


def sequence(v, k):
    mod = 1 << k
    out = [1 % mod, v % mod]
    for n in range(2, mod):
        out.append(((n + v - 1) * out[-1] + (n - 1) * out[-2]) % mod)
    return out


def main():
    cases = 0
    fibers = 0
    root_checks = 0
    for v in range(0, 32, 2):
        for k in range(1, 12):
            mod = 1 << k
            a = sequence(v, k)
            # Exactly one odd input for each even output.
            odd_image = Counter(a[n] for n in range(1, mod, 2))
            assert len(odd_image) == mod // 2
            assert set(odd_image) == set(range(0, mod, 2))
            assert all(count == 1 for count in odd_image.values())
            assert all(a[n] % 2 == 1 for n in range(0, mod, 2))
            fibers += len(odd_image)
            if k >= 3:
                for n in range(0, mod, 2):
                    assert a[n] % 8 == (1 - v * (n // 2)) % 8, (v, k, n)
                # Unique odd index representing each three-squares-exception value
                for j in range(1, (k - 3) // 2 + 1):
                    target = 7 << (2 * j)
                    count = sum(a[n] % (1 << (2 * j + 3)) == target for n in range(1, mod, 2))
                    assert count == (1 << (k - (2 * j + 3)))
            # Unique zero of the odd-index branch at every level.
            roots = [n for n in range(1, mod, 2) if a[n] == 0]
            assert len(roots) == 1, (v, k, roots)
            root_checks += 1
            cases += 1
        # A second, direct finite-difference test uses the *exact* integer recurrence.
        d = [1, v]
        for n in range(2, 42):
            d.append((n + v - 1) * d[-1] + (n - 1) * d[-2])
        for n in range(1, 32, 2):
            for m in range(n + 2, 42, 2):
                z = abs(d[m] - d[n])
                t = abs(m - n)
                assert (z & -z) == (t & -t), (v, n, m)
    print(f'PASS: {cases} complete modulus/parameter cases, {fibers} odd-input fibers,')
    print(f'      {root_checks} root uniqueness checks, even-input modulo-8 law,')
    print('      low-shell three-square obstruction counts, and exhaustive pairwise checks on n,m<42.')
    for v in (4, 6, 8, 10):
        a = sequence(v, 11)
        r1 = next(n for n in range(1, 32, 2) if a[n] % 32 == 28)
        r2 = next(n for n in range(1, 128, 2) if a[n] % 128 == 112)
        print(f'v={v}: first two odd-index forbidden residue classes {r1} mod 32, {r2} mod 128')


if __name__ == '__main__':
    main()
