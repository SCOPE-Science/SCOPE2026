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

The exact proof follows normalized affine interpolation and angular cone geometry; the finite numerical simulation is not a substitute for it.

The accompanying standalone `check_spherical_azimuth_visibility.py` requires Python and NumPy. A completed independent numerical implementation sampled 225,000 point pairs on round spheres in dimensions 2, 3, 5 and 6, sampled ambient interpolated geodesics directly, and compared geometric containment events to the exact formula. All prescribed numerical tolerances (0.012) passed; it also checked the algebraic equal-component extremal bounds.

`SPHERICAL_AZIMUTH_GEODESIC_VISIBILITY_OK 225000`

No machine proof of the universal identity and no independent human mathematical or historical audit was performed.
