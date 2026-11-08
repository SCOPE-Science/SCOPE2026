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
Run \(`python3 verify.py`\), requiring only Python 3 standard library. The attached \(`verification_output.txt`\) is the exact script output.

The script independently enumerates reduced row-echelon subspaces of \(k^3\), directly evaluates the \(\mathfrak{sl}_2\) bracket and idempotent Nijenhuis torsion for all operators obtained from complementary pairs over \(\mathbb F_3\) and \(\mathbb F_5\). It independently enumerates all \(3^9=19683\) endomorphism matrices over \(\mathbb F_3\) without starting from any subalgebra parameterization; only 74 satisfy both required equations and the rank counts are \((1,36,36,1)\). The derived orbit classification is also checked by direct conjugation of all upper-triangular matrices on complement lines for each field. The outputs include sizes \((12,12,12)\) for rank one at \(q=3\) and \((30,60,60)\) at \(q=5\).

The general-field classification rests on the symbolic argument in RESULT.md; small-field exhaustive enumeration cannot certify all odd prime powers. The script does not assert historical uniqueness, scheme-theoretic reducedness, or independent proof verification.
