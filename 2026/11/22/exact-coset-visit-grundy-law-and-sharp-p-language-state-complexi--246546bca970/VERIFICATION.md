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

The deterministic checker `check_grundy.py` constructs legal moves directly from suffix-product membership in the subgroup, computes recursive minimum-excluded values, and checks coset-visit counts and each binomial histogram coefficient. Cyclic cases are checked to length seven, with a nonnormal \(S_3\) subgroup checked to length five. The separate checker `check_minimal_dfa.py` explicitly explores the complete normalized-visited-set DFA, minimizes it via Moore partition refinement, and checks all one-letter set-separation witnesses for quotient groups of orders one through six, together with the Klein group and \(S_3\). The accompanying outputs were produced by executing the included scripts and report PASS. These are finite tests; the all-group mathematical statements are proved in RESULT.md and are not extrapolated from experiments.

Reproduce using `python3 check_grundy.py` and `python3 check_minimal_dfa.py` from the extracted directory. No external packages are needed.
