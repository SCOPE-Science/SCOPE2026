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

The accompanying `checker.py` is complete and uses only Python's standard library. Run it using `python checker.py`. At packaging, 82 independent checks passed: 44 exact Green-function versus finite-walk comparisons, 27 weighted inverse norms versus a separate degree-by-degree expansion, five saddle asymptotic log-error comparisons, and six large-saddle Gaussian-marginal comparisons. The finite-step tests use rapidly convergent regimes, not unproved exhaustive truncation claims.

For the infinite theorem, the proof in `RESULT.md` establishes the absolutely convergent inverse series, solves the Green recurrence, derives the unique positive saddle and proves Gaussian approximation and tail domination. It separately identifies the weak-limit statement and the fact that finite checks do not certify it in full generality.

All source comparisons, limitations and residual originality risks are disclosed in `AUDIT.json` and `REVIEW.md`. Independent mathematical audit has not been performed.
