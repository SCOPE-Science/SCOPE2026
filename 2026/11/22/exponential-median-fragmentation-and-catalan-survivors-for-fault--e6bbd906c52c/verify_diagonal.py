#!/usr/bin/env python3
"""Independent diagonal-obstacle dynamic program and extremal signatures."""
from math import comb
from itertools import product


def count_avoiding(a, b, faults):
    # Counts original-distance north/east paths without constructing a route graph.
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    dp[0][0] = 1
    for x in range(a + 1):
        for y in range(b + 1):
            if (x, y) == (0, 0):
                continue
            if (x, y) in faults:
                continue
            dp[x][y] = (dp[x-1][y] if x else 0) + (dp[x][y-1] if y else 0)
    return dp[a][b]


def route_signature(word, faults):
    x = y = 0
    vertices = {(x, y)}
    for letter in word:
        x += (letter == 'E')
        y += (letter == 'N')
        vertices.add((x, y))
    assert not vertices.intersection(faults)
    at = []
    x = 0
    at.append(x)
    for letter in word:
        x += (letter == 'E')
        at.append(x)
    return tuple(-1 if at[u+v] < u else 1 for u, v in sorted(faults))


def main():
    checked = 0
    for k in range(1, 13):
        side = 2 * k
        faults = {(2*i-1, 2*i-1) for i in range(1, k+1)}
        count = count_avoiding(side, side, faults)
        catalan = comb(4*k, 2*k) // (2*k + 1)
        assert count == catalan, (k, count, catalan)
        if k <= 10:
            seen = set()
            for bits in product((0, 1), repeat=k):
                # Every block moves between successive even-diagonal vertices.
                word = ''.join(('EENN' if bit else 'NNEE') for bit in bits)
                sign = route_signature(word, faults)
                assert sign not in seen
                seen.add(sign)
            assert len(seen) == 2 ** k
        checked += 1
    print('VERIFY_DIAGONAL_OK',{'catalan_dimensions':checked,
                                'largest_half_side':24,
                                'sharp_signatures_checked':2**10})


if __name__ == '__main__':
    main()
