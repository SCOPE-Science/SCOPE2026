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

The half-line recurrence is proved from an exact invariant of the Pell-type integer sequence and verified symbolically in `verify.py`. Global finite-size optimality is proved by strict concavity, supported-interior stationarity, and a uniform diagonal-dominance argument. The entropy boundary limit is proved by a two-ended profile comparison and an exponentially decaying residual.

Reproduce supplemental checks with `python verify.py` (Python 3, SymPy, NumPy, SciPy). The script reports exact recurrence checks and numerical tests for multiple finite path sizes. These finite tests do not certify infinite limits independently; the proof in `RESULT.md` establishes them. No external independent validation has been performed.
