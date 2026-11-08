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

# Reproduction and limits

Execute `python3 verify_genus6_deformation.py` using Python 3's standard library. This program performs an exact symbolic expansion of \(f_\lambda^c\) in \(\mathbb F_5[\lambda,x]\) and verifies every coefficient of the displayed \(6\)-by-\(6\) Cartier matrix. It then implements \(\mathbb F_{25}=\mathbb F_5[z]/(z^2+2)\), enumerates all 25 \(\lambda\) values, removes the unique member with \(\lambda^7=2\), and constructs the full Cartier matrix for all 24 smooth fibers. It computes ranks of successive products with the necessary inverse-Frobenius twists, including parameters outside \(\mathbb F_5\), and checks one special and 23 generic profiles by exact Gaussian elimination.

Expected final line: `GENUS6_TRIGONAL_DEFORMATION_F25_CARTIER_PASS ...`.

The proof of the all-parameter assertion is algebraic and appears in `RESULT.md`: the symbolic matrix and the two nilpotent chains suffice over any algebraically closed field of characteristic five. The finite-field replay is an independent check of those coefficients and finite specializations, not an exhaustive test of the algebraic closure. Scientific checks are same-model only; independent audit has not been performed.
