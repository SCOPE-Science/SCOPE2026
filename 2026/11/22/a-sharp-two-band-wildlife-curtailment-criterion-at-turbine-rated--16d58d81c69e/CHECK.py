"""Supplementary numerical checks for the two-band example; standard library."""
from math import exp, factorial, isclose


def bisect(f, l, r):
    sign = f(l) > 0
    assert f(l) * f(r) < 0
    for _ in range(70):
        m = (r + l) / 2
        fm = f(m)
        if fm == 0:
            return m
        if (fm > 0) == sign:
            l = m
        else:
            r = m
    return (r + l) / 2


def ratio(x):
    return x * exp(-x) if x <= 2 else x**4 * exp(-x) / 8


def risk_tail(x):
    return 0.75 * exp(-2*x) * sum((2*x)**j / factorial(j) for j in range(5))


def energy_tail(x):
    if x >= 2:
        return 8 * exp(-x)
    return exp(-x) * (x**3 + 3*x*x + 6*x + 6) - 30 * exp(-2)


def run():
    c = 0.3
    assert ratio(2) < c < ratio(1) < ratio(4)
    a, b, d, e = [bisect(lambda x: ratio(x)-c, l, r)
                  for l, r in [(0, 1), (1, 2), (2, 4), (4, 16)]]
    assert 0 < a < 1 < b < 2 < d < 4 < e
    risk = risk_tail(0)-risk_tail(a) + risk_tail(b)-risk_tail(d) + risk_tail(e)
    energy = energy_tail(0)-energy_tail(a) + energy_tail(b)-energy_tail(d) + energy_tail(e)
    h = bisect(lambda x: risk_tail(x)-risk, 2, 6)
    assert isclose(risk, 0.09967373841469, abs_tol=1e-13)
    assert isclose(energy, 0.35308503015247, abs_tol=1e-13)
    assert isclose(energy_tail(h), 0.18922131128610, abs_tol=1e-13)
    assert energy > energy_tail(h)

    # At the rated minimum the strict-level intervals touch at x=2.
    # At the smaller peak its isolated tie changes no integral.
    low = ratio(2)
    l = bisect(lambda x: ratio(x)-low, 0, 1)
    r = bisect(lambda x: ratio(x)-low, 4, 16)
    assert l < 1 < 2 < 4 < r
    budget_low = risk_tail(0)-risk_tail(l) + risk_tail(r)
    high = ratio(1)
    l = bisect(lambda x: ratio(x)-high, 2, 4)
    r = bisect(lambda x: ratio(x)-high, 4, 16)
    budget_high = risk_tail(0)-risk_tail(l) + risk_tail(r)
    assert 0 < budget_low < risk < budget_high < risk_tail(0)
    print('CHECK_OK', (a, b, d, e), (budget_low, risk, budget_high), energy, h, energy_tail(h))


if __name__ == '__main__':
    run()
