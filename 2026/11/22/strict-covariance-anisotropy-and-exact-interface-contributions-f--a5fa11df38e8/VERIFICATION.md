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

# Reproducibility and mathematical limits

The theorem is proved by an exact lower-envelope identity, disk-section moments and integration by parts. The finite checker is supplemental, not a replacement for the all-dimensional proof or an independent audit.

Run `python verify.py` with `sympy>=1.11` and `mpmath>=1.2`. In the reviewed run the checker reported `VERIFY_OK assertions= 138`. It checks the 3-active-ball example with exact rational polynomial integration (volume, two variances, strict gap and interface decomposition), the disk equality case, an unequal-radius 2-ball intersection, a 3-active-ball intersection and a 4-active-ball intersection. Numerical quadratures use 60-digit working precision and compare direct sectional moments with independent covariance and step-jump formulas in dimensions 2, 3, 4, 5, 7 and 9.

Checks were run from the bundled verifier before packaging. Independent mathematical audit has not been performed. The full 2023 curvature-constraint preprint was not accessible at review; no assertion of its full-text noncoverage is made. No proof for noncollinear ball centers or nonuniform densities is claimed.
