"""Supplementary reproducibility checks for random Fourier interpolation bounds.

Requirements: Python 3, NumPy, SciPy. Numerical checks support, but do not replace,
the elementary Vandermonde and distributional proofs in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma

checks = 0
for n in range(2, 11):
    k = n - 1
    for trial in range(16):
        # Deterministic, distinct but irregular circular nodes.
        rng = np.random.default_rng(1731 + 1000*n + trial)
        ts = np.sort(rng.uniform(0, 1, n))
        zs = np.exp(2j*np.pi*ts)
        v = np.array([[z**m for m in range(n)] for z in zs])
        inv = np.linalg.inv(v)
        p = []
        for j in range(n):
            others = [zs[l] for l in range(n) if l != j]
            # NumPy returns polynomial coefficients high-degree first.
            num = np.poly(others)
            denominator = np.prod([zs[j]-u for u in others])
            col = (num/denominator)[::-1]
            assert np.allclose(inv[:, j], col, rtol=5e-5, atol=5e-5)
            checks += 1
            p.append(1/abs(denominator))
        R = np.linalg.norm(inv, 'fro')**2
        S = sum(x*x for x in p)
        assert S*(1-1e-9) <= R <= math.comb(2*k,k)*S*(1+1e-9)
        checks += 1

# The Mellin identity is independently evaluated by direct quadrature.
for s in (0.1, 0.25, 0.5, 0.75):
    integral, err = quad(lambda u: (2*math.sin(math.pi*u))**(-s), 0.0, 0.5, epsabs=1e-9)
    integral *= 2
    formula = 2**(-s)*gamma((1-s)/2)/(math.sqrt(math.pi)*gamma(1-s/2))
    assert abs(integral-formula) < 2e-7
    checks += 1

# Exact small-order extremal identity: for n=2, sqrt(R)=2/|z1-z2|.
for gap in (0.12, 0.31, 0.77):
    zs = (1, np.exp(2j*np.pi*gap))
    v = np.array([[1,z] for z in zs])
    R = np.linalg.norm(np.linalg.inv(v), 'fro')**2
    assert abs(math.sqrt(R)-2/abs(zs[0]-zs[1])) < 1e-10
    checks += 1

print(f'CHECK_OK assertions={checks} dimensions=2..10')
