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

# Verification and reproduction

Execute `python tools/check_wendland.py` with Python 3 and `mpmath` installed. The script checks two independent Euclidean hypergeometric second-term ratios, evaluates representative Bessel-square Mellin integrals against the gamma formula, checks the gamma-ratio expansion, and calculates circle Fourier coefficients directly in a polynomial example. The expected success line is `WENDLAND_SECOND_ORDER_CHECKS_PASS`.

The code directly integrates a kernel in the qualifying parameter range and compares the generic and scale-calibrated second-order limits; it does not extrapolate a finite degree to an all-degree proof. All general-domain assertions rely on the proof in `RESULT.md` and the classical special-function identities cited there. The absolute Fourier and spherical-area normalizations are explicit.

Self-review: passed. Independent mathematical audit: not performed. No independent validation or machine proof is asserted.
