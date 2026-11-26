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

With the stipulated Loday embedding and known path-tubing face lattice, each ridge is exactly a pair of nested or disjoint separated proper intervals. Using [p,q]↦(p−1,q+1) gives the equivalent test of noncrossing diagonals of an (n+2)-gon. Projection of the facet normal to the sum-zero tangent space gives its signed cosine (n|I∩J|−|I||J|)/sqrt(|I||J|(n−|I|)(n−|J|)). Nested pairs have positive outward cosine and hence obtuse interior angle; disjoint pairs have the opposite signs. The complementary length substitution c=n−b exchanges the angle supports, not the multiplicities. Place the outer interval and then the inner interval to recover (n−b+1)(b−a+1); for two intervals in left-to-right order the positive separation gap gives binom(n−a−c+1,2). Independently, the acute total is the number of four distinct cuts from n+1; the total ridge count is binom((n+2)(n−1)/2,2)−binom(n+2,4), subtracting one crossing for each four polygon vertices. These give all stated totals and the precise deficit. A uniform acute ridge is a uniform distinct cut quadruple. For the nested branch, only O(n³) pairs share a cut, and only O(n²) quadruples would use the forbidden full outer interval. Scaling by n yields uniform continuous order statistics and the five spacings. Substitution gives both displayed laws, with the two branches asymptotically equally likely and denominators positive almost surely. The Dirichlet vector is on the intrinsic four-dimensional simplex in five coordinates (the phrase ‘five-dimensional simplex’ is imprecise); the open angle ranges are probability-one ranges, not claims that the topological supports omit their endpoints.

## originality

PASS

The facet geometry and pairwise normal formula are standard ingredients and the all-ridge count is a standard face count. The distinct contribution is the complete signed angle multiset with its branch-resolved multiplicities and the limiting distribution for uniform ridges of this Euclidean embedding. The cyclohedron near match has the same individual angle formulas but different multiplicities and a different limiting law.

## value

PASS

The full multiset gives quantitative shape information not encoded by the combinatorial type or an edge census. The reflected support with unequal incidence and the explicit branch-resolved weak limit specify which angular deviations occur and how often for a natural ridge sampling rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
