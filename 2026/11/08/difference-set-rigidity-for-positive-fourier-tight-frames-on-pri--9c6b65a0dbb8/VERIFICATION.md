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

# Verification status and reproducibility

The mathematical proof invokes exact prime-order Fourier-minor nonsingularity (Chebotarev), convex Carathéodory compression, Cauchy–Davenport and Vosper. Each nonstandard input is named with its needed quantifiers in `RESULT.md`. Critical steps were checked: off-diagonal moment normalization, lower cardinality through a square subminor, upper cardinality through conjugate-symmetric real moments, full affine independence, and the saturated and small-prime cases. The sharp result is analytical and is not inferred from finite experiments.

The accompanying `CHECK.py` uses NumPy and SciPy to construct positive Fourier rules by linear programming and check their Gram matrices. It ran successfully with `CHECK_OK prime_sizes=[2,3,5,7,11,13,17,19] configurations= 436`. All nonempty spatial sets were tested at prime orders \(2,3,5,7\); systematic and sampled configurations were checked at the larger listed primes. Numerical tolerance is \(2\times10^{-8}\), so the numerical tests are not a symbolic or universal certificate. The published exact prime Fourier-minor and convexity theorems, not the solver, furnish the universal proof.

No independent mathematical audit was performed. The literature comparison is explicitly limited to inspected sources and recorded residual priority risks. The classification does not supply noise-condition bounds or rule out earlier equivalent results under different terminology.
