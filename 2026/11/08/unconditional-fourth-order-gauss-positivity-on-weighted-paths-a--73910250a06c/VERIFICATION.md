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

The accompanying standalone `verify.py` recomputes the two-, three- and four-vertex rational end-step identities with exact symbolic arithmetic, verifies the conservation identity in the nontrivial cases, and checks the adjacent Green-function formula for several independent rationally weighted paths of orders two through nine. It returned `VERIFY_OK` after extraction from the deliverable package.

The proof of the unbounded family and the real-weight domain uses effective-resistance centering, an exact three-dimensional Perron inequality, and strict spectral-radius monotonicity; finite checks are illustrative and are not an exhaustive certificate for unbounded graph order. The polynomial-positivity certificates in the main theorem can be checked directly from their printed coefficients. External independent validation has not been performed.
