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

The analytic reconstruction uses the two circulant periodic hat-function Gram symbols, the exact Fourier quotient of their cross Gram, and its fourth-order Taylor expansion. The uniform inequality \(1-\mu(\omega)\ge c\operatorname{dist}(\omega,2\pi\mathbb Z)^4\) provides the summable spectral tail needed to justify trace-norm, rather than just strong, convergence.

Run `python3 check.py` using only the Python standard library. It computes exact-rational hat overlap integrals, independently checks finite Fourier spectra and tests fourth-order scaling, with 236 finite assertions passed in the recorded run. Finite checks cannot prove the infinite-dimensional tail theorem. No independent validation has been performed. The 2019 successive-projection paper was available only by abstract and remains a specific literature risk.
