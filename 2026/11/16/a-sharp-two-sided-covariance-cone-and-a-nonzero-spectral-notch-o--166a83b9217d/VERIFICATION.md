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

# Verification

The included `check_hyperbolic.py` requires Python 3, SymPy and mpmath. Run `python check_hyperbolic.py` in the extracted scientific package. Exact symbolic assertions reconstruct the complex-shift spherical transform, all coefficients of the derivative polynomial, the zero-frequency ratio, positivity of the derivative coefficients in the damping shift, and the positivity of the two denominator factorizations. The script performs 60 supplementary high-precision comparisons for selected damping and spectral parameters.

The proof uses published L1-Godement and noncompact C0-universality theorems, with their hypotheses explicitly checked in the manuscript. No finite sample or numerical root isolation is substituted for the Descartes uniqueness proof, spectral sign necessity, or the strict finite-site conclusion. This is a self-review and not independent validation or certification. Literature priority remains subject to stronger-source comparison.
