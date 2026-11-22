#!/usr/bin/env python3
"""Exact F_2[u] characteristic-polynomial and onsite-basis orbit census."""
from collections import Counter

def multiply(x, y):
    out = 0
    while y:
        if y & 1:
            out ^= x
        x <<= 1
        y >>= 1
    return out

def polynomial_data(code):
    x = [((code >> j) & 1) ^ (((code >> (j + 4)) & 1) << 1)
         for j in range(4)]
    trace = x[0] ^ x[3]
    determinant = multiply(x[0], x[3]) ^ multiply(x[1], x[2])
    return trace, determinant

def classify(code):
    trace, determinant = polynomial_data(code)
    entropy_coefficient = max([0] + [j for poly in (trace, determinant)
                                          for j in range(3) if (poly >> j) & 1])
    unit = determinant != 0 and determinant & (determinant - 1) == 0
    strong = (determinant != 0 and not unit and
              1 ^ trace ^ determinant != 0 and
              4 ^ multiply(2, trace) ^ determinant != 0)
    return entropy_coefficient, bool(strong)

def matmul(a, b):
    return [(a[0] & b[0]) ^ (a[1] & b[2]),
            (a[0] & b[1]) ^ (a[1] & b[3]),
            (a[2] & b[0]) ^ (a[3] & b[2]),
            (a[2] & b[1]) ^ (a[3] & b[3])]

def matdet(a):
    return (a[0] & a[3]) ^ (a[1] & a[2])

def pack(b, c):
    return sum(t << j for j, t in enumerate(b + c))

def orbit(code, group):
    b = [(code >> j) & 1 for j in range(4)]
    c = [(code >> (j + 4)) & 1 for j in range(4)]
    return {pack(matmul(matmul(p, b), [p[3], p[1], p[2], p[0]]),
                 matmul(matmul(p, c), [p[3], p[1], p[2], p[0]]))
            for p in group}

def main():
    counts = Counter(map(classify, range(256)))
    expected = {(0, False): 40, (1, False): 102, (1, True): 18,
                (2, False): 42, (2, True): 54}
    assert counts == expected, (counts, expected)
    group = [[(i >> j) & 1 for j in range(4)] for i in range(16)]
    group = [p for p in group if matdet(p)]
    assert len(group) == 6
    visited = set()
    orbit_counts = Counter()
    orbit_sizes = Counter()
    for code in range(256):
        if code in visited:
            continue
        o = orbit(code, group)
        assert code in o
        assert all(classify(j) == classify(code) for j in o)
        visited |= o
        orbit_counts[classify(code)] += 1
        orbit_sizes[len(o)] += 1
    assert len(visited) == 256
    assert orbit_counts == {(0, False): 12, (1, False): 17,
                            (1, True): 3, (2, False): 10, (2, True): 14}
    assert orbit_sizes == {1: 4, 2: 6, 3: 12, 6: 34}
    print('All 256 characteristic-polynomial tests passed.')
    print('Entropy/strong-transitivity counts:', sorted(counts.items()))
    print('Onsite basis-change orbits:', sorted(orbit_counts.items()))
    print('Orbit sizes:', sorted(orbit_sizes.items()))

if __name__ == '__main__':
    main()
