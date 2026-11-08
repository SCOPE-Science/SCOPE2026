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

The self-contained `CHECK.py` file is executable with Python 3 plus `mpmath` and `sympy`. Run `python CHECK.py` in the package directory. It compares two-sided finite first-return thresholds against the exact inverse recursion for three rational exponents, checks symbolic binomial coefficients, and tests the large-time residual of the normalized logarithmic expansion. It reports the total number of checks on successful completion. This supplies finite corroboration, not an exhaustive or independent proof.

The mathematical proof is in `RESULT.md`. Its critical points are the exact central-crossing itinerary and the absolute convergence of renormalized parabolic-coordinate increments. The limiting constant \(K_\ell\) is defined by an analytic limit, not approximated as a proof. No external validation or independent audit has been performed. The results concern fixed \(0<\ell<1\) and normalized Lebesgue initialization; changing the initial distribution or branch maps can alter the coefficients.
