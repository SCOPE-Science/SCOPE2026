#!/usr/bin/env python3
"""Exact certificate for the negative-entry-position Fourier spectrum of ASMs.
Run with Python 3.9+; no third-party dependencies.
"""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction
from math import factorial


def masks_from_row_transitions(n):
    """Enumerate via all legal transitions of column-prefix states."""
    states = [tuple(1 if j in s else 0 for j in range(n))
              for k in range(n + 1) for s in combinations(range(n), k)]
    by_size = {k: [s for s in states if sum(s) == k] for k in range(n + 1)}
    out = Counter()

    def rec(i, old, mask):
        if i == n:
            assert old == (1,) * n
            out[mask] += 1
            return
        for nxt in by_size[i + 1]:
            delta = [nxt[j] - old[j] for j in range(n)]
            nz = [v for v in delta if v]
            if nz != [1 if j % 2 == 0 else -1 for j in range(len(nz))]:
                continue
            new_mask = mask
            for j in range(1, n - 1):
                if 1 <= i < n - 1 and delta[j] == -1:
                    new_mask |= 1 << ((i - 1) * (n - 2) + (j - 1))
            rec(i + 1, nxt, new_mask)
    rec(0, (0,) * n, 0)
    return out


def masks_from_monotone_triangles(n):
    """Independent, topological enumeration of interlacing strict rows."""
    out = Counter()
    def rec(lower, rows_bottom_up):
        r = len(lower)
        if r == 1:
            rows = list(reversed(rows_bottom_up))
            previous = set()
            mask = 0
            for i, entries in enumerate(rows):
                current = set(entries)
                for j in range(2, n):
                    if 1 <= i < n - 1 and j in previous and j not in current:
                        mask |= 1 << ((i - 1) * (n - 2) + (j - 2))
                previous = current
            assert previous == set(range(1, n + 1))
            out[mask] += 1
            return
        for values in product(*(range(lower[j], lower[j + 1] + 1) for j in range(r - 1))):
            if all(values[j] < values[j + 1] for j in range(r - 2)):
                rec(values, rows_bottom_up + [values])
    rec(tuple(range(1, n + 1)), [tuple(range(1, n + 1))])
    return out


def transform(values):
    a = list(values)
    width = 1
    while width < len(a):
        for offset in range(0, len(a), 2 * width):
            for t in range(offset, offset + width):
                u, v = a[t], a[t + width]
                a[t], a[t + width] = u + v, u - v
        width *= 2
    return a


def symmetry_orbit(mask):
    assert 0 <= mask < 65536
    orbit = set()
    for reflect in (False, True):
        for turns in range(4):
            m = 0
            for row in range(4):
                for col in range(4):
                    a, b = row, (3 - col if reflect else col)
                    for _ in range(turns):
                        a, b = b, 3 - a
                    if mask >> (4 * row + col) & 1:
                        m |= 1 << (4 * a + b)
            orbit.add(m)
    return orbit


EXPECTED_REPS = [
    (4, 1910, 8), (8, 5501, 9), (8, 7151, 11), (8, 7806, 10),
    (8, 7911, 10), (8, 8031, 11), (8, 8043, 10), (8, 8119, 11),
    (8, 11195, 10), (8, 11255, 11), (8, 14076, 10), (8, 15095, 11),
    (8, 15354, 11), (8, 15865, 11), (8, 16310, 11), (8, 23279, 11),
    (8, 23545, 11), (8, 24505, 11), (8, 24511, 13), (8, 32239, 13),
    (8, 32719, 13), (8, 37871, 11), (4, 40863, 12), (4, 48623, 13),
]


def main():
    counts = {1: 1, 2: 2, 3: 7, 4: 42, 5: 429, 6: 7436}
    for n in range(1, 7):
        a = masks_from_row_transitions(n)
        b = masks_from_monotone_triangles(n)
        assert a == b, (n, a, b)
        assert sum(a.values()) == counts[n]
        assert a[0] == factorial(n)
        size = 1 << ((n - 2) ** 2) if n >= 2 else 1
        kernel = [a.get(k, 0) for k in range(size)]
        spectrum = transform(kernel)
        assert transform(spectrum) == [size * x for x in kernel]
        assert sum(z*z for z in spectrum) == size * sum(z*z for z in kernel)
        if n <= 5:
            assert all(z != 0 for z in spectrum), n
        if n == 6:
            zeros = {i for i,z in enumerate(spectrum) if z == 0}
            assert len(zeros) == 180
            assert Counter(i.bit_count() for i in zeros) == {
                8: 4, 9: 8, 10: 40, 11: 96, 12: 4, 13: 28}
            assert sum(z > 0 for z in spectrum) == 60402
            assert sum(z < 0 for z in spectrum) == 4954
            assert min(abs(z) for z in spectrum if z) == 2
            assert max(abs(z) for z in spectrum) == counts[n]
            assert all(spectrum[i] == sum(
                count * (-1 if (i & mask).bit_count() % 2 else 1)
                for mask,count in a.items()) for _,i,_ in EXPECTED_REPS)
            seen=set()
            reps=[]
            for f in sorted(zeros):
                if f not in seen:
                    orbit=symmetry_orbit(f)
                    assert orbit <= zeros
                    seen.update(orbit)
                    reps.append((len(orbit), min(orbit), min(orbit).bit_count()))
            assert seen == zeros
            assert reps == EXPECTED_REPS
            zhat = transform([int(i in zeros) for i in range(size)])
            assert transform(zhat) == [size * int(i in zeros) for i in range(size)]
            projection_norm = Fraction(size-len(zeros)+sum(abs(q) for q in zhat[1:]), size)
            assert projection_norm == Fraction(94295,8192)
            print('Order 6: kernel types',len(a),'nonzero modes',size-len(zeros),
                  'zero modes',len(zeros),'D4 zero orbits',len(reps),
                  'gap',2,'endpoint norm',projection_norm)
        print('Order',n,'total ASMs',counts[n],'kernel classes',len(a),'zeros',spectrum.count(0))
    print('PASS: two independent ASM generators, exact transforms, orbit and endpoint certificates')

if __name__ == '__main__':
    main()
