"""Independent reproducibility checks for the structural-zero count-evidence theorem.

Uses exact rational arithmetic for the witness and deterministic numerical
checks for algebraic formulas. Numerical tests supplement, not replace, proof.
Run with: python checker.py
"""
from fractions import Fraction
import math
import random


def likelihoods(p_low, p_high, rate, structural_zero):
    ratio = p_high / p_low
    theta = rate * (p_high - p_low)
    a_low = math.exp(-rate * p_low)
    a_high = math.exp(-rate * p_high)
    z = structural_zero
    b0 = (z + (1 - z) * a_high) / (z + (1 - z) * a_low)
    b1 = ratio * math.exp(-theta)
    return b0, b1, ratio, theta


def critical_structural_mass(p_low, p_high, rate):
    r = p_high / p_low
    t = rate * (p_high - p_low)
    if t <= math.log(r):
        return None
    e = math.exp(-rate * p_high)
    return (r - 1) * e / (1 - r * math.exp(-t) + (r - 1) * e)


def exact_witness():
    p_l = Fraction(1, 4)
    p_h = Fraction(3, 4)
    eta = Fraction(3, 4)
    a_l = Fraction(1, 2)
    a_h = Fraction(1, 8)
    b0 = (eta + (1 - eta) * a_h) / (eta + (1 - eta) * a_l)
    b1 = (p_h / p_l) * a_h / a_l
    b2 = (p_h / p_l) * b1
    eta_c = ((p_h / p_l) - 1) * a_h / (1 - (p_h / p_l) * a_h / a_l + ((p_h / p_l) - 1) * a_h)
    assert (b0, b1, b2, eta_c) == (Fraction(25, 28), Fraction(3, 4), Fraction(9, 4), Fraction(1, 2))
    assert b1 < b0 < 1 < b2


def monte_carlo_parameter_checks():
    rng = random.Random(204108)
    checks = 0
    for _ in range(30000):
        p_l = rng.uniform(0.025, 0.8)
        p_h = rng.uniform(p_l + (1 - p_l) * 0.01, 0.995)
        lam = rng.uniform(0.1, 30)
        eta = rng.uniform(0, 0.995)
        b0, b1, r, theta = likelihoods(p_l, p_h, lam, eta)
        assert 0 < b0 < 1 + 1e-12
        assert b1 > 0 and r > 1
        assert abs(b1 * r - r * r * math.exp(-theta)) < 1e-12
        c = critical_structural_mass(p_l, p_h, lam)
        if c is None:
            assert b0 < b1 or math.isclose(b0,b1,abs_tol=1e-12,rel_tol=1e-12)
        else:
            assert 0 < c < 1
            # At the analytic critical mass the first step is level.
            c0,c1,_,_ = likelihoods(p_l,p_h,lam,c)
            assert math.isclose(c0,c1,abs_tol=1e-11,rel_tol=1e-10)
            if abs(eta-c) > 1e-8:
                assert (b0 > b1) == (eta > c)
        # Direct countercheck of the Poisson likelihood for positive counts.
        for k in (1, 2, 3, 5):
            n0 = (1-eta)*math.exp(-lam*p_l)*(lam*p_l)**k/math.factorial(k)
            n1 = (1-eta)*math.exp(-lam*p_h)*(lam*p_h)**k/math.factorial(k)
            assert math.isclose(n1/n0, b1*r**(k-1), rel_tol=1e-10)
            checks += 1
    return checks

if __name__ == '__main__':
    exact_witness()
    count = monte_carlo_parameter_checks()
    print('EXACT WITNESS PASSED; SUPPLEMENTARY POSITIVE-COUNT CHECKS', count)
