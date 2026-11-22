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

The derivation is analytic and relies on a global maximization reduction, endpoint Taylor expansions, a nondegenerate quadratic maximum away from the cusp, and dominated convergence on a moving critical window. The standalone `verify.py` checks the actual parametric curve rather than relying on precomputed output. It uses standard-library `math`, `random` and `statistics` only, performs deterministic geometric checks and numerical area approximations, and exits nonzero on failure.

Computations are finite corroboration. They do not formally establish infinite quantifiers, the proof's global compactness step, absence of historical coverage, or total-variation convergence. The latter claims rest on explicit analysis in RESULT.md. The physical phase measure differs from arclength measure.
