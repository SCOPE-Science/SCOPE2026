"""Supplementary numerical checks for sharp two-destination congestion share bounds.

Requires NumPy. Run: python3 verify.py. This checker is not an infinite proof.
"""
import numpy as np

rng = np.random.default_rng(1227)
K = 80
u = (np.arange(K) + 0.5) / K
D = u[:, None] - u[None, :]
checks = 0

for alpha in [0.01, 0.1, 0.5, 1, 2, 10, 50]:
    lo = alpha / (1 + 2 * alpha)
    hi = 1 - lo
    for _ in range(100):
        mat = rng.lognormal(0, 2, (K, K))
        # Approximately doubly stochastic with strictly positive entries.
        for _ in range(75):
            mat /= mat.sum(axis=1, keepdims=True)
            mat /= mat.sum(axis=0, keepdims=True)
        mat /= mat.sum()

        def equilibrium(scale):
            left, right = 0.0, 1.0
            for _ in range(75):
                z = (left + right) / 2
                response = mat[D > scale * (2 * z - 1)].sum()
                if response > z:
                    left = z
                else:
                    right = z
            return (left + right) / 2

        x, y = equilibrium(alpha), equilibrium(2 * alpha)
        # Discretization permits a small tolerance, unlike the exact theorem.
        assert lo - 1e-9 < x < hi + 1e-9, (alpha, x, lo, hi)
        assert (x - 0.5) * (y - 0.5) > -1e-8, (alpha, x, y)
        assert abs(y - 0.5) <= abs(x - 0.5) + 1e-8, (alpha, x, y)
        checks += 1

    for gap in [0.04, 0.01, 0.001]:
        delta = lo + gap * (0.5 - lo)
        x = 1 - delta
        t = alpha * (2 * x - 1)
        assert delta > t and delta - 1 < t
        checks += 1

print(f"PASSED {checks} supplementary finite numerical checks")
