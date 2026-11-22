"""Finite checks for independent-digit multiplier return identities.

Run with python3 check.py. All infinite-dimensional claims have analytic proofs.
"""
import cmath
import math


def phase_moment(base, positions, probabilities, n):
    z = 1 + 0j
    for s, p in zip(positions, probabilities):
        z *= 1 - p + p * cmath.exp(2j * math.pi * ((n % (base ** s)) / (base ** s)))
    return z


def squared_return_from_moment(z):
    return 2 - 2 * z.real


def analytic_variance_bound(base, gap_bound, p):
    return 4 * p * (1 - p) * math.sin(math.pi / (2 * base ** gap_bound)) ** 2


def main():
    count = 0
    base = 3
    for k in (1, 2, 3, 5, 7):
        n = base ** k
        for cap in (k + 5, k + 10, k + 20):
            positions = list(range(1, cap + 1))
            probabilities = [1 / (j + 1) for j in positions]
            moment = phase_moment(base, positions, probabilities, n)
            assert -1e-12 <= squared_return_from_moment(moment) <= 4 + 1e-12
            assert squared_return_from_moment(moment) < 1.5
            count += 2
    for n in range(2, 400):
        j = math.ceil(math.log(2 * n, base))
        while base**j < 2 * n:
            j += 1
        assert 1 / (2 * base) < n / base**j <= .5
        phase = abs(cmath.exp(2j * math.pi * n / base**j) - 1)
        assert phase + 1e-12 >= 2 * math.sin(math.pi / (2 * base))
        count += 2
    constant = 4 * sum(math.sin(math.pi / base**h)**2 for h in range(1, 45))
    for k in (100, 500, 3000, 15000):
        moment = 1 + 0j
        for h in range(1, 55):
            moment *= 1 + (cmath.exp(2j * math.pi / base**h) - 1)/(k + h + 1)
        scaled = k * squared_return_from_moment(moment)
        assert abs(scaled - constant) < 7 / math.sqrt(k)
        count += 1
    print('CANTOR_BERNOULLI_FINITE_CHECK_OK', count)


if __name__ == '__main__':
    main()
