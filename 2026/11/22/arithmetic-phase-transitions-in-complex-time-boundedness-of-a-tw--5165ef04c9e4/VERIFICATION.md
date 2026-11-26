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

# Verification of the slice-period classification

The analytic proof in `RESULT.md` checks boundedness via coordinate restriction and Fubini. Below the first threshold, the boundary of the two-window indicator is Haar-null; density of the irrational line transfers a hypothetical slice translation to an almost-everywhere window symmetry. The first Fourier coefficient of each proper arc rules out any other circle translation. At both thresholds equality is allowed by the closed boundedness test.

The legacy `check_geometry.py` samples densities from the known two-rate region. It does not verify the slice translation groups, and the present proof does not use it. There is no computational or formal proof certificate for the slice-period statement.
