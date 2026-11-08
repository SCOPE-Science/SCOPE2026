#!/usr/bin/env python3
"""Reproduce parity-support and exact finite-length checks using Python stdlib."""
from math import log2


def binom_odd(top, bottom):
    return 0 <= bottom <= top and (bottom & top) == bottom


def direct_binomial_sum(n, kind):
    value = 0
    for k in range(n + 1):
        top = n + 5 * k
        bottom = 2 * n + 2 * k if kind == 'U' else 2 * k
        if binom_odd(n, k) and binom_odd(top, bottom):
            value += 1
    return value


def binary_allowed(n, kind):
    allowed = {0, 1, 2, 3} if kind == 'U' else {0, 3}
    return all(len(run) % 5 in allowed for run in bin(n)[2:].split('0') if run)


def count_by_recurrence(kind, last):
    jumps = (1, 2, 3, 4, 5) if kind == 'U' else (1, 4, 5)
    numerator = (1, 1, 1, 1) if kind == 'U' else (1, 0, 0, 1)
    result = []
    for m in range(last + 1):
        result.append((numerator[m] if m < len(numerator) else 0)
                      + sum(result[m - j] for j in jumps if m - j >= 0))
    return result


def seed_mod2(kind):
    values = [1, 1, 1, 1] if kind == 'U' else [1, 2, 2, 3]
    for _ in range(60):
        values.append(values[-1] + values[-2] - values[-3] + values[-4])
    return [v & 1 for v in values]


def root_and_constant(kind):
    jumps = (1, 2, 3, 4, 5) if kind == 'U' else (1, 4, 5)
    ncoeff = (1, 1, 1, 1) if kind == 'U' else (1, 0, 0, 1)
    def d(z):
        return 1 - sum(z ** j for j in jumps)
    left, right = 0.5, 1.0
    for _ in range(90):
        mid = (left + right) / 2
        if d(mid) > 0:
            left = mid
        else:
            right = mid
    rho = (left + right) / 2
    nval = sum(c * rho ** j for j, c in enumerate(ncoeff))
    derivative = -sum(j * rho ** (j-1) for j in jumps)
    return 1 / rho, -nval / (rho * derivative)


def main():
    for kind, pattern in [('U', [1, 1, 1, 1, 0]),
                          ('V', [1, 0, 0, 1, 0])]:
        parities = seed_mod2(kind)
        assert all(parities[j] == pattern[j % 5]
                   for j in range(len(parities)))
        for n in range(1024):
            assert (direct_binomial_sum(n, kind) & 1) == binary_allowed(n, kind), (kind, n)
        sequence = count_by_recurrence(kind, 24)
        for m in range(15):
            brute = sum(binary_allowed(n, kind) for n in range(1 << m))
            assert brute == sequence[m], (kind, m, brute, sequence[m])
        root, constant = root_and_constant(kind)
        delta = log2(root)
        ratio = sequence[24] / (constant * root ** 24)
        assert abs(ratio - 1) < 0.02
        print('{}: 1024 direct sum parity checks; 15 exhaustive dyadic counts; period 5 confirmed'.format(kind))
        print('{} first 16 dyadic counts: {}'.format(kind, sequence[:16]))
        print('{} lambda {:.12f}; delta {:.12f}; C {:.12f}; a24/(C*lambda^24) {:.9f}'.format(kind, root, delta, constant, ratio))
    assert all(not binary_allowed(n, 'V') or binary_allowed(n, 'U') for n in range(1 << 15))
    assert binary_allowed(1, 'U') and not binary_allowed(1, 'V')
    print('Strict support inclusion: checked for all n < 32768; witness n=1')
    print('CHECKER_OK')


if __name__ == '__main__':
    main()
