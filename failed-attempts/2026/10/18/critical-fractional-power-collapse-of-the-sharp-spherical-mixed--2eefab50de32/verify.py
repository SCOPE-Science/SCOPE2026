#!/usr/bin/env python3
"""Supplementary numeric checks of critical Bessel moments.

Requires numpy and scipy. Finite quadrature is not a proof of an
infinite-domain limit or positivity theorem. No external data required.
"""
import math
import numpy as np
from scipy.special import jv, gammaln
from scipy.integrate import simpson


def cosine_mean(q):
    return math.exp(gammaln((q + 1) / 2) - math.log(math.pi) / 2
                    - gammaln((q + 2) / 2))


def check_one_dimension(d, cutoff=550.0, step=0.017):
    nu = d / 2 - 1
    qc = 2 * d / (d - 1)
    radii = np.arange(0.0001, cutoff, step)
    orders = [np.abs(jv(nu + k, radii)) for k in (0, 1)]
    exponent_c = d - 1 - nu * qc
    critical_difference = simpson(
        (orders[0] ** qc - orders[1] ** qc) * radii ** exponent_c,
        x=radii)
    B = 2 / (d - 1) * (2 / math.pi) ** (qc / 2) * cosine_mean(qc)
    K = (2 * math.pi) ** d * (2 / qc) * critical_difference / B ** (1 / d)
    print(f'd={d} qcritical={qc:.8f} finite_delta={critical_difference:.8f} '
          f'B={B:.8f} predicted_K_from_cutoff={K:.8f}')
    assert critical_difference > 0
    tested = 0
    for epsilon in (0.03, 0.01, 0.003):
        q = qc + epsilon
        a = (d - 1) * epsilon / 2
        leading_tail = ((2 / math.pi) ** (q / 2) * cosine_mean(q)
                        * cutoff ** (-a) / a)
        moments = [simpson(z ** q * radii ** (d - 1 - nu * q),
                           x=radii) + leading_tail for z in orders]
        assert moments[0] > moments[1] > 0
        gap = (2 * math.pi) ** d * (moments[0] ** (2 / q)
                                   - moments[1] ** (2 / q))
        ratio = gap / epsilon ** (1 / d) / K
        print(f'  epsilon={epsilon:.3g} normalized_ratio={ratio:.8f}')
        assert 0.94 < ratio < 1.03, (d, epsilon, ratio)
        tested += 1
    return tested


if __name__ == '__main__':
    count = sum(check_one_dimension(d) for d in (3, 4, 5))
    print(f'VERIFY_OK {count} cutoff-assisted Bessel moment and scaling comparisons')
