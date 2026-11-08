"""Reproduce finite checks for the exact Bayesian belief-switching theorem.

The infinite orbit, equidistribution and irrationality assertions are proved in RESULT.md,
not inferred from these finite tests.
"""
from fractions import Fraction
from math import log, exp, floor

LOW = Fraction(3, 17)
HIGH = Fraction(13, 7)


def update(x, gamma):
    return x / (x + gamma * (1 - x))


def step(x):
    return update(x, LOW if x < Fraction(1, 2) else HIGH)


def logit(x):
    return log(float(x / (1 - x)))


def self_test():
    identities = 0
    orbit_checks = 0
    a = log(17 / 3)
    c = log(13 / 7)
    length = a + c
    alpha = a / length
    for num in range(1, 20):
        for den in range(num + 1, 24):
            x = Fraction(num, den)
            for gamma in (LOW, HIGH, Fraction(1, 2), Fraction(2, 1)):
                y = update(x, gamma)
                assert y / (1 - y) == (x / (1 - x)) / gamma
                identities += 1
    for x0 in (Fraction(1, 2), Fraction(1, 10), Fraction(9, 10), Fraction(7, 20), Fraction(17, 20), Fraction(6, 13)):
        x = x0
        for k in range(100):
            y = step(x)
            assert y > 0 and y < 1
            if x < Fraction(1, 2):
                assert y / (1 - y) == (x / (1 - x)) * Fraction(17, 3)
            else:
                assert y / (1 - y) == (x / (1 - x)) * Fraction(7, 13)
            x = y
            orbit_checks += 1
        assert Fraction(7, 20) <= x < Fraction(17, 20)
    for x0 in (Fraction(1, 2), Fraction(7, 20), Fraction(17, 20), Fraction(2, 5), Fraction(3, 4)):
        x = x0
        for k in range(500):
            if Fraction(7, 20) <= x < Fraction(17, 20):
                break
            x = step(x)
        assert Fraction(7, 20) <= x < Fraction(17, 20)
        # Compare exact-rational updating with the mechanical-word formula.
        phase = (logit(x) + c) / length
        assert -1e-12 <= phase < 1 + 1e-12
        n_high = 0
        for n in range(140):
            observed = int(x >= Fraction(1, 2))
            mechanical = floor(phase + (n + 1) * alpha) - floor(phase + n * alpha)
            assert observed == mechanical, (x0, n, observed, mechanical)
            n_high += observed
            assert abs(n_high - (n + 1) * alpha) < 1.0
            x = step(x)
            orbit_checks += 1
    # Exact periodic comparators: a/c=1 and 2 respectively.
    for low, high, period in ((Fraction(1, 2), Fraction(2, 1), 2),
                              (Fraction(1, 4), Fraction(2, 1), 3)):
        def step_special(x):
            return update(x, low if x < Fraction(1, 2) else high)
        x = Fraction(1, 2)
        for _ in range(period):
            x = step_special(x)
        assert x == Fraction(1, 2)
    mean = log(13 / 3) / log(Fraction(221, 21))
    above = a / length
    assert 0.6229 < mean < 0.6231
    assert 0.7369 < above < 0.7371
    print(f"VERIFY_OK odds_identities={identities} orbit_and_itinerary_checks={orbit_checks} "
          f"support=[7/20,17/20] above_half={above:.12f} belief_mean={mean:.12f}")


if __name__ == '__main__':
    self_test()
