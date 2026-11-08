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

The proof in `RESULT.md` supplies the all-parameter argument. `verify_cross_skeleton.py` performs supplementary exact rational checks with only standard Python modules. Run `python verify_cross_skeleton.py` from the extracted package directory. It enumerates all coordinate supports for \(2\le d\le7\) and \(1\le s\le d\), compares independent face-distance and sorted-distance implementations, tests explicit rational holes below each threshold, and tests points on and inside the expanded cross-polytope at the sharp parameter.

Expected exact successful output begins with `CROSS_SKELETON_EXACT_OK` and records `support_distances: 2025`, `sharp_obstructions: 27`, `coverage_samples: 9450`, and `boundary_cases: 27`, totaling 11,529 assertions.

These are finite arithmetic checks. They do not establish the infinite theorem; steps 1–4 in the result give the exact proof. No independent mathematical audit has occurred, and novelty is historically provisional.
