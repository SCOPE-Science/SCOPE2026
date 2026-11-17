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

# Reproducibility and verification

The attached `check_product_acuteness.py` is standalone Python code using NumPy and mpmath. Running `python check_product_acuteness.py` in a Python environment with these dependencies produced `PRODUCT_ACUTENESS_CHECKS_OK`. Its direct checks include an exact one-dimensional Bernoulli-height integral at four scales, algebraic six-permutation identities including repeated ordinate values, and simulation of all three original strict-angle dot products in uniform, triangular and two-atom height laws at matched variance.

The Bernoulli finite-width exact values test the predicted \(12\) coefficient as the logarithm grows, while direct simulation tests the geometry without using the asymptotic event criterion. At finite thickness the logarithmic convergence is slow and should not be used to infer an exact coefficient from the printed estimates. The proof does not depend on simulated agreement, numerical quadrature or computational claims about infinitely many samples.

The analysis proves the rare-acuteness asymptotic, fixed-parameter \(O(\varepsilon^2)\) remainder and conditional joint total-variation convergence. It does not prove uniform convergence over distribution families or general unbounded-support extension. Independent mathematical audit has not been performed.
