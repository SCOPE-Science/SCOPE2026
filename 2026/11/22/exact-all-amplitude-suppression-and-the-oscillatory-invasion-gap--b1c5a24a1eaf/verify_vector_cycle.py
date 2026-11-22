#!/usr/bin/env python3
"""Reproducible numerical diagnostics for an exact epidemiological theorem.

Requires Python 3, NumPy, SciPy. Numerical integration here is diagnostic only:
the exact statements are proved analytically in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def ecological_cycle(amplitude, delta):
    """Return a dense solver and period for N(0)=1+amplitude, D(0)=1."""
    def rhs(t, state):
        n, d = state
        return [(1 - d) * n, delta * (n - 1) * d]

    def maximum_event(t, state):
        return state[1] - 1.0
    maximum_event.direction = 1
    maximum_event.terminal = False
    out = solve_ivp(rhs, (0, 25), (1 + amplitude, 1),
                    dense_output=True, events=maximum_event,
                    rtol=2e-11, atol=2e-12, max_step=.025)
    evs = out.t_events[0]
    assert len(evs) >= 2 and evs[0] < 1e-7
    period = float(evs[1])
    assert 2.0 < period < 20.0
    return out.sol, period


def floquet_profile(cycle, period, gamma_total, kappa, Bv=1):
    """Principal log growth rate and positive eigenvector; B_h=kappa/Bv."""
    Bh = kappa / Bv
    def rhs(t, matrix_flat):
        n = float(cycle(t)[0])
        a = np.array([[-gamma_total, Bh*n], [Bv, -1.0]])
        return (a @ matrix_flat.reshape((2, 2))).ravel()
    solution = solve_ivp(rhs, (0.0, period), np.eye(2).ravel(),
                         rtol=2e-11, atol=2e-12, max_step=.02)
    matrix = solution.y[:, -1].reshape((2, 2))
    ev, v = np.linalg.eig(matrix)
    j = int(np.argmax(ev.real))
    dominant = float(ev[j].real)
    eigenvector = np.asarray(v[:, j].real, dtype=float)
    eigenvector *= np.sign(eigenvector[0])
    eigenvector /= eigenvector[1]
    assert np.all(eigenvector > 0)
    return math.log(dominant) / period, eigenvector


def validate_one(amplitude, delta=2, gamma_total=1.5):
    cycle, period = ecological_cycle(amplitude, delta)
    ts = np.linspace(0, period, 5001)
    nvalues = cycle(ts)[0]
    nmean = np.trapezoid(nvalues, ts)/period
    assert abs(nmean-1) < 3e-7, nmean

    def exponent(kappa):
        return floquet_profile(cycle, period, gamma_total, kappa)[0]
    assert exponent(gamma_total) < 0
    critical = brentq(exponent, gamma_total, gamma_total+2,
                      xtol=2e-11)
    assert critical > gamma_total
    assert abs(exponent(critical)) < 1e-9

    # Independently integrate a positive Floquet trajectory and evaluate
    # the exact time-averaged Riccati identity.
    growth, principal = floquet_profile(cycle, period, gamma_total, critical)
    def infected_rhs(t, u):
        h, y = u
        return [-gamma_total*h+critical*cycle(t)[0]*y, h-y]
    trajectory = solve_ivp(infected_rhs, (0, period), principal,
                           dense_output=True, rtol=1e-11,
                           atol=1e-12, max_step=.01)
    vals = trajectory.sol(ts)
    z = vals[0]/vals[1] -1
    mean_z = np.trapezoid(z,ts)/period
    mean_zsq = np.trapezoid(z*z,ts)/period
    assert abs(mean_z) < 3e-7, mean_z
    assert abs((critical-gamma_total)-mean_zsq) < 2e-6
    return period,critical,mean_zsq,exponent(gamma_total)


def main():
    g, delta = 1.5, 2
    predicted = g*g/(2*((g+1)**2+delta))
    assert abs(predicted-3/22) < 1e-14
    for amplitude in (0.025, 0.05, 0.10, 0.20, 0.40, 0.80):
        period, critical, exact_term, growth = validate_one(amplitude)
        ratio = (critical - g)/amplitude**2
        print(f"eps={amplitude:.3f} period={period:.8f} "
              f"threshold={critical:.10f} "
              f"growth_at_g={growth:.9f} "
              f"mean_z_squared={exact_term:.9f} "
              f"scaled_shift={ratio:.8f}")
    print(f"small-amplitude predicted threshold-shift coefficient: {predicted:.10f}")
    print("PASS: six periodic-orbit diagnostics, eigenvalue and Riccati checks")


if __name__ == '__main__':
    main()
