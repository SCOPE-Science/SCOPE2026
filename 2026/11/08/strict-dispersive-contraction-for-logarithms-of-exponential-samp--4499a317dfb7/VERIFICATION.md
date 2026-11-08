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

# Verification

The probability law has exactly the stated cumulative distribution function; for integer sample size it is obtained by independence of the exponentials. The quantile is explicitly inverted. Critical proof points are the derivative identity, the strictly increasing integral kernel \(g\), the strict quantile derivative comparison, and the strict integrated-quantile inequality for centered variables. All boundaries are interior in \(u\), with positive real shape parameters. Moments exist because of the exponential left tail and double-exponential right tail.

The accompanying `checker.py` uses only Python's standard library. It checks independent cdf/quantile inversion, analytic-versus-finite-difference derivatives, sample-size monotone derivatives, and every pairwise spacing inequality on a finite parameter grid. Reproduce with `python3 checker.py`; output includes the verified diagnostic count. Numerical diagnostics are not infinite proofs; the mathematical argument establishes the result for all parameters.

The source comparison explicitly excludes integer-sample variance monotonicity from the new contribution; the more general distributional order remains subject to independent literature validation. No independent audit was performed.
