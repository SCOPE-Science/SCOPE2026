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

# Reproducibility and scope

Run `python3 check.py` with Python 3.9 or later from a folder containing this file and `check.py`. Expected output: `RICKER_BOUNDARY_TWO_CYCLE_CHECK_OK`.

The checker uses exact rational arithmetic for the parameter witness's rare-predator factors and for 300 randomized rational substitutions into the strict Jensen-defect identity. It also checks selected positive threshold gaps and convergence of the first-order gap coefficient numerically. Its finite tests do not constitute a universal proof. The complete analytical proof, including the positive-equilibrium uniqueness argument, tangent and transverse multipliers, local hyperbolicity and onset expansion, is given in RESULT.md. No independent audit or verification is asserted.
