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

# Verification details

Execute `python3 verify_wheel.py` from the directory containing this document and the verifier. The verifier builds each unweighted wheel Laplacian directly, removes the two selected leader coordinates, inverts the grounded matrix with exact rational arithmetic, and checks every pair of leaders for rim sizes 4 through 10. It independently constructs the tridiagonal Schur expression for every separation for rim sizes 4 through 18 and exactly reproduces the finite formulas for rim sizes 4 through 8. The code reports 323 exact-rational checks, in addition to an exact integer certificate of the positive analytic boundary witness; its floating-point illustration is not a certificate and is not needed for the proof.

The infinite range follows from the Green-function recurrence, Schur complement, Cauchy–Schwarz bound and the positive derivative/witness inequalities in RESULT.md. No finite sample or test log is treated as a proof for all sizes. This verification does not constitute independent mathematical audit, bibliographic completeness, or a computationally exhaustive check beyond the stated finite ranges.
