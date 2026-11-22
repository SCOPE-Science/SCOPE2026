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

# Mathematical verification

The bundled `CHECKER.py` runs with Python 3.10+ and the standard library; no network, third-party package, or externally persisted intermediate state is needed. The expected complete output is included in `CHECKER_OUTPUT.txt`.

Verified by exact integer arithmetic: all twenty-seven exceptional classes; all forty-five tritangent triples; all 135 incidence edges; exact reduced Laplacian determinant; full Weyl permutation group of size 51,840; twenty-five conjugacy classes with sizes summing to the group order; twenty-five prime-local coinvariant Smith decompositions using each of two independently deleted roots; twenty-three distinct fixed-group isomorphism types; and the order-three equal-line-cycle contrast.

Finite arithmetic is sufficient here because the Weyl group is finite and the modulus cutoffs exceed every nontrivial elementary-divisor valuation, as checked against the exact reduced determinant. The graph pairing lemma is proved in the result text. There is no independent mathematical audit, no unconditional Néron-model interpretation, and no assertion that every Weyl type is realized over every finite field.
