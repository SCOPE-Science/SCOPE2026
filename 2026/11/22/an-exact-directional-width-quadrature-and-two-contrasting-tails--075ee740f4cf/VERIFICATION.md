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

# Reproducible mathematical checks

From the extracted artifact directory, with Python 3, NumPy and SciPy installed, execute `python check_tricylinder_width.py`. The expected success line is `TRICYLINDER_WIDTH_CHECKS_OK 251`.

The program compares the exact piecewise support value to 180 independent constrained SLSQP maximizations over all three quadratic cylinder inequalities, checks the complete one-dimensional CDF against 262,144 deterministic-seed scrambled Sobol uniform sphere directions, tests nine exact spherical-cap upper-tail thresholds, verifies a further 50 support bounds, and prints low-tail logarithmic convergence ratios. The numerical tolerances reflect quadrature and sampling rather than an infinite certificate.

The proof in RESULT.md, not this test file, establishes all angular and asymptotic identities for infinitely many directions. Independent audit has not been performed. Materially unreadable earlier historical literature remains a priority risk.
