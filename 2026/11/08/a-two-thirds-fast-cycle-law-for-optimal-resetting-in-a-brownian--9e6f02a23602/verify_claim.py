#!/usr/bin/env python3
"""Reproduce algebra and numerical cross-checks for an overdamped two-stroke harmonic protocol."""
import math
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar


def work(reset, half_period, hot_temp, cold_temp, hard_k, soft_k):
    A = reset + 2.0 * hard_k
    B = reset + 2.0 * soft_k
    alpha = hot_temp - cold_temp
    beta = 2 * (hot_temp * soft_k - cold_temp * hard_k)
    F = math.expm1(-A * half_period) * math.expm1(-B * half_period) / (-math.expm1(-(A + B) * half_period))
    return (hard_k - soft_k) * (alpha * reset + beta) * F / (A * B)


def main():
    qh, qc, a, b, r, p, q = sp.symbols('qh qc a b r p q', positive=True)
    A, B = r + a, r + b
    hot = 2 * qh / A
    cold = 2 * qc / B
    # p and q are the hot/cold exponential attenuation factors.
    vh, vc = sp.symbols('vh vc')
    solution = sp.solve([vh - (p * vc + hot * (1 - p)),
                         vc - (q * vh + cold * (1 - q))], [vh, vc], dict=True)[0]
    Fpq = (1 - p) * (1 - q) / (1 - p * q)
    assert sp.simplify(solution[vh] - solution[vc] - (hot - cold) * Fpq) == 0
    alpha = qh - qc
    beta = qh * b - qc * a
    K = (qh + qc) * (a - b)
    assert sp.expand(alpha * (a + b) - 2 * beta - K) == 0
    assert sp.simplify((alpha * r + beta) / (2 * r + a + b) -
                       (alpha / 2 - K / (2 * (2 * r + a + b)))) == 0
    # Verify two nontrivial terms of hyperbolic attenuation expansion at rational parameters.
    t = sp.symbols('t')
    for aa, bb in [(sp.Rational(3), sp.Rational(5)),
                   (sp.Rational(7, 3), sp.Rational(11, 5)),
                   (sp.Rational(17, 2), sp.Rational(1, 2))]:
        x, y = aa * t / 2, bb * t / 2
        H = (aa + bb) / (aa * bb * t) * 2 * sp.sinh(x) * sp.sinh(y) / sp.sinh(x + y)
        assert sp.simplify(sp.limit(H, t, 0) - 1) == 0
        assert sp.simplify(sp.limit((H - 1) / t**2, t, 0) + aa * bb / 12) == 0
    # Verify that the scaled limiting loss has exactly the claimed critical point.
    c, al, kk = sp.symbols('c al kk', positive=True)
    loss = kk / (4 * c) + al * c**2 / 24
    assert sp.simplify(sp.diff(loss, c) * (12 * c**2) - (al * c**3 - 3 * kk)) == 0
    # Independent numerical integration of the piecewise variance ODE,
    # compared to the separate closed work formula, from periodic fixed-point data.
    hotT, coldT, kh, kl = 4., 1., 3., 1.
    for rr, period in [(0., .3), (1.5, .4), (5., .7), (12., .05)]:
        aa, bb = rr + 2*kh, rr + 2*kl
        eh, ec = math.exp(-aa*period), math.exp(-bb*period)
        mh, mc = 2*hotT/aa, 2*coldT/bb
        vc0 = (ec * mh * (1-eh) + mc * (1-ec)) / (1-ec*eh)
        vhot = solve_ivp(lambda tt, vv: [-aa*vv[0]+2*hotT], [0, period], [vc0],
                         rtol=1e-12, atol=1e-13).y[0, -1]
        vcold = solve_ivp(lambda tt, vv: [-bb*vv[0]+2*coldT], [0, period], [vhot],
                          rtol=1e-12, atol=1e-13).y[0, -1]
        assert abs(vcold-vc0) < 2e-11
        assert abs((kh-kl)*(vhot-vcold)/2-work(rr,period,hotT,coldT,kh,kl)) < 2e-11
    K_numeric = (hotT+coldT)*2*(kh-kl)
    alpha_numeric = hotT-coldT
    scale = (3*K_numeric/alpha_numeric)**(1/3)
    last_ratio = None
    for period in [.1,.01,.001,.0001]:
        optimum = minimize_scalar(lambda log_r: -work(math.exp(log_r), period, hotT, coldT, kh, kl),
                                  method='bounded', bounds=(-10, 19), options={'xatol':1e-11})
        assert optimum.success
        rr = math.exp(optimum.x)
        ratio = rr/(scale*period**(-2/3))
        assert 0.8 < ratio < 1.01
        if last_ratio is not None:
            assert abs(1-ratio)<abs(1-last_ratio)
        last_ratio = ratio
        print(f'half_period={period:.6g} optimum_r={rr:.9f} asymptotic_ratio={ratio:.8f}')
    assert last_ratio is not None and abs(last_ratio-1)<0.003
    print('PASS: symbolic fixed-point algebra, hyperbolic coefficients, independent moment-ODE integration, asymptotic optimum checks')

if __name__ == '__main__':
    main()
