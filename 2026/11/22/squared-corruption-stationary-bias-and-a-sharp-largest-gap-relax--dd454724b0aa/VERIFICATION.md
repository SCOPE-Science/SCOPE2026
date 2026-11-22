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

# Reproduction and bounds
Run `python3 verification/verify.py` with Python 3.10+ standard library. Its exact rational checks verify transition normalization and detailed balance for multiple distinct-level configurations; verify the exact two-level stationary and all-time formulas; and verify the sharp corruption partition bounds. A separate arbitrary-precision decimal diagnostic tests the unique-largest-gap spectral constant in a three-state example. The program prints `VERIFY_OK 11746` and `SPECTRAL_DIAGNOSTIC_OK ...` if successful.

The spectral limit itself is an **infinite-parameter statement** and is established by the variational compactness proof in RESULT.md; the displayed finite numerical check is not proof. The fixed exponential model is different from median/MAD-adaptive exponential methods. No claims are made for general higher-dimensional matrices, tied maximal gaps, or independent audit.
