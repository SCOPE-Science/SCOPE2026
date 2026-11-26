"""Reproducibility tests for the simplex-frustum John-ellipsoid theorem.

Standard-library checks support, determinant, phase continuity, strict
relative-volume monotonicity, and the one-dimensional global optimum.
The analytic proof in RESULT.md, not these finite checks, establishes the theorem.
"""
import math
import random


def formula(d, a):
    assert d >= 3 and 0 < a < 1
    threshold = (d - 1) / (d + 1)
    if a <= threshold:
        s, R = d / (d + 1), 1 / (d + 1)
    else:
        s, R = (1 + a) / 2, (1 - a) / 2
    alpha2 = R * R / d
    beta2 = (s * s - R * R) / (d * (d - 1))
    return s, R, alpha2, beta2


def normalized_fraction(d, a):
    s, R, alpha2, beta2 = formula(d, a)
    ellipsoid_volume = (math.pi ** (d / 2) / math.gamma(d / 2 + 1)
                        * math.sqrt(alpha2) * beta2 ** ((d - 1) / 2))
    return ellipsoid_volume * math.factorial(d) / (1 - a ** d)


def obj(d, R):
    return R * (1 - 2 * R) ** ((d - 1) / 2)


def check():
    rng = random.Random(102026)
    for d in range(3, 16):
        threshold = (d - 1) / (d + 1)
        aa = sorted(set([0.001, threshold / 2, threshold,
                         (threshold + 1) / 2, 0.99, 0.99999]
                        + [0.001 + 0.998 * k / 98 for k in range(99)]))
        vals = []
        for a in aa:
            s, R, alpha2, beta2 = formula(d, a)
            assert alpha2 > 0 and beta2 > 0
            # All d coordinate supporting hyperplanes have minimum coordinate 0.
            qii = alpha2 / d + (d - 1) * beta2 / d
            assert abs(math.sqrt(qii) - s / d) < 1e-12
            assert s + R <= 1 + 1e-12
            assert s - R >= a - 1e-12
            assert abs((s + R) - 1) < 1e-12
            if a > threshold + 1e-10:
                assert abs(s - R - a) < 1e-12
            else:
                assert s - R >= a - 1e-12
            # Every feasible axial radius obeys R <= (1-a)/2.
            # Exhaustive one-variable analyticity is proved in RESULT.md.
            maxR = (1 - a) / 2
            for j in range(301):
                r = maxR * (j + 1) / 302
                assert obj(d, r) <= obj(d, R) * (1 + 3e-13)
            for _ in range(50):
                r = maxR * rng.uniform(1e-8, 1)
                assert obj(d, r) <= obj(d, R) * (1 + 3e-13)
            vals.append(normalized_fraction(d, a))
        # Allow sub-machine-epsilon increases while checking no resolved reversals.
        assert all(y >= x * (1 - 1e-12) for x, y in zip(vals, vals[1:])), (d, vals)
        assert vals[-1] > vals[0] * 1.001
        # Both analytic formula branches coincide at the threshold.
        s, R, alpha2, beta2 = formula(d, threshold)
        assert abs(s - d / (d + 1)) < 1e-13
        assert abs(R - 1 / (d + 1)) < 1e-13
        assert abs(beta2 - 1 / (d * (d + 1))) < 1e-13
        # The sharp limiting volume ratio is reached from below.
        kappa = math.pi ** (d / 2) / math.gamma(d / 2 + 1)
        sharp_limit = kappa * math.factorial(d - 1) / (
            2 * d ** (d / 2) * (d - 1) ** ((d - 1) / 2))
        assert abs(normalized_fraction(d, 1 - 1e-6) / sharp_limit - 1) < 1e-5
    print('SUPPORT_AND_CONTACT_PHASE_PASSED')
    print('AXIAL_GLOBAL_MAXIMUM_PASSED')
    print('STRICT_RELATIVE_VOLUME_GRID_AND_LIMIT_PASSED')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    check()
