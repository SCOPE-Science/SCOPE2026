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

The standard-library program `verification/check_heat_bv.py` was run from its embedded source file. It independently computes the wrapped-Gaussian and Fourier heat kernels and their antipodal variation coefficient, samples nonantipodal displacements, evaluates 105 random signed zero-mass Jordan mixtures, and checks representative strict semigroup, small-time Gaussian-tail and long-time Fourier expansions.

Passing output concludes with `ALL_CIRCLE_HEAT_BV_CHECKS_PASS`.

The program uses finite floating-point quadrature and sampling. It does **not** certify global inequalities, all angular shifts, all real BV inputs or infinite-series identities; those depend on the explicit analytical proof in RESULT.md. No independent external audit was performed.
