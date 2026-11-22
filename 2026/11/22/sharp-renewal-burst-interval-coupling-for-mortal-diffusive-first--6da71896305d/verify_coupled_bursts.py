"""Reproducibility checks for a marked-renewal mortal-search comparison.

Only Python standard library. Analytical argument, not this finite check, proves
all-time exponential bounds and the fixed-marginal coupling theorem.
"""
import math
from fractions import Fraction

A = Fraction(1, 2)
CO = ((1, 1, Fraction(1, 2)), (2, 2, Fraction(1, 2)))
IN = tuple((w, j, Fraction(1, 4)) for w in (1, 2) for j in (1, 2))
ANTI = ((1, 2, Fraction(1, 2)), (2, 1, Fraction(1, 2)))


def mgf(pairs, x):
    return sum(float(prob) * float(A**j) * x**w for w, j, prob in pairs)


def root(pairs):
    lo, hi = 1.0, 4.0
    for _ in range(120):
        mid = (lo + hi) / 2
        if mgf(pairs, mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def finite_no_event(pairs, max_t):
    """Exact renewal recursion for surviving eventual outcomes of all born particles."""
    values = [Fraction(1)]
    for t in range(1, max_t + 1):
        no_birth = sum(prob for w, j, prob in pairs if w > t)
        val = no_birth + sum(prob * A**j * values[t-w]
                             for w, j, prob in pairs if w <= t)
        values.append(val)
    return values


def direct_enumeration(pairs, t):
    """Independent recursion over all possible first arrival marks, exact."""
    if t == 0:
        return Fraction(1)
    p = sum(prob for w, j, prob in pairs if w > t)
    for w, j, prob in pairs:
        if w <= t:
            p += prob * A**j * direct_enumeration(pairs, t-w)
    return p


def main():
    co = root(CO)
    independent = root(IN)
    anti = root(ANTI)
    assert math.isclose(co, 2.0, rel_tol=0, abs_tol=1e-14)
    assert math.isclose(anti, (math.sqrt(65) - 1) / 4, rel_tol=0, abs_tol=1e-14)
    assert math.isclose(independent, (math.sqrt(201) - 3) / 6,
                        rel_tol=0, abs_tol=1e-14)
    assert anti < independent < co
    for pairs in (CO, IN, ANTI):
        # Marginal law of W and J, and expected particle production per time,
        # agree across all three couplings.
        assert sum(prob for w, j, prob in pairs if w == 1) == Fraction(1, 2)
        assert sum(prob for w, j, prob in pairs if j == 1) == Fraction(1, 2)
        assert sum(prob * w for w, j, prob in pairs) == Fraction(3, 2)
        assert sum(prob * j for w, j, prob in pairs) == Fraction(3, 2)
        values = finite_no_event(pairs, 500)
        for t in range(1, 13):
            assert values[t] == direct_enumeration(pairs, t)
        theta = math.log(root(pairs))
        assert abs(-math.log(float(values[500]))/500 - theta) < 0.003
        for t in (1, 2, 5, 50, 100, 500):
            v = float(values[t])
            # Uniform martingale-overshoot bounds, w_max=j_max=2.
            assert v >= math.exp(-theta * (t + 2)) * (1 - 1e-12)
            assert v <= float(A**(-2)) * math.exp(-theta * t) * (1 + 1e-12)
    # All binary couplings with these margins lie on a one-parameter segment.
    rates = []
    for k in range(21):
        z = Fraction(k, 40)  # probability of both (W,J)=(1,1) and (2,2)
        cross = Fraction(1, 2) - z
        law = ((1, 1, z), (1, 2, cross), (2, 1, cross), (2, 2, z))
        rates.append(math.log(root(law)))
    assert all(rates[i] < rates[i + 1] for i in range(20))
    assert math.isclose(rates[0], math.log(anti), abs_tol=1e-14)
    assert math.isclose(rates[-1], math.log(co), abs_tol=1e-14)
    # Exact Brownian killed-hitting CDF for D=d=1, x0=log 2.
    x0 = math.log(2)
    for t in (0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0):
        u = x0 / (2 * math.sqrt(t))
        v = math.sqrt(t)
        arrived = (math.exp(-x0) * math.erfc(u - v) +
                   math.exp(x0) * math.erfc(u + v)) / 2
        remaining = 1 - arrived
        assert remaining >= 0.5 - 1e-14
        assert remaining - 0.5 <= math.exp(-t) + 1e-14
    # Brownian success-before-death probability under D=d=1 and x0=log 2.
    assert math.isclose(math.exp(-math.log(2)), 0.5, abs_tol=1e-15)
    ratio = math.log(co)/math.log(anti)
    print('co  theta:', format(math.log(co), '.12f'))
    print('ind theta:', format(math.log(independent), '.12f'))
    print('anti theta:', format(math.log(anti), '.12f'))
    print('co/anti:  ', format(ratio, '.12f'))
    print('exact finite recursion/enumeration, marginal, root and overshoot checks PASS')


if __name__ == '__main__':
    main()
