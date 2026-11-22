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

# Reproducibility

`checker.py` requires Python 3.9+ and SciPy, and is invoked as `python checker.py` from the directory containing it. It checks 180 exact rational parameter identities between two independent algebraic constructions of the equal-time squared-mode covariance, seven independent reset-age Gaussian-mixture numerical quadratures, and nine lagged chronological ratios. It does not establish completeness of the literature search or independently certify the analytic proof.

The proof itself is self-contained in `RESULT.md`: the generator closes on the three relevant second/mixed-fourth monomials, and the centered energy monomials are exact eigenfunctions for the conditional first moments. The strict sign classification is an elementary but global inequality on a strictly decreasing polynomial; no simulation is used to infer strictness or uniqueness. The statement requires a stationary law of a stable Ornstein–Uhlenbeck diffusion with Poisson resetting and bounded reset marks.
