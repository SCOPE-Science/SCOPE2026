#!/usr/bin/env python3
"""Independent finite checks for idempotent endomorphisms of even cycles."""
from itertools import product
from math import log, pi, sqrt, exp, comb


def from_path_walks(n):
    """Rank census by distinct fixed arcs and complementary path walks."""
    assert n >= 4 and n % 2 == 0
    result = [0] * (n + 1)
    result[n] = 1
    for k in range(2, n // 2 + 2):
        length = n - k + 1
        state = [0] * k
        state[0] = 1
        for _ in range(length):
            nxt = [0] * k
            for i, multiplicity in enumerate(state):
                if i:
                    nxt[i - 1] += multiplicity
                if i + 1 < k:
                    nxt[i + 1] += multiplicity
            state = nxt
        result[k] = n * state[-1]
    return result


def direct_enumeration(n):
    """Enumerate actual homomorphisms as closed +/-1 walks, then square maps."""
    result = [0] * (n + 1)
    for initial in range(n):
        for steps in product((-1, 1), repeat=n):
            if sum(steps) % n:
                continue
            mapping = [initial]
            point = initial
            for step in steps[:-1]:
                point = (point + step) % n
                mapping.append(point)
            if all(mapping[mapping[i]] == mapping[i] for i in range(n)):
                result[len(set(mapping))] += 1
    return result


def main():
    totals = []
    for n in range(4, 15, 2):
        actual = direct_enumeration(n)
        predicted = from_path_walks(n)
        assert actual == predicted, (n, actual, predicted)
        totals.append((n, sum(actual)))
        # The full endomorphism count is independently parameterized by
        # closed +/-1 step words, which have 2+binomial(n,n/2) choices.
        assert n * (2 + comb(n, n // 2)) >= sum(actual)
    assert totals == [(4, 9), (6, 25), (8, 73), (10, 221),
                      (12, 685), (14, 2157)]

    # Compare the exact integer recurrence with the analytic leading scale.
    a = log(2)
    s = (pi * pi / a) ** (1 / 3)
    c = 1.5 * a * s
    B = 16 * sqrt(2 * pi * a * s / 3)
    ratios = []
    for n in (64, 128, 256):
        spectrum = from_path_walks(n)
        exact = sum(spectrum)
        log_scale = log(B) + n * a + log(n) / 6 - c * n ** (1 / 3)
        ratio = exp(log(exact) - log_scale)
        assert 1.0 < ratio < 1.8, (n, ratio)
        ratios.append((n, round(ratio, 4)))
    print('DIRECT_IDEMPOTENTS_OK', totals)
    print('SADDLE_SANITY_OK', ratios)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
