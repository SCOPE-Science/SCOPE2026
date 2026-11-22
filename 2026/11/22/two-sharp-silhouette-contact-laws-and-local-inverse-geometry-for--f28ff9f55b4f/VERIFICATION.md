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

# Verification of the circular-frustum contact law

The proof and all assumptions are written in RESULT.md. From a directory containing the files, run `python3 checks/frustum_checker.py` using the Python standard library. The file includes no generated external data and is entirely standalone.

The checker independently constructs planar projected rim samples, takes their convex hull, compares direct polygonal area/perimeter against the analytical two-disk formulas at multiple tilt angles and six nondegenerate parameter sets, evaluates the support-function integral, checks both sharp \(3/2\)-power leading constants under decreasing angular offsets, and independently checks both dimension inverses. The replayed run reported `PASS: 156 independent finite analytic/convex-hull checks`.

These finite tests cannot establish global theorems for all real parameters. The continuum argument relies on the exact convex-hull characterization, Green's area integral, Cauchy's perimeter formula and uniform Taylor remainders for each fixed nondegenerate parameter triple. The available sources do not settle historical priority or external mathematical validation. The numerical checker has no claim to independent verification of the proof.
