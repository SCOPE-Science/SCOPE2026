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

# Mathematical verification and reproducibility

Run `python3 check_q1_sixth.py` from the directory containing the other files. The checker depends only on Python 3's standard library, creates no external artifact, and computes all sixth-moment coefficients independently from the monomial product integration formula over two uniform independent coordinates.

The program checks the exact ten rational sixth-moment coefficients, both symmetric substitutions, the complete coefficientwise nonnegative lower deficit, the exact upper positive antisymmetry term, the stationary quadratic and boundary signs, and equality witnesses. Additional finite floating-point evaluations of the algebraic cubic deficit are explicitly supplementary consistency checks, not a proof of an interval statement.

The **analytic proof** covers all real triples, including vanishing coefficients. The lower deficit is an identity in squared coefficient magnitudes with strictly positive coefficients, so the complete lower zero locus follows directly. The upper relation reduces maximization to a one-dimensional strictly concave cubic; its root and positive remainder factorization prove the entire upper interval and all equality cases. Orthogonality and affine change of variables establish the stated normalization and parallelogram scope.

No independent external mathematical audit or additional validation channel has been performed. An inaccessible or unindexed previously published equivalent formulation remains a possible originality risk.
