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

# Verification and reproduction

The theorem is proved analytically in `RESULT.md` through the stationary adjoint, a complete quadratic-form positivity criterion, and the regenerative resolvent. Its quantifiers include every finite dimension, every positive event rate, arbitrary probability reset laws, singular positive-semidefinite defects and boundary cases. The analytic argument, rather than any finite experiment, proves this universal claim.

To reproduce independent finite arithmetic checks, run `python verify_gaussian_reset.py` with SymPy 1.12 or newer. The program verifies 55 stationary-generator monomial identities, exact Gaussian normalization and first-two-moment calculations, factorization of the noncentral threshold density, characteristic-transform consistency, a genuinely noncommuting feasible covariance, and an anisotropic no-go covariance whose Lyapunov defect has determinant \(-17/16\).

Expected observed final output:

```
PASS: 55 exact polynomial stationarity identities; threshold 11/4; noncommuting threshold 85/21; indefinite defect -17/16.
```

The checks use exact rational operations, not simulation. They do not constitute exhaustive computation over all dimensions or all covariance matrices. No separate external scientific validation is claimed.
