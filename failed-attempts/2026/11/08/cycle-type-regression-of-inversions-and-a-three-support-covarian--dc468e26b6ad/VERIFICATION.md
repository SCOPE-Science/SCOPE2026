---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The conditional average over relabelings is a five-overlap-type inversion count: probabilities 0,1/3,1,2/3,1/2 yield E[inv|C_1,C_2]=n(n-1)/4+n(1-C_1)/6-C_1(C_1-1)/12+C_2/6. Classical cycle factorial moments then yield covariance -(n+1)/6 at j=1, 1/12 at j=2, 1/6 at j=n, and zero at other j, including n=3 and j=n-1 cancellation. Independently enumerated all permutations n=3..7 to verify the class regression and n=3..6 for cycle-count covariances.

## originality

FAIL

FAILED by exact earlier general theorem. Axel Hultman, Permutation statistics of products of random permutations (2013 preprint, 2014 journal), Theorem 6.2, gives conjugacy mean of inversions as n(n-1)/4 chi^(n) -(n+1)/6 chi^(n-1,1) -1/6 chi^(n-2,1,1). The elementary identities chi^(n-1,1)=C_1-1 and chi^(n-2,1,1)=binom(C_1-1,2)-C_2 transform it EXACTLY into submitted formula (1) for every n>=3. The covariance entries are routine evaluations via the established cycle factorial moments, with j=2 previously explicitly reported as prior by 2026-11-02 positional-two-cycle work. This is implication coverage despite different character language.

## value

FAIL

The apparently substantive full cycle-type regression is identical to Hultman Theorem 6.2; the remaining three-support covariance is a short mechanical consequence using classical disjoint-cycle factorial moments. There is no independently motivated new structural theorem beyond existing class projection plus routine linear covariance evaluations. Exactness and executable checks do not restore distinct value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
