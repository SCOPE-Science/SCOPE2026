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

# Reproduction and limits

The self-contained `verify.py` file runs with Python 3 standard-library modules only. It checks direct Gaussian-autocorrelation quadratures against the closed formula, brackets and solves fixed- and full-template stationary equations, tests unique-peak implications on supplied grids, and evaluates both overhead asymptotic laws and the limiting information ratio. The observed execution passed **3,561 numerical assertions**. It printed `0.989939082841904` for the dimensionless limiting duration and `0.629396379324979` for the fixed-to-matched limiting information ratio. At \(\beta=0.0005\) inverse seconds and \(h=14\) seconds, the computed durations were 343.9137776 and 346.2406090 seconds.

The analytic proof in `RESULT.md`, not the floating-point code, establishes uniqueness, strictness and asymptotics for all positive parameters. The checker is supplementary and does not validate astronomical instrumentation, data-processing pipelines or historical originality. No external independent audit was performed.
