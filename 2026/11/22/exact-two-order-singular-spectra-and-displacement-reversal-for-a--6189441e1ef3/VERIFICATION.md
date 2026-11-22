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

# Verification notes

The proof first identifies each cross-adjoint product by its action on the dense coherent-state kernel span, then gives a direct two-sided Weyl-unitary factorization into a scalar and the diagonal Fock dilation. This is an exact operator identity for all stated parameters; it establishes the full singular multiset without relying on truncation. All \(p>0\) Schatten claims follow from a convergent geometric series.

The displacement-order difference follows by expanding two exact multipliers. The Hermitian determinant identity \((1-|a|^2)(1-|c|^2)-|1-a\overline c|^2=-|a-c|^2\) proves the indefinite case; the equal-slope case is a perfect square.

The standalone `verification.py` uses fixed-seed complex parameter tests and finite Fock sections (cutoff 80) to check 166 explicit identities or singular-value predictions. It requires Python and NumPy; running `python verification.py` outputs the count of passing assertions. It neither certifies every complex parameter nor replaces the exact factorization.

Unverified limits: nonlinear inducing maps, boundary-slope cases, spectra beyond singular values, and independent external review. The literature comparison was bounded and does not prove that no prior equivalent theorem exists.
