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

# Reproducible checks

Run `python3 verify_cartier.py` with SymPy installed. The verifier reconstructs the matrix from the polynomial equation, checks the full support of the second and third Frobenius-twisted products, the rank-controlling determinants, the vanishing fourth product and all \(3125\) \(\mathbb F_5\) coefficient specializations. Compare the output with `verification_output.txt`, including `ALL_CHECKS_PASSED`.

The proof of the infinite-field statement is the exact polynomial identity and matrix-rank argument in `RESULT.md`; finite-field exhaustive checks verify only \(\mathbb F_5\) points. The downloaded literature was used for comparison, not as mathematical certification. No independent external verification or complete \(5\)-torsion classification is claimed.
