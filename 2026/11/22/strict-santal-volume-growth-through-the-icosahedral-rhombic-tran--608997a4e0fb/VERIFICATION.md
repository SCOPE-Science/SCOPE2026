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

# Verification of the exact polar-volume law

Run `python check.py` from this directory. The standard-library part computes rigorous rational bounds for radicals using integer square roots, checks strict lower-branch positivity, and proves decreasing positive derivative on the upper branch. It does not use approximations as inequalities. Optional SciPy/NumPy code computes both primal and polar hull volumes for ten parameter values to independently corroborate the formulas. Those samples are not substitutes for the analytic convex-geometric face decomposition valid for every real parameter in the claimed interval. The Santaló point is the origin by central symmetry. The source geometry is that of unit-norm icosahedral vertices and unit-norm dodecahedral facet normals.
