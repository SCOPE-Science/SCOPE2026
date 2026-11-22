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

The theorem is verified analytically by the three exact interpolation moments at two sixth-root circle nodes, the Banach-valued maximum-modulus reduction, and the scalar quadratic squared-modulus identity. These are written in full in `RESULT.md`.

Reproduction: run `python3 check_quadratic_section.py` from the directory containing the unpacked files. It performs exact calculations in a rational quadratic field and 384 supplemental finite trials, and prints `QUADRATIC_BIDISK_SECTION_EXACT_CERTIFICATE_OK 384`. A finite check is not evidence of general validity; the proof is the exact interpolation certificate and the extremal polynomial.

The scalar equality classification is derived from saturation of both node estimates and a stationary condition at an interior boundary angle. The proof does not characterize all vector-valued equality cases, higher degrees, or full-function-space Taylor truncations. No independent mathematical audit has been performed.
