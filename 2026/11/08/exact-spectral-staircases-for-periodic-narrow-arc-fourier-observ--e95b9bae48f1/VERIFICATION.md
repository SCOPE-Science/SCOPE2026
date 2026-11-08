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

The source file `repro/check_periodic_windows.py` is standalone Python 3 code requiring `mpmath` (tested with 85 decimal digits). Running `python3 repro/check_periodic_windows.py` returned `PERIODIC_FOURIER_STAIRCASE_CHECKS_PASS 134`.

The script checks six distinct frequency masks and cyclic aperture orders. It compares predicted moment-determinant coefficients with high-precision eigenvalues, integrates representative entries over the original multiple arcs, verifies the exact Fourier-congruence block spectrum, checks a terminal inverse-Vandermonde identity, and tests the \(5/2\) condition-number constant in a concrete six-mode example.

The general result is proved analytically using exact cyclic Fourier cancellation and leading coefficients of exterior powers of an analytic finite-rank operator. The finite test set is not exhaustive over all possible masks and does not certify uniqueness or historical priority.
