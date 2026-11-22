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

The all-size proof reduces the Hermitian matrix to one central Schur complement and then evaluates a monic quotient at its distinct positive weight values. This argument is analytic and holds for arbitrary real flux angles and every integer \(m\ge2\).

Exact reproduction: run `python verify_exact.py`. Six exact SymPy characteristic-polynomial identities for two through four petals, classwise inverse reconstruction, each rooted third moment, a nontrivial isospectral pair and its broken-weight counterexample passed.

Independent floating-point stress test: run `python verify_numerical.py`. For each size \(m=2,3,\ldots,9\), 30 seeded sets of positive integer internal weights and real phases were tested. Four spectral determinant evaluations per sample, deconvolved classwise inversions and every rooted cubic moment passed: 240 cases total.

The verification code tests finite cases; correctness for arbitrary \(m\) rests on the displayed Schur complement and evaluation proof. Historical priority and independent validation have not been established.
