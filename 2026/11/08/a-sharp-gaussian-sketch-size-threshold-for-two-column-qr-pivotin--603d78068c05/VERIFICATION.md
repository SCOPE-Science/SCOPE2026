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

# Verification of the two-column Gaussian-pivot theorem

The proof in RESULT.md is analytic. For any full-rank real two-column input, it computes the two projection errors, diagonalizes the quadratic-form difference of sketched squared norms, identifies the ratio of independent chi-square variates as symmetric beta, and optimizes its CDF over column correlation. The sketch-size threshold is proved using a symmetric-beta CDF inequality. The four-row optimum follows from an exact rational derivative, and the high-contrast law uses the leading small-beta-CDF asymptotic.

The included Python 3 standard-library script `verify.py` ran to successful completion with **1,316 diagnostic assertions**. Checks include exact rational low-sketch-row formulas, derivative algebra, explicit eigenvalues, seeded Gaussian simulations against beta predictions, sample grids for correlation extremality and the universal risk ceiling, and asymptotic constants. These finite checks do not prove the unlimited-dimensional/integer or asymptotic statements; the analytic argument carries those conclusions.

No independent audit was performed. Publication-precedence uncertainty remains for possible historical first-pivot calculations, including material not available in full. No claim is made about full QR factorizations or non-Gaussian sketches.
