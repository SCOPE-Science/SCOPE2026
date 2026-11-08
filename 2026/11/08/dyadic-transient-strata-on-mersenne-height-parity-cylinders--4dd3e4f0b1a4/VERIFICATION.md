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

# Verification notes

All programs require Python 3 and only its standard library. Execute `python3 check_grid_ranks.py`, `python3 check_local_algebra.py`, and `python3 check_census.py`; each prints a PASS line or raises an exception on disagreement. The captured stdout files correspond to these commands. The direct grid checks compare binary adjacency power ranks with the closed partition; the quotient-ring checks use a distinct monomial encoding; the finite full-state census computes the periodic basin and each entrance time by removing indegree-zero states. All three are bounded tests. The all-parameter statement is derived in RESULT.md, not extrapolated from test ranges. No independent audit is claimed.
