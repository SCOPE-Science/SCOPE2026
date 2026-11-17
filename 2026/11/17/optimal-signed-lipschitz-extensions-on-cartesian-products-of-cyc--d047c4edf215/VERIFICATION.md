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

# Finite verification and limitations

The general result is proved in `RESULT.md`; this numerical program supplies a separate bounded consistency check, not an exhaustive proof of infinitely many parameters.

Run `python check_torus.py` in an environment with NumPy and SciPy (HiGHS linear programming). The program independently generates the graph-edge Lipschitz inequalities, optimizes the Kantorovich–Rubinstein dual linear programs, tests the uniform, correlated and independent optimal couplings, probes signed perturbations, and checks the rank of predicted affine marginal constraints. It evaluates the products \(C_3\square C_3\), \(C_3\square C_4\), \(C_4\square C_4\), \(C_4\square C_5\), \(C_4\square C_6\), \(C_5\square C_5\), \(C_5\square C_6\), and \(C_3\square C_4\square C_4\).

The expected final line is `CYCLE_PRODUCT_SIGNED_OPTIMALITY_LP_CHECKS_PASS`. Numerical tolerances apply only to the finite LP corroborations; no numerical solver is used for the all-parameter proof. A full external independent audit remains unperformed.
