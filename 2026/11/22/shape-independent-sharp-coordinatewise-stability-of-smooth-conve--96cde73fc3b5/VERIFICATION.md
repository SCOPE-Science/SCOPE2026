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

# Mathematical verification
The exact bound follows by rewriting the firm nonexpansivity inequality as a Euclidean ball constraint on every projection secant. The weighted maximum norm and its weighted sum dual each have the stated upper bound. The tangent projector has the exact row-sum supremum, with an explicit unit normal and signed direction. For a smooth compact convex body, tangent-halfspace convergence at a supporting point with that normal proves the lower bound. Strict support and the smoothness of positive parallel bodies prove nonattainment and shape-discontinuity clauses.

Reproduction: run `python3 verify.py` using Python's standard library. It produces `PASS: 4228 supplementary checks; proof is analytic`. The tests use several fixed anisotropic ellipsoids, tangent-normal perturbations at diminishing scales, two-input inequalities in both weighted norms, and box clamping. Floating-point checks do not establish arbitrary convex-body statements or historical originality.
