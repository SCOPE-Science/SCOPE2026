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

# Exact finite verification

Run `python3 verify_closure.py`; separately compile `verify_gp.cpp` with `g++ -O2 -std=c++17 verify_gp.cpp -o verify_gp` and execute `./verify_gp`. Both programs were run locally with assertions enabled, and their actual outputs are supplied in `closure_output.txt` and `gp_output.txt`. The first enumerates exactly 1024 subsets of the ten edges of \(K_5\) and checks the necessary-and-sufficient closure relation, the explicit state classification, all moves and component eccentricities. The second enumerates all \(2^{20}\) vertex subsets of the generalized Petersen model and independently checks minimum size, direct independent domination, reconfiguration and component geometry. The model-isomorphism permutation is printed in RESULT.md and can be checked directly against 30 edges. Finite enumeration is exhaustive for this one twenty-vertex graph; it gives no statement about larger hosts.
