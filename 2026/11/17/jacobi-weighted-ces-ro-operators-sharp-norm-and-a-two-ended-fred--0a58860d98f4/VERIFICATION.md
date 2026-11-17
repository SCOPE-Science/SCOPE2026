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

Use Python 3 standard library: `python CHECKER.py`. The embedded checker completed 181 finite assertions covering exact rational parameter identities, the weighted logistic norm density, representative phase regimes, and semigroup translation inequalities. These checks contain no mathematical proof of an infinite-dimensional Fredholm statement.

The proof is in `RESULT.md`. Its critical reusable identities are the isometry \(Uf=xf\), transformed density \(\rho(y)=e^{-pAy}(1+e^y)^{p(A-B)}\), exact one-sided integration conjugacy, and derivative factorization \(H-\lambda I=-\lambda(D-1/\lambda)H\). The closed-range and index claims are justified by the explicit one-sided inverses and the dual annihilator, not by matrix truncations. Boundary non-Fredholmness is established using normalized cutoff Weyl sequences; zero is handled by high-frequency differentiation tests.

No independent mathematical audit has been performed. Residual priority risk includes general weighted differential-operator dichotomy theorems that may cover a broader formulation.
