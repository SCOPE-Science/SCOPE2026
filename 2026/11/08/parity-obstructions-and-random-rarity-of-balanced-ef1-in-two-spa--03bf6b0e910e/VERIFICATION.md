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

# Checks and reproducibility

Run `python verify_euler_fairness.py` from this directory using Python 3 and the standard library. The program computes EF1 directly from each vertex's received valued edge count, checks the exact minimum-group-good and neutral-good thresholds for 741 finite Eulerian cases, checks cycle minimum-allocation counts, and exhaustively enumerates the 4,058 labeled 2-regular simple graphs on three through eight vertices against the exact exponential-generating-function counts. The executable program passed. Analytic proofs, not finite enumeration, cover arbitrary graph size and the asymptotic probability laws. No independent audit was performed.
