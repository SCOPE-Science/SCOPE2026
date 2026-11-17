"""Finite numerical tests for a diagonal sampled-resolvent phase law.

The proof of its limit statements is analytic; this script tests finite
matrices and predicted asymptotic constants, not infinite-dimensional claims.
Requires NumPy. Run: python check_phase.py
"""
import math
import numpy as np


def scaled_error(base, exponent, ratio, level, laplace=1.3, window=25):
    """Maximize the exact diagonal error on indices level +/- window."""
    mesh = ratio * base**(-level)
    indices = np.arange(max(0, level - window), level + window + 1)
    frequencies = 2.0 * math.pi * np.float64(base) ** indices
    p = laplace + frequencies**exponent + 1j * frequencies
    z = mesh * p
    symbol = mesh / (-np.expm1(-z)) - 0.5 * mesh - 1.0 / p
    abs_symbol = np.abs(symbol)
    return float(np.max(abs_symbol) / mesh**exponent), int(indices[np.argmax(abs_symbol)])


def limiting_height(exponent, numerator):
    return (2.0 * math.pi * numerator)**(-exponent)


def lorentzian_width(base, exponent, ratio, depth):
    return ratio * (2.0 * math.pi)**(exponent - 1.0) * base**((exponent - 1.0) * depth)


def main():
    checked = 0
    cases = [(2, 0.5, 40), (3, 0.6, 28), (4, 0.7, 22)]
    for base, exponent, level in cases:
        for depth, numerator, ratio in [(0, 1, 1.0), (1, base + 1, 1.0 + 1.0 / base)]:
            measured, index = scaled_error(base, exponent, ratio, level)
            predicted = limiting_height(exponent, numerator)
            assert abs(measured - predicted) < 3e-5, (base, ratio, measured, predicted)
            assert index == level + depth, (base, depth, index)
            checked += 2
            width = lorentzian_width(base, exponent, ratio, depth)
            small = base**(-(1.0 - exponent) * level)
            for offset in (-2.0, -0.5, 0.0, 0.5, 2.0):
                measured, index = scaled_error(base, exponent, ratio + offset * small, level)
                predicted = limiting_height(exponent, numerator) / math.hypot(1.0, offset / width)
                assert abs(measured - predicted) < 3e-5, (base, offset, measured, predicted)
                assert index == level + depth, (base, offset, index)
                checked += 2
        for ratio in (math.sqrt(2.0),):
            measured, index = scaled_error(base, exponent, ratio, level)
            assert measured < 0.002, (base, measured, index)
            checked += 1
    # A rational with denominator not dividing a power of the radix.
    # For base three, 3/2 never resonates; for base two, 4/3 never resonates.
    for base, exponent, level, ratio in ((2, 0.5, 40, 4.0/3.0), (3, 0.6, 28, 1.5)):
        measured, _ = scaled_error(base, exponent, ratio, level)
        assert measured < 0.002, (base, ratio, measured)
        checked += 1
    # Composite-base denominator test: 3/2 resonates already for base four.
    measured, index = scaled_error(4, 0.7, 1.5, 22)
    assert abs(measured - limiting_height(0.7, 6)) < 3e-5 and index == 23
    checked += 1
    print(f"Passed {checked} finite diagonal-symbol assertions (3 radices, 3 exponents).")


if __name__ == "__main__":
    main()
