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

# Verification record

Execute `python3 verify.py` in the directory containing this file. The program independently enumerates torsion-zero idempotent matrices over prime fields for the three-dimensional cases \((n,q)=(1,2),(1,3),(1,5)\). It then enumerates all subspaces in dimension five in reduced row-echelon form, determines Lie closure directly from brackets, and counts ordered complementary subalgebra pairs for \((n,q)=(2,2),(2,3)\). It compares each complete rank histogram with the theorem and checks symmetry and the unrestricted-projection formula in characteristic two for additional dimensions. Expected final line: `VERIFY_OK`.

Observed direct-matrix rank histograms: `(1,28,28,1)`, `(1,63,63,1)`, `(1,275,275,1)`. Observed independent complementary-subalgebra rank histograms: `(1,496,9920,9920,496,1)` and `(1,2025,35802,35802,2025,1)`.

The verifier does not enumerate matrices in arbitrary dimensions or extension fields. The claim for every prime power and the asymptotic exponent comparison are supported by the complete mathematical proof, which also specifies every counted lift and subspace case. No external audit or external formal certification was performed.
