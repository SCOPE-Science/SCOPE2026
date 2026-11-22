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

# Verification of phase-resolved survival asymptotics

The mathematical verification is an analytic proof, not an inference from finite experiments. The main steps are: an exact killed-walk sine spectral identity, independent block-Laplace factorization, a small-frequency concentration estimate for each fixed initial site, a Gamma-moment calculation for the limiting phase ratio, and a monotonicity squeeze establishing uniformity in phase. The strictly positive cusp coefficient uses the fractional Bernstein integral rather than an invalid pointwise positivity assumption for a sign-changing spectral weight. The finite left derivative follows from \(s|\varphi'(s)|\le1-\varphi(s)\); the right slope diverges only for \(0<\alpha<1\).

Running `python3 check.py` alongside the files passed 193 deterministic assertions with NumPy and SciPy. Checks included the independent Bessel survival formula for deterministic rates; exact sine-integral finite-time survival for Mittag–Leffler, positive-stable, mixed and exponential rate transforms; phase contrasts for several sites and phase fractions; direct finite-redraw fractional cusp coefficients; the unique minimum at phase \(1/4\) when \(\alpha=1/2\); and monotonicity within each redraw interval. All numerical tests are finite and do not prove the asymptotic uniform limit, cusp positivity for every rate law, or originality.

No claim is made about a noise-robust inverse procedure, random renewal redraw schedules, a drifted walker or the finite-interval model. Published formulas were used as mathematical antecedents and their content is not represented as an independently established new derivation. Independent scientific audit remains unperformed.
