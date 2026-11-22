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

# Reproducibility and boundaries

With Python 3 and SymPy, run `python CHECK.py`. The program asserts the exact equilibrium formulas, nonzero algebraic denominators under the theorem assumptions, the affine sign comparison, recovery and infection balance, strict positivity, and the rational witness including the unique crossing at \(\delta=4\). It also runs a finite rational parameter sweep of 36 systems; this sweep is a diagnostic rather than an infinite proof.

The infinite-parameter proof is the reciprocal linear system and affine sign argument in `RESULT.md`. The proof of local asymptotic stability is Theorem 3 of Gatti--Como (arXiv:2604.21065) under its own stated assumptions. The result does not assert nonlinear global convergence, stochastic fate, or a multi-group ranking classification. The present checks are reproducible algebraic validations and a self-review, not an independent audit.
