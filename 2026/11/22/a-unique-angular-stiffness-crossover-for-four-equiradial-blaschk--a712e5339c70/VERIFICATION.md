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

# Reproducibility and limitations

`RESULT.md` provides an analytic proof for all admissible radii and every angular direction near the square. Run `python3 check.py` with the standard Python library to perform finite arithmetic and independent finite-difference diagnostics. The script checks the geometric Fourier sums against closed rational stiffness formulas using exact fractions; separately checks the reciprocal-polynomial factorization and algebraic crossover bracket; and compares direct pairwise Poisson convolution energy with Hessian predictions. These finite checks do not prove the infinite Fourier series identities, the global uniqueness of a crossing, or the general remainder estimate: each is explicitly argued in `RESULT.md`.

Mathematical scope: fixed common radius \(0<r<1\), degree-four finite Blaschke products, and local angular perturbations around a labeled regular square. Global angular or variable-radius extrema are not asserted. The originality comparison remains best-knowledge with an explicit risk of unlocated equivalent Poisson-energy results. No independent audit has been performed.
