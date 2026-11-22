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

# Mathematical verification

`RESULT.md` gives a direct proof from the half-line Jacobi recurrence through threshold inertia to a uniform secular Taylor expansion. Its hypotheses exclude uncontrolled simultaneous approach of \(\alpha\) to a threshold. A standalone executable `check.py` uses Python 3.10+, NumPy 1.24+, and SciPy 1.10+. Running `python check.py` on the packaged source printed `WEAK_BLOCK_EDGE_DIAGNOSTIC_OK 104`. The finite tests compare finite Jacobi sections only away from band thresholds and use the exact scalar matching equation for asymptotic coefficients near the edge. Diagnostics do not certify infinite limits or historical uniqueness; those are assessed through the proof and literature comparison, respectively. Independent mathematical validation has not been performed.
