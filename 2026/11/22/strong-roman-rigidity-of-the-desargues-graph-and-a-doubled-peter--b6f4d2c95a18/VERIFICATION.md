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

The supplied `verify.cpp` exhausts all weight-fourteen strong Roman assignments using the analytically forced four label-multiplicity profiles. Its exact search checks 7,441,920 assignments, finds 40 feasible labelings, and reconstructs the doubled Petersen subdivision and its distances. The separate `verify_geometry.py` generates 40 feasible configurations from two explicit representatives under all 120 permutations of the five-element ground set and independently checks the 60 exchange edges, vertex-degree pattern, radius and diameter. Both were executed successfully from their actual paths before packaging.

The analytic lower bound excludes all weights below fourteen. The exhaustive search excludes weight-fourteen solutions outside the listed 40. These are ordinary finite computations and not a general theorem about arbitrary cubic graphs. No independent external validation has been performed.
