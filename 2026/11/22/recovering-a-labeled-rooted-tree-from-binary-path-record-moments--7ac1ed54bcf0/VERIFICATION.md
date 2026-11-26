---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Exchangeability gives the reciprocal path-size marginal. For two comparable distinct vertices, their record events are tests of two independent insertion ranks in the uniform relative ordering of the longer path (the insertion-rank vector is in bijection with the full permutation). For incomparable vertices transform marks to independent uniform survival values. On t<s the integrand is t^(k+a-1)s^(b-1) and integrates to 1/[(k+a)(k+a+b)]; the other half gives the analogous k+b term. Subtracting the marginal product gives the positive covariance claimed. The unique zero-covariance candidate at the preceding depth is then the parent; the root is identified by marginal one. For independent repeated vectors, the n+binom(n,2) bounded scalar averages obey the simultaneous Hoeffding bound with error eta=1/(24n^3); no within-vector independence is needed. The smallest spacing of reciprocal depth means is 1/[n(n-1)] and covariance error is at most 3 eta. The three covariance denominator factors are at most n (the largest is the union size k+a+b), so the record's weaker lower bound 1/[n^2(2n-1)] also holds. The stated depth rounding, 1/(4n^3) threshold, and sufficient replication count therefore work, including with the root constant and with no incomparable pair. The supplied finite checker and its reported output were inspected, not executed; the uniform bound is proved analytically.

## originality

PASS

Best-of-knowledge pass for recovering the full vertex-labeled tree, including unary ancestry, by the particular marginal and covariance signature of all path minima, with an explicit uniform replication guarantee. The record process, independent ranks along a path and concentration tools are not novel.

## value

PASS

This turns a standard forward process into a concrete inverse result with severe data compression: one synchronized bit per label suffices as a repeated observation, and only first and pairwise means are needed. The explicit nonvanishing separation provides a noise-to-exact-recovery guarantee for every rooted labeled tree, not just for a random-tree ensemble or a restricted degree class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
