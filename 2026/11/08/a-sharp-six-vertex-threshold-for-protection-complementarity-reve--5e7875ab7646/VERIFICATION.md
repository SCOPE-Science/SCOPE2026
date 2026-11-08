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

Run `python verify.py` from this extracted package. The program requires only Python 3 standard-library modules and asserts: (1) 32768 possible forward-edge subgraphs of the six-vertex DAG with fixed source and target; (2) 196608 graph-and-unordered-candidate-pair cases; (3) 18 distinct conditional mixed-difference coefficient triples; and (4) exactly 24 strictly reversing cases, all possessing the same polynomial triple `(1,0,-1)`. The code independently tests 64 Boolean witness states by breadth-first directed reachability, and 24 exact rational heterogeneous reliability assignments against the displayed identity.

The proof of no sign reversal on at most five vertices is purely combinatorial, using monotonicity and impossibility of a three-intermediate-vertex directed majority network. The exhaustive classifier covers six-vertex DAGs after removal of irrelevant terminal incident edges; it does not certify all cyclic six-vertex networks or any larger order. Scientific originality depends on comparisons against the cited literature and remains contingent on wider historical-priority investigation. Independent audit has not been performed.
