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

# Reproducible mathematical checks

Run `python3 artifacts/verify.py` with a standard Python 3 interpreter. The program independently enumerates all vertices for Cartesian-product pyramids over the standard triangle, unit square, and an off-origin translated triangle, for one through four product factors. It compares every covariance entry with the stated formula using exact rational arithmetic. It separately computes the volume second moments by direct beta-integral identities, rather than by reusing the rank-one covariance derivation.

Successful replay prints `PRODUCT_PYRAMID_DUAL_COVARIANCE_CHECKS_PASSED` with the profile, vertex, and entry counts. Tested code output: `matrices= 24 exact_entries= 984 enumerated_vertices= 592`.

The finite tests do not prove the universal dimension-asymptotic result. Its proof is the exact conditional covariance representation followed by the Schur-complement estimate given in RESULT.md; it covers any fixed full-dimensional convex polytope without integer-vertex restrictions. There is no claim of independent review or external certification.
