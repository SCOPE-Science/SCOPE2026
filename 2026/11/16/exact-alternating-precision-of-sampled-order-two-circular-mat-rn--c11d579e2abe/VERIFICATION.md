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

## Reproducible checks

Run `python verify_precision.py`. The script requires Python 3 and the `mpmath` package. It constructs the matrix from a real-space periodization rather than the reciprocal-frequency representation, directly inverts each sampled covariance, and verifies the claimed closed inverse and all off-diagonal signs at 60-decimal-digit arithmetic precision.

Tests cover all integers from 3 to 16 inclusive and positive range values 0.12, 0.8, 2.5, 7 and 19. The reported 14,980 assertions compare matrix entries, signs, and Fourier spectra. The order-one control also verifies the exact vanishing of non-neighbor precision entries.

## Analytical boundaries

No finite test proves the assertions for all range parameters and sample counts. The decisive steps are the positive continuous Fourier alias sum, the exact rational division and geometric-series inversion, the strict inequality for the even-size nearest-neighbor case, and the odd-size comparison to the strictly negative three-site inverse. The proof covers all real positive ranges and all integer sizes at least three.

The sign pattern refers to exact zero/nonzero conditional-dependence structure, not a thresholded numerical graph. Numeric values should not be used to infer whether small distant precision entries are exactly zero.
