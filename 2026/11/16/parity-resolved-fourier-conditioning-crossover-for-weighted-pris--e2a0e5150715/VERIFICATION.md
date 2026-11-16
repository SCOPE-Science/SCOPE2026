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

`rung_spectrum_checker.py` is standalone Python 3 using only the standard library. Execute `python rung_spectrum_checker.py` from the directory containing that file; expected output is `PASS: 666 checks`.

The script independently enumerates every perfect matching of the simple prism for 3–14 columns. It compares the weighted partition-function recurrence, exact rational single-rung and pair-rung probabilities, and the numerical Fourier eigenvalues with the closed formulas for each of the positive rational activities 1/3, 1 and 5/2. The numerical comparisons use tolerance 3e-10; the count and moment comparisons are exact fractions. The script does not test infinite parameters or provide a proof of the asymptotic limits; these are established by the finite algebra and Taylor expansions in `RESULT.md`. The main theorem is limited to positive rung activities and does not characterize full-edge covariance spectra.
