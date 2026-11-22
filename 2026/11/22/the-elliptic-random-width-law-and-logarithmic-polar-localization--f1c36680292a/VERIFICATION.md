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

The companion Python checker compares the support formula against the exact square-section optimizer, verifies the elliptic-density formula against the original product-integral representation, integrates the probability density, and runs fixed-seed independent spherical Monte Carlo comparisons. The proof in `RESULT.md`, not the simulation, establishes the identity and conditional limit. The complete elliptic integral in the formulas uses the modulus, while SciPy `ellipk` uses the squared modulus. Comparison tolerances are included in the checker.

Scientific limitations: no assertion for unequal-radius bicylinders, a non-right crossing angle, or random boundary-chord sampling. An independent mathematical audit has not been performed.
