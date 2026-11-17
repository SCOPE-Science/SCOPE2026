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
# Verification details

The mathematical argument is self-contained in `RESULT.md`: exact pair-order correlations, a closure-based cancellation identity, Cauchy–Binet and two-dimensional spectral extremality, Haar–Stiefel row-sphere conditional moments, and an explicit order-ratio sign calculation. There is no reliance on finite experiments to deduce the all-size theorem.

The attached `check_area_variance.py` was executed with Python and NumPy. It exhaustively enumerated every edge permutation for 18 exact integer closed lists with 3–7 edges. The exact rational values agreed with both the sum of squared determinants and the determinant of the edge second-moment matrix. A separate Haar sampler with Gaussian QR produced 180,000 independent frames for each of 3, 4, 5, 10 and 25 edges. Empirical signed-area variances were 0.009513687, 0.011124909, 0.010620600, 0.005747868 and 0.001515837; the respective exact predictions were 0.009523810, 0.011111111, 0.010582011, 0.005772006 and 0.001506369. All five comparisons satisfied the specified 4% relative tolerance. The checker printed `EXCHANGEABLE_SIGNED_AREA_VARIANCE_OK`.

Numerical tests are corroborative and do not independently prove infinitely many cases. Independent mathematical and historical validation was not performed.
