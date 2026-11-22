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

The analytic verification proceeds from exact Bernstein basis-image coefficients, strict positivity of their alternating-sine sums and decreasing-weight integrals, an endpoint-derivative Fourier tail, and exact cyclic Fourier aliasing. The minimization uses reciprocal-square lattice identities and treats zero-mass parity endpoints separately.

Run `python checker.py` from this folder, with `numpy` and `mpmath` available. Its successful execution produced 7,807 supplementary finite checks: degrees one through nine, sampled input harmonics, frequencies through thirty, exact degree-two circulant spectra, and scaled eigenvalue limits. Computations do not prove the infinite-dimensional claims.

The stated result concerns fixed Bernstein degree and fixed source covariance. No independent mathematical audit has been conducted.
