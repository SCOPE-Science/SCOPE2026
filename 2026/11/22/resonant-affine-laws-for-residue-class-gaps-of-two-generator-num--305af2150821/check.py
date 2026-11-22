"""Separate-method finite tests of the binary-semigroup residue transfer theorem.

All tests compare the claimed integer identities against direct Boolean
coin-representability, not against the Fourier proof or an Apéry formula.
"""
from math import gcd


def gap_counts(a, b, m):
    assert a > 1 and b > 1 and gcd(a, b) == 1 and m >= 2
    stop = a * b - a - b
    can = [False] * (stop + 1)
    can[0] = True
    for n in range(1, stop + 1):
        can[n] = (n >= a and can[n - a]) or (n >= b and can[n - b])
    result = [0] * m
    for n in range(1, stop + 1):
        if not can[n]:
            result[n % m] += 1
    assert sum(result) == (a - 1) * (b - 1) // 2
    return result


def shifted_addition(v, delta):
    return [x + y for x, y in zip(v, delta)]


def verify():
    transfer_a = transfer_b = bounds = special = 0
    for m in range(2, 15):
        for a in range(2, 30):
            for b in range(2, 30):
                if gcd(a, b) != 1:
                    continue
                old = gap_counts(a, b, m)
                d, e = gcd(a, m), gcd(b, m)
                baseline = ((d - 1) * b + (e - 1) * a) / m
                discrepancy = max(old) - min(old)
                assert abs(discrepancy - baseline) <= m / 2 + m * m / 4 + 1e-12
                bounds += 1
                if gcd(a + m, b) == 1:
                    shifted = gap_counts(a + m, b, m)
                    predicted = [(b - e) // 2 + ((r * pow(a, -1, e)) % e)
                                 for r in range(m)]
                    assert shifted == shifted_addition(old, predicted), (a, b, m)
                    transfer_a += 1
                if gcd(a, b + m) == 1:
                    shifted = gap_counts(a, b + m, m)
                    predicted = [(a - d) // 2 + ((r * pow(b, -1, d)) % d)
                                 for r in range(m)]
                    assert shifted == shifted_addition(old, predicted), (a, b, m)
                    transfer_b += 1
                if a % m == 0 and b % m == 1:
                    predicted = [((a - m + 2 * r) * (b - 1)) // (2 * m)
                                 for r in range(m)]
                    assert old == predicted, (a, b, m)
                    special += 1
    print('PASS', 'discrepancy_cases', bounds,
          'a_shift_cases', transfer_a, 'b_shift_cases', transfer_b,
          'arithmetic_histogram_cases', special)


if __name__ == '__main__':
    verify()
