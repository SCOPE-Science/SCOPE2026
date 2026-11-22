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

# Reproducibility and scope of checks

The analytical proof in `RESULT.md` establishes the universal lower bound, nonattainment, construction of the minimizing sequence, convergence, the critical vanishing exponent, and the three-state realization. The standard-library `check.py` checks stationary-rate perturbations with rational numbers, verifies the three equal edge-current derivatives and friction, and numerically checks positive excess and convergence in a scalar exactly soluble example. Execute `python3 check.py` in the directory containing these files; no third-party Python dependencies are required.

The numerical tests alone do not establish the optimization over arbitrary admissible paths. Conversely, the analytic theorem is exact only for the leading-order slow-driving functional; higher-order physical corrections are not analyzed. Independent scientific audit has not been performed.
