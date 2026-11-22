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

# Verification and limitations

The analytic evidence is fully provided in `RESULT.md`, including the exact face-area normalization, chamber Jacobian, full CDF quadrature, extremal certificates, spherical cap count and first-overlap lens estimate. `CHECK.py` is a standalone Python 3 diagnostic run requiring only the standard library. It independently generates planar projected polygons from fourteen vertices and compares their areas with the formula; enumerates the 36 first-overlap pairs; and tests exact and asymptotic CDF claims by deterministic midpoint integration. Its successful tests are supplementary diagnostics, not infinite formal proofs. Repeating it with `python3 CHECK.py` requires no outside scientific files.

The full CDF is an exact one-dimensional integral, not an elementary closed form. The area median is numerical rather than interval certified. A plausible broader later projection-density work was not read in full; its possible implications remain a priority risk. No independent audit or independent validation is claimed.
