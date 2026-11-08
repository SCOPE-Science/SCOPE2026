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

The algebraic proof applies to every real \(c>0\) and \(\mu>0\). Two exhaustive first-event equations on the reachable configurations, together with neutral-label and endpoint-reflection symmetries, give the exact absorbing probability. The sign of a single numerator gives the unique phase boundary and all equality cases.

`checker.py` uses only the Python standard library. Its independent full-state enumeration includes all \(12\) configurations containing both species and solves their linear first-extinction equations by exact rational elimination. It checks \(81\) distinct positive rational parameter pairs, three placement probabilities at each pair, and the strict/tie classification; it also checks three specific examples. The checker does not establish arbitrary-real identities on its own. There are no simulated infinite-time survival claims or extrapolations to longer graphs.

Self-review: passed. Independent audit: not yet performed.
