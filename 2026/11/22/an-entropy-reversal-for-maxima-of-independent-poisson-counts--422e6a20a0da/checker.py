"""Reproduce finite-intensity entropy differences and Gaussian-limit constants.

Only Python's standard library is required. Numerical experiments illustrate the
proved formulas, and are not substitutes for the asymptotic arguments.
"""
import math


def poisson_probabilities(rate):
    if rate <= 0:
        raise ValueError('rate must be positive')
    nmax = int(rate + 20.0 * math.sqrt(rate) + 80)
    mode = int(rate)
    p = [0.0] * (nmax + 1)
    p[mode] = math.exp(-rate + mode * math.log(rate) - math.lgamma(mode + 1.0))
    for k in range(mode, 0, -1):
        p[k - 1] = p[k] * k / rate
    for k in range(mode + 1, nmax + 1):
        p[k] = p[k - 1] * rate / k
    return p


def entropy_difference(rate, sample_size):
    if sample_size < 2 or int(sample_size) != sample_size:
        raise ValueError('sample_size must be an integer at least two')
    p = poisson_probabilities(rate)
    f = 0.0
    parent_h = 0.0
    maximum_h = 0.0
    maxmass_sum = 0.0
    for pk in p:
        nxt = f + pk
        # A factorized sum avoids subtraction of almost-equal CDF powers.
        multiplier = sum(nxt ** (sample_size - 1 - j) * f ** j
                         for j in range(sample_size))
        maximum_mass = pk * multiplier
        if pk > 0.0:
            parent_h -= pk * math.log(pk)
        if maximum_mass > 0.0:
            maximum_h -= maximum_mass * math.log(maximum_mass)
        maxmass_sum += maximum_mass
        f = nxt
    if abs(f - 1.0) > 2e-11 or abs(maxmass_sum - 1.0) > 2e-11:
        raise ArithmeticError('truncation did not capture probability one')
    return maximum_h - parent_h


def normal_max_second_moment(sample_size, intervals=40000):
    assert intervals % 2 == 0
    low, high = -12.0, 12.0
    delta = (high - low) / intervals
    def integrand(x):
        phi = math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)
        Phi = 0.5 * math.erfc(-x / math.sqrt(2.0))
        return sample_size * x * x * phi * Phi ** (sample_size - 1)
    v = integrand(low) + integrand(high)
    for i in range(1, intervals):
        v += (4 if i % 2 else 2) * integrand(low + i * delta)
    return v * delta / 3.0


def gaussian_entropy_limit(sample_size):
    second = normal_max_second_moment(sample_size)
    return 0.5 * (second - 1.0) + (sample_size - 1.0) / sample_size - math.log(sample_size)


def small_rate_prediction(rate, sample_size):
    return ((sample_size - 1) * math.log(1.0 / rate)
            + (sample_size - 1) - sample_size * math.log(sample_size)) * rate


def main():
    for m in (2, 3, 5, 10):
        small = entropy_difference(1e-4, m)
        prediction = small_rate_prediction(1e-4, m)
        large = entropy_difference(200.0, m)
        limit = gaussian_entropy_limit(m)
        print('sample_size=%d, small=%.12g, prediction=%.12g, large=%.12g, limit=%.12g'
              % (m, small, prediction, large, limit))
        assert small > 0 and large < 0
        assert abs(small - prediction) <= 1.0e-5
        assert abs(large - limit) < 0.07
    assert abs(gaussian_entropy_limit(2) - (0.5 - math.log(2.0))) < 5e-12
    print('All finite numerical consistency checks passed.')


if __name__ == '__main__':
    main()
