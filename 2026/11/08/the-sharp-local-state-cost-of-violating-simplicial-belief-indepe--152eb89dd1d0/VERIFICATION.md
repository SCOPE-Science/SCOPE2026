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

## Reproducibility
Run `python3 independence_checker.py` with the Python standard library. It exhausts all chromatic complexes on three distinguished single-state agents, all permissible downward directions, all eight Boolean local valuations and every possible root-containing face, for 6,600 cases; no false binary instance occurs. It also builds an upward countermodel for each arity from two to eight and checks all modal-definedness and truth conditions directly. Output: `ALL_CHECKS_OK three_vertex_cases 6600 counterexamples 0 sharp_witness_sizes [4, 5, 6, 7, 8, 9, 10]`. The arbitrary-arity result follows from the proof, not from extrapolating the checked finite instances. Historical priority and independent validation remain unperformed.
