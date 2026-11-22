"""Exact small-instance checks for primitive-word convolution spectra.

Uses ordinary integer arithmetic throughout: Walsh transforms for binary
alphabets, cyclotomic coefficient comparisons for cyclic alphabets of
orders 3 and 4, and binary dot products for the Klein four-group.
"""
from itertools import product
from math import prod


def mobius(m):
    primes = []
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            primes.append(p)
        p += 1
    if m > 1:
        primes.append(m)
    return (-1) ** len(primes)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def radical(n):
    return prod(p for p in divisors(n) if p > 1 and
                all(p % d for d in range(2, int(p ** .5) + 1)))


def is_primitive(w):
    n = len(w)
    return all(any(w[j] != w[j % d] for j in range(n))
               for d in divisors(n) if d < n)


def expected_frequency(c, q):
    n = len(c)
    total = 0
    for d in divisors(n):
        mu = mobius(n // d)
        if mu and all(sum(c[j] for j in range(r, n, d)) % q == 0
                      for r in range(d)):
            total += mu * (q ** d)
    return total


def test_binary_fast(n):
    x = [int(is_primitive(tuple((mask >> i) & 1 for i in range(n))))
         for mask in range(1 << n)]
    v = x[:]
    step = 1
    while step < len(v):
        for start in range(0, len(v), 2 * step):
            for j in range(start, start + step):
                a, b = v[j], v[j + step]
                v[j], v[j + step] = a + b, a - b
        step *= 2
    d0 = n // radical(n)
    assert sum(z != 0 for z in v) == 2 ** (n - d0)
    assert min(abs(z) for z in v if z) == 2 ** d0
    assert max(abs(z) for z in v) == v[0] == sum(x)
    for mask, z in enumerate(v):
        c = [(mask >> i) & 1 for i in range(n)]
        assert z == expected_frequency(c, 2), (n, mask, z)
    return len(v)


def test_cyclic(q, n):
    words = list(product(range(q), repeat=n))
    primitive = [w for w in words if is_primitive(w)]
    count = 0
    values = []
    for c in words:
        coeff = [0] * q
        for w in primitive:
            exponent = sum(a * x for a, x in zip(c, w)) % q
            coeff[exponent] += 1
        if q == 3:
            assert coeff[1] == coeff[2], (q, n, c, coeff)
            val = coeff[0] - coeff[2]
        elif q == 4:
            assert coeff[1] == coeff[3], (q, n, c, coeff)
            val = coeff[0] - coeff[2]
        else:
            raise ValueError(q)
        assert val == expected_frequency(c, q), (q, n, c, val)
        count += (val != 0)
        values.append(val)
    d0 = n // radical(n)
    assert count == q ** (n - d0), (q, n, count)
    assert min(abs(v) for v in values if v) == q ** d0
    assert max(abs(v) for v in values) == len(primitive)
    return len(words)


def test_klein(n):
    q = 4
    words = list(product(range(4), repeat=n))
    primitive = [w for w in words if is_primitive(w)]
    count = 0
    values = []
    for c in words:
        total = sum((-1) ** sum((a & 1) * (x & 1) +
                                 ((a >> 1) & 1) * ((x >> 1) & 1)
                                 for a, x in zip(c, w))
                    for w in primitive)
        # In the Klein group, a character product is trivial exactly
        # when the bitwise XOR of the character labels is zero.
        pred = sum(mobius(n // d) * q ** d for d in divisors(n)
                   if all(__import__('functools').reduce(
                       lambda a, b: a ^ b, c[r:n:d], 0) == 0
                          for r in range(d)))
        assert total == pred, (n, c, total, pred)
        count += (total != 0)
        values.append(total)
    assert count == q ** (n - n // radical(n))
    assert min(abs(v) for v in values if v) == q ** (n // radical(n))
    assert max(abs(v) for v in values) == len(primitive)
    return len(words)


if __name__ == '__main__':
    binary = sum(test_binary_fast(n) for n in range(2, 13))
    ternary = sum(test_cyclic(3, n) for n in range(2, 7))
    cyclic4 = sum(test_cyclic(4, n) for n in range(2, 5))
    klein = sum(test_klein(n) for n in range(2, 5))
    print('PASS binary_frequency_tests=%d ternary=%d cyclic4=%d klein=%d' %
          (binary, ternary, cyclic4, klein))
