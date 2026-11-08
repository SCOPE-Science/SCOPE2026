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

The proof supplies the analytic verification: additivity of support functions; the exact Gaussian-radius identity; a joint independent upper/lower Poisson convergence; the stated Gaussian-hazard tail bounds for short windows; and the chi-square radius normalization. The point-process functional has finite moments of every order by the Gumbel shift of interval maxima and integration of \(|\log(t-s)|^p\) over the triangle.

Run `python3 verify_path_width.py`. This standalone Python 3 script uses only the standard library. Executed successfully, it returned `INTERVAL_ASSOCIAHEDRON_WIDTH_AND_POISSON_CHECKS_PASSED`. It tested all interval ranges for sample sizes 2 through 12 against an independent monotone-stack calculation; the exact segment width at size 2; the finite Poisson Cartesian-tree formula against midpoint quadrature for a fixed five-point configuration; and seeded Gaussian and truncated-Poisson simulations of the predicted scaling. The tested Gaussian size was 4500 (200 draws) and the Poisson cutoff was 5 (550 paired draws). The observed scaled Gaussian mean was approximately -1.002703 and the paired cutoff-Poisson mean approximately -0.861751, to be compared with the asymptotic mean \(\gamma-3/2\approx-0.9227843351\). Slow extreme-value convergence and finite-cutoff upward bias explain why these are not numerical equality tests.

This script neither verifies all input dimensions nor independently proves the infinite Poisson limit; the analytic truncation and uniform-integrability steps are necessary. The public artifact makes no claim of independent validation.
