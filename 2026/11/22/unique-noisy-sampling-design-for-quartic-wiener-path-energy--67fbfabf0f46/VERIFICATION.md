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

# Verification and scope
The standalone `verify_quartic_design.py` reproduces exact symbolic identities for all covariance integrals, the full derivative numerator and denominator, all eight coefficients of the transformed-polynomial sign certificate, the quadratic-comparison quotient derivatives, the zero-noise polynomial and boundary values. The code also independently evaluates the optimum numerically for seven noise choices and compares to 199 locations per choice. Such finite evaluations are supplementary only: unique interior optimality is proved by the analytic sign-change certificate and continuity.

Run from this directory: `python verify_quartic_design.py` with SymPy and mpmath as in `requirements.txt`. The mathematical statement is for all finite nonnegative variances, not only the seven checked numbers.

No external independent mathematical audit, publication-priority certification, or adaptive-sensor validation was performed.
