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

From a directory containing `verify.py`, run `python verify.py` with SymPy available. The checker solves the cubic and quintic center-manifold invariance equations over exact rational functions, normalizes with the left critical eigenfunctional, and confirms the reciprocal-clock coefficients symbolically. Three finite numerical trajectories, for \(b=1/10,1/4,1/2\), offer diagnostic sanity checks only. The proof of the infinite-iterate asymptotic is in `RESULT.md`, not in numerical iterations. No external independent audit has been performed.
