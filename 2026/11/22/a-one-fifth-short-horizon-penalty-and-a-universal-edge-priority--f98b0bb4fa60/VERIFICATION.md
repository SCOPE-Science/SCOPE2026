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

# Reproducibility and proof boundary

Run `python3 verify.py` from the directory containing the extracted files. Python 3 with NumPy, SciPy and SymPy is required. A recorded execution returned `PASS 1157 finite checks`; finite exact and numerical checks cover the tridiagonal short-time equations, the closed-form radical expression, strict first-neighbor priority reversal, the budget, exact full spectra on small paths, direct centered-vector eigenrelations, finite-horizon numerical minimization, and convergence of the quadratic ratio toward \(6/5\).

The infinite-family result rests on the proof in `RESULT.md`: strict Hessian positivity for the spectral exponential trace; a uniform Taylor expansion on a compact simplex; a positive definite quadratic program with an exact recurrence solution; a Rayleigh upper bound; an exact polynomial-basis eigenvalue computation for the parabolic edge profile; uniqueness of equality; and a compactness argument for the large-horizon optimizer. Numerical minimization at extremely long horizons can be unreliable because nonconstant heat modes underflow; the analytical asymptotic argument does not use such numerical runs.

The new theorem has had self-review only. Independent mathematical audit and external validation have not been performed. Originality is qualified by inaccessible or unindexed potential equivalents.
