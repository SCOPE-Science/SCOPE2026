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

# Verification and limits

The proof gives exact parity secular relations for the upper half-line Jacobi eigenvalue. The thresholds are obtained from their removable limits at zero exterior Floquet exponent. Symbolic differentiation checks that the derivative of defect strength with respect to that exponent tends to \(\frac{ab}{a+b}\); uniform Taylor expansion on exponents of order inverse square defect depth yields the fourth-order spectral law. Floquet eigenvector tails give the strong rescaled \(L^2\) profile.

The supplementary script `check_parity_quartic.py` uses arbitrary-precision numerical root calculations and comparisons across distinct positive weight pairs, depths and parity. Execute with Python 3 and the public `mpmath` package: `python check_parity_quartic.py`. It is corroborative, not a proof of generality or an independent audit. Known exact thresholds are credited as prior.
