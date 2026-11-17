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

# Reproducibility and limits

Execute `python verification/check_spiked_angles.py` from the extracted package with Python 3, NumPy and SciPy. The checker evaluates the analytic densities numerically with quadrature; it reconstructs support functions of explicit simplex vertices for 720 random tests; it compares simulated origin/partial-location masses with asymptotic formulas for four spike regimes using 240,000 simulated random objectives. The reproduced output ends with `SPIKED_LECTURE_HALL_PASS analytic_norms=7 finite_vertex_tests=720 stochastic=240000`.

The geometry and probabilistic limits are justified in `RESULT.md`, not by the finite experiments. Numerical tolerances are intentionally larger than Monte Carlo sampling errors to allow finite-size discretization bias. The use of a classical Brownian maximum-time density and the lack of an exhaustive historical priority review are explicit limitations. No independent validation has been conducted.
