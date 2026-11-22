"""Supplementary reproducibility checks for blackbody-mixture chromatic pivots.

No finite testing replaces the proof for all temperature distributions.
Run: python3 verify.py (Python 3 standard library only).
"""
import math
import random

WIEN_CONSTANT_MICRON_K = 14387.76877


def photon_occupation(T, x):
    z = x / T
    return 1.0 / math.expm1(z)


def split_contrasts(temperatures, weights, baseline, x):
    b0 = photon_occupation(baseline, x)
    hot = sum(w * (photon_occupation(T, x) - b0)
              for T, w in zip(temperatures, weights) if T > baseline)
    cold = sum(w * (b0 - photon_occupation(T, x))
               for T, w in zip(temperatures, weights) if T < baseline)
    return hot, cold


def contrast(temperatures, weights, baseline, lam_micron):
    x = WIEN_CONSTANT_MICRON_K / lam_micron
    hot, cold = split_contrasts(temperatures, weights, baseline, x)
    return hot - cold


def bisection_root(temperatures, weights, baseline, a, b):
    fa = contrast(temperatures, weights, baseline, a)
    fb = contrast(temperatures, weights, baseline, b)
    assert fa > 0 > fb, (fa, fb)
    for _ in range(75):
        m = (a + b) / 2
        fm = contrast(temperatures, weights, baseline, m)
        if fm > 0:
            a = m
        else:
            b = m
    return (a + b) / 2


def main():
    checks = 0
    rng = random.Random(235172)
    xgrid = (100, 300, 1000, 3000, 10000, 20000, 50000)
    # Random mixtures with both temperature sides test strict ratio ordering.
    for _ in range(2500):
        temperatures = [rng.uniform(3000, 4990), rng.uniform(5010, 7500)]
        temperatures += [rng.uniform(3000, 7500) for _ in range(rng.randrange(1, 9))]
        weights = [rng.uniform(0.05, 3) for _ in temperatures]
        norm = sum(weights)
        weights = [w / norm for w in weights]
        previous = -1.0
        for x in xgrid:
            hot, cold = split_contrasts(temperatures, weights, 5000, x)
            assert hot > 0 and cold > 0
            ratio = hot / cold
            assert ratio > previous, (temperatures, weights, previous, ratio, x)
            previous = ratio
            checks += 1
    # The exact three-temperature illustrative mixture.
    Ts, ws, T0 = (4000., 5000., 6000.), (0.2, 0.7, 0.1), 5000.
    assert sum(T*w for T, w in zip(Ts, ws)) == 4900
    assert contrast(Ts, ws, T0, 0.4) > 0
    assert contrast(Ts, ws, T0, 0.6) < 0
    root = bisection_root(Ts, ws, T0, 0.4, 0.6)
    assert 0.5302 < root < 0.5304, root
    checks += 4
    # Equal first moments imply strictly positive spectral excess, due to curvature.
    assert sum(T*w for T, w in zip(Ts, (0.2,0.6,0.2))) == 5000
    for x in xgrid:
        hot, cold = split_contrasts(Ts, (0.2,0.6,0.2), T0, x)
        assert hot > cold
        checks += 1
    # Bolometric-neutral hot/cold area weights: exactly equal fourth moment.
    wc = 0.1
    wh = wc * (T0**4 - 4000.**4) / (6000.**4 - T0**4)
    w0 = 1.0 - wc - wh
    assert wh > 0 and w0 > 0
    fourth = wc*4000.**4 + w0*T0**4 + wh*6000.**4
    assert abs(fourth/T0**4 - 1) < 1.e-14
    assert wc*4000 + w0*T0 + wh*6000 < T0
    assert contrast(Ts, (wc,w0,wh), T0, 0.1) > 0
    assert contrast(Ts, (wc,w0,wh), T0, 50) < 0
    checks += 4
    print('Supplementary numeric checks passed:', checks)
    print('Illustrative unique crossover (micrometres): %.12f' % root)
    print('Bolometric-neutral hot fraction: %.12f' % wh)
    print('Bounds: examples only; global uniqueness is analytical.')


if __name__ == '__main__':
    main()
