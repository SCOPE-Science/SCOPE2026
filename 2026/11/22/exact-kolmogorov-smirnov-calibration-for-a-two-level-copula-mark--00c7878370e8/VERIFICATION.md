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

The formulas are established by the analytic argument in `RESULT.md`. The optional standalone code `verify.py` uses Python 3, NumPy and SciPy and can be run as `python3 verify.py` from the extracted directory. This code checks block integration, stationary probabilities and eigenvalue; the equality between a normalized Green function and the integrated copula eigenfunction; the exact killed-Brownian-kernel quadrature against the independent Kolmogorov CDF; strict ordering at representative parameters; the limit toward the periodic case; and a seeded 3000-sample Monte Carlo comparison at sample length 1000. Its checks have finite tolerance and are not a certificate for the infinite-dimensional functional CLT, exact heat-kernel identity, or strict stochastic ordering. Those are proved separately.

The numerical integration uses an absolutely convergent sine-series heat kernel for strictly positive durations and barriers. At very small barriers, alternative series representations may be numerically preferable; the present reproduction only checks the displayed representative thresholds. The random Monte Carlo check is controlled by a fixed seed and a conservative acceptance tolerance. All assumptions on the stationary law, finite \(\alpha>0\), and exact known parameters remain essential.

No independent mathematical validation has been performed.
