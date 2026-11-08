"""Independent exhaustive orbit check for the sunlet binary reversible wave."""
from collections import Counter


def step(state, n):
    mask = (1 << n) - 1
    u = state & ((1 << (2*n))-1)
    v = state >> (2*n)
    core, leaf = u & mask, u >> n
    left = ((core << 1) | (core >> (n-1))) & mask
    right = ((core >> 1) | (core << (n-1))) & mask
    nxt = ((left ^ right ^ leaf) | (core << n)) ^ v
    return nxt | (u << (2*n))


def counts(n):
    result = Counter()
    full = 1 << (4*n)
    for state in range(full):
        value = step(state, n)
        period = 1
        while value != state:
            value = step(value, n)
            period += 1
            if period > 3*n:
                raise AssertionError('period exceeds expected upper bound')
        result[period] += 1
    return dict(sorted(result.items()))


def expected(n):
    values = {1:1}
    prev = 1
    for j in range(0,n.bit_length()):
        period = 3 * (1 << j)
        population = (1 << (4*(1 << j)))
        values[period] = population-prev
        prev = population
    return values


if __name__ == '__main__':
    n = 4
    observed = counts(n)
    predicted = expected(n)
    assert observed == predicted, (observed, predicted)
    print('n=4, field=GF(2), states=65536')
    print('exact observed primitive-period populations:', observed)
    print('expected primitive-period populations:', predicted)
    print('PASS: exhaustive direct orbit enumeration')
