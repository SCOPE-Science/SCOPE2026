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

# Reproducibility and proof boundaries

Run `python verify.py` in a Python environment with no third-party packages. The script enumerates all matrix-and-central-functional idempotent derivations of the symmetric-bracket algebra with two-dimensional quotient over the prime fields of orders 3, 5 and 7 for a split form; the exact counts are 7, 11 and 15. It also finds only the zero idempotent for the anisotropic diagonal form over the prime fields of orders 3 and 7. A separate finite search enumerates maximal totally isotropic planes and their transverse ordered pairs in split four-dimensional quotient spaces over fields of orders 3 and 5, giving 8/24 and 12/60 planes/pairs respectively. Including their central-function choices produces 217 and 1501 idempotent derivations. Successful output ends with `VERIFY_OK`.

The infinite-family assertions are proved in RESULT.md using the adjoint projection criterion and a count of orthogonal isotropic complements, not through finite enumeration. The script does not exhaust arbitrary prime powers, dimensions or every quadratic-form class. Characteristics two and degenerate forms are excluded. The same-model correctness, originality and value review is recorded in REVIEW.md and AUDIT.json; no independent mathematical audit has been performed.
