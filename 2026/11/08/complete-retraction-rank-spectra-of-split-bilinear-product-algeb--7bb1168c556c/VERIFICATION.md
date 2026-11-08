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

The standalone `verify.py` uses finite-field arithmetic and row-reduced subspace enumeration independently of the combinatorial derivation. It exhaustively checks all subspaces of dimensions zero through four for the indicated four-dimensional cases, all subspaces of the two-dimensional cases, and all maps with center image in the square ideal in the three-dimensional cases over prime fields. It checks the endomorphism property directly on basis pairs and the idempotence property directly on matrices.

Tested fields: \(\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\). Tested pairing classes: all available generic, split symmetric, and alternating cases for \(n=1,2\). It additionally checks the maximal-rank formulas for \(n\leq4\) algebraically. Run `python3 verify.py` from the package root; expected final line: `VERIFY_OK_BILINEAR_RETRACTIONS`.

The full infinite-family theorem is justified by the mathematical proof. Finite enumerations cannot establish universal novelty or correctness, and independent mathematical review has not been performed.
