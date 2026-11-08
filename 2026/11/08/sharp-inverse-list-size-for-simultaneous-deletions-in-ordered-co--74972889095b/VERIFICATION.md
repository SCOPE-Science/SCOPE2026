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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 and its standard library. The checker constructs all \(\binom{q+1}{2}^n\) valid two-row sources directly, deletes one symbol separately from each of their two rows, deduplicates outputs from different deletion positions, and counts all distinct sources for each received pair. It checks the exact optimum and the set of maximizing outputs, including cases where the received rows are not ordered.

Successfully executed complete tests for \(q=2\), lengths \(1\) through \(8\); \(q=3\), lengths \(1\) through \(5\); \(q=4\), lengths \(1\) through \(4\); and \(q=5,6\), lengths \(1\) through \(3\). All 23 tested instances passed, ending in `VERIFY_OK`.

The checker is an independent finite implementation of the channel definition, not a formal proof of the infinite-parameter assertion. The analytical induction, counting of one-insertion supersequences, and strict inequality establishing unique equality are provided in `RESULT.md`. No external or independent review has been performed.
