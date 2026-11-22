"""Numerical spot checks for the clipped-ramp hyperplane projection formulas.

These checks do not replace the analytic proofs for arbitrary measures,
all budgets, or the asymptotic limits.
"""
from math import isclose


def threshold(beta):
    return 2.0 * (beta + 2.0) / (beta + 1.0)


def optimal_amplitude(beta, budget):
    critical = threshold(beta)
    if budget < critical * (1.0 - 1e-13):
        return None
    coefficient = 2.0 ** (beta + 1.0) / (beta + 2.0)
    def moment_deficit(t):
        return t - coefficient * t ** (beta + 2.0) / budget ** (beta + 1.0) - 1.0
    if isclose(budget, critical, rel_tol=1e-14):
        return budget / 2.0
    low, high = 1.0, budget / 2.0
    for _ in range(110):
        middle = (low + high) / 2.0
        if moment_deficit(middle) < 0:
            low = middle
        else:
            high = middle
    return (low + high) / 2.0


def exact_clipped_moment(beta, budget, amplitude):
    c = (beta + 1.0) * 2.0 ** beta
    cut = amplitude / budget
    if cut >= 0.5:
        return 2.0 * c * budget * 0.5 ** (beta + 2.0) / (beta + 2.0)
    left = budget * cut ** (beta + 2.0) / (beta + 2.0)
    right = amplitude * (0.5 ** (beta + 1.0) - cut ** (beta + 1.0)) / (beta + 1.0)
    return 2.0 * c * (left + right)


def main():
    assertions = 0
    for beta in [-0.75, -0.5, 0.0, 0.5, 1.0, 2.0, 5.0]:
        critical = threshold(beta)
        assert optimal_amplitude(beta, critical * 0.75) is None
        assertions += 1
        critical_amplitude = optimal_amplitude(beta, critical)
        assert isclose(critical_amplitude, critical / 2, rel_tol=2e-12)
        assertions += 1
        for factor in [1.0, 1.0001, 1.1, 2.0, 10.0, 1e2, 1e3]:
            L = critical * factor
            M = optimal_amplitude(beta, L)
            assert M is not None and M > 1 - 1e-12 and M <= L/2 * (1 + 1e-12)
            assertions += 1
            assert isclose(exact_clipped_moment(beta, L, M), 1, rel_tol=5e-12, abs_tol=5e-12)
            assertions += 1
            for fraction in [0.1, 0.5, 0.9]:
                m = M * fraction
                assert exact_clipped_moment(beta, L, m) < 1
                assertions += 1
        if beta <= 1:
            for L in [critical * 1e5, critical * 1e6, critical * 1e7]:
                M = optimal_amplitude(beta, L)
                asym = (2.0 ** (beta + 1.0) / (beta + 2.0)) * L ** (-beta - 1)
                if asym > 1e-12:
                    assert abs((M - 1) / asym - 1) < 0.1
                    assertions += 1
        if beta == 0:
            for L in [4, 5, 10, 100]:
                amplitude = L / 2 * (1 - (1 - 4 / L) ** 0.5)
                assert isclose(optimal_amplitude(beta, L), amplitude, rel_tol=1e-12)
                assertions += 1

    # Nonpower positive density w(t)=0.8(1+t) on (0,1/2).
    def nonpower_moment(L, M):
        cut = min(0.5, M / L)
        small = L * (cut**2 / 2 + cut**3 / 3)
        # The bracket is integral from cut to 1/2 of (1+t).
        big = M * ((0.5 + 0.5**2/2) - (cut + cut**2/2))
        return 1.6*(small+big)

    critical_nonpower = 3.75
    assert isclose(nonpower_moment(critical_nonpower, critical_nonpower/2), 1, abs_tol=1e-12)
    assertions += 1
    for L in [3.75, 4.0, 5.0, 10.0, 50.0]:
        low, high = 0.0, L/2
        for _ in range(90):
            mid = (low + high)/2
            if nonpower_moment(L, mid)<1:
                low=mid
            else:
                high=mid
        M=(low+high)/2
        assert isclose(nonpower_moment(L,M), 1, abs_tol=1e-12)
        assertions+=1
        assert nonpower_moment(L,M*.99)<1
        assertions+=1
    assert nonpower_moment(3.74, 50) <1
    assertions+=1

    print('SIGNED_DENSITY_PROJECTION_CHECK_OK', assertions)


if __name__ == '__main__':
    main()
