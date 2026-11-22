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

# Reproducibility of the anticanonical torus weight hierarchy

Execute `python3 verify_anticanonical_f1.py` with Python 3 and its standard library. The program enumerates all 511 nonempty leading-monomial subsets of the nine monomials and verifies that every candidate affine footprint has value and slope bounded by the stated target. This proves the combinatorial certificate for all \(t\ge4\). It also enumerates each of the 65,536 subsets of the 16 rational torus points over \(\mathbb F_5\), computes exact evaluation ranks, and verifies the entire nine-term hierarchy there. Explicit constructions are tested over \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_{11}\).

The checker prints `ANTICANONICAL_F1_HIERARCHY_VERIFIED` only after all assertions succeed. All prime powers are established by the algebraic footprint inequalities, interpolation, and subspace constructions in `RESULT.md`; numerical tests in finitely many fields alone cannot prove this uniformity. The complete footprint coefficients are additionally preserved in `footprint_certificate.json`.

All mathematical assertions are limited to the dense rational torus over fields with \(q\ge5\). Literature priority was checked against the explicitly identified related works, but no independent historical audit has occurred.
