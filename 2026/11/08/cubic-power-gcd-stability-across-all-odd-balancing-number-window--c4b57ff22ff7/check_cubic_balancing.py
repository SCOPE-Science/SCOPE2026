"""Reproducible finite tests for an exact cubic balancing-number gcd theorem.

The finite tests corroborate, but do not constitute, its infinite proof.
"""
from math import gcd


def balancing(n):
    v = [0, 1]
    while len(v) <= n:
        v.append(6 * v[-1] - v[-2])
    return v


def check(max_m=70, max_n=12):
    b = balancing(2 * max_m + max_n + 8)
    d31, d32 = 1, 199
    direct_cases = 0
    for m in range(1, max_m + 1):
        g = b[m] + b[m - 1]
        A = 4 * g * g + 3
        assert (g * g - 1) % 8 == 0
        H = 3 * (g * g - 1) // 8
        assert 7 * d31 == g * (4 * g * g + 3)
        assert gcd(A + H, 6 * (36 * A + H)) == 7
        k = 2 * m - 1
        value_gcd = 0
        for n in range(max_n + 1):
            s = n + m
            exact_sum = sum(b[n + j] ** 3 for j in range(1, k + 1))
            derived_sum_7 = g * b[s] * (A * b[s] ** 2 + H)
            assert derived_sum_7 % 7 == 0
            assert 7 * exact_sum == derived_sum_7
            value_gcd = gcd(value_gcd, exact_sum)
            direct_cases += 1
        assert value_gcd == g, (m, value_gcd, g)
        d31, d32 = d32, 198 * d32 - d31
    # A genuine contrasting boundary: the exponent-seven gcd can be larger.
    z = 0
    for n in range(8):
        z = gcd(z, sum(b[n + j] ** 7 for j in range(1, 4)))
    assert z == 49
    return {"m_values": max_m, "n_values_per_m": max_n + 1,
            "window_identity_cases": direct_cases,
            "D3_analytic_coefficient_cases": max_m,
            "two_value_gcd_cases": max_m,
            "exponent_seven_counterexample": z}


if __name__ == '__main__':
    import json
    print(json.dumps(check(), sort_keys=True))
