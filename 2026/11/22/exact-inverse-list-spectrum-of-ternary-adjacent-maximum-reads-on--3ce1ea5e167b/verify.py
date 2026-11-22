#!/usr/bin/env python3
"""Independent integer checks of ternary proper-source adjacent maximum reads.

Only the Python standard library is needed.  Lengths and outputs are indexed,
not quotiented by rotation or alphabet relabeling.
"""
from collections import Counter, defaultdict
from itertools import product


def sources(n):
    def rec(t):
        if len(t) == n:
            yield tuple(t)
        else:
            for a in range(3):
                if not t or a != t[-1]:
                    yield from rec(t + [a])
    yield from rec([])


def direct_fibers(m):
    f = Counter()
    for x in sources(m + 1):
        y = tuple(max(a, b) for a, b in zip(x, x[1:]))
        f[y] += 1
    return f


def runs_of_twos(y):
    runs = []
    run = 0
    for a in y:
        if a == 2:
            run += 1
        else:
            runs.append(run)
            run = 0
    runs.append(run)
    return runs


def formula(y):
    m = len(y)
    if all(a == 2 for a in y):
        return 3 * 2 ** (m // 2) if m % 2 == 0 else 2 ** ((m + 3) // 2)
    rs = runs_of_twos(y)
    if any(r % 2 for r in rs[1:-1]):
        return 0
    return 2 ** (1 + sum(r // 2 for r in rs))


def matrix(y):
    # Initial count at input symbol 0/1 is a=1 each, at symbol 2 b=1.
    a = b = 1
    for letter in y:
        if letter == 1:
            b = 0
        else:
            a, b = b, 2 * a
    return 2 * a + b


def poly_add(p, q, scale=1, shift=0):
    r = p.copy()
    for k, v in q.items():
        r[k + shift] += scale * v
        if not r[k + shift]:
            del r[k + shift]
    return r


def generating_polynomials(M):
    # [z^m] z(1+z)^2 / ((1-u z^2)(1-z-u z^2))
    p = [Counter() for _ in range(M + 1)]
    numerator = {1: 1, 2: 2, 3: 1}
    for m in range(M + 1):
        v = Counter({0: numerator[m]}) if m in numerator else Counter()
        if m >= 1:
            v = poly_add(v, p[m - 1])
        if m >= 2:
            v = poly_add(v, p[m - 2], 2, 1)
        if m >= 3:
            v = poly_add(v, p[m - 3], -1, 1)
        if m >= 4:
            v = poly_add(v, p[m - 4], -1, 2)
        p[m] = v
        assert all(c >= 0 for c in v.values()), (m, v)
    return p


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def run_tests():
    polys = generating_polynomials(100)
    count_inputs = 0
    count_outputs = 0
    for m in range(1, 15):
        fiber = direct_fibers(m)
        count_inputs += 3 * (2 ** m)
        count_outputs += len(fiber)
        assert len(fiber) == fibonacci(m + 3) - 1
        for y in product((1, 2), repeat=m):
            observed = fiber[y]
            assert observed == formula(y) == matrix(y), (m, y, observed, formula(y), matrix(y))
        expected_hist = Counter()
        for t, count in polys[m].items():
            expected_hist[2 ** (t + 1)] += count
        max_all_two = formula((2,) * m)
        expected_hist[max_all_two] += 1
        assert Counter(fiber.values()) == expected_hist, (m, Counter(fiber.values()), expected_hist)
        assert max(fiber.values()) == max_all_two
        assert {y for y,v in fiber.items() if v==max_all_two} == {(2,)*m}
        assert min(fiber.values()) == 2
        assert sum(v==2 for v in fiber.values()) == (1 if m==1 else 3 if m==2 else 4)
    for m in range(1,101):
        p = polys[m]
        assert sum(p.values()) + 1 == fibonacci(m+3)-1
        alltwo = formula((2,) * m)
        assert 2*sum((2 ** k)*n for k,n in p.items()) + alltwo == 3*(2**m)
    print('PASS: every source of length 2..15 enumerated,', count_inputs, 'sources total')
    print('PASS: all 2-letter outputs of lengths 1..14 checked against an independent matrix recurrence')
    print('PASS: full fiber multiplicity polynomials from rational generating function, lengths 1..100')
    print('PASS: exact image sizes, source mass, min and unique max, lengths 1..100')
    for m in [1,2,3,4,5,6,7,8,10,12,14]:
        print('m=%d outputs=%d min=%d max=%d' % (m, fibonacci(m+3)-1, 2, formula((2,)*m)))

if __name__ == '__main__':
    run_tests()
