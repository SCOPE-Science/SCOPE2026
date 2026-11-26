---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof in `RESULT.md` checks the physical-speed normalization, including the factor of \(1/\sqrt2\) in the half-width of each orthonormally rotated coordinate. For a finite replay, run `python3 CHECK.py` with `mpmath`: it compares the inferred geometric scales with projections computed directly from the four cardinal vertices, and tests the beta ratio, both sides of each inner caustic, the two outer caustics, and critical increments and endpoint limits. The finite comparisons supplement the analytic proof rather than certify its full parameter range. Reconstructing the physical rates separately requires independent calibration of the trap relaxation rate.
