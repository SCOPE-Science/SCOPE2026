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
# Verification and reproducibility

Execute `python3 verify.py` in a directory containing `verify.py`; no third-party dependencies are required. This execution produced `WALSH_QUADRATIC_BALL_EXACT_CHECKS_PASS 80228`.

All entries of the Gram matrix were independently counted by enumeration of Boolean vertices for dimensions \(5\) through \(10\) and all ball radii. Sector actions were checked against the displayed \(3\)-by-\(3\), \(2\)-by-\(2\), and scalar formulas. Integer polynomial coefficients and the finite minimal-ball determinants were checked independently, avoiding floating-point eigensolvers. The checker is a bounded finite test; the general theorem depends on the binomial count, invariant sector decomposition, determinant factorization and elementary symmetric polynomial proof in RESULT.md.

The sharp asymptotic \(\lambda_{\max}/\lambda_{\min}\sim n^8/256\) is justified analytically by a radial Rayleigh lower bound, the cubic trace and root products, not by extrapolating the finite checker. Historical priority is provisional, particularly because the relevant 2021 continuation could not be read in full. No independent external mathematical validation is asserted.
