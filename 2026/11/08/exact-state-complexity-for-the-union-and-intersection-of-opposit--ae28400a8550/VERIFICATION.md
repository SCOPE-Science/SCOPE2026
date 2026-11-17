---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: The greedy two-pattern subsequence-progress DFA product for P=0^a1^b,Q=1^b0^a has four exact disjoint reachable regions D0-D3; the simultaneous split (a,b) is unreachable. Counting gives R=n(n+3)/2+ab. Threshold suffix probes recover both progress coordinates for intersection, showing all R reachable states distinguishable; for union exactly n+1 absorbing accepted states merge and no others, giving R-n=n(n+1)/2+ab. Independent full BFS and partition refinement for all 81 pairs a,b=1..9 confirmed both formulas. Universal result rests on reachability witnesses and threshold proofs, not finite enumeration.

## originality

PASS

PASS qualified: published general state-complexity bounds for all-sided ideals and decomposition theorems for shuffle ideals address arbitrary inputs and worst cases but do not directly give the sharp two-parameter opposite-run counts or a fixed gap n. Resultary semantically similar opposite-run shuffle results concern shuffles (fixed-composition concatenations), not the union/intersection of upward scattered-subsequence ideals. No equivalent published exact formula located; an unindexed quotient classification remains a risk.

## value

PASS

PASS: Exact deterministic state complexity for Boolean combinations of two natural subsequence-upward ideals provides nontrivial quadratic closed classifications and a structural description of the precise accepting-sink reduction; useful in automata quotient complexity and succinctness questions, not a textbook unparameterized bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
