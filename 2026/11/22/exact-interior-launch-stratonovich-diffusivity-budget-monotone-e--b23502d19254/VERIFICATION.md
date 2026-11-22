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

The self-contained `check.py` executes the exact symbolic factorization and rational identities for the cubic optimum, normalized minimum, strict gain derivative, budget split and both asymptotic constants. It then performs 11 independent bounded numerical optimizations and 330 random positive heterogeneous-profile comparisons at fixed average diffusivity. The program completed successfully on Python with SymPy and SciPy. A sampled comparison is not the infinite proof; the continuum proof uses strict Jensen convexity and the explicitly signed derivative.

The leading assumptions are dimension one, reflecting and absorbing endpoints, positive diffusion coefficients with a finite intrinsic length, a mean-diffusivity budget and the Stratonovich intrinsic-coordinate interface prescription. The exact optimizer is generally discontinuous; smooth profiles approximate it but do not attain it within the smooth-only class. No result about independent validation or independent audit is asserted.
