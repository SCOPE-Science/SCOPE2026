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

# Verification

`verify.py` is a standalone Python 3 checker requiring SymPy and mpmath. Execute `python verify.py`.

It derives the exact general Laplace transform, checks two exact symbolic identities and the rational example, compares 150 independent matrix-exponential evaluations to the explicit difference solution, computes five successive integral crossover horizons, and samples symmetric mixing strengths to check monotone movement toward its analytic limiting time. All checks passed. Reproducible reference values: \(t_0=0.48562329495372988614\ldots\), \(t_1=0.92165190130663244676\ldots\), and \(t_\infty=0.32437208648653150558\ldots\).

These finite computations support, but cannot independently certify, universal quantifiers. The full proof is in RESULT.md, including strict log-concavity, uniqueness, strict hierarchy, endpoint asymptotics and exchange monotonicity. No independent external audit has been performed.
