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

The analytic proof reduces the section shape to the spectrum of a two-dimensional quadratic form. The exactly circular sections occur at four unit normals. In local tangent-plane coordinates the eigenvalue gap has invertible first variation, giving four shrinking disks and the exact quartic probability coefficient. A separate algebraic perfect-square certificate proves the global coefficient inequality, and an explicit involution proves exact inverse multiplicity.

The independent numerical script `verify.py` uses Python 3, NumPy and SciPy. It checks 4,500 alternative plane-basis eigenvalue calculations against the invariant trace formula, eight zero-eccentricity evaluations across two triaxial examples, the exact rational two-shape inverse ambiguity, 1,048,576 low-discrepancy uniformly distributed normals, and six checks against explicit spheroidal CDF values. It printed:

`VERIFY_OK alternative_plane_bases=4500 circular_normals=8 sobol_normals=1048576 exact_ambiguity=1 axisymmetric_CDF_cases=6 quartic_coeff=0.5`

These finite diagnostics do not constitute a proof of an infinite limit. The limit is derived by the local nondegenerate Jacobian and spherical area measure, and global uniqueness of the circular planes is established algebraically. There was no independent audit or formal certification.
