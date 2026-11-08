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
Run `python3 abstract_checker.py`, `python3 finite_models_checker.py`, and `python3 finite_box_checker.py`. Each uses the Python 3 standard library only.

The exact abstract checker enumerates all 68 realizable truncated-category states, constructs the full successor-state set at every state, computes the two exact Boolean-algebra partition refinements, and asserts equality of the reported type profiles and their fixed-point property. The finite-model checker enumerates actual pointed valuations in six complete bipartite graphs to check agreement with direct semantics and closure under the noncontingency operator; the box checker separately corroborates the necessity profiles on fixed bipartite graphs. Both are supplementary to the structural induction in the proof, and no finite list of models alone establishes the universal theorem.

The novel numerical values have not undergone an independent audit. Search incompleteness remains a historical-priority risk; the formula-count claims are restricted to the stated frame family and one-variable languages.
