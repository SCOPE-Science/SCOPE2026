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

Run `python checker.py` with Python 3.10+ (standard library only).

The program reconstructs every multiset of three vectors in \(\mathbb F_2^3\), including zeros and repetitions; exhaustively examines the \(5922\) full-rank unordered container pairs; verifies every expectation as an exact rational number by both subspace inversion and an independent observed-position Markov recursion; establishes the \(125/56\) minimum, all \(28\) unordered equality pairs and their geometric characterization; and checks the next-achievable value \(127/56\).

The program additionally checks the proposed survival law for each positive round through eight by exact history counting. The survival law for all rounds is proved symbolically in `RESULT.md`, rather than inferred from these finite checks. The proof's finite optimization has exactly \(5922\) feasible multisets to inspect, so the complete enumeration is an exhaustive proof of that finite component. Independent human mathematical validation has not been performed.
