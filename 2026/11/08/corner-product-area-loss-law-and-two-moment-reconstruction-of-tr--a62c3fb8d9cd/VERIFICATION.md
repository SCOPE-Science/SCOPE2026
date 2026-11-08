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

# Verification summary

Run `python3 VERIFY.py` with Python 3, NumPy, and SciPy. The deterministic computation reconstitutes convex-hull area directly from sampled planar coordinates and separately computes the predicted missing corner triangles. It also checks reconstruction of several scalene, isosceles, right, and equilateral triangles from exact-population limit formulas, and compares high-sample-size hull simulations against the independent-product-exponential predictions.

Observed output from the included executable:

`VERIFY_OK triangle_inversions=5 exact_cap_hull_identities= 480 scaled_area_trials= 6400`

For a repeated cubic root, numerical polynomial roots are inherently ill-conditioned; the code uses a loose numerical tolerance there while its analytic reconstruction follows Vieta's exact identities. All finite computations supplement, but do not certify, the asymptotic theorem. The finite-sample exceptional event and all fixed moment quantifiers are handled analytically in the proof. No independent audit has been performed.
