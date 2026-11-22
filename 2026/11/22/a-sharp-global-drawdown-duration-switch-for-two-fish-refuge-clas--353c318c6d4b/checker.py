#!/usr/bin/env python3
"""Reproduce numerical consistency checks for an exponential-latency two-class drawdown model.

Only Python's standard library is required. Finite checks supplement, not replace,
the exact proof in RESULT.md.
"""
import math
import random
from fractions import Fraction


def survival(T, lam, mu, c_fast, c_slow, weight):
    """A randomly selected individual's exact survival chance in the stated model."""
    def latency_cdf(t):
        return -math.expm1(-lam * t) if t > 0 else 0.0
    return math.exp(-mu * T) * (
        weight * latency_cdf(T - c_fast)
        + (1 - weight) * latency_cdf(T - c_slow)
    )


def predicted_argmax(lam, mu, c_fast, c_slow, weight):
    rho = mu / lam
    delay = lam * (c_slow - c_fast)
    K = 1.0 + 1.0 / rho
    threshold = math.log((weight ** (-1.0 / rho) - weight) / (1 - weight))
    early = c_fast + math.log(K) / lam
    late = c_fast + math.log(K * (weight + (1 - weight) * math.exp(delay))) / lam
    if delay < threshold - 1e-10:
        return [late]
    if delay > threshold + 1e-10:
        return [early]
    return [early, late]


def main():
    rng = random.Random(440023)
    trials = 5000
    for _ in range(trials):
        lam = rng.uniform(0.35, 2.0)
        rho = rng.uniform(0.3, 3.5)
        mu = rho * lam
        c_fast = rng.uniform(0.02, 2.0)
        delay = rng.uniform(0.04, 4.0)
        c_slow = c_fast + delay / lam
        weight = rng.uniform(0.02, 0.98)
        peaks = predicted_argmax(lam, mu, c_fast, c_slow, weight)
        peak_value = max(survival(t, lam, mu, c_fast, c_slow, weight) for t in peaks)
        # Include exact breakpoints and one unbounded-tail buffer on the grid.
        stop = max(c_slow + 15 / min(lam,mu), max(peaks) + 4 / lam)
        for i in range(301):
            t = stop * i / 300
            assert survival(t, lam, mu, c_fast, c_slow, weight) <= peak_value + 2e-12
        assert survival(c_slow, lam, mu, c_fast, c_slow, weight) <= peak_value + 2e-12

    # Exact two equal maxima with strictly positive mandatory refuge times:
    # lambda = mu = 1, c_fast=ln 2, c_slow=ln 8, w=1/3.
    # At T=ln 4: (1/3)*(1/4)*(1-2/4)=1/24.
    early_value = Fraction(1, 3) * Fraction(1, 4) * (1 - Fraction(2, 4))
    # At T=ln 12: (1/3)*(1/12)*(1-2/12) + (2/3)*(1/12)*(1-8/12)=1/24.
    late_value = (Fraction(1, 3) * Fraction(1, 12) * (1 - Fraction(2, 12))
                  + Fraction(2, 3) * Fraction(1, 12) * (1 - Fraction(8, 12)))
    valley_value = Fraction(1, 3) * Fraction(1, 8) * (1 - Fraction(2, 8))
    assert early_value == late_value == Fraction(1, 24)
    assert valley_value == Fraction(1, 32) < early_value
    # At the critical delay, the peak-to-peak gap is exactly -log(w)/mu.
    for rho in (0.25, 0.5, 1., 2., 4.):
        for w in (0.1, 0.25, 0.6, 0.9):
            E = (w**(-1/rho) - w) / (1-w)
            d = math.log(E)
            C = w + (1-w)*E
            first = math.log1p(1/rho)
            second = math.log((1+1/rho)*C)
            assert second > d > first
            assert abs((second - first) + math.log(w)/rho) < 2e-12
            assert abs(w * C**rho - 1) < 2e-12
    print("PASS: 5000 randomized cases, 1,505,000 grid evaluations and 5,000 join checks, exact rational two-peak certificate, 20 critical-delay identities")


if __name__ == "__main__":
    main()
