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

# Verification

Run `python3 verify_cpa.py` with the standard Python library. The script constructs Lie brackets directly from a companion matrix, solves all symmetric biderivation constraints by finite-field Gaussian elimination, and tests all CPA identities on basis triples for every biderivation in the four cases listed below. It does not impose the claimed normal form before elimination.

- Over \(\mathbb F_2\), degree \(2\): biderivation dimension \(6\), CPA count \(8\), rank counts \((1,3,4)\).
- Over \(\mathbb F_3\), degree \(2\): biderivation dimension \(6\), CPA count \(18\), rank counts \((1,8,9)\).
- Over \(\mathbb F_2\), degree \(3\): biderivation dimension \(9\), CPA count \(16\), rank counts \((1,7,0,8)\).
- For the degree-two Lie algebra after extending scalars from \(\mathbb F_2\) to \(\mathbb F_4\): biderivation dimension \(6\), CPA count \(64\), rank counts \((1,23,40)\).

Expected completion marker: `CPA_IRREDUCIBLE_GALOIS_DESCENT_VERIFIED`. Algebraic arguments in `RESULT.md`, not the enumerations, establish the general all-degree, all-field formulas. The script verifies selected rational-point and rank cases, but not geometric smoothness, generic Galois cycle counts, or the complete zeta function by exhaustive enumeration. Those are proved separately in the text.
