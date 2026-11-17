---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed Cov(Q_F,Q_G)=4∑_{i<j}FijGij and spectral monotonicity via doubly-stochastic p_kl; n=2 has two ordered sign-response levels. In n=3 the eight sign vectors reduce to four equal-mass antipodal classes; Birkhoff/rearrangement says identity coupling maximizes covariance iff all six pairwise class differences agree in sign. Exact rational L²=[[21,24,14],[24,401,2],[14,2,13]], class responses and all 24 class permutations independently evaluated: shared contrast variance 62/9, second/third coordinate swap 2/9, ratio31; Gershgorin diagonal-dominance SPD and increasing f,g on positive spectrum. Actual verify_coupling.py checked structurally. No higher-dimensional optimality claimed.

## originality

PASS

The signed-permutation universality theorem already shows any optimal n<=3 joint probe coupling is realizable by a signed permutation; it does not provide the shared-identity six-inequality criterion, monotone same-operator spectral covariance or the 31-fold polynomial example. Classical monotone rearrangement is credited. No source inspected gives this precise pairwise criterion and same-matrix witness.

## value

PASS

The exact boundary determines when the cost-free common-probe variance reduction widely used in multilevel stochastic trace differences is optimal among ALL full-product-sign-preserving couplings; strict quantitative 31-fold improvement and exact implementable permutation are genuine design counterexamples beyond merely restating Birkhoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
