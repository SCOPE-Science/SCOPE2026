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

The exact ray-length reduction, four minimizing charts, six maximizing charts, and limiting tangent-area integrations are proved in `RESULT.md`. To reproduce deterministic diagnostics with Python 3 standard library, run `python3 checks/verify_sphericon.py` after extracting all embedded files to their relative paths. The script uses no network access or third-party packages and checks exact extremal directions, both local normal forms, and the area constants numerically.

The separate Sobol experiment used \(2^{21}\) spherical directions and checked convergence trends; it is not required for the proof and is not an exhaustive certificate. The total-variation conditional laws follow from the analytic changes of variables and dominated convergence, not from simulation. The full original 1999 magazine article could not be read in its entirety; available construction descriptions and other relevant sources were inspected. No independent audit has been performed.
