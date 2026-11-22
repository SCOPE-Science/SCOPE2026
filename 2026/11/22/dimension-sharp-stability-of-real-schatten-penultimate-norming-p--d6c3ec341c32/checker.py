"""Standalone finite diagnostics for near-conformal real matrix two-planes.

Uses only Python's standard library. Finite samples do not replace the proof.
"""
import math


def check_case(n, t):
    assert n >= 4 and n % 2 == 0 and 0 < t < 0.5
    m = n // 2
    p = 1.0 + t / (m - 1)
    q = 1.0 - t
    epsilon = t / (m - 1)
    exact_peak = 1.0 + epsilon
    # On each 2-by-2 skew block of aI+bB, the two singular values
    # coincide and equal sqrt(a*a + b*b * block_weight*block_weight).
    for j in range(1025):
        theta = math.pi * j / 1024
        a, b = math.cos(theta), math.sin(theta)
        s_plus = math.hypot(a, b*p)
        s_minus = math.hypot(a, b*q)
        observed = m * s_plus / ((m - 1)*s_plus + s_minus)
        assert 1.0 - 1e-12 <= observed <= exact_peak + 1e-12
    at_pure_skew = m*p/((m-1)*p+q)
    assert math.isclose(at_pure_skew, exact_peak, rel_tol=1e-12)

    # Frobenius normalization of B and its exact extreme singular levels.
    alpha = 1/math.sqrt(1+t*t/(m-1))
    s_plus, s_minus = alpha*p, alpha*q
    witness_lower = (s_plus-s_minus)/2
    formula_lower = n*epsilon*alpha/4
    assert math.isclose(witness_lower, formula_lower, abs_tol=1e-12)

    # A=I, B=alpha*B_t is a Hilbert--Schmidt orthogonal normalized basis.
    # Its explicit conformal correction is U=I, J=diag(R,...,R).
    nearest_explicit_distance = max(abs(s_plus-1), abs(s_minus-1))
    if epsilon <= 1/(100*n):
        assert nearest_explicit_distance <= 33*n*epsilon + 1e-12
    return 1


def main():
    cases = 0
    for n in (4, 6, 8, 10, 12, 14, 16):
        for t in (1e-7, 1e-5, 1e-4, 5e-4, 1e-3, 1e-2):
            cases += check_case(n, t)
    assert cases == 42
    print('NEAR_CONFORMAL_TWO_PLANE_DIAGNOSTIC_OK', cases)


if __name__ == '__main__':
    main()
