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

The theorem is proved analytically in `RESULT.md`; `verify_prism_covariance.py` is a standalone numerical check and does not constitute verification of an infinite parameter space.

Run `python verify_prism_covariance.py` with Python 3 (standard library only). The script constructs actual three-dimensional prism vertices, forms their orthogonal planar projections onto two independent in-plane basis vectors, computes convex-hull areas using the monotone-chain algorithm, computes the width from extreme vertex dot products, and estimates their common-direction covariance. The tests use a square, thin rectangle, equilateral triangle and regular 32-gon at three heights each, plus rectangle angular integrals and exact circular-width moments. On the source checked, the final line was `ALL_SAME_NORMAL_PRISM_COVARIANCE_CHECKS_PASSED`.

All finite Monte Carlo checks use a fixed seed and tolerances; independent normal sampling would test a different statistic. Sharp inequalities, constant-width cases and all-height quantifiers are established only by the explicit analytical proof. Complete text of the broad 2026 width/brightness preprint was not accessible; independent mathematical audit has not occurred.
