"""Direct finite checks for corank-one contraction centralizers.

Run with Python 3; no external packages are needed.
"""
from collections import Counter
from itertools import product
from math import comb


def full_contractions(n):
    for increments in product((0, 1), repeat=n - 1):
        top = sum(increments)
        for initial in range(1, n - top + 1):
            values = [initial]
            for step in increments:
                values.append(values[-1] + step)
            yield tuple(values)


def compose(first, second):
    return tuple(first[value - 1] for value in second)


def special(n, i):
    return tuple(j if j <= i else j - 1 for j in range(1, n + 1))


def coefficients(n, i):
    result = Counter()
    if i >= 2:
        for h in range(i - 1):
            result[h + 1] += (i - 1) * comb(i - 2, h)
    for h in range(i):
        for j in range(n - i + 1):
            result[h + j + 1] += comb(i - 1, h)
    return result


def expected_difference(n, i):
    # Coefficient of P_{n,i+1}-P_{n,i} by an independent convolution.
    d = Counter()
    if i == 1:
        for r in range(1, n):
            d[r] = 1
    else:
        factors = Counter({0: 1, 1: i})
        for j in range(1, n - i):
            factors[j] += 1
            factors[j + 1] += 1
        for h in range(i - 1):
            for j, count in factors.items():
                d[1 + h + j] += comb(i - 2, h) * count
    return d


for n in range(2, 11):
    universe = list(full_contractions(n))
    assert len(universe) == (n + 1) * (2 ** (n - 2))
    for i in range(1, n):
        alpha = special(n, i)
        observed = Counter()
        for f in universe:
            if compose(f, alpha) == compose(alpha, f):
                observed[len(set(f))] += 1
        predicted = coefficients(n, i)
        assert observed == predicted, (n, i, observed, predicted)
        assert 2 * sum(observed.values()) == (2*n - i + 1) * 2 ** (i - 1), (n, i)
        reflection = tuple(n + 1 - alpha[n - j] for j in range(1, n + 1))
        reflected_count = Counter(len(set(f)) for f in universe if compose(f, reflection) == compose(reflection, f))
        assert reflected_count == predicted, (n, i, reflected_count, predicted)
    for i in range(1, n - 1):
        delta = coefficients(n, i + 1)
        delta.subtract(coefficients(n, i))
        delta = +delta
        assert delta == expected_difference(n, i), (n, i, delta, expected_difference(n, i))
        assert all(delta[r] > 0 for r in range(1, n))
        assert delta[n] == 0
    print(f'n={n}: verified {n-1} centralizer rank polynomials and reflected counterparts')
print('ALL_CORANK_COMMUTANT_TESTS_PASSED')
