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

The analytical proof gives an exact scalar KKT reduction, a clipping-pattern no-exit argument for all positive regularization times, a separate zero-time analysis, an explicit counterexample for every failed local budget, and an algebraic feasibility criterion for penalty design. Its scope is finite real weighted stars with positive diagonal quadratic fidelity.

Reproduce the finite checks with `python3 checks/verify_star_fusion.py` from the package root (Python 3 standard library only). The checker finds exact-rational KKT roots, tests the four-leaf positive-time fusion/unfusion witness, and runs many monotonicity and capacity comparisons. The output from a run was: `PASS exact-rational KKT, explicit unfusion, weight-budget and monotone-grid tests: 175512`.

These computations are finite corroboration, not an exhaustive proof for arbitrary real data or arbitrarily many leaves. The mathematical proof is self-contained in `RESULT.md`. The sufficient half of the diagonal-dominance observation is an established generalized-lasso result; the claimed new content is the star-specific converse and exact feasible-weight threshold. Literature priority is qualified.
