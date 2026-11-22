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

# Reproducibility and limits

The exact proof is in `RESULT.md` and uses only affine-normalized conic equations, Cauchy–Schwarz, Tonelli's theorem, elementary trigonometric integration and gamma-quotient asymptotics. It establishes the mean-area formula for every positive integer sample count, the full two-parameter pairwise area formula, and exact transversality of four crossings. Numerical calculations are independent diagnostics only.

`check_overlap.py` runs with Python 3 and SciPy. The executed checker compared independent radial numerical integrals for 205 ellipse-parameter pairs with the trigonometric formula, finding maximum absolute error 1.1102230246251565e-15. It also independently reconstructed all four common boundary points, with maximum polynomial residual 3.3306690738754696e-16 and a nonzero Jacobian in each numerical case. `check_hierarchy.py` performed factorized numerical one-dimensional integrations of the m-fold pointwise expression for sample counts 1, 2, 3, 4, 5, 10, 20, and 100; those integrals agreed with the beta identity at numerical precision (absolute deviations at most 9.3e-12).

These tests do not establish numerical certification outside the sampled parameters, do not certify novelty, and do not constitute independent mathematical audit. No external independent audit has been performed.
