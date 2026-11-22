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

Execute `python3 check_resonance.py` from this directory. It uses only the Python standard library, tests the exact algebraic-drift identity against 400 randomly chosen states and parameters, checks the two-step global contraction for 100 sets of initial fibers, checks six supercritical root/stability instances, and compares one irrational-rotation coordinate mean to the proven first-order bound. The deterministic run returned PASS.

The infinite-time statements rely on explicit analytic identities, a two-step contraction of continuous periodic fiber graphs, unique ergodicity of irrational rotation, and elementary scalar bifurcation analysis. Finite tests do not establish the all-state or all-parameter conclusions. No independent mathematical validation was conducted.
