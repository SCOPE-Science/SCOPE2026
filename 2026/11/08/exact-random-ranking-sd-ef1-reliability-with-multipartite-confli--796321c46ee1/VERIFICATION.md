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

# Mathematical verification and limits

Run `python3 verify.py` with Python 3 standard library only. The checker performs 71,110 direct existential-removal SD-EF1 comparisons, 181 fully enumerated assignment comparisons for the exact multipartite count, exhaustive bottom-set tests for seven small graph families at their worst-case thresholds, and exact integer hypergeometric probability evaluations for balanced bipartite graphs of sizes 100, 400 and 1600 on each side. The script reports `ALL CHECKS PASSED`. The comparisons are finite; the written bijection argument and classical hypergeometric CLT independently establish the general statements.

Checks do not independently establish publication novelty, formal certification, or arbitrary heterogeneous-preference cases.
