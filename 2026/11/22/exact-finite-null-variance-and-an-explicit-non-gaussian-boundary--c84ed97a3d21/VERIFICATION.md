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

# Reproducibility and boundaries

The standalone Python 3 standard-library program `check.py` performs exact finite enumerations for \(n=3,4,5,6\), checking the literal double rank comparison against both a faster rank-count implementation and the signed quadratic identity. It computes the finite mean and variance as exact rational numbers and checks the analytic formulas. It also approximates the positive solutions of \(\tan(\omega/2)=\omega\) by bisection, checks reciprocal spectral traces and the hyperbolic product, and runs two seeded simulations as secondary consistency checks. The program reports **100,725 assertions passed**.

The proof of the limiting characteristic function is in `RESULT.md`; a finite numerical experiment does not certify a distributional limit. The theorem is for a fixed two-coordinate score and independent uniform null observations only. No independent review, formal verification, trained-classifier guarantee, or significance-level calibration for the original studentized algorithm is asserted.
