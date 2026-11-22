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

# Reproducibility

Run `python3 checks/verify_k3n.py` with Python 3 from the package root. The checker uses only the standard library. It verifies the eight exact rational matrix inequalities, independently enumerates all 432 spanning trees of the four-column graph and their signs against every one of 4096 Fourier masks, and searches every mask through the conjectured threshold for 8, 12, and 16 columns. The expected success marker is `K3N_SHARP_FOURIER_THRESHOLD_VERIFIED`.

The general assertion is established by the exact Schur-complement and positive-semidefinite proof in `RESULT.md`. Exhaustive tests for any fixed dimensions alone would not prove the general result. No independent audit was performed.
