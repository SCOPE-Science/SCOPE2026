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

# Verification and reproducibility

The exact derivation is in RESULT.md. Run `python verify.py` with Python 3 to replay 832 exact integer and rational assertions. The recorded output is in `verification_output.txt`. The checker uses no nonstandard libraries, and includes full sign-vector enumeration through dimension 12, a separate cumulative-binomial quantile calculation, low-dimensional arbitrary rational weights, fixed-mask covariances, four-vertex complete graph exact variances and a finite suite of algebraic strictness checks through dimension 128.

The exact proof, not finite checking, establishes all dimensions and all real symmetric matrices of dimension at most three. For large dimensions, the checker tests the resulting exact binomial formulas rather than enumerating vectors. The scalar rearrangement argument and the four-class translation theorem are elementary arguments supplied in the proof, not delegated to a code oracle.

For the optional decimal limit evaluation, install the package in `requirements.txt` and run `python limit_numeric.py`. The recorded floating-point result is in `limit_numeric_output.txt`. The output is numerical quadrature with a library error estimate, not an independently certified mathematical enclosure. The exact integral and its limiting interpretation are established analytically.

No independent scientific audit or external validation is asserted.
