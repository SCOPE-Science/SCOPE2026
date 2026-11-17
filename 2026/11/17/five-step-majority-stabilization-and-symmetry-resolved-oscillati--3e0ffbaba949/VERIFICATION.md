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

Both standalone enumerators were executed on the complete finite domains. `majority_permutohedron.cpp` evaluates all 16,777,216 states and checks the full group of 48 graph symmetries; `verify_factorized.py` uses the independent Cartesian graph realization with a checked 24-vertex isomorphism certificate and exhausts the two 4096-state two-step maps. The second program then combines all ordered pairs of side states, rather than calling the first program or consulting its output.

Outputs recorded in `census.jsonl` and `factorized_output.json`. They agree exactly on the fixed count, temporal-two population, maximum entrance time, and all 12 labelled first-entry totals. The C++ program also computes the geometric class distribution and gives a sharpness witness (initial bit mask 9762). The full proofs and finite boundaries are in RESULT.md.

These are finite exhaustive checks of a specified graph and update rule. No inference is made for larger permutohedra, other graph models, or uninspected historical literature. Independent external mathematical review has not been performed.
