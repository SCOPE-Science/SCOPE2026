"""Reproduce finite checks for a symmetric two-species Ricker exclusion theorem.

Uses Python's standard library. Finite tests are not a proof of the universal claim.
"""
from math import exp, log


def step(x, y, R, alpha):
    return x * exp(R - x - alpha*y), y * exp(R - y - alpha*x)


def check_one_step(R, alpha, x, y):
    xn, yn = step(x, y, R, alpha)
    drift = log(xn/yn) - log(x/y)
    assert abs(drift - (alpha-1)*(x-y)) < 2e-11
    assert abs(log(xn/x) - (R-x-alpha*y)) < 2e-11
    assert abs(log(yn/y) - (R-y-alpha*x)) < 2e-11


def check_rate(R, alpha, x0, y0, steps=12000):
    lx, ly = log(x0), log(y0)
    for _ in range(steps):
        x = exp(lx) if lx > -745 else 0.0
        y = exp(ly) if ly > -745 else 0.0
        lx, ly = lx+R-x-alpha*y, ly+R-y-alpha*x
    loser = ly if x0 > y0 else lx
    observed = loser/steps
    predicted = -(alpha-1)*R
    assert abs(observed - predicted) < 0.006, (R, alpha, observed, predicted)
    return observed, predicted


def main():
    for R, alpha, x, y in [(.6, 1.5, .8, .5), (2.5, 1.2, .9, .6),
                            (5.0, 1.5, 2.0, 1.0), (5.0, 2.5, 1.0, 2.0)]:
        check_one_step(R, alpha, x, y)
        print('RATE', R, alpha, x, y, check_rate(R, alpha, x, y))
    for R, alpha in [(.3, .1), (.8, .6), (.99, .95)]:
        along = 1-R
        across = 1-R*(1-alpha)/(1+alpha)
        assert max(abs(along), abs(across)) < 1
    print('VERIFY_OK one_step_log_identities=12 extinction_rates=4 coexistence_sinks=3')


if __name__ == '__main__':
    main()
