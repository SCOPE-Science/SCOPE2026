"""Finite arithmetic/trigonometric diagnostics for the phase-response construction.
The all-orders and all-integers assertions rest on the accompanying proof.
"""
import math


def poly_U(n):
    """Integer coefficients, low order first, for Chebyshev U_n."""
    u0 = [1]
    if n == 0:
        return u0
    u1 = [0, 2]
    for _ in range(1, n):
        two_x_u1 = [0] + [2 * a for a in u1]
        size = max(len(two_x_u1), len(u0))
        u2 = [(two_x_u1[j] if j < len(two_x_u1) else 0)
              - (u0[j] if j < len(u0) else 0) for j in range(size)]
        u0, u1 = u1, u2
    return u1


def h_poly(q):
    """h(theta)=sin(theta)*cos(theta)*P(cos(theta)), P integer polynomial."""
    coeff = poly_U(2 * q)
    coeff[0] += (-1) ** (q + 1)
    coeff = [(-1) ** (q + 1) * a for a in coeff]
    coeff += [0] * max(0, 2 - len(coeff))
    # This gives 1+(-1)^{q+1}U_{2q}, divisible by x^2.
    assert coeff[0] == 0 and coeff[1] == 0
    return coeff[2:]


def evaluate(p, x):
    total = 0.0
    for c in reversed(p):
        total = total * x + c
    return total


def h(q, t):
    return math.sin(t) * math.cos(t) * evaluate(h_poly(q), math.cos(t))


def H(q, a, t):
    m = 2 * q + 1
    return (-1) ** (q + 1) * math.sin(m * t) - a * math.cos(t)


def run():
    test_count = 0
    for q in range(0, 8):
        m = 2 * q + 1
        p = h_poly(q)
        for k in range(513):
            t = 2 * math.pi * (k + 0.25) / 513
            expected_b = (-1) ** (q + 1) * math.sin(m * t)
            actual_b = -math.sin(t) + math.cos(t) * h(q, t)
            assert abs(actual_b - expected_b) < 2e-9, (q, k, actual_b, expected_b)
            test_count += 1
        # cos(theta)=0 is covered without dividing by cos(theta).
        assert all(abs(-math.sin(t) - (-1) ** (q + 1) * math.sin(m * t)) < 1e-12
                   for t in (math.pi / 2, 3 * math.pi / 2))
        for a in (0.12, 0.37, 0.81):
            extrema = [(math.pi / 2 + j * math.pi) / m for j in range(2 * m)]
            signs = [1 if H(q, a, t) > 0 else -1 for t in extrema]
            assert all(signs[j] == -signs[(j + 1) % (2 * m)]
                       for j in range(2 * m))
            assert abs(H(q, a, 0) + a) < 1e-13
            test_count += 1
    print(f"PASS {test_count} finite response and alternating-sign checks for m=1..15.")
    print("This script does not certify the infinite-family theorem or persistence.")


if __name__ == '__main__':
    run()
