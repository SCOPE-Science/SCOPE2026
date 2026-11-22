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

# Mathematical verification

The analytic proof uses the stationary renewal representation, Mori et al. [1, Eqs. (4), (9), (10)], dominated convergence, the exact Laplace moments \(\mathbb E|Z|^p=\Gamma(p+1)\), and finite binomial expansion for even powers. These prove the displayed universal limit and all-rate derivative sign. Run \`python3 check.py\` with Python 3.10+; it reports exact algebraic parameter checks. For additional independent diagnostics, generalized-Gauss–Laguerre integration was performed at 95 nodes per variable on six tail indices and five reset rates. Those finite computations are illustrations, not a substitute for the proof.

Proof limits: the tail theorem presupposes the explicit log-density bounds and the finite \(p\)-moment; it does not cover zero-width point resetting, external potentials, reset apparatus work, or every possible stochastic-entropy convention. Publication priority has not been independently audited.

Reference: https://arxiv.org/abs/2211.15372.
