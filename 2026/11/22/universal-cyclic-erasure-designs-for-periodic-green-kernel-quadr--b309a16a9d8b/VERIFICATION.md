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

# Verification and reproducibility

Execute `python verify_circular_ou.py` using Python 3 with NumPy installed. A successful run prints `PASS 687 independent matrix/gap/weight/erasure/optimizer checks`.

The script compares Schur-complement posterior integral variances from the full periodic covariance matrix against the sum of Dirichlet-bridge variances on cyclic gaps, with six sample sizes, four range parameters and twenty reproducible knot configurations each. It independently checks all Bayesian integral coefficients on multiple grids; enumerates every possible Bernoulli delivery subset for sizes two through six, four survival probabilities and three range parameters; checks the exact expected-risk expression and uniform lower bound; and verifies a continuum of nonuniform optimal four-site alternating-failure designs against nearby nonoptimal perturbations. The tests include single surviving sites, a fully delivered design, nonuniform knots, and several short and long correlation ranges.

Finite numerical verification cannot certify a statement quantified over all sample sizes, all correlated rotation-invariant failure laws and all positive range parameters. The general proof uses the exact Green operator and Dirichlet decomposition, Jensen equality, subgroup arithmetic and dominated convergence, given in `RESULT.md`. Floating point tests are corroboration only. No independent audit, formal proof assistant, or external experimental validation has been performed.
