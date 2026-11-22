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

## Reproduction

Execute `python checker.py` using Python with NumPy and SciPy. It tests the exact determinant identity against matrix computations, the rank-null radius and its sign transition for representative parameters, and an illustrative two-branch tie. A successful execution prints `diagnostic_checks_passed 323` and a numerical equal-height example.

## Scope of verification

The checker is finite and numerical, and does not prove infinite-domain statements, uniqueness of the rank-defect radius, or existence of an exact equal-height parameter. Those facts follow from the separate analytic proof and continuity argument in RESULT.md. The illustrative decimal root is not an interval certificate or a uniqueness result. No experimental validation and no independent audit are claimed.
