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

The companion `verification.py` compares piecewise exact integration of \(a^2T_{n,a}\) against an independent adaptive-quadrature implementation over multiple finite positive samples. It also compares the exact Dirichlet second-moment formula with Monte Carlo estimates at several sample sizes and weights, and checks the algebraic Brownian/Poisson moment identities. The reported run passed 71 assertions with a fixed pseudorandom seed.

The mathematical proof, not simulation, establishes the weak limits and the non-uniform-integrability effect. The moment formula uses exactly normalized exponentials \(Y_i=X_i/\overline X_n\); no iid assumption is imposed on those normalized coordinates. The Poisson process functional is defined for every \(c>0\), the Brownian regime requires \(a_n/n\to0\), and the supercritical expectation is a separate calculation not inferred from convergence in probability. Review and external validation statuses are not interchangeable.
