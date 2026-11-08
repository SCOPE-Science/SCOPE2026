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

# Verification

Run `python3 check_ladder.py` from this directory; no nonstandard Python packages are required. The executable builds rational vertex Laplacian pseudoinverses and uses independent exact integration of the effective resistance on each ordered pair of unit edges. It checks the maximizing edge set and the closed squared constant for every integer from 2 through 9. The known degenerate four-edge-circle boundary at the smallest size is checked for the value, while the nondegenerate cases are checked for exactly two strict midpoint maximizers.

A completed run printed `EXACT_RATIONAL_LADDER_GREEN_CHECKS_PASSED 8 sizes, all edges, all edge pairs`. In particular, squared sharp constants were `307/588` and `419/600` for the three- and four-rung ladders. The checker is a finite diagnostic, not a proof for all integer sizes.

The universal proof is the resistance-polarization identity, edgewise Brownian-bridge integral, strict vertex-potential ordering from the path resolvent, comparison with end rails, and independent Gaussian centering computation. The closed-form gap is positive because each end rung has resistance at most 3/4, and hence its edge quadratic is strictly concave for three or more rungs. Exact equality cases follow from the Riesz representer in the mean-zero energy Hilbert space.

No independent mathematical audit or external certification has occurred. The 2014 Carmona–Encinas–Mitjana full text was not available for material comparison, and bibliographic priority therefore remains qualified.
