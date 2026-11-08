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

# Reproducible finite checks

Run `python verification.py` with Python 3.9 or newer. No third-party libraries, network access, auxiliary data, or hidden state are required. The checker lists all vertices of each polar factor, takes Cartesian products, tests the sharp norm bound, computes exact rational ranks of farthest polar-vertex normal matrices, checks every corner of each predicted incenter box with 62-decimal-digit precision, and counts exactly the tangent facets at those corners.

The completed checker run returned:

`LAYERED_TWINNED_INCENTER_CHECKS_PASSED profiles= 27 polar_vertices= 7210 incenter_corners= 121`

The finite verification does **not** establish the theorem for arbitrary positive layer sizes. The universal claims rely on the analytic arguments about polar vertex sets and strict convexity in `RESULT.md`. An additional separate numerical linear-program check of thirteen profiles agreed with the radius and tangent-normal rank predictions; that LP is not needed to reproduce the standalone checks.
