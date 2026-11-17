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

The packaged `verify.py` constructs both graphs from their explicit coordinate adjacency definitions, confirms the strongly regular parameters, enumerates every legal product-of-simplices Hom cell, and verifies the integral presentation of first homology using only unit pivots and the remaining rank-two Smith determinantal divisors. The actual output is in `verification_output.json`.

`check_fields.py` separately reconstructs signed two-cell boundaries, checks the chain identity in all 45,120 two-cells per graph, and computes exact ranks over three prime fields. Its actual output is in `fields_output.json`.

The checker finds 22,950 unit pivots and remaining determinantal divisors 2 and 4 for the rook graph, and 22,982 unit pivots with no residual nonzero matrix for the Shrikhande graph. Both have 23,042 free fundamental one-cycle coordinates before imposing two-cell relations.

The calculations prove integral first homology for these exact two finite complexes. They do not compute higher homology, fundamental groups, all automorphism actions, or a general classification. No independent mathematical audit has been performed.
