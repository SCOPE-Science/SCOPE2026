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

Sorting a supporting covector with three distinct levels gives an ordered partition; strict ordering of the generator ensures dimension n−3 and prevents collapsing faces. The ridge lies in the two nested-subset facets. Sum-zero projections of their normals have product ac/n and squared norms a(b+c)/n and c(a+b)/n, so the interior angle is the supplement of their acute separation. Counting ordered partitions gives the stated multinomial measure conditioned on nonempty blocks. The cyclic exterior cotangents have pairwise products a/n,b/n,c/n; their sum of angles is π, proving the exact mean by cyclic invariance. Independently put q=B/n, t=q−1/3 and d=(A−C)/(2n). The angle is π/2+atan(sqrt(((1−q)²/4−d²)/q)), hence its d=0 part is π−2 atan(sqrt(q)) and its d² coefficient is −4 sqrt(q)/[(1−q)(1+q)²]. Expanding gives L=−3 sqrt(3)t/4, Q=sqrt(3)(27t²/32−9d²/8), C=−sqrt(3)(81t³/64+27td²/16). The one-draw centered coordinates (T,D)=(2/3,0),(−1/3,1/2),(−1/3,−1/2) are equiprobable. Their variances are 2/9 and 1/6, covariance zero, and third moments E[T³]=2/27 and E[TD²]=−1/18. The linear term gives the CLT and 3/(8n); the cubic contribution 2LQ has expectation −9/(16n²). Pairings of draws give E[Q²+2LC]=99/(64n²)+O(n⁻³) (exactly 99(2n−1)/(128n³) including the one-draw terms). Degree-five centered moments and absolute sixth moments are O(n⁻³); outside a fixed balanced neighborhood the bounded angle contributes exponentially little, as does conditioning on nonempty blocks. Thus the net coefficient is 63/64. The sole size triple at n=3 gives zero variance; for n≥4 cyclic placements of n−2 in (n−2,1,1) yield different angles.

## originality

PASS

The supported distinction is the type-A count-weighted spectrum and especially its second-order variance. The normal fan, ordered-partition method, aggregate mean and pointwise angle as a function of three sizes are not independent novelty claims.

## value

PASS

Count-sampled dihedral concentration is a natural statistic on this classical fan, distinct from the traditional angle sum. The exact second-order term quantifies convergence and can distinguish fans that share the same leading normal law. It is evaluated by geometric and fourth-order sampling calculations, not supplied by the known aggregate mean or a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
