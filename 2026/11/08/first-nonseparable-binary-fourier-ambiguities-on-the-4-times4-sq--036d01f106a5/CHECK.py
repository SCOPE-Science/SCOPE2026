"""Exhaustive exact-integer certificate for binary square Fourier-autocorrelation fibers.

Run with Python 3: python CHECK.py. Only standard-library modules are used.
"""
from collections import Counter, defaultdict


def samples(code, n):
    return [[1 - 2 * ((code >> (n * y + x)) & 1)
             for x in range(n)] for y in range(n)]


def shifts(n):
    return ([(0, dx) for dx in range(1, n)] +
            [(dy, dx) for dy in range(1, n)
             for dx in range(1 - n, n)])


def autocorrelation(code, n):
    a = samples(code, n)
    return tuple(sum(a[y][x] * a[y + dy][x + dx]
                     for y in range(n) for x in range(n)
                     if 0 <= x + dx < n and y + dy < n)
                 for dy, dx in shifts(n))


def reverse_and_normalize(code, n):
    size = n * n
    rev = sum(((code >> j) & 1) << (size - 1 - j)
              for j in range(size))
    if rev & 1:
        rev ^= (1 << size) - 1
    return rev


def sign_reversal_class(code, n):
    assert code % 2 == 0  # upper-left entry is +1
    return min(code, reverse_and_normalize(code, n))


def tensor_product(code, n):
    a = samples(code, n)
    return all(a[y][x] * a[0][0] == a[y][0] * a[0][x]
               for y in range(n) for x in range(n))


def enumerate_fibers(n):
    fibers = defaultdict(set)
    for word in range(1 << (n * n - 1)):
        code = word << 1  # exhaustive global-sign normalization
        fibers[autocorrelation(code, n)].add(sign_reversal_class(code, n))
    return list(fibers.values())


def independent_correlation(a, dy, dx):
    # Independent coefficient extraction in P(X,Y)P(X^{-1},Y^{-1}).
    n = len(a)
    coeff = defaultdict(int)
    for y in range(n):
        for x in range(n):
            for v in range(n):
                for u in range(n):
                    coeff[(y - v, x - u)] += a[y][x] * a[v][u]
    return coeff[(dy, dx)]


def run():
    expected = {
        1: ({1: 1}, 0),
        2: ({1: 6}, 0),
        3: ({1: 134, 2: 1}, 0),
        4: ({1: 16488, 2: 12}, 8),
    }
    for n, (histogram, required_nontensor) in expected.items():
        fibers = enumerate_fibers(n)
        actual = dict(Counter(map(len, fibers)))
        assert actual == histogram, (n, actual)
        nontensor = [f for f in fibers if len(f) > 1
                     and all(not tensor_product(a, n) for a in f)]
        assert len(nontensor) == required_nontensor, (n, len(nontensor))
        assert sum(map(len, fibers)) == len({sign_reversal_class(w << 1, n)
                                            for w in range(1 << (n * n - 1))})
        print(f"n={n}: {len(fibers)} Fourier-power fibers; sizes={actual}; "
              f"all-nontensor double fibers={len(nontensor)}")

    # Two explicitly inequivalent non-tensor masks with the same full spectrum.
    first, second, n = 12442, 3238, 4
    assert sign_reversal_class(first, n) != sign_reversal_class(second, n)
    assert not tensor_product(first, n) and not tensor_product(second, n)
    assert autocorrelation(first, n) == autocorrelation(second, n)
    for dy, dx in shifts(n):
        ca = independent_correlation(samples(first, n), dy, dx)
        cb = independent_correlation(samples(second, n), dy, dx)
        assert ca == cb
    print("WITNESS_AND_INDEPENDENT_AUTOCORRELATION_CHECK_PASSED")
    print("ALL_EXHAUSTIVE_CHECKS_PASSED")


if __name__ == '__main__':
    run()
