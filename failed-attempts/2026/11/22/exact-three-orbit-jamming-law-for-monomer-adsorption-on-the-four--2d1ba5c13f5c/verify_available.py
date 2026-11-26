"""Exact jamming-law verification using residual available-vertex masks."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache

DIM = 4
N = 1 << DIM
FULL = (1 << N) - 1
CLOSED = tuple((1 << v) | sum(1 << (v ^ (1 << j)) for j in range(DIM))
               for v in range(N))

@lru_cache(maxsize=None)
def distribution(available):
    """Coefficient k is the exact chance of k further acceptances."""
    if not available:
        return (Fraction(1),)
    count = available.bit_count()
    result = [Fraction(0)] * (count + 1)
    for v in range(N):
        if available & (1 << v):
            for k, prob in enumerate(distribution(available & ~CLOSED[v])):
                result[k + 1] += prob / count
    while result[-1] == 0:
        result.pop()
    assert sum(result) == 1
    return tuple(result)


def conditional(prefix):
    remaining = FULL
    for v in prefix:
        assert remaining & (1 << v)
        remaining &= ~CLOSED[v]
    return {k + len(prefix): p for k, p in enumerate(distribution(remaining)) if p}


if __name__ == '__main__':
    expected = {4: Fraction(1, 6), 5: Fraction(64, 165), 8: Fraction(49, 110)}
    law = {k: p for k, p in enumerate(distribution(FULL)) if p}
    assert law == expected, (law, expected)
    assert conditional([0]) == expected
    assert conditional([0, 15]) == {8: Fraction(1)}
    assert conditional([0, 3]) == {4: Fraction(1, 12), 5: Fraction(4, 15), 8: Fraction(13, 20)}
    assert conditional([0, 7]) == {4: Fraction(1, 3), 5: Fraction(2, 3)}
    assert sum(k * p for k, p in law.items()) == Fraction(1018, 165)
    print('PASS exact available-mask probabilities', law)
    print('PASS rational conditional branches; cached masks', distribution.cache_info().currsize)
