"""Independent exact short-length test of two-deletion entropy runner-up."""
from itertools import product, groupby
from math import comb

def embed(pattern, host):
    dp = [1] + [0] * len(pattern)
    for x in host:
        for i in range(len(pattern) - 1, -1, -1):
            if pattern[i] == x:
                dp[i + 1] += dp[i]
    return dp[-1]

def posterior_product(y):
    n = len(y)
    result = 1
    for x in product((0, 1), repeat=n + 2):
        e = embed(y, x)
        if e:
            result *= pow(e, e)
    return result

def expected(n):
    chosen = []
    for first in (0, 1):
        for left in range(n - 1):
            right = n - 2 - left
            if abs(left - right) <= 1:
                runs = (1,) * left + (2,) + (1,) * right
                word = []
                bit = first
                for r in runs:
                    word.extend([bit] * r)
                    bit ^= 1
                chosen.append(tuple(word))
    return set(chosen)

for n in range(2, 9):
    alt = {tuple(i % 2 for i in range(n)), tuple(1 - i % 2 for i in range(n))}
    winners = expected(n)
    # Two smallest distinct correction products correspond to largest entropy levels.
    products = [(posterior_product(y), y) for y in product((0, 1), repeat=n)]
    levels = sorted(set(v for v, _ in products))
    assert len(levels) >= 2
    assert {y for v, y in products if v == levels[0]} == alt
    assert {y for v, y in products if v == levels[1]} == winners
    print('n=', n, 'runner_up_words=', len(winners), 'exact_fiber_test=PASS', flush=True)
print('DIRECT_EXACT_PASS')
