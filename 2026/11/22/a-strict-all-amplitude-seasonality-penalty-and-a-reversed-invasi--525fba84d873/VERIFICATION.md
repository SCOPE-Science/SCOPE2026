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

# Mathematical verification

The proof is self-contained in `RESULT.md`: positive period-map eigenvector, scalar Hill-equation transformation, positive periodic Riccati variable, exact mean-square defect, and explicit Cauchy–Schwarz estimate. Rational inequalities certify the nonzero, oppositely signed averaged and periodic invasion exponents without numerical inference.

The standalone `verify.py` script runs using only Python's standard library. It checks the witness's rational sign certificate, the compatible mosquito-population inequality, and explicit fourth-order Runge–Kutta period-map computations. The latter are corroboratory and do not establish universal infinite-time mathematical claims.

Scientific limits: fixed losses and one seasonal coupling only; no vertical infection, low-density shrinking adjustment, random populations, or assertions about global nonlinear persistence. This review has not been independently audited.
