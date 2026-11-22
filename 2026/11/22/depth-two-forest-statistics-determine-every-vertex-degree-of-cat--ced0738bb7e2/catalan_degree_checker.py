"""Exact finite checks for Catalan-matroid base-polytope vertex degrees.

The two degree calculations are independent: one checks every exchanged binary
word for Dyck admissibility, the other parses nested Dyck blocks. An integer
polynomial recurrence independently produces the degree generating polynomial.
"""
from collections import Counter
from math import comb


def dyck_words(n):
    def rec(prefix, u, d):
        if u == d == n:
            yield prefix
        else:
            if u < n:
                yield from rec(prefix + 'U', u + 1, d)
            if d < u:
                yield from rec(prefix + 'D', u, d + 1)
    yield from rec('', 0, 0)


def is_dyck(word):
    h = 0
    for step in word:
        h += 1 if step == 'U' else -1
        if h < 0:
            return False
    return h == 0


def degree_by_exchange(word):
    symbols = list(word)
    ups = [i for i, x in enumerate(symbols) if x == 'U']
    downs = [i for i, x in enumerate(symbols) if x == 'D']
    count = 0
    for i in ups:
        for j in downs:
            symbols[i], symbols[j] = symbols[j], symbols[i]
            count += is_dyck(symbols)
            symbols[i], symbols[j] = symbols[j], symbols[i]
    return count


def depth_two_sizes(word):
    """Subtree sizes of children of depth-one roots in the Dyck forest."""
    sizes = []
    stack = []
    for step in word:
        if step == 'U':
            stack.append(1)
        else:
            size = stack.pop()
            if len(stack) == 1:
                sizes.append(size)
            if stack:
                stack[-1] += size
    assert not stack
    return sizes


def degree_by_forest(word):
    n = len(word) // 2
    return comb(n, 2) + sum(comb(s, 2) for s in depth_two_sizes(word))


def poly_add(a, b):
    out = Counter(a)
    for k, v in b.items():
        out[k] += v
    return out


def degree_polynomial(n):
    """Coefficient recurrence for the full excess-degree polynomial."""
    F = [Counter({0: 1})]
    for m in range(1, n + 1):
        p = Counter(F[m - 1])
        for s in range(1, m):
            w = comb(2 * (s - 1), s - 1) // s
            shift = comb(s, 2)
            for k, v in F[m - s].items():
                p[k + shift] += w * v
        F.append(p)
    return F


def check(max_n=9):
    Fs = degree_polynomial(max_n)
    for n in range(1, max_n + 1):
        spectrum = Counter()
        min_paths = []
        max_paths = []
        low = comb(n, 2)
        high = (n - 1) ** 2
        for word in dyck_words(n):
            d = degree_by_exchange(word)
            assert d == degree_by_forest(word), (n, word, d, degree_by_forest(word))
            spectrum[d - low] += 1
            if d == low:
                min_paths.append(word)
                assert max(sum(1 if t == 'U' else -1 for t in word[:j])
                           for j in range(1, 2*n+1)) <= 2
            if d == high:
                max_paths.append(word)
                if n >= 3:
                    assert word.startswith('UU') and word.endswith('DD')
                    assert is_dyck(word[2:-2])
        assert spectrum == Fs[n], (n, spectrum, Fs[n])
        assert len(min_paths) == 2 ** (n - 1)
        if n >= 3:
            assert len(max_paths) == comb(2*n-4,n-2) // (n-1)
        assert sum(spectrum.values()) == comb(2*n,n)//(n+1)
        print(f'n={n}, vertices={sum(spectrum.values())}, '
              f'min={low}, count_min={len(min_paths)}, '
              f'max={high}, count_max={len(max_paths)}, '
              f'edges={sum((low+k)*v for k,v in spectrum.items())//2}')
    print('CATALAN_POLYTOPE_DEGREES_EXACT_PASS')


if __name__ == '__main__':
    check()
