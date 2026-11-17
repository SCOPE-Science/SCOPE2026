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
# Verification and scope

The standalone `artifacts/verify_paley.py` was run with Python 3 standard library and returned `EXACT_PALEY_AND_RADIAL_SOFT_THRESHOLD_WITNESS_CHECKS_PASS 21` for all prime moduli congruent to one modulo four through \(197\). Each test separately evaluates the spectral projection kernel as a direct sum of complex roots of unity and from the Legendre Gauss expression, every nonzero translated kernel chord, an arc maximizer, and a **finite two-input** radial-shrinkage witness. The DC response is compared modulo the constant mean.

The analytic proof covers all primes in the specified congruence class. Finite floating-point experiments are corroborative rather than an infinite proof; the exact Gauss sum and Legendre correlation identities, convex atomic decomposition, and the explicit soft-threshold ray construction are the decisive steps. The nonlinear Lipschitz upper constant is not asserted sharp. Historical priority beyond inspected sources is not certified. Independent mathematical audit has not been performed.
