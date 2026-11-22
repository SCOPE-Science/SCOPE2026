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

Run `python3 checker.py` with standard Python 3. The package was checked using exact rational finite-distribution transitions, the imbalance second moment and its analytic recursion, selected two-time correlations computed independently with an augmented state, and the monotone sign classification through finite ages. The reproduced checker printed `PASS: 470 exact rational assertions and finite distributions`.

The infinite-age claims are derived in `RESULT.md` from a scalar recurrence, strict positivity of its gamma product, the exact sign numerator and a locally uniform gamma-ratio asymptotic. Finite tests cannot independently validate an infinite limit. The reported originality review is based on identified literature comparisons, not on a proof of global priority. Independent audit: not performed.
