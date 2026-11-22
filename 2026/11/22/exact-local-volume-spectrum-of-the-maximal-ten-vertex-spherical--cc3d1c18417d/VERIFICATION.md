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

The mathematical proof in RESULT.md derives the full quadratic form and diagonalizes it without relying on sampling or finite enumeration. Its key identities are the signed-facet determinant formula, the second-order planar area expansion, the mixed-bivector pairing, and the exact five-point Fourier spectrum. The six zero eigenvalues are matched with all generators of the orthogonal orbit.

The standalone `checker.py` uses an independently implemented four-by-four determinant and direct unit-sphere-normalized perturbations. Running `python checker.py` produces finite-difference comparisons for first and second angular harmonics, a residual cross motion, a symmetric cross motion, a rotational zero mode and a generic direction. The program asserts agreement at finite-difference precision, eigenvalue ordering, 30 total multiplicities and the exact simplification of the smallest eigenvalue. Separately, `python full_hessian_check.py` (requiring NumPy) assembles the complete 30-by-30 Hessian from 25 determinants per perturbed configuration and numerically checks all five exact eigenvalue clusters; its observed maximum discrepancy is below `3e-6`.

Numerical agreement cannot certify the second-variation identity for infinitely many directions. That identity is proved analytically in RESULT.md; the numerical tests are only a consistency check. The previously published global volume maximization is used as an antecedent, not independently reproduced here.
