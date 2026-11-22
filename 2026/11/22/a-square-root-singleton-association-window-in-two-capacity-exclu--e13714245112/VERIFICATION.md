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

The fixed-mass stationary product weights were reconstructed using a local incoming-minus-outgoing telescoping identity on the nine occupancy pairs. The singleton covariance was expressed as an exact determinant of symmetric three-point walk probabilities. A nonnegative characteristic-function moment representation and strict Cauchy--Schwarz verify the positive half-filled sign; fixed total particle number verifies the contrasting negative occupation covariance.

The square-root scaling was proved by symmetrizing the determinant *before* applying Fourier Laplace asymptotics. Its exact square-difference integrand yields the Gaussian sign polynomial without relying on cancellation between approximate probabilities. The undeformed finite-size formula follows by exact hypergeometric counting.

Run `python3 check.py` with Python 3 to reproduce the exact small-system global-balance tests, exact coefficient identities, sharp phase-window tests and noncertifying numerical asymptotic checks. The current check passes 8187 assertions.

The numerical checks are finite and cannot certify the infinite-size limit. The proof covers only the specified positive rates and fixed deformation in the limit. The boundary scaling value has zero leading coefficient and no sign claim. Publication priority remains conditional on the literature coverage described in REVIEW.md.
