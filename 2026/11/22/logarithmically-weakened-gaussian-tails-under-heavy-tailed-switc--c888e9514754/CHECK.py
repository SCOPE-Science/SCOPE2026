"""Independent numerical checks for the logarithmic Gaussian tail theorem.

Run: python CHECK.py
Requires Python 3 and scipy. This verifies finite-parameter consequences
and asymptotic convergence bounds; it does not replace the proof.
"""
import math
from scipy.integrate import quad


def verify_case(a, b, diffusion, stiff_time, beta, scale):
    assert 0 < a < b and diffusion > 0 and stiff_time > 0
    assert beta > 1 and scale > 0
    lvar, hvar = diffusion / a, diffusion / b
    gaplo = (lvar - hvar) * (1 - math.exp(-2 * b * stiff_time))
    gaphi = lvar - hvar
    mean = scale / (beta - 1)
    constant = scale**beta / ((mean + stiff_time) * (beta - 1))
    assert 0 < gaplo <= gaphi < lvar

    # An exact bound for the soft-phase contribution, valid regardless of
    # the random variance at the beginning of that phase.
    def ratio_bound(log_displacement, entry_gap):
        center = log_displacement / a
        q = math.exp(2 * log_displacement)
        def integrand(age):
            y = (entry_gap / lvar) * math.exp(-2 * a * age)
            k = q * y
            if k > 1400:
                return 0.0
            return (1 + age / scale)**(-beta) * math.exp(-k / (2*(1-y))) / math.sqrt(1-y)
        left = max(0.0, center - 40 / a)
        right = center + 40 / a
        middle = quad(integrand, left, right, epsabs=2e-13, limit=150)[0]
        # Beyond right, kernel differs from unity by at most O(exp(-80)).
        analytic_tail = scale / (beta-1) * (1 + right/scale)**(1-beta)
        return (middle + analytic_tail) / (mean + stiff_time)

    prev = 0.0
    for r in (16., 32., 64., 128., 256.):
        theoretical = constant * (r / a)**(1-beta)
        lower = ratio_bound(r, gaphi) / theoretical
        upper = ratio_bound(r, gaplo) / theoretical
        assert 0.91 < lower <= upper < 1.04, (r, lower, upper)
        assert lower > prev, (r, lower, prev)
        prev = lower
        print('log(|x|/sqrt(D/a))=', r,
              'soft phase lower/limit=', round(lower, 9),
              'upper/limit=', round(upper, 9))
    # The stiff phase can be near the largest variance only if the preceding
    # whole soft residence was longer than the corresponding threshold.
    r = 128.
    threshold = (2*r + math.log(gaplo/lvar)) / (2*a)
    stiff_nearedge_upper = stiff_time/(mean+stiff_time) * (1+threshold/scale)**(-beta)
    soft_nearedge_asym = constant * (r/a)**(1-beta)
    assert stiff_nearedge_upper/soft_nearedge_asym < 0.03


if __name__ == '__main__':
    verify_case(.5, 2., 1., 1., 2.5, 1.)
    verify_case(.8, 1.4, 1.5, .4, 2.2, 1.3)
    print('All independent quadrature and rare-event bounds passed.')
