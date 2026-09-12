"""Toy crossover model illustrating the coalescing-saddle obstruction.

1D analogue of the N-dependent spectral-curve pinching:
  I_N(gamma) = int_{-L}^{L} exp(N * (-x^4/4 + delta x^2/2)) dx,
  delta = gamma * N^{-1/2}.

Fixed-delta steepest descent gives two separated saddles at x=+-sqrt(delta).
As delta -> 0 at rate N^{-1/2}, saddle separation ~ N^{-1/4} while the
Gaussian fluctuation scale is N^{-1/2}: the standard quadratic (fixed-saddle)
approximation cannot be uniform in gamma. This mirrors the Aztec obstruction
where the smooth-phase saddles coalesce as a_N -> 1.
Uses only the standard library + numpy.
"""
import json
import math

import numpy as np


def integrand(x, N, delta):
    return np.exp(N * (-x ** 4 / 4.0 + delta * x ** 2 / 2.0))


def trapz_integral(N, delta, L=3.0, n=400001):
    x = np.linspace(-L, L, n)
    return float(np.trapz(integrand(x, N, delta), x))


def quad_fixed_saddle_approx(N, delta):
    # Sum of two Gaussian approximations at x = +-sqrt(delta):
    # S'' = -3x^2 + delta = -2 delta at each saddle.
    # Each contributes exp(N delta^2/4) * sqrt(2pi/(N*2*delta)).
    if delta <= 0:
        return float("nan")
    return float(
        2.0 * math.exp(N * delta ** 2 / 4.0) * math.sqrt(2.0 * math.pi / (N * 2.0 * delta))
    )


Ns = [400, 1600, 6400]
gammas = [0.5, 1.0, 2.0, 4.0]
rows = []
for N in Ns:
    for g in gammas:
        delta = g * N ** (-0.5)
        num = trapz_integral(N, delta)
        qa = quad_fixed_saddle_approx(N, delta)
        rows.append(
            {
                "N": N,
                "gamma": g,
                "delta": delta,
                "saddle_separation": 2.0 * math.sqrt(delta),
                "fluctuation_scale": N ** (-0.5),
                "numeric": num,
                "fixed_saddle_quad": qa,
                "rel_error_quad": abs(qa - num) / num,
            }
        )
        print(
            f"N={N} gamma={g}: sep={2*math.sqrt(delta):.4f} "
            f"fluct={N**-0.5:.4f} num={num:.6f} quad={qa:.6f} "
            f"relerr={abs(qa-num)/num:.3f}"
        )

with open("toy_crossover_results.json", "w") as f:
    json.dump(rows, f, indent=1)
print("wrote toy_crossover_results.json")
