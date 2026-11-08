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

The standalone `verify.py` uses exact integer macrocell graphs and Python rational arithmetic. Execute with `python3 verify.py` from the directory containing the script. It prints `SEVEN_ROTATIONS_EXACT_GRAPH_OK` after checking the complete return towers, the rigid cycles and selected exact branch coordinates. The proofs of recurrence and exhaustion of all levels are analytic induction over the recurring finite-state tower descriptions; finitely many point samples alone would not establish absence of cycles. The imported ergodicity theorem is Theorem 1.4 of Bruin and Lukina (2023). Independent mathematical review has not been performed.
