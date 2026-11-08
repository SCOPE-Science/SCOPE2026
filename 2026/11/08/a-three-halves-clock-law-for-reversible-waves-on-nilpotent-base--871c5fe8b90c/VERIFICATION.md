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

# Reproducibility and limits

Extract the supplied `check_matrix.py`, `check_states.py`, `check_matrix.out`, and `check_states.out` into one directory, then run `python3 check_matrix.py` and `python3 check_states.py`. Both use only the Python 3 standard library, integer bitsets, and exact arithmetic in characteristic two.

The matrix test enumerates all 1,099 labelled simple graphs with 1–5 vertices and recognizes 278 whose binary adjacency is nilpotent. For all 278 it checks the parity-derived Jordan partitions of the matched prisms, their exact reversible-wave orders, and 4,170 fixed-subspace dimensions. It separately checks the dyadic open ladders of lengths 3, 7, and 15. The state test directly iterates all 4,096 ordered binary two-time-level states on \(P_3\square K_2\), obtaining exactly 1, 15, 240, and 3,840 states of least periods 1, 3, 6, and 12.

The output files record actual successful runs. No exhaustive search over all graphs, all field extensions, or all graph orders is claimed. The general arbitrary-graph and extension-field assertions depend on the written algebraic proof, not finite simulation. The literature comparison is qualified by the full-text access limits identified in REVIEW.md. Independent audit remains unperformed.
