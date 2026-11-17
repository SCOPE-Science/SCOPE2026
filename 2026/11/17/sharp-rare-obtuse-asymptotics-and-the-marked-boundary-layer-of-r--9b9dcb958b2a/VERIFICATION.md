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

The file `verify_ball_obtuse.py` is standalone after installing NumPy and SciPy. It computes the Gram saddle determinant, inverse and Hessian, checks exact algebraic constants, samples 400,000 volume-uniform triangles in each of dimensions 2 and 3, and compares against the published acute probabilities. It then importance-integrates the exact finite-dimensional Gram density at dimension 10,000 using 250,000 independent weighted draws and the analytic beta-integral normalizer.

Observed diagnostics: `GRAM_DETERMINANT_HESSIAN_CONSTANT_OK`, `FINITE_DIMENSION_SANITY_OK`, and `EXACT_GRAM_IMPORTANCE_CHECK_OK`. The high-dimensional probability ratio to its predicted leading asymptotic was approximately \(1.07815\), with numerical importance-sampling relative standard error approximately \(0.00056\), consistent with a non-negligible pre-asymptotic correction. All numerical checks are finite and cannot certify an infinite-dimensional asymptotic claim.

The analytic proof includes: the exact Gram density, strict global determinant maximization under the obtuse linear constraint, full Hessian expansion, the active one-sided integrals, and the conditional-density convergence argument. No separate independent mathematical audit has been performed.
