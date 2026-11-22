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

# Reproduction

Run `python3 verify_ssa2.py` from this directory (standard library only).

The program builds the entire reachable deterministic state graph, including the failure sink. It checks 22,985 reachable accepted states and 22,986 total complete states; performs forward suffix refinement with exact counts \(2,17,2715,6807,7295,7311,7311\); and independently performs inverse-transition Hopcroft minimization to 7,311 states. It also independently checks the literal two-disjoint-factors definition on every one of the 349,525 DNA words of length at most nine.

The all-length proof is the state-invariant induction plus completeness of the finite traversal and stable right-congruence partition. The finite-word sampling check alone would not justify the claim. Results are not evidence of independent audit or an automaton-minimality theorem for other stem lengths.
