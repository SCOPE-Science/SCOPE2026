"""Exact independent checks for transport of tent-map periodic-point measures.

Usage: python verify.py (Python 3 stdlib only). No external data or packages.
"""
from fractions import Fraction as F


def inverse_fixed_points(n):
    branches = [(F(1), F(0))]
    for _ in range(n):
        branches = [(a / 2, b / 2) for a, b in branches] + [(-a / 2, 1 - b / 2) for a, b in branches]
    points = sorted(set(b / (1 - a) for a, b in branches))
    assert len(points) == 2 ** n
    return points


def transport_moment(points, p):
    m = len(points)
    assert isinstance(p, int) and p >= 1
    total = F(0)
    for j, x in enumerate(points):
        left, right = F(j, m), F(j + 1, m)
        assert left <= x <= right
        total += ((x - left) ** (p + 1) + (right - x) ** (p + 1)) / (p + 1)
    return total


def transport_sup(points):
    m = len(points)
    return max(max(x - F(j, m), F(j + 1, m) - x) for j, x in enumerate(points))


def predicted_points(m):
    r = m // 2
    return [F(0)] + [v for k in range(1, r) for v in (F(2*k, m+1), F(2*k, m-1))] + [F(m, m+1)]


def main():
    for n in range(1, 11):
        m = 2 ** n
        points = inverse_fixed_points(n)
        assert points == predicted_points(m)
        assert transport_moment(points, 1) == F(2*m*m - 1, 6*m*(m*m-1)), (n, "W1")
        assert transport_moment(points, 2) == F(1, 6*(m*m-1)), (n, "W2 squared")
        assert transport_sup(points) == F(1, m), (n, "W infinity")
        assert max(b-a for a,b in zip(points,points[1:])) == F(2, m+1)
        for p in (3,4):
            v = transport_moment(points, p)
            asymptotic = F(2, (p+1)*(p+2))
            # Exact finite m test for convergence envelope; crude but uniform.
            assert abs((m**p)*v-asymptotic) < F(10*p, m)
    print("VERIFY_OK independent_inverse_branch_enumerations=10 W1_exact=10 W2_exact=10 Winfty_exact=10 max_gap_exact=10 higher_p_exact_Riemann_bounds=20")

if __name__ == "__main__":
    main()
