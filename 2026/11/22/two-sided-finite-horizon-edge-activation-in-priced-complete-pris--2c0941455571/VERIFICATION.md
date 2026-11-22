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

The deterministic `verify.py` program requires Python 3 and NumPy. Execute `python3 verify.py` beside `RESULT.md`. The reproduced output is `VERIFY_OK 15520`.

The independent matrix assembly checks the spectrum of weighted clique-prism Laplacians against the four eigenvalue classes derived in the proof. Further checks compare the prescribed optimum against symmetric feasible grids, randomized asymmetric feasible weights, and each side of both exact support-activation thresholds. The code separately checks the budget identity.

These are finite reproducibility checks, not independent mathematical certification and not an exhaustive search over real edge allocations, parameters or times. Strict convexity, boundary KKT signs, and the spectral product identity provide the infinite-family proof. The limiting laws are obtained analytically from the exact threshold and interior equations. A separate independent audit has not been performed.
