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

# Verification of second-order recoding fluctuations

Run `python verify.py` with Python 3 standard library. The checker tests exact rational parity expansions, independent-degree convolutions, subset counting, finite critical means, harmonic weight identities and the closed-form second-order covariance constants. Finite checks are consistency tests only; their output is not a proof of the infinite central limit theorem.

Analytic verification: a uniform binomial/log approximation identifies the first-order dependence on centered negative-increment count, whose Taylor remainder has aggregate \(L^2\)-size \(O(\log N)\). Harmonic-weight triangular arrays obey Lindeberg and give covariance matrix with entries \(1,1,2\). Conditional coefficient-row independence gives a stable Gaussian noise term, independent of increment history. Cross-covariation moment limits follow from exact conditional orthogonality and an \(L^2\)-negligible remainder. The first-order quenched law is checked via Hoeffding, Fubini and the martingale functional CLT.
