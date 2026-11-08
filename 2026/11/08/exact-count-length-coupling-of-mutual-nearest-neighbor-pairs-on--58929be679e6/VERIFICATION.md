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
Run `python verify.py` with Python 3 and its standard library from the extracted directory. The checker exhaustively iterates the \((n-1)!\) relative orders of interpoint spacings for each \(3\le n\le9\), uses exact rational moments of independent exponential order-statistic increments, and compares the count mean, reciprocal-edge length mean, count variance, mixed covariance, and (for \(n\ge5\)) length variance to the displayed formulas. It passes 33 exact assertions and records the two small-size covariance exceptions.

The checker is finite corroboration only, not a proof of the all-size formulas or joint weak convergence. The proof is the exponential spacing representation, explicit local integrals and covariance summation, then the finite-dependent Gaussian limit with gamma normalization. Independent scientific validation has not been performed.
