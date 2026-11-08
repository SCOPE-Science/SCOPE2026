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

Execute the standalone `verify.py` with Python 3. The program has no third-party dependencies. It recomputes the age variance both by exact expression and independent quadrature, checks the derivative, solves the monotone saddle with bisection, checks the strict derivative and concavity inequalities numerically, confirms both endpoint regimes, and directly quadratures the original stationary Gaussian age mixture at finite reset rates with zero and nonzero bounded deterministic propulsion.

The verifier additionally compares the exact deterministic-heading active/passive log-density contrast divided by \(\sqrt R\) with its analytical limit for both parallel and antiparallel headings. The strictly positive angular-diffusion formula is proved by Brownian path support and is not asserted to be certified by Monte Carlo. The numerical checks are evidence of internal consistency, not a substitute for the global analytical proof. In particular they cannot establish uniqueness or all-\(z\) assertions by themselves. At finite rate the active model has order-\(R^{-1/2}\) deviations at the sampled rare displacement; the numerical tolerance acknowledges this asymptotic speed. A fixed heading is a special case of independent bounded unit-vector orientation.

The exact identity for the integrated variance is \(F(u)=\int_0^u(1-e^{-s})^2ds\), and the exact passive stationary mean-square displacement is \(8D/[r(1+r\tau)(2+r\tau)]\). These supply independent normalization cross-checks. Every stated limit and positivity/uniqueness assertion is separately proved in RESULT.md.

**Limitations:** No independent audit; no finite-precision output should be interpreted as a rigorous infinite-domain certificate. Publication-priority assessment remains qualified because the passive saddle equation is pre-existing.
