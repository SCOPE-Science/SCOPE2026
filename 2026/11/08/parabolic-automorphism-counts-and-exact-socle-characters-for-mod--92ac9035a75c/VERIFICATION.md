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
# Reproducibility checks

Execute `python3 verify.py` in a directory containing the embedded file, using Python 3 standard library only. The script enumerates all allowed algebra-generator images for the displayed small finite rings; no theorem formula is used to decide whether an individual map is invertible. Instead, it builds the full substitution matrix in the monomial basis and computes its rank over the field. For each invertible substitution it multiplies the top-degree socle monomial and reads the scalar coefficient, then compares counts with the parabolic and determinant predictions. The tested finite fields are \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (the last represented by its irreducible quadratic polynomial). The eight configurations are \((2;1),(2;2),(2;1,1),(2;1,2),(3;1),(4;1),(4;2),(4;1,1)\), with automorphism totals \(1,4,24,2048,6,3,48,2880\) respectively. The run completes with `VERIFY_OK`.

The finite checks do not enumerate larger groups or extension fields, and they cannot certify a universal theorem. The unrestricted claim is proved using the monomial Frobenius identity, nilpotent-ideal lifting, triangular linear substitutions, the socle's highest-degree property, and arithmetic in cyclic multiplicative groups. An independent audit of the proof has not been performed.
