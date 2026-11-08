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
# Verification notes

The package includes a self-contained standard-library script `verify.py`. Run `python verify.py` to check normalization roots, interface identities, strict variational bounds, quadrature of the maximizing density, the special \(L=2\) infimum, and large-budget scaling. The expected success line is `CESARO_CAP_EXTREMAL_CHECK_OK 73 finite assertions`.

The proof uses the exact unitary transform and finite-interval rank estimates; the script supplies no infinite-dimensional or independent certification. The spectral coefficient relies on second-order Volterra asymptotics and a tail-counting localization argument, which are spelled out in RESULT.md. Publication priority remains subject to independent literature review.
