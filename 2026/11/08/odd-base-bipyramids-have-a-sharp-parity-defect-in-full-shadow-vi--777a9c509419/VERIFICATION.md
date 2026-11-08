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
# Reproducible verification

Use `python verify_odd_bipyramid.py` with Python 3 standard library. The script checks the full-vertex formula for three odd base orders and three height choices by independently numerically integrating the polar Cauchy shell probabilities; it reconstructs planar convex hulls for thousands of independently generated planar apex pairs, verifies support-inequality classification for those samples, compares deterministic Monte Carlo frequencies with analytic probabilities, and checks optimizing-height bounds and a large-order asymptotic value. The completed run emitted `ALL_ODD_BIPYRAMID_SILHOUETTE_CHECKS_PASSED`.

The program tests finitely many cases and is not a formal or exhaustive verification. Universal claims, exact normalization, all-height endpoint limits, optimizer brackets and asymptotic constants rest on the proof in RESULT.md. In particular, finite-order uniqueness of an optimizer is not asserted, and external independent review has not occurred.
