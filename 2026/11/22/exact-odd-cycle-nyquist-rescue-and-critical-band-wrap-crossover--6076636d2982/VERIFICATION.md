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

## Reproducibility

Run `python sinc_circle_check.py` with Python 3 and no third-party packages. This rebuilds complete rational wrapped-B-spline spectra and compares them with nullity, minimum-frequency, crossover and critical-gap formulas using integer and rational arithmetic.

Observed result: 3,627 exact rational spectra, 2,232 rank comparisons, 2,142 exact edge/crossover comparisons and 21 critical-width odd-cycle identities passed.

## Analytical status and limits

The general theorem is proved by Fourier/characteristic-function identity, circular arc-convolution monotonicity, strict support counting, and a simplex-volume calculation at the exact B-spline edge. The finite checker is diagnostic and cannot establish universal quantification. Independent verification is not performed.
