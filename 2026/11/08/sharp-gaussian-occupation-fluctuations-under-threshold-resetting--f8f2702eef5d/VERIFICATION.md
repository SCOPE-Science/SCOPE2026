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

The theorem is established by Brownian time change, killed Green kernels, an explicit Poisson-equation solution, Itô isometry, and a regenerative renewal-reward CLT. These steps cover all real sluggishness exponents \(\alpha\ge0\), thresholds \(L>0\), and reset fractions \(0\le\rho<1\). The boundary case \(\alpha=0\), where ordinary Brownian diffusion is recovered, is included.

Run `python checker.py` with the Python standard library. The included executable makes 300 checks. Forty-nine integer-exponent/rational-position combinations use exact rational arithmetic to test the mean excursion clock, positive occupation mean, equality of independent centered second-moment and Dirichlet-energy formulas, and positivity. It also checks the rational symmetric formula, matched-frequency ratio, and inequalities. Noninteger exponents use separate piecewise quadratures; discrete killed-chain approximations solve three tridiagonal systems without using the continuum integral as input. The last step confirms observed convergence within declared mesh tolerances. The checker printed `PASS: 300 exact rational / independent finite-difference assertions` in the delivered version.

Proof and code do not establish finite-time rates, arbitrary-duration resets, or equivalence of the spatial stationary distributions under the two protocols. The numerical experiments are not an infinite-state proof. Publication priority and independent external validation remain unperformed.
