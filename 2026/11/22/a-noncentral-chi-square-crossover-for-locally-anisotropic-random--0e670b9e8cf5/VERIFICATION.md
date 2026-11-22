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

# Reproduction and limitations

Install Python 3, NumPy and SciPy, then run `python verify_anisotropy.py` from the directory containing the embedded artifacts. A successful local run prints `ALL_ANGULAR_ANISOTROPY_ZONOTOPE_CHECKS_PASSED`.

The script independently verifies twelve even-degree and six odd-degree Legendre quadratures, spherical conditional degree-two eigenprojections at five latitudes, the first spectral coefficient \(-\pi/64\), truncated trace/Hilbert–Schmidt sums, the sample density's quadratic moment, determinant identities at several finite sizes, and analytic variance and essential-supremum constants. The analytic derivation additionally evaluates the first six Legendre integrals *exactly* with polynomial beta integration; these exact identities are stated in the proof and are not inferred from the numerical routine.

Proof completeness is based on the bounded canonical triple-kernel overlap estimate, the exact moving degree-two harmonic mean, finite-mode triangular-array central limit theorems, and a uniform canonical-pair tail estimate. The numerical tests are diagnostic and cannot verify all dimensions, limits or the complete historical priority landscape.

The original random-zonotope article was accessible by abstract and date, but the complete document was unavailable; this is a literature-access limitation rather than scientific certification. Independent mathematical validation has not been performed.
