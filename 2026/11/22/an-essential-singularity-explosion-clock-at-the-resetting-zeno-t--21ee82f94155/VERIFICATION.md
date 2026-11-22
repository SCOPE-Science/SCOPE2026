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

# Verification of the resetting-Zeno accumulation clock

The analytic proof is in `RESULT.md`. `verification/check.py` is standalone Python 3 code requiring only the standard library. Invoke `python verification/check.py` from the extracted package root.

Executed checks: 208 equality comparisons of independently computed finite-depth exact rational mean times, for terminal depths 1 through 26 and multiple rational reset strengths, acceleration ratios and integer power exponents. The critical binomial generating identity was also tested. Near-critical numerical ratios at reset-hazard exponents \(1.3,1.15,1.08,1.04,1.02\) are approximately \(0.994117544,0.993813326,0.995540903,0.997363977,0.998567482\), respectively, relative to the asymptotic formula at \(c=0.4\), \(r=0.55\), \(\tau=1\).

The finite-depth computations and approximate special-function evaluations are independent consistency checks only. The almost-sure dichotomy, exact infinite-depth expectation, amplitude and weak limit depend on the analytic infinite-product, renewal, Gamma-series and Laplace arguments in the proof. There has been no independent external audit.
