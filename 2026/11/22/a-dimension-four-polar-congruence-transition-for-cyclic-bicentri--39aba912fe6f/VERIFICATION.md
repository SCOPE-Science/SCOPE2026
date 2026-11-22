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

# Reproduction

Run `python check.py` with Python and NumPy. The test reconstructs vertex Gram matrices and facet normals, verifies both reciprocal configurations, tests the determinant formula, and checks the four-dimensional vertex permutation. Tests are sampled in finitely many dimensions/parameters, not an exhaustive proof. The all-dimensional proof is in `RESULT.md`.
