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

# Reproducibility and limits of verification

The accompanying standalone `check.py` ran successfully against the stated ODE. SymPy verifies, by differentiation and algebraic simplification, (i) the reciprocal integrating-factor derivative, (ii) the logarithmic coordinate derivative, and (iii) the squared-coupling balance. Three parameter combinations with positive, zero and negative initial coupling were integrated using SciPy's DOP853 solver and an upward-threshold event. For each combination, five shrinking starting displacements were tested; removing both asymptotic terms left bounded, converging-looking residuals. These diagnostics check numerical implementation and identities but do not prove the infinite-time claim.

The infinite-time argument is the exact integration in RESULT.md; importantly, the \(\int\kappa^2\,dt\) identity bounds the Taylor error uniformly even though the passage time tends to infinity. The literature comparison includes the originating full open-access paper and accessible abstracts of two related adaptive-coupling articles, without claiming to have read the inaccessible related full texts. No independent audit has been performed.

Reproduce the diagnostics with `python check.py`, with Python packages `sympy`, `numpy`, and `scipy` installed.
