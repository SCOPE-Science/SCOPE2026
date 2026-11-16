"""Exact integer checks of the Fourier spectrum of fan-graph spanning trees.

Usage: python check_fan_walsh.py
No third-party dependencies.
"""
from itertools import combinations
from math import gcd


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def fan_edges(n):
    # Vertex 0 is the hub; the path has vertices 1 through n.
    return [(0, i) for i in range(1, n + 1)] + [(i, i + 1) for i in range(1, n)]


def indicator_of_trees(n):
    edges = fan_edges(n)
    out = [0] * (1 << len(edges))
    for choice in combinations(range(len(edges)), n):
        parent = list(range(n + 1))

        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x

        mask = 0
        possible = True
        for e in choice:
            u, v = edges[e]
            ru, rv = root(u), root(v)
            if ru == rv:
                possible = False
                break
            parent[ru] = rv
            mask |= 1 << e
        if possible and len({root(i) for i in range(n + 1)}) == 1:
            out[mask] = 1
    return out


def walsh_transform(values):
    a = values[:]
    m = len(a)
    h = 1
    while h < m:
        for i in range(0, m, 2 * h):
            for j in range(i, i + h):
                u, v = a[j], a[j + h]
                a[j], a[j + h] = u + v, u - v
        h *= 2
    return a


def signed_tree_determinant(n, freq):
    s = [-1 if (freq >> i) & 1 else 1 for i in range(n)]
    t = [-1 if (freq >> (n + i)) & 1 else 1 for i in range(n - 1)]
    if n == 1:
        return s[0]
    previous2, previous1 = 1, s[0] + t[0]
    for i in range(1, n):
        diagonal = s[i] + t[i-1] + (t[i] if i < n-1 else 0)
        previous2, previous1 = previous1, diagonal * previous1 - previous2
    return previous1


def special_zero_mask(n, toggles=0):
    # All path-edge signs positive, all spoke signs negative except
    # freely chosen spokes whose path vertex index is 2 modulo 3.
    mask = (1 << n) - 1
    for j, i in enumerate(range(2, n + 1, 3)):
        if (toggles >> j) & 1:
            mask ^= 1 << (i - 1)
    return mask


def check():
    for n in range(1, 10):
        indicator = indicator_of_trees(n)
        spectrum = walsh_transform(indicator)
        total_trees = sum(indicator)
        assert total_trees == fibonacci(2*n), (n, total_trees)
        assert spectrum[0] == total_trees
        assert max(map(abs, spectrum)) == total_trees
        min_positive = min(abs(w) for w in spectrum if w)
        assert min_positive == (2 if n % 3 == 0 else 1), (n,min_positive)
        assert (0 in spectrum) == (n % 3 == 0), n
        g = 0
        for w in spectrum:
            g = gcd(g, w)
        assert g == (2 if n % 3 == 0 else 1), n
        for freq, w in enumerate(spectrum):
            assert w == signed_tree_determinant(n, freq), (n, freq, w)
        if n % 3 == 0:
            k = n // 3
            zeros = set()
            for t in range(1 << k):
                mask = special_zero_mask(n, t)
                zeros.add(mask)
                zeros.add(mask ^ ((1 << (2 * n - 1)) - 1))
            assert len(zeros) == 2 ** (k + 1), n
            assert all(spectrum[freq] == 0 for freq in zeros), n
            assert abs(spectrum[special_zero_mask(n) ^ 1]) == 2, n
        else:
            assert abs(spectrum[special_zero_mask(n)]) == 1, n
        print(f'n={n}, trees={total_trees}, zeros={spectrum.count(0)}, '
              f'least_positive={min_positive}, gcd={g}')

    # Long-size exact arithmetic checks of constructive witnesses.
    for n in range(1, 151):
        x = signed_tree_determinant(n, special_zero_mask(n))
        assert (x == 0) == (n % 3 == 0), n
        if n % 3 == 0:
            assert abs(signed_tree_determinant(n, special_zero_mask(n) ^ 1)) == 2, n
        else:
            assert abs(x) == 1, n
    print('FAN_WALSH_EXACT_PASS n=1..9 full spectra; n=1..150 witnesses')

if __name__ == '__main__':
    check()
