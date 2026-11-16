"""Independent integer checks for four-colour character congruences.

Run with Python 3.9+; no dependencies. The computation is finite corroboration,
not a substitute for the universal proof in RESULT.md.
"""
from itertools import product
from math import comb


def fwht(data):
    data = list(data)
    h = 1
    while h < len(data):
        for left in range(0, len(data), 2 * h):
            for j in range(left, left + h):
                x, y = data[j], data[j + h]
                data[j], data[j + h] = x + y, x - y
        h *= 2
    return data


def mask_edges(n, mask):
    edges = [(i, j) for j in range(n) for i in range(j)]
    return [e for index, e in enumerate(edges) if mask & (1 << index)]


def full_spectrum(n, edges):
    x = [0] * (1 << (2*n))
    for colors in product(range(4), repeat=n):
        if any(colors[i] == colors[j] for i, j in edges):
            continue
        index = sum(c << (2*i) for i, c in enumerate(colors))
        x[index] = 1
    total = sum(x)
    return fwht(x), total


def balanced(index, n):
    z = 0
    for i in range(n):
        z ^= (index >> (2*i)) & 3
    return z == 0


def direct_character_sum(n, edges, frequency):
    total = 0
    for c in product(range(4), repeat=n):
        if any(c[i] == c[j] for i, j in edges):
            continue
        phase = 0
        for i, x in enumerate(c):
            b = (frequency >> (2*i)) & 3
            phase ^= (b & x).bit_count() & 1
        total += 1 if phase == 0 else -1
    return total


def stirling_second(n, k):
    a = [[0] * (k+1) for _ in range(n+1)]
    a[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i,k)+1):
            a[i][j] = j*a[i-1][j] + a[i-1][j-1]
    return a[n][k]


def biclique_edges(m, n):
    return [(i, m+j) for i in range(m) for j in range(n)]


def main():
    cases = 0
    coefficients = 0
    for n in range(1, 5):
        for edge_mask in range(1 << comb(n, 2)):
            edges = mask_edges(n, edge_mask)
            spectrum, total = full_spectrum(n, edges)
            assert total % 4 == 0
            for a, value in enumerate(spectrum):
                assert (value == 0 if not balanced(a, n) else value % 16 == total % 16)
                coefficients += 1
            cases += 1
    checked = 0
    directly = 0
    for m in range(2, 5):
        for n in range(2, 5):
            d = m + n
            edges = biclique_edges(m, n)
            spectrum, total = full_spectrum(d, edges)
            assert total % 16 == (4 if (m+n)%2==0 else 12)
            expected = sum(stirling_second(m,k) * (4 if k==1 else 12 if k==2 else 24) * (4-k)**n for k in range(1,4))
            assert total == expected
            for a, val in enumerate(spectrum):
                if balanced(a,d):
                    assert val != 0 and val % 16 == total % 16
                    checked += 1
                else:
                    assert val == 0
            # Compare against a second method: direct signed sums at fixed indexed frequencies.
            for a in [0,1,5,7,17,31,53,79,127, 255, (1<<(2*d))-1]:
                if a < len(spectrum):
                    assert direct_character_sum(d, edges, a) == spectrum[a]
                    directly += 1
    print('CHROMATIC_FOURIER_RESIDUE_PASS',
          'graphs=', cases,'general_coefficients=', coefficients,
          'biclique_balanced_coefficients=',checked,'direct_checks=',directly)

if __name__ == '__main__':
    main()
