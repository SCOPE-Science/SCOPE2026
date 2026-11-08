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

# Reproducibility and verification

Execute `python3 verify.py` with Python 3.9+ using the standard library only. The verified output from the package is `VERIFY_OK 5540`.

The checks compute rational polynomials \(Q_q\) for \(1\le q\le8\), and for each check their value at zero, all \(q\) orthogonality equations, exact \(L^2\) and \(L^4\) arcsine moments and the two derived variance expressions. They also check a Dirichlet/Chebyshev identity on a fixed grid, solve small full finite-dimensional GMRES projection systems to test exact odd-step stagnation, and compare finite Toeplitz trace quadratures to their limit. Seeded Gaussian Monte Carlo tests only check rough scale consistency for small fixed iteration counts.

The proof's essential infinite-dimensional steps are not experimentally certified. They are: the Toeplitz spectral Riemann-sum limit, the real-Haar ratio-of-quadratic-forms central limit theorem, and the \(O_{\mathbb P}(N^{-1})\) residual minimization remainder. The analytic argument is supplied in `RESULT.md`. No independent validation has been performed.
