---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The associated `verify_group_reset.py` runs with Python 3, NumPy and mpmath. It requires no downloads or external data. Execute `python verify_group_reset.py` from the folder containing the program. On the examined execution it printed:

```
PASS 52 checks; n=2 r=250 samples=6000; sample_mean=16.2272927 exact_mean=16.2116725; sample_variance=1.3863857 exact_variance=1.4162424; normal_limit_variance=1.4166667
```

The code checks the exact Gaussian-order-statistic values at \(N=2\), \(N=3\), and further numerical integrals at \(N=5\); exact beta-function identities at five frequencies; limiting mean and variance ratios; and seeded direct iteration of the Poisson-interval Gaussian-maximum map. The simulation checks are loose-tolerance finite diagnostics. They are not an exhaustive computation or an independent proof of convergence. Analytical verification is in the exact affine kernel, finite-rate moment identities, fourth-moment bounds, predictable quadratic-variation limit, Lindeberg check and exponentially controlled perpetuity tail in `RESULT.md`.

The variance coefficient requires retaining the correlation of the exponential inter-reset time and Gaussian maximum: the innovation is \(\sqrt{2DE}\,M_N-kc_NE\), not an independent Brownian-noise increment with fixed excursion length. This is independently checked via the finite-rate variance identity.

Independently performed validation: none. No external certification is claimed.
