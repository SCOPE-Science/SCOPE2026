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

The standalone `verify.py` uses only the Python 3 standard library, seeded deterministic draws and quadrature routines. Run it with `python3 verify.py` in a directory containing both this note and the script. On the checked package it printed:

```
PASS 20666 supplementary exact-formula, optimality-grid, integral and scaling checks
```

The script checks Gaussian covariance integral identities against independent Simpson integration; equality of the exact boundary formula with direct conditional covariance; superiority to sampled arbitrary endpoint pairs; strictly increasing optimal gaps across noise levels; closed-form zero-noise roots; the fixed-kernel large-noise expansion; and the joint correlation/noise asymptotic limits. Such checks can identify numerical mistakes, not certify an unbounded continuum theorem. Mathematical correctness depends on the explicit argument in `RESULT.md`.

The single observation is \(Y=X(v)-X(u)+\varepsilon\), where the measured noise is added **after** differencing. The quantity called explained variance is \(\operatorname{Var}(\mathbb E[J\mid Y])\), not the posterior variance remaining. At zero noise coincident readings are excluded, since their contrast is identically zero.

The mathematical review included checking stationary-point uniqueness, the exact Gaussian observation normalization, reflected minimizers, and asymptotic boundaries. No independent audit has been performed.
