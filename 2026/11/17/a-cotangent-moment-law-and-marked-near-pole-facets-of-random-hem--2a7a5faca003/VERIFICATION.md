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

# Verification record

The proof uses the exact gnomonic projection of spherical hull edges to planar segments, the tangent geometry of disk-hit angular apertures, a first-order bound under the finite cotangent moment, and a conditional-density change of variables. These are analytic checks; repeated finite experiments are not substitutes for their limiting arguments.

Run `python check.py` with NumPy available (see `requirements.txt`). The reproducible seeded experiment evaluates one million independent samples per configuration for sample sizes 3, 4, 5 and 6 with hemisphere area sampling and sample sizes 3 and 5 with the projected-disk sampling law. It checks classical Wendel containment, six rare-clearance coefficients, and one selected-edge colatitude observable. The recorded execution printed `POLE_CLEARANCE_COTANGENT_MARKED_LAW_DIAGNOSTIC_OK`; successful diagnostics are finite-threshold corroboration only.

The historically plausible Carnal 1970 paper could not be obtained from open sources or the authorized institutional connection. Scientific priority with respect to that work remains uncertain; independent mathematical validation has not been performed.
