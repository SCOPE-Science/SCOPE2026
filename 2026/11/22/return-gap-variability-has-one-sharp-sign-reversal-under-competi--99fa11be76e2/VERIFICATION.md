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

# Verification of the return-gap sign law

The mathematical proof is in RESULT.md: strict convex order yields two positive Laplace-excess factors, and the expected-response difference is a positive fast exponential minus a positive slow exponential. Dividing by the slow exponential produces a strictly decreasing expression with exactly one real zero. The pair of gap distributions has equal first and second moments by explicit finite sums, but its exponential moments give opposite rational response differences.

The standalone Python-standard-library `checker.py` evaluates the exact finite sums as rational numbers; running `python3 checker.py` prints a PASS message. It checks support positivity, first two moments, four exponential excesses, both signs, and crossover thresholds. These checks support the finite witness only. The general convex-order assertion is not established by running code.

Limitations: only a nonnegative, two-exponential response index is proved; no empirical calibration, biological validation, external expert validation, or independent external audit has been performed. The theorem concerns two episodes with an exogenous random gap, not an arbitrary long event series.
