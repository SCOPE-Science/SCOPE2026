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

# Verification record

Run `python3 verify.py` with Python 3.9 or newer, using only the standard library. The verifier builds the candidate distribution from the **proved symbolic generating function** via formal polynomial recurrence and independently enumerates distinct valid subsequence strings by bit masks; it compares every coefficient by half-length for 18 finite source configurations over even alphabet sizes 2, 4, 6 and 8. A separate direct check covers 466 distinct symmetric hosts and confirms the general reflected-half-word lemma. Additional finite greedy-period tests cover several instances.

Expected terminal line: `VERIFY_OK configurations=18 masks=751506 symmetric_hosts=466 tests=histogram_greedy_half_spectrum`.

These finite experiments are not a proof of all parameters. The published proof derives the arbitrary-parameter weak-descent criterion, exact involution pairing, finite-state recurrence and formal power-series simplification. The verifier does not assert that equivalent earlier literature does not exist; independent scientific validation has not been performed.
