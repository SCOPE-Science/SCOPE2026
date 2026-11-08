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
# Reproduction and limits

Run `python3 verify_brightness.py` from the extracted package directory using Python 3 and its standard library. The checker constructs the five three-dimensional vertices for each test height, projects them into a plane perpendicular to seeded unit directions, and computes convex hull areas using the monotone-chain algorithm in floating-point arithmetic. Independently it evaluates the Cauchy formula, all fifteen facet-plane pair cross-products, and all sixty-four possible signed normal sums for prescribed heights, including algebraic transition values. It compares these against the claimed three-piece minimum, two-piece maximum, and the sharp ratio at height \(3/4\).

Expected successful terminal markers are `BIPYRAMID_SHADOW_BOUNDS_CHECKS_PASSED` and `FULL_FACET_PAIR_AND_SIGN_VECTOR_CERTIFICATES_PASSED`. The test uses deterministic pseudorandom directions only for corroboration; the complete continuous-parameter proof is in `RESULT.md`. The checker is floating-point rather than a formal proof checker. Independent mathematical audit has not been performed.
