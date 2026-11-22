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

The continuous optimization is proved analytically in `RESULT.md` via strict log-concavity and explicit Karush–Kuhn–Tucker conditions. The complete allocation is specified by a unique monotone scalar root and strict branch-activation thresholds. The infinite geometric-habitat corollary follows from finite-support optimality, tail convergence, and asymptotic inversion.

Run `python3 checker.py` in this directory. The checker uses only Python's standard library. In an actual execution it passed 39,710 supplementary checks of feasibility, optimized values against random feasible competitors, threshold ordering, the common-barrier effort inequality, and the exact geometric-weight threshold identity. These finite checks do not certify the theorem on infinite parameter domains, nor do they establish historical novelty.

Model limitations include independent passage, an idealized exponential return on every barrier, linear improvement costs and no calibrated site-specific costs or constraints. This record has not undergone independent external scientific validation.
