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

# Checks and reproducibility

The formulae in `RESULT.md` were checked by differentiating \((H-1)H'=\lambda(H/z-1)\) exactly. With \(Y=H''\), \((1-H)Y'=B-AY\), where \(A=\lambda/z-3H'\) and \(B=2\lambda z^{-2}(H'-H/z)\). Their endpoint values are \(\lambda-3m\) and \(2\lambda(m-1)\), respectively, and \(1-H\sim m(1-z)\). Positivity of \(H'''\) is the crucial sign constraint. No numerical data is used to infer moment finiteness or the infinite-series asymptotics.

For direct computational spot checks, run `python verify.py`. This uses the exact given recurrence with rational arithmetic for 32 coefficients, then double-precision convolution for a finite prefix at three rates on both sides of the threshold. It verifies positivity and finite recurrence residuals, reports finite partial moments, and compares the observed finite-branch partial third moment to its infinite-limit prediction. Dependencies: Python 3 and NumPy. Failure of a finite-prefix test is not a proof that an infinite moment does or does not exist; numerical truncation and floating-point rounding are scientific limitations.

The logarithmic transfer uses the classical positive-coefficient index-zero Hardy–Littlewood–Karamata Tauberian theorem, applied to the nonnegative sequence \((k^3-k^2)n_k\), not a numerical fit. No independent audit or external proof certification is claimed.
