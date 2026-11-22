"""Reproduce finite-sample normalized-max Kolmogorov discrepancies.

Dependencies: Python 3, numpy, scipy. Numerical checks are not proofs.
"""
import math
import numpy as np
from scipy.special import gammaincc, gammaln

CASES = ((0.5, 2.0, (500, 5000, 20000)),
         (1.0, 2.0, (500, 5000, 20000)),
         (2.0, 2.0, (500, 5000, 20000)),
         (3.0, 0.5, (500, 5000, 20000)))


def predicted_limit(alpha, beta):
    c = math.exp(alpha * math.log(beta) - math.lgamma(alpha + 1))
    if alpha < 1:
        return 2 * math.exp(-2)
    if alpha == 1:
        return 4 * math.exp(-2) / beta
    return (alpha * c ** (-1 / alpha) * (1 + beta / (alpha + 1))
            * (1 + 1 / alpha) ** (1 + 1 / alpha)
            * math.exp(-(1 + 1 / alpha)))


def finite_k(alpha, beta, n, upper_x=30):
    c = math.exp(alpha * math.log(beta) - gammaln(alpha + 1))
    a = (c * n) ** (1 / alpha)
    jmax = int(math.ceil(upper_x * a))
    # Sample lattice sites across the extreme-value scale; not an exhaustive supremum.
    j = (np.arange(jmax + 1, dtype=float) if jmax <= 50000
         else np.unique(np.rint(np.linspace(0, jmax, 50000))))
    F = gammaincc(alpha, beta / (j + 1))
    H = np.power(F, n)
    x1, x2 = j / a, (j + 1) / a
    G1 = np.exp(-np.power(x1, -alpha, where=x1>0, out=np.full_like(x1, float('inf'))))
    G2 = np.exp(-np.power(x2, -alpha))
    return float(np.max(np.maximum(np.abs(H - G1), np.abs(H - G2))))


def main():
    for alpha, beta, ns in CASES:
        predicted = predicted_limit(alpha, beta)
        scaled = []
        for n in ns:
            k = finite_k(alpha, beta, n)
            scaled.append(k * (n if alpha <= 1 else n ** (1 / alpha)))
        print(f"alpha={alpha}, beta={beta}, scaled n={ns}: "
              + ", ".join(f"{v:.8f}" for v in scaled)
              + f"; proposed limit={predicted:.8f}")
        assert math.isfinite(predicted) and predicted > 0
        assert abs(scaled[-1]/predicted - 1) < 0.15, (alpha, beta, scaled[-1], predicted)
    print("Finite-sample limit sanity checks: passed (not a proof).")

if __name__ == '__main__':
    main()
