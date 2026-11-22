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

Run `OPENBLAS_NUM_THREADS=1 python verify.py` in the extracted directory after installing NumPy and SciPy. The program constructs full weighted helm Laplacians independently of the orbit formula, checks inverse-eigenvalue traces, solves the exact one-dimensional stationarity equation, probes feasible local departures, and compares asymptotic scales. Its completed run produced `OK finite assertions: 389`, with the tested large sizes and observed normalized values printed for transparency.

The proofs of strict convexity, exact spectrum, eventual hub saturation, derivative asymptotics and the maximum-degree ratio are analytic and are supplied in `RESULT.md`. Diagnostics are finite and do not purport to prove an infinite asymptotic statement. No independent external mathematical audit has been performed.
