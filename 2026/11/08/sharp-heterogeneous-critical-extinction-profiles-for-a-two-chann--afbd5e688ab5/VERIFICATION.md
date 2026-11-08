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

Run `python check.py` with Python 3, numpy and scipy. The program first executes rational exact checks of the three-node triangle plus one environment, including the spectral-threshold equality, normalization \(W=9/2\), coefficient \(K=5/3\), and its two coordinate limits. It next integrates the actual saturating nonlinear ODE to three increasingly late times to test convergence. Finally, 30 heterogeneous connected instances check the eigenvectors, left/right zero modes, spectral bound, normalization and quadratic coefficient against direct matrix calculations.

Printed final line: `ALL CHECKS PASS`. Numerical integration and random testing provide reproduction and error detection, not proof for all finite hypergraphs or infinite time. The analytic proof is in RESULT.md. The independent audit remains unperformed.
