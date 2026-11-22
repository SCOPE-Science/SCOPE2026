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

# Direct verification and limits

The mathematical proof and all stated parameter restrictions are in RESULT.md. Run `python verify.py` using Python 3 and NumPy to rebuild each tested path Laplacian and added-link Laplacian, check the rank-one and spectral-moment identities, evaluate long-time traces, and compare best second-positive centered chords at increasing orders.

A local replay returned `VERIFY_OK 6227 finite numeric/integer consistency checks`. The matrix checks use floating-point eigensolvers and verify finitely many graph orders. They are not an exhaustive certificate of the infinite theorem or of a unique finite-time crossover. The analytic recurrence, inertia, and continuum variational arguments supply the proofs for all claimed indices.

Independent mathematical audit has not been performed.
