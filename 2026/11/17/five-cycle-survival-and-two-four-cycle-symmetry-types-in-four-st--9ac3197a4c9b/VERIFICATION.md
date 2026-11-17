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

The finite computational certificate enumerates all \(4^{10}=1{,}048{,}576\) labelled states. `verify_kneser.py` uses only Python standard-library modules, constructs Petersen adjacency from disjoint two-subsets, verifies \(F_1^{31}=F_1^{11}\) and \(F_2^5\equiv0\) on every state, classifies every first-entry time, and enumerates full \(S_5\) symmetry orbits of temporal cycles. `verify_outer_inner.cpp` independently constructs the graph from a five-cycle, five spokes and an inner pentagram, then uses indegree elimination on the complete functional graph to determine every initial state's entry time and eventual period.

To reproduce, run `python3 verify_kneser.py`, then `c++ -O2 -std=c++17 verify_outer_inner.cpp -o verify_outer_inner`, then `./verify_outer_inner 4 1` and `./verify_outer_inner 4 2`. Corresponding captured stdout appears in `check_kneser.txt` and `check_outer_inner.txt`. Both executions passed all assertions. Every count is finite and exact; no inference about other graphs or an infinite graph sequence is made. A separate independent mathematical audit is not included.
