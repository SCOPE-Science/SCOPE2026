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

Run `python verify.py` with SymPy, NumPy and SciPy. The script symbolically recomputes the two differential identities and tests nine parameter/initial-data configurations, 54 clock samples, nine integrated-penalty values and nine long-time equilibrium values. These are reproducibility checks, not independent validation. The all-parameter conclusions follow from the proof in `RESULT.md`; numerical samples do not certify universal convergence. The script has no network access requirements.
