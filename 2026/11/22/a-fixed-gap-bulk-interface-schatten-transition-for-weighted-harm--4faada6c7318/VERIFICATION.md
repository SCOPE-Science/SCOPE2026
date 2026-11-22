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

# Reproducibility and limits

Run `python3 CHECKER.py` with Python 3 and the standard library. The program tests each Toeplitz factor separately on signed harmonic Fourier basis modes, derives the two-product difference without using the asserted three-branch formula, compares both results across four weight parameters and all finite indices in the displayed ranges, checks reflection antisymmetry, and samples the fixed-interface gamma scaling and leading norm constant. The recorded output was `NEAR_DIAGONAL_HARMONIC_BERGMAN_DIAGNOSTIC_OK 88784`.

The actual limiting proof is analytic: moment identities, digamma bounds, microscopic gamma limit, Riemann-sum estimates, and dominated convergence. The finite test is neither exhaustive over \(n,d,\beta,p\) nor an independent verification of the infinite claims. The upper-regime gamma series is convergent only when \(p>1/(1-\beta)\), while the critical logarithm is proved separately. The source date is the first arXiv posting, not the later revision date.
