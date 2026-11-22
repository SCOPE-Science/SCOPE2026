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

# Reproducible exact checks

Run the three Python 3 standard-library scripts `check_orbits.py`, `check_direct.py`, and `check_relations.py` in the same directory as `orbit_certificate.json`. The first exhausts the ten affine orbits of six-subsets in the ternary three-space and checks their ranks. The second independently enumerates all 296010 subsets and directly counts zeros at all 26 nontrivial characters. The third verifies all 106 admissible projective affine relations in dimension four, their balanced phase-word counts, the five-dimensional simplex count, and the dimension-uniform counting identity in dimensions two through eight.

The all-dimensional conclusion rests on the algebraic reduction to intrinsic affine dimension at most five. The programs use no floating-point tests, external inputs, internet access, or saved execution logs. These checks do not constitute an independent audit. They do not address arbitrary complex weights, noise stability, or historical priority beyond the cited comparisons.
