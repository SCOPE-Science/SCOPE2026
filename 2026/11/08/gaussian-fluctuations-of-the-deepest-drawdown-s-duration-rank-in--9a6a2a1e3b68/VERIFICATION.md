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

## Finite reproducibility

From the folder containing this document, run `python3 verify.py`. It checks \(424\) assertions using only Python's standard library. Exact rational dynamic programming computes first-return probabilities, exact rational tridiagonal systems produce bounded hitting transforms, and both are compared with their independently derived formulas. The final analytic derivatives are also checked by numerical finite differences for specified fixed probabilities.

## Infinite argument and limits

The proof of the rank law is not delegated to the checker. Its nonstandard ingredients are the explicit bivariate generating function for exact excursion depth/duration; its analytic quasi-power expansion; tight extreme-height centering; and *uniform*, rather than selected-threshold-conditional, binomial concentration of duration counts across \(O(\log n)\) possible duration thresholds. The distinction is essential because depth selection and duration are dependent. The proof assumes fixed \(1/2<p<1\), completed nonzero excursions, and integer-even durations. No independent mathematical audit is recorded.
