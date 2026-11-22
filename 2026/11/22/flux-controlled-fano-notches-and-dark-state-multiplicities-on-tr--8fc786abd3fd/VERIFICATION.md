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

`python3 verify.py` is a standalone Python 3 standard-library test program. It uses complex Gaussian elimination on the original finite side-device Hamiltonian, retaining the hub and all \(2m\) peripheral sites, to compute scattering amplitudes; it does not reuse the Schur-complement formula in that branch. The exact reduced formula is independently compared across loop counts \(m=1,2,3,4,5,8\), four nontrivial flux phases, and seven propagation energies. Endpoint cubic signs and the one-notched, two-notched, and three-notched regions are checked independently. For \(m=3,4,5,9\), local half-height points at three weak fluxes are computed numerically and compared with the explicit asymptotic coefficients. The linear constraints on compact embedded eigenvectors are checked at generic and endpoint flux values.

The observed output is `ALL_CHECKS_PASSED 345`. The solver uses double-precision arithmetic for numerical scattering, so these checks do not certify the continuum statement or an infinite-size limit. Completeness is established by the analytic cubic sign argument, the explicit \(\ell^2\) support/kernel proof, and the implicit-function expansion in RESULT.md. Independently performed external validation and independent audit are not claimed.
