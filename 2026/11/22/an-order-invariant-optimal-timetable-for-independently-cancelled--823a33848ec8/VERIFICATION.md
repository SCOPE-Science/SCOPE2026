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

## Reproducibility

Run `python check_reliability.py` with Python 3 standard library. The script constructs the exact rational active-block quadratic form from all Bernoulli cancellation patterns. It verifies exact stationarity, the exact minimum, strict positive perturbation costs, and invariance of the optimized value across all 12 distinct cyclic orderings of an illustrative four-service reliability multiset. It also checks configurations through seven services. It prints `VERIFIED 21 full exact rational configurations` and `ALL EXACT CHECKS PASSED` on completion.

## Mathematical verification and limits

The proof is independent of floating-point output. The identities needed for arbitrary service count are the quadratic active-block representation, independent endpoint-extension recurrences, and the positive-definite all-success contribution. The finite tester does not verify every number of services or arbitrary real reliabilities. The model excludes capacity limits, delays, correlated cancellations, and passenger anticipation. No independent scientific audit is claimed.
