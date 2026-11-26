---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In the uniform matching, edge probabilities and conditioning on a specified chord give the stated exact moments; an independent bit-mask enumeration of all 3, 15, 105, 945, 10395 and 135135 matchings at n=2 through 7 matched all five moments as reduced rational numbers (at n=7 they are 7, 252/13, 28/3, 50568/1859 and 2058/143 in the order EX, ET, Var X, Var T, Cov). For the unbounded argument, ranking iid paired endpoints is uniform and preserves the endpoint order within each pair. The cusp error is O_p(n^(4/3)) by DKW and the bounded chord-length density. In the linear rank correction, conditioning on the first chord gives zero by uniformity; in the reverse direction the one-endpoint contribution J has J(0)=0 and J'(x)=2[f(1-x)-f(x)]=0 a.e., and the centering term vanishes by antisymmetry. Disjoint summands and summands sharing only one index therefore give zero covariance in the off-diagonal sum, so its variance is O(n^2). The projection vector for t uniform on [0,1/2] is (2t(1-t)-1/3, 2t-1/2). Its covariance gives the claimed Gaussian law, determinant 1/8640, limiting slope 1/2 and squared correlation 15/16. Finite enumeration is a check of moments only, not of convergence.

## originality

FAIL

A distinct published Resultary finding dated 2026-10-18 states the same theorem for the same rank-defined shorter-arc span and crossing-pair count, with covariance matrix transposed in coordinate order only, the same finite moments and the same regression consequences. This is demonstrated prior coverage, not a claim about dependence or authorship.

## value

FAIL

The regression invariant is meaningful in isolation, but the submission repeats all of it and the complete joint law. The alternative empirical-CDF argument does not establish a useful stronger estimate or a new class of statistics: the earlier occupancy proof already gives O_p(n) error against the same leading iid span sum, while the submitted bounds give O_p(n^(4/3)). No separately substantiated advance remains in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
