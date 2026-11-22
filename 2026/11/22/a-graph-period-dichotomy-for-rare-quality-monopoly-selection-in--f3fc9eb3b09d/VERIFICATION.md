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

# Reproducibility and proof checks

The independent-Bernoulli engagement formula, the one-step rare-quality monopoly exit rates, the transient fundamental-matrix expression and the graph-period reachability proof are given in `RESULT.md`. They establish the general theorem without relying on computer experiments.

Run `python verify.py` with Python 3 and NumPy installed. The checker enumerates all \(2^6=64\) engagement states for the path and triangle on three users. It constructs the exact-form transition formula as floating-point matrices, computes zero-strength absorption probabilities from the linear system \((I-Q_0)h=r\), and solves the positive-strength stationary distribution directly. It asserts that the path has zero blackout contribution, the triangle has positive blackout contribution, and that the stationary mixture approaches the predicted limit.

The explicit parameter set is \(a_v=b_v=1/2\), \(g_v=1\), \(q_1=4/5\), \(q_2=3/5\), and \(\varepsilon=10^{-5}\). For the path the predicted limit is \(4/7\), while for the triangle it is approximately \(0.571868335801036\). Finite-precision inversion is used only for corroboration; it cannot establish the infinite-family graph-period criterion. There is no independent scientific audit.
