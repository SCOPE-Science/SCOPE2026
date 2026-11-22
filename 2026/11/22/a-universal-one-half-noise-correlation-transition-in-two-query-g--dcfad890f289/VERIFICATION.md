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

# Verification and limits

`verify.py` (Python 3, standard library and SymPy) reproduces symbolic identities for the correlated-noise Gaussian conditional variance and the finite Brownian-bridge benchmarks, the exact vertex comparison and the rational witness. It also checks 501 rational reflected-pair configurations and 1,200 fixed-seed rational covariance configurations against the proved uniform matrix-resolvent estimate. These finite computations do not establish an all-grid or all-parameter proof; the mathematical arguments are in `RESULT.md`. The exact checker was executed successfully on the included source.

The theorem requires \(\eta>0\) and fixed \(-1<\rho<1\), a compact observation domain, a continuous positive-semidefinite kernel, and a nonnegative target cross-covariance reaching a unique positive maximum and having at least one zero. The correlation \(\rho=1/2\) is an unresolved leading-order tie rather than a claimed unique geometric limit; no complete finite-noise global optimum is reported. Published-source comparison cannot establish historical uniqueness, and independent mathematical validation has not been performed.
