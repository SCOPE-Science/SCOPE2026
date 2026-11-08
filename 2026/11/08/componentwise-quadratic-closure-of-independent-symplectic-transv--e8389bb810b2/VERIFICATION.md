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

Direct finite-field tests execute `python3 verify.py` (standard library only). The checker constructs actual transvection matrices, forms their entire Lie bracket closure by repeated commutators, and verifies the graph-component dimension law independently of the symbolic tensor proof. Nondegenerate four-dimensional alternating forms are exhaustively covered over \(\mathbb F_3\); additional specified samples and path matrices are tested. The recorded stdout is in `verify_output.txt`.

The theorem for arbitrary fields and dimensions follows from the symbolic proof in RESULT.md, not from the finite experiments. No claims are made for characteristic two or dependent vectors. Independent mathematical audit has not been performed.
