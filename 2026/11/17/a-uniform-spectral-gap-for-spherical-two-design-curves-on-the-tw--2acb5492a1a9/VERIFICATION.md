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

Run `python3 verify.py` in this directory. It uses only the Python standard library and tests the exact radical polynomial, the claimed decimal length, and 1000 deterministic positive-semidefinite Fourier covariance examples. The program does not enumerate all curves and is not an infinite proof. The universal bound is established by equations (1)–(5) in `RESULT.md`.

## Mathematical checks

The spectral inequality uses only a mean-zero orthonormal triple of coordinate functions and the circle's frequency eigenvalues. The rank-two covariance statement uses the two-dimensional span of the first harmonic, the matrix inequality from covariance additivity, and the variational characterization of the second eigenvalue. The fourth Fourier amplitude of the second harmonic equals the gap between its two nonzero covariance eigenvalues, and sphere-valuedness forces cancellation by higher harmonics. These steps apply to arbitrary periodic `H^1` curves.

## Unproved statements

Neither optimality of the lower bound nor existence or regularity of a length minimizer is established. The self-review did not perform independent historical certification.
