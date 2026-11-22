"""Numerical diagnostics for the reset-Adler stationary phase-density theorem.
Requires Python 3.9+ and scipy. Run: python verify.py.
These finite checks supplement, and do not replace, the analytic proof.
"""
import math
from scipy.integrate import quad


def drift(theta, detuning, coupling):
    return detuning - coupling * math.sin(theta)


def elapsed_age(theta, detuning, coupling):
    if detuning == coupling:
        return (math.tan(theta) + 1.0 / math.cos(theta) - 1.0) / coupling
    return quad(lambda u: 1.0 / drift(u, detuning, coupling), 0, theta,
                epsabs=1e-11, epsrel=2e-11, limit=250)[0]


def stationary_density(theta, detuning, coupling, rate):
    age = elapsed_age(theta, detuning, coupling)
    den = drift(theta, detuning, coupling)
    if detuning > coupling:
        period = 2 * math.pi / math.sqrt(detuning**2 - coupling**2)
        return rate * math.exp(-rate * age) / (den * (-math.expm1(-rate * period)))
    return rate * math.exp(-rate * age) / den


def run_checks():
    checks = 0
    cases = [(1.3, 1, .4), (1.3, 1, 1.0), (1.3, 1, 1.7),
             (.7, 1, .2), (.7, 1, .7), (.7, 1, .9),
             (.7, 1, 1.0), (.7, 1, 1.2),
             (1., 1, .2), (1., 1, .8), (1., 1, 1.5)]
    for detuning, coupling, rate in cases:
        upper = 2 * math.pi if detuning > coupling else math.asin(detuning/coupling)
        cut = 0 if detuning > coupling else 1e-5
        mass = quad(lambda th: stationary_density(th, detuning, coupling, rate),
                    0, upper-cut, epsabs=1e-9, epsrel=1e-9, limit=700)[0]
        omitted_mass = 0 if detuning > coupling else math.exp(
            -rate * elapsed_age(upper-cut, detuning, coupling))
        # The omitted tail is computed exactly from the age-survival formula.
        assert abs(mass + omitted_mass - 1) < 1e-6
        checks += 1
        for frac in [.07, .19, .31, .47, .63, .81, .93]:
            th = frac * upper
            h = 1e-6
            derivative = (math.log(stationary_density(th+h, detuning, coupling, rate))
                          - math.log(stationary_density(th-h, detuning, coupling, rate))) / (2*h)
            predicted = (coupling * math.cos(th) - rate) / drift(th, detuning, coupling)
            assert abs(derivative-predicted) < 2e-6
            checks += 1
    detuning, coupling, rate = .7, 1., .24
    gamma = math.sqrt(coupling**2-detuning**2)
    edge = math.asin(detuning/coupling)
    for d1, d2 in [(1e-3, 5e-4), (8e-4, 4e-4)]:
        slope = (math.log(stationary_density(edge-d2, detuning, coupling, rate))
                 - math.log(stationary_density(edge-d1, detuning, coupling, rate))) / math.log(d2/d1)
        assert abs(slope-(rate/gamma-1)) < .01
        checks += 1
    detuning = coupling = 1.
    rate = .3
    for gap in [.045, .025, .015]:
        th = math.pi/2-gap
        logp = (math.log(rate)-math.log(drift(th, detuning, coupling))
                - rate*elapsed_age(th, detuning, coupling))
        leading = (math.log(2*rate/coupling)+rate/coupling-2*math.log(gap)
                   -2*rate/(coupling*gap))
        assert abs(logp-leading) < .1
        checks += 1
    for detuning in [1.01, 1.3, 2, 7]:
        period_numeric = quad(lambda th: 1/drift(th, detuning, 1),
                              0, 2*math.pi, epsabs=1e-10, epsrel=1e-10)[0]
        period_exact = 2*math.pi/math.sqrt(detuning**2-1)
        assert abs(period_numeric-period_exact) < 1e-8
        checks += 1
    print(f"Passed {checks} deterministic numerical checks")


if __name__ == '__main__':
    run_checks()
