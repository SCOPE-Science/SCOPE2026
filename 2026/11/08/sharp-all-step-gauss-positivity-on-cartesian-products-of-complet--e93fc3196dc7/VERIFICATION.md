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

The file `artifacts/verify.py` is a standalone Python 3 standard-library exact-rational checker. From the root of this package, run `python3 artifacts/verify.py`.

The recorded successful output is:

`VERIFY_OK polynomial_certificates 9 rational_kernels 320 row_sums 55 green_identities 246 positive_green 243 large_step_witnesses 12`

The checker reconstructs the three positive-coefficient polynomial certificates for all three surviving two-factor parameter pairs. It evaluates exact tensor spectral kernels for 11 parameter samples at five positive rational timesteps, tests all row-sum identities, and compares two separate rational formulas for the nearest-neighbor Laplacian pseudoinverse for all sorted tuples of two to five factor orders between two and six. Strict pseudoinverse positivity is checked in 243 excluded samples, and 12 negative transition witnesses are evaluated at large positive timesteps.

These tests are exact arithmetic but finite. The infinite parameter and all-timestep claims are established only by the tensor decomposition, the positive-coefficient certificates, and the symbolic Green-function inequalities in `RESULT.md`. The negative conclusion for arbitrary excluded graphs is eventual and does not claim the same witness timestep for all graphs.

No third-party paper is embedded. No independent external validation is asserted.
