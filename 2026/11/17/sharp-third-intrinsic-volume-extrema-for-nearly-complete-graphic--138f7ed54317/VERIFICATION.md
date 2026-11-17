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

# Verification

Run `python3 artifacts/verify.py` from the extracted package root using Python 3 standard library. The checker enumerates 2,160 deletion patterns exhaustively for orders four through seven, and 400 deterministic sampled deletion patterns for orders eight through ten. It computes all three-edge wedge weights and verifies exact coefficients of the \(1,\sqrt2,\sqrt6\) basis for the inclusion-exclusion identity; the finite ordering comparisons additionally use standard double precision. The expected terminal success signature is `DENSE_ZONOTOPE_V3_CHECKS_PASSED exhaustive_deletions=2160 random_deletions=400`.

The unbounded cases, strict extremum, equality classification, and exact gap rely on the analytical proof in RESULT.md. No infinite-range computational certificate and no independent audit are claimed.
