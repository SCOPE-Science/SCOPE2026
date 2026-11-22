"""Supplementary finite diagnostics for the quintic pole-detuning theorem.

The proof is analytic and contained in RESULT.md. All computations here are
finite reproducible checks, not infinite-time positivity certificates.
Python 3 standard library only.
"""
import math


def G(delta, ratio, t):
    a1 = 1.0 / (1.0 + delta * delta)
    ar = 1.0 / (ratio * ratio + delta * delta)
    b1 = math.cos(t) + delta * math.sin(t)
    br = math.cos(ratio * t) + (delta / ratio) * math.sin(ratio * t)
    return (a1 - ar - math.exp(-delta * t) * (a1 * b1 - ar * br)) / (ratio * ratio - 1.0)


def Q(delta, ratio, t):
    a1 = 1.0 / (1.0 + delta * delta)
    ar = 1.0 / (ratio * ratio + delta * delta)
    return (a1 * (math.cos(t) + delta * math.sin(t)) -
            ar * (math.cos(ratio * t) + delta / ratio * math.sin(ratio * t))) / (a1 - ar)


def phase_q(m, phi, theta):
    return (m * m * math.cos(phi) - math.cos(m * phi + theta)) / (m * m - 1)


def integral_simpson(fun, end, intervals=2000):
    if intervals % 2:
        raise ValueError("even interval count required")
    h = end / intervals
    res = fun(0) + fun(end)
    for j in range(1, intervals):
        res += (4 if j % 2 else 2) * fun(j * h)
    return res * h / 3


def run():
    checks = 0
    # The integral and exact trigonometric representation are independent routes.
    for delta in (0.0, 0.07, 0.41):
        for ratio in (1.5, 2.0, 2.3, 3.0):
            for t in (0.2, 0.7, 1.4, 2.5):
                integral = integral_simpson(lambda s: math.exp(-delta * s) *
                                            (math.sin(s) - math.sin(ratio*s)/ratio) /
                                            (ratio*ratio-1), t)
                assert abs(integral - G(delta, ratio, t)) < 1e-9
                checks += 1
    # At integer resonance, strict positivity away from multiples of 2pi.
    for m in (2, 3, 4, 5):
        for j in range(1, 500):
            t = (2*math.pi) * (j + .37) / 500
            assert G(0, m, t) > 0
            checks += 1
        h = .02
        v = G(0, m, h)
        assert abs(v / h**4 - 1/24) < 0.001
        checks += 1
    # The exact phase formula has a strict supercritical-beating witness.
    # These phase values are numerical examples, not needed to define kappa.
    examples = ((2, .51940195, .6527169, .276300984683),
                (3, .32676503, .86358643, .109506554151))
    for m, phi, theta, kap in examples:
        for sign in (-1, 1):
            eps = sign * .002
            phase = phi if sign > 0 else (2*math.pi - phi)
            t = phase + 2*math.pi*round((theta/abs(eps) - phase)/(2*math.pi))
            assert abs(abs(eps)*t - theta) < .007
            ratio = m + eps
            bad_delta = .7 * kap * abs(eps)
            good_delta = 1.3 * kap * abs(eps)
            assert Q(bad_delta, ratio, t) > math.exp(bad_delta*t)
            checks += 1
            # At this witness the stronger damping reverses the sign.
            assert Q(good_delta, ratio, t) < math.exp(good_delta*t)
            checks += 1
            assert phase_q(m, phase, eps*t) > math.exp(bad_delta*t)
            checks += 1
    print(f"PASS: {checks} supplementary finite checks; analytic proof is in RESULT.md")


if __name__ == '__main__':
    run()
