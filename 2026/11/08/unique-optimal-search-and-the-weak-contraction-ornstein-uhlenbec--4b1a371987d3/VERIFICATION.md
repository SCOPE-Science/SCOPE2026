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

The result is a paper-and-pencil theorem starting from the published finite-\(a\) series. Its nonstandard analytic steps are the \(q\)-gamma product limit, a uniform entire-series majorization, positivity of the derivative-sign function, and non-escape of optimal scaled rates. These steps are written with explicit hypotheses and coefficients in `RESULT.md`.

Run `python checker.py` with Python 3 and `mpmath` installed. The script evaluates finite-multiplier and limiting series to 55-digit working precision, tests the complete-reset special case against \(e^\beta-1\), locates scalar stationary points by bisection, checks the derivative and nearby objective values, and compares the limit series with independent Gaussian quadrature. The performed run reported 33 passed numerical assertions and the constants shown in `RESULT.md`.

The numerical diagnostics only sample finite parameters. The asserted uniqueness and convergence over infinite domains rest on the analytic proof. No machine-checked formal proof, rigorous rounding interval, or external independent scientific audit is claimed.
