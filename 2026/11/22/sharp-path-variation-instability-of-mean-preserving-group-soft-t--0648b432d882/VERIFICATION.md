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

# Verification record

The bundled standard-library-only `verification.py` checks the algebraic certificate in finite dimensions. Invoke `python verification.py` in the same directory. Its successful final line is `ALL_CENTERED_GROUP_SHRINKAGE_BV_CHECKS_PASS`.

Analytical checks: centered Euclidean proximal formula and its derivative; induced rank-one path variation norm; dual sign and centered cut factorization; symmetric rank-two eigenvalues; alternating-sign maximum \(4n-6\); midpoint cut maximum \(\lfloor n^2/4\rfloor\); explicit critical perturbations; distinction between a sharp supremum and attainment. These are presented and proved in `RESULT.md`.

Computational checks: exhaustive signs and cuts for \(2\le n\le9\), near-threshold witnesses, 2,550 deterministic random two-input and one-input variation checks on dimensions \(2\le n\le18\). Floating-point tolerances account for numerical cancellation near the shrinkage sphere. The all-dimensional statement is proved analytically, not extrapolated from the experiments.

The standalone code verifies mathematical examples only. Independent audit, broader unindexed literature completeness, and generalization beyond finite real paths are not established.
