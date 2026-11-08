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

Execute `python VERIFY.py` with Python 3.10+; no third-party modules are required. The extracted standalone exact-rational test script reports `VERIFY_OK 86 assertions; Q3 trees 384`.

The independent calculation paths are weighted Laplacian matrix-tree determinants on the cubes of dimension 3, 4, and 5; exhaustive spanning-tree enumeration on the three-dimensional cube; and direct Walsh spectral kernel evaluation in dimensions 3 through 10. All comparisons use integer or exact rational arithmetic. No numerical convergence experiment establishes the general identity: that proof is in RESULT.md. The checker does not test every dimension or resolve historical priority. No independent mathematical audit has been conducted.
