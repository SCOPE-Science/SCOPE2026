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

The proof is analytic and finite-dimensional at each parameter: exact Walsh diagonalization, binomial Abel summation, a positive increment-pair inequality, and the operator norm bound \(\|D_p-(J-I)\|_2<1/2\). There is no machine-assisted infinite certification.

Run `python3 folded_cube_rate_check.py` using Python 3. The program performs exact integer and rational checks where appropriate and floating-point comparisons solely for finite illustrative power evaluations. It verifies (i) the Abel transform and a separate exact first-power identity; (ii) positivity of integer paired coefficients; (iii) explicit upper-obstruction arithmetic and direct character sums for smaller dimensions; and (iv) the explicit small-power norm inequality. The final success line is `FOLDED_CUBE_EXPONENTIAL_RATE_FINITE_CHECKS_OK`.

The script's finite range and floating arithmetic cannot prove that the inequalities hold for all dimensions. That step is in the written proof. The verified claim concerns only dimensions divisible by four and at least twelve. Exact individual generalized-roundness exponents, the polynomial asymptotic prefactor and independent validation remain open in this package.
