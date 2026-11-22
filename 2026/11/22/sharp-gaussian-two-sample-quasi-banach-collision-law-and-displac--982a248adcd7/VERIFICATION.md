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

The proof directly inverts the two-site Gaussian Gram matrix, obtains a uniform global tail bound after scaling by the separation, and applies a local second-order analytic expansion and strict concavity at the limiting maxima. Those steps establish the all-real-line supremum and two-point extremizer uniqueness for sufficiently small positive separation.

The supplementary script `gaussian_collision_check.py` uses only standard Python and verifies 16,272 numerical assertions for selected exponents and separations, including direct matrix identities, local maximizations and finite evaluation grids. It is not an exhaustive certificate for a continuum or an asymptotic proof. No independent audit has been conducted.
