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

The complete proof is in `RESULT.md`, with exact beta integrals and a compactness-based endpoint polynomial lower bound. The included `cap_checker.py` independently evaluates the exact full-sphere and cap moment matrices for each azimuthal order at bandwidths 0 through 5, using 110-digit `mpmath` arithmetic (install the version pinned in `requirements.txt`). It tests the leading sector coefficients, the full-spectrum condition-number leading constant and the zonal rescaled Jacobi polynomial values. The observed finite-case pass marker is `POLAR_CAP_FIXED_BAND_PASS`.

The numerical eigenvalue and eigenvector tests are not an infinite-dimensional or all-bandwidth proof. The theoretical statements require fixed bandwidth and shrinking cap. Independent audit: not performed.
