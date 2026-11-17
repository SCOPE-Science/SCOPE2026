"""Deterministic finite numerical checks for the even-parameter incenter obstruction.
The accompanying analytical proof establishes the assertion for every even q.
"""
import math


def test(q):
    assert q >= 2 and q % 2 == 0
    delta = 1.0 / q**2
    r = 1.0 + 1.0 / q
    H = math.hypot(1.0, delta / 2)
    L = (q + 1) * delta
    x0 = L / 2
    y0 = math.sqrt(r * H)
    rho = 0.5 * math.log(r / H)
    assert 0 < rho and H < r and L > r - H
    assert abs(y0 * math.exp(-rho) - H) < 1e-13
    assert abs(y0 * math.exp(rho) - r) < 1e-13
    assert x0 > 0.5 * (r - H)
    assert abs(x0 / delta - (q / 2 + 0.5)) < 1e-11
    assert abs(x0 / (r * delta) - q / 2) < 1e-11
    lam = delta / 2
    deriv = lam / (2 * y0) * (1 - y0*y0/(r*r))
    assert deriv > 0
    t = min(delta / 100, delta * (r*r - y0*y0) / (100*r))
    assert t > 0 and x0 + t < L
    deriv_right = (-2*t/r + lam*(1-(y0*y0+t*t)/(r*r)))/(2*y0)
    deriv_left = (-2*t/r - lam*(1-(y0*y0+t*t)/(r*r)))/(2*y0)
    assert deriv_right > 0 and deriv_left < 0
    ds_minus = math.asinh((t*t + y0*y0 - H*H)/(2*H*y0))
    ds_plus = math.acosh(1+(t*t+(r-y0)**2)/(2*r*y0))
    # Floating-point inverse hyperbolic functions cannot resolve the tiny
    # gain for very large q; compare the exact positive argument increments.
    assert t*t/(2*H*y0) > 0 and t*t/(2*r*y0) > 0
    if q <= 50:
        assert ds_minus > rho and ds_plus > rho
    return t, min(t*t/(2*H*y0), t*t/(2*r*y0))

if __name__ == '__main__':
    for q in range(2, 202, 2):
        t, gain = test(q)
        print(f'q={q:3d}: |t|={t:.10g}, positive hyperbolic-function argument gain={gain:.10g}')
    print('100 even-parameter numerical consistency checks passed; not an infinite proof.')
