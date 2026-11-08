#!/usr/bin/env python3
"""Exact self-contained enumeration of binary two-row Fourier-intensity fibers.

Only the Python standard library is required. All arithmetic is integral.
"""
from collections import Counter, defaultdict


def sign(bits, j):
    return 1 - 2 * ((bits >> j) & 1)


def reverse(n, bits):
    return sum(((bits >> j) & 1) << (n - 1 - j) for j in range(n))


def canonical(n, a, b):
    mask = (1 << n) - 1
    # The four arrays related by global sign and central inversion.
    x, y = reverse(n, b), reverse(n, a)
    return min((a, b), (a ^ mask, b ^ mask),
               (x, y), (x ^ mask, y ^ mask))


def direct_signature(n, a, b):
    # All non-redundant aperiodic autocorrelations, at row lags 0 and 1.
    # The omitted row lag -1 follows by C(-1,-j)=C(1,j).
    rows = ([sign(a, i) for i in range(n)],
            [sign(b, i) for i in range(n)])
    out = []
    for dr in (0, 1):
        for dj in range(1 - n, n):
            v = 0
            for r in range(2 - dr):
                for j in range(n):
                    if 0 <= j + dj < n:
                        v += rows[r][j] * rows[r + dr][j + dj]
            out.append(v)
    return tuple(out)


def fast_signature(n, a, b):
    # Independently compute just the nonconstant row-0 correlations
    # and all row-1 correlations using Hamming distance.
    out = []
    for j in range(1, n):
        mask = (1 << (n - j)) - 1
        out.append(2 * (n - j)
                   - 2 * ((a ^ (a >> j)) & mask).bit_count()
                   - 2 * ((b ^ (b >> j)) & mask).bit_count())
    for j in range(1 - n, n):
        if j >= 0:
            mask = (1 << (n - j)) - 1
            out.append(n - j - 2 * ((a ^ (b >> j)) & mask).bit_count())
        else:
            mask = (1 << (n + j)) - 1
            out.append(n + j - 2 * (((a >> -j) ^ b) & mask).bit_count())
    return tuple(out)


def packed_from_direct(n, sig):
    zero_row = sig[:2 * n - 1]
    one_row = sig[2 * n - 1:]
    assert zero_row[n - 1] == 2 * n
    assert all(zero_row[n - 1 - k] == zero_row[n - 1 + k]
               for k in range(1, n))
    return tuple(zero_row[n:] + one_row)


def fiber_census(n):
    groups = defaultdict(list)
    visited = 0
    for a in range(1 << n):
        for b in range(1 << n):
            if canonical(n, a, b) != (a, b):
                continue
            visited += 1
            direct = direct_signature(n, a, b)
            assert packed_from_direct(n, direct) == fast_signature(n, a, b)
            groups[direct].append((a, b))
    counts = Counter(len(fiber) for fiber in groups.values())
    assert sum(t * c for t, c in counts.items()) == visited
    return visited, counts, [tuple(fiber) for fiber in groups.values()
                             if len(fiber) > 1]


def polynomial_autocorrelation(n, a, b):
    # Laurent coefficient dictionary of P(z,w)P(z^-1,w^-1).
    P = {(r, j): sign(bits, j)
         for r, bits in enumerate((a, b)) for j in range(n)}
    out = {}
    for (r, j), c in P.items():
        for (s, k), d in P.items():
            out[(r - s, j - k)] = out.get((r - s, j - k), 0) + c * d
    return out


def main():
    expected = {
        1: (2, {1: 2}),
        2: (6, {1: 6}),
        3: (20, {1: 20}),
        4: (72, {1: 72}),
        5: (272, {1: 272}),
        6: (1056, {1: 1048, 2: 4}),
        7: (4160, {1: 4160}),
        8: (16512, {1: 16488, 2: 12}),
    }
    for n, expected_row in expected.items():
        visited, counts, examples = fiber_census(n)
        assert (visited, dict(counts)) == expected_row, (n, visited, counts)
        if n == 6:
            assert len(examples) == 4
            for fiber in examples:
                for a, b in fiber:
                    # Both arrays are nonseparable (not a row outer product).
                    assert a != b and a != (b ^ ((1 << n) - 1))
                    assert canonical(n, a, b) == (a, b)
            for (a, b), (c, d) in examples:
                assert polynomial_autocorrelation(n, a, b) == polynomial_autocorrelation(n, c, d)
        print(f'n={n}: classes={visited}, fibers={dict(sorted(counts.items()))}')
    # A fixed, presentation-friendly nonseparable double fiber.
    assert canonical(6, 3, 22) == (3, 22)
    assert canonical(6, 15, 26) == (15, 26)
    assert (3, 22) != (15, 26)
    assert polynomial_autocorrelation(6, 3, 22) == polynomial_autocorrelation(6, 15, 26)
    print('ALL_EXACT_TWO_ROW_CHECKS_PASSED')


if __name__ == '__main__':
    main()
