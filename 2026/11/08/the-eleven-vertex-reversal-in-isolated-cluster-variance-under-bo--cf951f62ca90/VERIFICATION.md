---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For Z the sum of the isolation indicators, vertex v has isolation probability 2^(−d(v)). Nonadjacent indicators depend on disjoint edge sets. For an adjacent pair the joint probability is twice the product of the marginals, so twice its covariance equals that joint probability, giving exactly equation (1). The star and double-star formulas follow by summing over leaves and centers. Independently generated every rooted tree through order 11 as a multiset of smaller rooted trees and deduplicated unrooted trees by the least code over all choices of root. Evaluated exact first and second moments over all retained-edge subsets for each unrooted representative, independently of equation (1). The counts for n=3–11 were 1,2,3,6,11,23,47,106,235. The unique minimizers through 10 had star degrees; at 11 the unique minimizer has nine leaves and adjacent degree-5 and degree-6 centers, hence is D(5,6). Its variance is 10239/4096; the star value is 2632703/1048576 and the gap is 11519/1048576. For balanced a+b=n≥11, monotonicity of k/2^k bounds a/2^a+b/2^b by 1/4, with equality only at n=11. AM–GM gives 4^(−a)+4^(−b)≥2^(1−n), with equality only at a=b. The equalities cannot coincide; hence the double-star variance is strictly below (n−1)/4, which is strictly below the star variance. This proves the unbounded comparison analytically.

## originality

PASS

The supported contribution is the sharp eleven-vertex first reversal for the variance of the total number of isolated vertices over all unlabeled trees, including the unique minimizer there and the uniform larger-order comparison. The nearby indexed site-percolation result changes both the random variable construction and the class. The primary sources inspected concern rooted-cluster sizes or cluster distributions rather than this extremum. The standard covariance identity is not credited as new.

## value

PASS

The dispersion of failed connections measured by the total number of isolated vertices is a natural percolation invariant, distinct from a typical cluster size. Comparing the star with all other shapes asks exactly when concentrating dependencies at one hub ceases to be optimal. The sharp first reversal, the unique first alternative, and the proof that this is not a transient anomaly provide a useful exact extremal benchmark rather than an arbitrary finite slice or a numerical restatement of a standard identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
