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

# Reproducibility notes

Run `python3 verify_progress.py` with a standard Python 3.9+ interpreter. The script uses only the standard library, no downloaded data, and deterministically reports `CHECKS_OK 460` on success. It independently integrates the exact first-step signed-angle expression, checks agreement with the explicit arcsinh/arcsin formula, examines finite anisotropy minima and verifies the isotropic limit. All required input parameters and the construction are stated in `RESULT.md`.

The finite checker supports the exact formulas but does not certify uniformity as \(\delta\to0\); that claim is established by the integral evaluation and compact, uniform asymptotic analysis in `RESULT.md`. No independent verification has been performed.
