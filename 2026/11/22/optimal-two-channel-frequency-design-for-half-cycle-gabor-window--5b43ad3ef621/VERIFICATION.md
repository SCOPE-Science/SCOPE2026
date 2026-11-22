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

# Reproducibility and verification

Execute `python3 CHECK.py` with Python 3.10 or later; the script uses only the standard library. Its run on the included unmodified source completed **85,546 passing assertions**. The finite tests independently calculate Fourier coefficients of the rectangular window, evaluate all candidate frequency gaps in tested dimensions, construct full complex-valued frame matrices, verify off-diagonal Fourier cancellation, and test unequal power allocations.

The all-parameter claims rest on the analytic proof in RESULT.md. Finite verification does not establish the infinite integer quantifier, originality, or independent certification. The principal possible bibliographic risk is an older formulation of optimal pairs of shifted discrete Fejér-kernel responses.
