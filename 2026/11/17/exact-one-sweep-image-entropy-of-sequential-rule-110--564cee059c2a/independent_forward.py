#!/usr/bin/env python3
"""Independent exhaustive forward simulation and output-predecessor test."""


def rule110(l, c, r):
    # Independent direct Boolean expression (not the bit-number decoder).
    return ((1-c) & r) | (c & (1 - (l & r)))


def sweep(x):
    bits = list(x)
    n = len(bits)
    for i in range(n):
        bits[i] = rule110(bits[(i-1) % n], bits[i], bits[(i+1) % n])
    return tuple(bits)


def reachability(y):
    n = len(y)
    first = y[0]
    # Try the actual endpoint old bit and previous-new bit independently.
    possible = set()
    for old_last in (0, 1):
        for old_first in (0, 1):
            for old_second in (0, 1):
                if rule110(old_last, old_first, old_second) == first:
                    possible.add((old_last, old_second))
    for i in range(1, n-1):
        possible = {(last, following) for last, current in possible
                    for following in (0, 1)
                    if rule110(y[i-1], current, following) == y[i]}
    return any(last == old_at_last and
               rule110(y[-2], last, first) == y[-1]
               for last, old_at_last in possible)


def all_words(n):
    for code in range(1 << n):
        yield tuple((code >> i) & 1 for i in range(n))


def main():
    # Direct exhaustive image construction, independent of transfer matrix.
    counts = []
    for n in range(3, 17):
        image = {sweep(x) for x in all_words(n)}
        assert len(image) < 1 << n
        # For smaller lengths verify exact membership including all absent words.
        if n <= 13:
            assert all(reachability(y) == (y in image) for y in all_words(n))
        counts.append(len(image))
    expected = [5, 11, 20, 39, 75, 143, 274, 522, 996,
                1898, 3617, 6892, 13131, 25018]
    assert counts == expected, (counts, expected)
    print("Independent Rule 110 forward sweep: PASS")
    print("All 2^n initial states checked at each n=3..16")
    print("Full reachability membership checked at each n=3..13")
    print("image counts n=3..16:", counts)

if __name__ == "__main__":
    main()
