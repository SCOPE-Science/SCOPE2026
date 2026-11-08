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

Run `python3 verify_friendship.py` in the artifact folder to reconstruct and verify every entry of `state_certificate.csv` from the six-type transition map and to rederive the ten exact exponential-polynomial formulas. `proof_log.txt` records `PROOF_CHECK_OK` and the hash of the complete 189-state certificate.

Run `python3 check_graph.py` to evolve all labelled graph configurations for five values of the petal parameter, including exactly 199,287 initial states in total; `graph_log.txt` records `BRUTE_FORCE_OK 199287`. The second checker uses explicit graph adjacency lists rather than the support-state recurrence.

The infinite-family assertion rests on the exact six-type quotient, the ordered-lift verification for every recurrent quotient state, and symbolic inclusion–exclusion, not numerical extrapolation. Other update rules and graph families are unproved. No independent audit has been performed.
