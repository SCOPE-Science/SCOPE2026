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

# Reproducibility and limits

Execute `python3 verify.py` from the extracted artifact directory (Python 3 standard library only). The script ran successfully and reported `PASS 225 auxiliary checks`. It checks quadrature consistency for Gaussian and exponential correlations, the Gaussian derivative, strict comparisons against geometric alternatives to the optimum for 15 pairs of drift and overhead, overhead monotonicity, and both Gaussian asymptotics. The check of \(c=h=1\) returned \(T_h=1.378327080411\ldots\). The analytic proof, not these finite checks, establishes global uniqueness and asymptotic limits.

Validation is limited to the specified idealized matched-filter information-rate model. No empirical telescope data or external independent audit were used.
