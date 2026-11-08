"""Independent state-by-state dynamics; no matrices and no third-party packages."""
from itertools import product
from math import gcd


def v_p(m, p):
    count = 0
    while m % p == 0:
        m //= p
        count += 1
    return count


def dimension(n, k, p):
    g = gcd(n, k)
    if p == 2:
        correction = (n % 2 and k % 2)
    else:
        correction = (v_p(n, p) == v_p(k, p))*(1+(g % 2 == 0))
    return 2*g-int(correction)


def update(state, n, p):
    u, v = state[:n], state[n:]
    return tuple((u[(i-1) % n] + u[(i+1) % n] - v[i]) % p for i in range(n)) + u


def divisors(k):
    return [d for d in range(1, k+1) if k % d == 0]


total = 0
cases = 0
for p, lengths in ((2, range(3, 8)), (3, range(3, 6)), (5, (3,))):
    for n in lengths:
        order = n*(p if p != 2 or n % 2 else 1)
        ds = divisors(order)
        counts = {d: 0 for d in ds}
        for state in product(range(p), repeat=2*n):
            now = state
            for k in range(1, order+1):
                now = update(now, n, p)
                if k in counts and now == state:
                    counts[k] += 1
            assert now == state, ('order failure', p, n, state)
            total += 1
        for k in ds:
            assert counts[k] == p**dimension(n, k, p), (p, n, k, counts[k])
            cases += 1
print('PASS independent state enumeration: %d configurations, %d fixed-point totals' % (total, cases))
