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

Execute `python3 verify.py` with a Python 3 standard-library installation. The script directly forms the supporting lines and their products rather than calling the asserted radial factorization to compute the left-hand side. It verifies polynomial values, affine precision, the nonadjacent-line intersection property, and the exact vertex value for every integer \(3\le n\le35\) on 20 chosen test points per order. This execution produced `PASS: 2556 finite standard-library checks for n=3..35`.

A separate supplemental mpmath 65-digit high-precision check over orders \(3\le n\le29\) passed 1164 assertions; the corresponding routine is not needed to reproduce the main package and is not part of the finite certificate. The general theorem, strict monotonicity, and limiting law follow from the symbolic proof, not the checks. Specific numerical tolerances bound roundoff and do not certify the polynomial identity for all points.

No independent audit has been performed.
