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

The symbolic checker in `check_cubic.py` verifies the exact cubic polynomial, its two derivative roots, both endpoint-factorization identities, and 253 ordered rational location cases. Optional finite-grid primal linear programs probe pairs on and off the recovery boundary, with the two true sites included in each grid. These finite calculations do not prove recovery or failure for arbitrary measures; the argument in `RESULT.md` relies on gauge duality, endpoint monotonicity and Vandermonde uniqueness. No independent scientific validation has been performed.
