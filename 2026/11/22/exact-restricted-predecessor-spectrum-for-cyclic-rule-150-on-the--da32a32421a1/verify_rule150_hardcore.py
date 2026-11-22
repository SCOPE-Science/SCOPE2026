"""Independent finite checks of indexed cyclic Rule 150 on the no-11 language.

Run with Python 3: python verify_rule150_hardcore.py
The infinite-length claims are proved by the accompanying mathematical argument;
these computations check the stated small instances, not all ring lengths.
"""
from collections import Counter


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def valid(x, n):
    return all(not (((x >> i) & 1) and ((x >> ((i + 1) % n)) & 1))
               for i in range(n))


def rule150(x, n):
    value = 0
    for i in range(n):
        bit = ((x >> ((i - 1) % n)) ^ (x >> i) ^
               (x >> ((i + 1) % n))) & 1
        value |= bit << i
    return value


def expected(n):
    if n % 3:
        return {1: lucas(n)}
    k = n // 3
    return {degree: number for degree, number in (
        (1, lucas(n) - 3 * 2**k + 3),
        (2, 3 * 2**(k - 1) - 3),
        (3, 1),
    ) if number}


def check():
    for n in range(1, 22):
        inputs = [x for x in range(1 << n) if valid(x, n)]
        assert len(inputs) == lucas(n), ('domain', n)
        fibers = Counter(rule150(x, n) for x in inputs)
        hist = Counter(fibers.values())
        assert dict(hist) == expected(n), ('spectrum', n, hist, expected(n))
        assert sum(m * number for m, number in hist.items()) == lucas(n)
        if n % 3 == 0:
            k = n // 3
            assert fibers[(1 << n) - 1] == 3, ('triple output', n)
            # There are 2^k source configurations colliding for each
            # nonzero kernel shift. This is a check independent of histogram.
            for triple in (0b011, 0b101, 0b110):
                shift = sum(triple << (3 * i) for i in range(k))
                compatible = sum(valid(x ^ shift, n) for x in inputs)
                assert compatible == 2**k, ('collision-shift', n, triple)
            assert len(fibers) == lucas(n) - 3 * 2**(k - 1) + 1
        else:
            assert len(fibers) == lucas(n)
    print('VERIFY_OK all indexed cyclic inputs n=1..21; kernel-pair counts and fiber spectra')


if __name__ == '__main__':
    check()
