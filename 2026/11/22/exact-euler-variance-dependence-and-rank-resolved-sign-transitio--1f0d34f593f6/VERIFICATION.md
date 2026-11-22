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

# Reproducibility of the finite-sample covariance proof

Execute `python3 check_topo_variance.py` with Python 3.8 or later. It uses only the Python standard library and prints `PASS EXACT ASSERTIONS 1210` when successful.

The checker builds the unbiased-variance quadratic form from pairwise differences rather than from the claimed coefficient formulas, evaluates every Dirichlet second moment under the conditional simplex shift using exact fractions, and compares it with the closed covariance formula at all interior ranks for every integer sample size from 2 through 17 at five rational thresholds. It also checks the total covariance and integer sign boundaries, including the rational switch thresholds and an opposing-sign example at the same radius. These computational checks have finite scope; the analytic proof in `RESULT.md` supplies the general quantifiers. No independent mathematical audit was performed.
