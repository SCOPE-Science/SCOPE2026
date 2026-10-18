---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The scalar stationarity equation for the unique real p-mean, sum_i sign(m−x_i)|m−x_i|^(p−1)=0, gives coordinate monotonicity, translation covariance and |m(x)−m(y)|<=||x−y||_infinity. It yields global n^(1/p) and the n=2 midpoint identity. For n>=3, p<2, an input with one zero residual and balancing remaining residuals gives m(x+epsilon e_i)/epsilon→1; for p>2, differentiating off the diagonal yields nonnegative weights w_i proportional |r_i|^(p−2), with each w_i<=1/2 by residual balance and concavity. Hölder then gives exact (n/2)^(1/p), reached as a derivative at (1,-1,0,...). Continuity/segment split handles the singular diagonal; p=2 is the orthogonal average, n=2 is the midpoint. Proof is correct across all claimed ranges.

## originality

FAIL

FAIL positive stronger-prior implication: published full RESULT of "Sharp l_p stability of finite-chain isotonic metric projections" (Resultary f78c125227d5) explicitly proves the identical scalar p-mean Lipschitz estimates on every pooled block and uses full-pooling perturbations proving the sharp same constants. For a block of size n, that block map is exactly metric projection onto the all-ones line; its upper bounds and sharp full-pooling witnesses already entail every branch. This is statement-level coverage without requiring a matching title or the same target geometry. The 1997/2017 works may be weaker, but the published stronger Resultary record is decisive.

## value

PASS

PASS as a mathematical object: sharp global Lipschitz continuity and discontinuity in p for the canonical metric-projection p-mean are structurally informative and natural in finite-dimensional approximation. Their scientific value remains even though they are already explicitly proved as a block lemma and sharp examples in the stronger published isotonic study; correctness/value cannot override originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
