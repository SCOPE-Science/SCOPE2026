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

The standalone `verify.py` uses exact integer polynomial arithmetic, not numerical approximations. For each \(2\le n\le12\) it constructs \(\sigma_\lambda\sigma_\mu a^2\) using the two-variable Schur formula, evaluates the Grassmannian top coefficient, checks that the middle Gram matrix equals the displayed integral tridiagonal matrix and has determinant one, and checks that all chosen high-degree pairings form lower-triangular matrices with diagonal one. It also checks the Plücker degree against the Catalan formula. Replay command: `python3 verify.py`.

Observed terminal output: `ALL_EXACT_SCHUR_PAIRING_CHECKS_OK`. The mathematical proof uses the general Pieri rule and an explicit all-parameter indexing argument. The finite checker does not certify the entire infinite family or an exhaustive novelty search. The comparison with previously published formulas remains limited to the sources and statements identified in the review.
