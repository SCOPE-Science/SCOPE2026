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

# Verification record

The exact operator factorization follows from the Poisson semigroup multiplier \(s^\ell\) and the degree \(\ell\pm1\) coordinate selection rule. Bounded coordinate multiplication has essential spectrum \([-1,1]\), giving the analytic sharp cutoff on all finite configurations. The endpoint weight is positive except at a measure-zero pole; injectivity on every spherical harmonic gives integral strict positivity and \(C(S^d)\)-universality. The zonal Jacobi characteristic polynomial is Legendre, with magnetic-order comparison establishing the finite-band threshold on \(S^2\).

Reproduce finite algebraic and quadrature checks with the exact embedded file `CHECKER.py` using `python3 CHECKER.py` (Python 3 standard library). Expected: `PASS: 28 rational Legendre/Jacobi/witness checks; 4 Poisson factorization quadratures`. The rational negative supercritical test equals \(-1/80\) and does not rely on floating-point data. Quadratures corroborate four fixed parameter pairs; they do not establish the all-dimensions analytic theorem.

Full texts of the motivating 2026 deformation manuscript and a related 2024 axial spherical covariance study could not be inspected, leaving a substantive priority-comparison risk. This verification is not independent or external certification.
