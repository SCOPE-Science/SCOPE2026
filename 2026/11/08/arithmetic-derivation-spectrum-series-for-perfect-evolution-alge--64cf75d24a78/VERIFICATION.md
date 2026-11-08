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

# Computational verification

The self-contained `verify.py` exhaustively solves the derivation identities by row reduction for small prime fields, verifying the first-window counts; it separately tests connected cyclic-block tuple counts. `verify_extension.py` performs direct exhaustive arithmetic over an explicit model of the quadratic field with nine elements, and `verify_series.py` verifies formal-series coefficients exactly using integer and rational arithmetic plus SymPy. The checks were executed from the package contents and returned `VERIFY_OK`, `VERIFY_EXTENSION_OK`, and `VERIFY_SERIES_OK`.

The mathematical proof is universal; finite checks do not verify infinitely many fields or dimensions. The matrix labeling is fixed, and no claim about isomorphism-class enumeration is made. Independent mathematical review has not been performed.
