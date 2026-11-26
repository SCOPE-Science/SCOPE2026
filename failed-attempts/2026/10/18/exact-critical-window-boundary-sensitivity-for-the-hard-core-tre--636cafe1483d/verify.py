"""Independent finite checks for the critical hard-core tree boundary profile.

The analytical convergence theorem requires the proof in RESULT.md.
"""
from fractions import Fraction
from math import expm1, sqrt


def finite_root_ratio(branching, depth, fugacity, zero_leaf):
    """Independently enumerate admissible independent sets, without recursion."""
    # Breadth-first numbering of the full regular rooted tree.
    parents = [-1]
    first_at_depth = [0]
    current = [0]
    for _ in range(depth):
        following = []
        for parent in current:
            for _ in range(branching):
                following.append(len(parents))
                parents.append(parent)
        current = following
        first_at_depth.append(current[0])
    nn = len(parents)
    assert nn <= 15
    active = [Fraction(0), Fraction(0)]
    for mask in range(1 << nn):
        if zero_leaf and depth and (mask >> first_at_depth[-1]):
            continue
        if zero_leaf and not depth and (mask & 1):
            continue
        if any((mask >> child & 1) and (mask >> parent & 1)
               for child, parent in enumerate(parents) if parent >= 0):
            continue
        weight = fugacity ** mask.bit_count()
        active[mask & 1] += weight
    return active[1] / active[0]


def recurrence_ratio(branching, depth, fugacity, zero_leaf):
    r = Fraction(0) if zero_leaf else fugacity
    for _ in range(depth):
        r = fugacity / (1 + r) ** branching
    return r


def critical_constant(branching, t):
    b = branching
    a = (b - 1) / b
    base = 2 * sqrt(6 * (b - 1)) / (b * sqrt(b + 1))
    z = a * t
    correction = 1.0 if z == 0 else sqrt(z / (-expm1(-z)))
    return base * correction


def finite_profile(branching, height, t):
    b = branching
    lc = b ** b / (b - 1) ** (b + 1)
    lam = lc * (1 + t / height)
    def f(r): return lam / (1 + r)**b
    rf, rz = lam, 0.
    for _ in range(height):
        rf, rz = f(rf), f(rz)
    return sqrt(height) * (-1 if height % 2 else 1) * (rf / (1 + rf) - rz / (1 + rz))


def main():
    finite_checks = 0
    for b, heights in ((2, (0, 1, 2, 3)), (3, (0, 1, 2))):
        for h in heights:
            for lam in (Fraction(1, 2), Fraction(1), Fraction(3, 2)):
                for zero in (False, True):
                    exact = finite_root_ratio(b, h, lam, zero)
                    prediction = recurrence_ratio(b, h, lam, zero)
                    assert exact == prediction, (b, h, lam, zero, exact, prediction)
                    finite_checks += 1

    derivative_checks = 0
    for b in range(2, 12):
        # Exact chain rule for the third derivative of F(F(r)) at the flip fixed point.
        f1 = Fraction(-1)
        f2 = Fraction((b + 1) * (b - 1), b)
        f3 = Fraction(-(b + 1) * (b + 2) * (b - 1)**2, b*b)
        third_double = f3*f1**3 + 3*f2*f1*f2 + f1*f3
        cubic = -third_double / 6
        expected = Fraction((b + 1) * (b - 1)**3, 6 * b*b)
        assert cubic == expected
        # Moving fixed point: lambda = r*(1+r*)**b.
        rc = Fraction(1, b - 1)
        r_delta = rc / 2
        # At a fixed point F'(r*)=-b*r*/(1+r*).
        f1_delta = -Fraction(b, 1) / (1+rc)**2 * r_delta
        multiplier_delta = 2*f1*f1_delta
        assert multiplier_delta == Fraction(b-1,b)
        derivative_checks += 1

    numeric_checks = 0
    worst_relative = 0.
    for b in (2, 3, 5, 7):
        for t in (-4., 0., 3.):
            for n in (12000, 12001, 24000, 24001):
                observed = finite_profile(b, n, t)
                target = critical_constant(b, t)
                relative = abs(observed / target - 1)
                worst_relative = max(worst_relative, relative)
                assert relative < 0.025, (b, t, n, observed, target, relative)
                numeric_checks += 1
    print(f"VERIFY_OK: {finite_checks} exact independent finite-tree partition comparisons; "
          f"{derivative_checks} exact cubic coefficient identities; "
          f"{numeric_checks} finite-depth crossover checks; "
          f"worst_relative={worst_relative:.6g}")

if __name__ == '__main__':
    main()
