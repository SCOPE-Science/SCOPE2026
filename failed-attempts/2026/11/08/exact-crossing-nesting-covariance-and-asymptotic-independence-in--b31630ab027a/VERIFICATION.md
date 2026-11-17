---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Uniform random matching is equivalently obtained by ranking n iid pairs of continuous uniform endpoints. For fixed chord length t, p_X=2t(1-t), p_N=t^2+2l(1-r), p_A=l^2+(1-r)^2; exact integration on 0<l<r<1 gives projection variances 1/45 and mixed projection covariance 0. Identical chord-pair indicators contribute -1/9 mixed covariance, disjoint pairs contribute zero and overlapping different pairs contribute zero, yielding Cov=-n(n-1)/18 and stated marginal/aligned moments. Hoeffding order-2 degenerate remainder is O(n^2) in L2, negligible under n^{3/2} scale, so iid vector CLT yields independent standard normals. Independently enumerated all (2n-1)!! matchings n=2..7 with exact rational moments; this is finite corroboration only.

## originality

FAIL

Published October 13, 2026 result establishes the identical mixed covariance -n(n-1)/18, correlation -5/[2(n+3)], bivariate independent Gaussian CLT, and identical first-order projection orthogonality for totals of pairs of chords. The aligned count is binom(n,2)-X-N, so its covariance consequences are immediate. A second October 18 published result confirms the prior coverage. No new mixed theorem survives.

## value

FAIL

The exact negative covariance and the orthogonality mechanism are worthwhile stochastic-combinatorial information, but this package duplicates the full already published theorem for identical variables and sample space. Its aligned statistic is an elementary deterministic linear combination, not a distinct motivated unknown fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
