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

The claim is established analytically in `RESULT.md`. `verify.py` performs exact rational finite-state probability checks, tests the uniform negative generator drift over finite state ranges, compares with a labeled event-level simulation, and samples a large finite graph for the Poisson-parity diagnostic. The fixed-size checks do not establish the infinite-size limit; that step uses martingale fluid convergence, deterministic-intensity Poisson time change and the explicit Lyapunov bound. Execute `python verify.py` with a standard Python 3 interpreter; no external packages are necessary. Rates are per currently available edge, with internal-edge rate one and interclique rate \(\lambda\).
