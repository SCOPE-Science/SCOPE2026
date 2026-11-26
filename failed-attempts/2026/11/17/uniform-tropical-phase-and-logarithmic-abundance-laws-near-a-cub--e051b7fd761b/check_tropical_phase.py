"""Independent numerical and algebraic spot checks of a tropical orbit limit.

Requires Python 3, numpy, scipy. These finite checks corroborate but do not
establish the uniform-in-energy assertion, which has an analytic proof.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def reference_phase(a, b, c, s):
    p1 = 1/(2*a*b)
    p2 = p1 + 1/(2*b*c)
    P = p2 + 1/(2*a*c)
    if 0 <= s <= p1:
        return np.array([0., 2*a*s, 1/a-2*b*s])
    if s <= p2:
        z = s - p1
        return np.array([2*b*z, 1/b-2*c*z, 0.])
    z = s-p2
    return np.array([1/c-2*a*z, 0., 2*c*z])


def check_one(a, b, c, h, delta=.12):
    L = -math.log(h)
    P = (a+b+c)/(2*a*b*c)
    u0 = 1-delta
    q = lambda w: c*math.log(u0)+b*math.log(delta-w)+a*math.log(w)-math.log(h)
    approx = math.exp((math.log(h)-c*math.log(u0)-b*math.log(delta))/a)
    w0 = brentq(q, approx*0.01, delta/2, xtol=1e-290)
    y0 = np.log([u0, delta-w0, w0])

    def rhs(_t, y):
        u, v, w = np.exp(y)
        return np.array([2*(a*v-b*w), 2*(-a*u+c*w), 2*(b*u-c*v)])

    def crossing(_t, y):
        return np.exp(y[0])-u0

    crossing.direction = 1
    crossing.terminal = False
    end = 2*L*P+10
    sol = solve_ivp(rhs, (0, end), y0, events=crossing, method="DOP853",
                    max_step=.08, rtol=2e-12, atol=2e-13, dense_output=True)
    assert sol.success
    roots = sol.t_events[0]
    roots = roots[roots > 1]
    assert len(roots) >= 1
    T = float(roots[0])
    phases = np.linspace(0, 1, 701)
    phase_error = max(np.max(np.abs(-sol.sol(f*T)/L -
                       reference_phase(a,b,c,f*P))) for f in phases)
    assert abs(T-L*P) <= 0.05
    assert phase_error*L <= 7
    assert abs(sum([c, a, b])/(a+b+c) - 1) < 1e-14
    return T, L*P, phase_error, L*phase_error


def main():
    for a,b,c,h in [(1.,1.,1.,1e-8), (2.,3.,1.,1e-11)]:
        T, leading, error, scaled = check_one(a,b,c,h)
        print(f"a={a:g} b={b:g} c={c:g} h={h:g}: "
              f"period={T:.9f}, leading={leading:.9f}, "
              f"phase_error={error:.6g}, scaled_error={scaled:.6g}")
    print("TROPICAL_KOLMOGOROV_LOG_PHASE_CHECK_OK")


if __name__ == '__main__':
    main()
