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

# Verification of the rational-window frame calculation

The analytic proof establishes the compact Zak-fiber multiplier, its complete common-zero list, explicit first derivatives and positive-definite quadratic minimization. The complete common-zero list is obtained by the rational function factorization in `RESULT.md` and is also proved in the cited prior work. The uniform remainder is justified by absolute convergence of the first differentiated Zak series, continuity on the compact fundamental torus and localization to the common-zero fiber.

Run `python CHECK.py` with Python 3 and its standard library. The checker evaluates all six constants, tests the numerical anisotropy, compares independent integer-lattice sums with the analytic zero values and derivatives, and assesses sharp quadratic trial values for real and imaginary perturbations of two small sizes. On the documented run the output was `CHECK_OK: formulas, Zak values, derivatives, and local sharp quadratic trials`.

The finite truncation has a slower \(O(N^{-1})\) error for frequency derivatives of an algebraic-tail window, which is handled by the check's stated tolerance. These tests are consistency evidence only: they do not prove global nonvanishing for the infinite Gabor system, the complete Zak-zero theorem, or mathematical priority. The frame result is proved analytically, and independent validation has not been performed.
