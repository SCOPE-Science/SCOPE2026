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

# Verification and reproducibility

The supplied `checker.py` uses only the Python 3 standard library. Running `python3 checker.py` verifies exact Legendre recurrence integrals, exact parity relations, explicit negative neighboring-degree compression eigenvalues for ordinary spherical heat, and numerical stress tests of the fractional spectral-order transition. It reports 249 assertions across exact and numerical checks. The exact rational assertions test stated identities; numerical checks validate examples but do not establish universal quantifiers.

The optional `finite_gram_check.py` requires NumPy and reconstructs finite-site covariance matrices on 64 equally spaced circle points from a converged Fourier series. For \(a=1\), \(v\) of magnitude \(0.3\), \(t=2\), \(\alpha=0.75\), the matrix is indefinite despite all diagonal entries being positive. The same holds for \(a=1\), \(\|v\|=0.2\), \(t=0.5\), \(\alpha=1\). These computations support, but are not the basis of, the theorem.

The infinite-dimensional proof is self-contained in `RESULT.md`. It uses uniform absolute convergence of the strictly positive harmonic spectrum; the equivalence of finite-site positivity and smooth integral quadratic forms for continuous kernels; the harmonic degree selection rule for multiplication by a coordinate; a normalized adjacent-degree Jacobi operator; zonal Gegenbauer recurrence coefficients; and concavity/asymptotics of the fractional spectral gaps. The exact norm \(\rho_{d,t,\alpha}\) is specified mathematically and need not be computed numerically for the classification. No independent validation has been performed.
