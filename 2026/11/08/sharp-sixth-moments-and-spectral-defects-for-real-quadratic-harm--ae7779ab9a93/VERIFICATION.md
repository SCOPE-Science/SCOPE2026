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

# Reproducible scientific checks

From this package directory run `python verify_sixth_s3.py` with Python 3 and SymPy installed. The checker expands the Dirichlet(1/2,1/2,1/2,1/2) sixth moment of a trace-zero quadratic form, verifies every exact coefficient of the resulting three-variable homogeneous sextic, and compares it to the determinant-and-cubic-trace identity. It also checks the two exact remainder identities, the balanced and one-versus-three endpoint values, 342 nonzero small integer trace-zero spectral tests, and all nine basis-matrix quaternion identifications by exact trace pairing.

The verification run produced:

```text
FULL_DIRICHLET_SIXTH_MOMENT_POLYNOMIAL_IDENTITY_OK 28
ENDPOINTS_AND_342_RATIONAL_SPECTRAL_TESTS_OK 27/7 15
EXACT_TWO_SIDED_SPECTRAL_DEFICIT_IDENTITIES_OK
SO3_QUATERNION_NINE_DIMENSIONAL_ISOMETRY_OK 9
ROTATION_MATRIX_COEFFICIENT_EQUALITY_MODES_OK
ALL_S3_SIXTH_MOMENT_CHECKS_OK
```

The finite rational tests cannot prove an inequality for all real eigenvalues. Universality and equality classification are established by the AM–GM and constrained-extremum arguments in `RESULT.md`. All computations use the scripts embedded alongside this document; no external certificate is assumed.
