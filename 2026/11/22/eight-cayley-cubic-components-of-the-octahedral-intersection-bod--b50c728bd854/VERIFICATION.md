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

# Reproducible checks

Run `python check.py` with Python 3, SymPy and NumPy. This test passed 320 assertions during preparation. It verifies exact algebraic identities (Laplace partial fractions and Cayley coordinate transform), exact factorization of all eight signed cubics, ordinary-node Hessian determinants, and independent polygonal plane-section areas for 160 seeded nonaxial normals and additional axis/boundary cases. The analytic argument in RESULT.md proves infinitely many directions; these finite tests are only consistency checks.

No independent audit, external certification, or machine-checked formal proof is claimed. The accessible primary texts and indexed scientific records were compared for the new result; priority may be affected by unindexed or uninspected supplementary material.
