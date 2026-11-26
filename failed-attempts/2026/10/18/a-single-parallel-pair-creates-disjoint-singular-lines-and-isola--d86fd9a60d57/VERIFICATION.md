---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

An independent chart check uses the partition constraints: group {1,2} into a single part and treat the rest as singletons. The polytope has nonnegative coordinates, part sums at most 1, and total 2. This description is integral: its part-sum projection is the rank-two hypersimplex, and splitting the {1,2} sum between two coordinates lifts a convex combination of its vertices to a convex combination of allowed bases. At a vertex with both basis elements ≥3, the active constraints on differences give nonnegative row supplies −δ_i,−δ_j and nonnegative outside demands, with equal total. Integral transportation realizes every lattice point using complete bipartite exchanges. At the vertex {1,j}, the independent nonnegative coordinates for the supplies are −(δ_1+δ_2),−δ_j, with demands on [n] excluding 1,2,j; the extra coordinate δ_2≥0 is a unimodular free factor. This gives saturated chart semigroups D_{2,n−2} and A¹×D_{2,n−3}, with minors as the complete relation ideal (exchanging row assignments preserves the margins). On a nonzero matrix entry the determinantal cone is smooth, and the origin has tangent dimension 2q>q+1 for q≥2. The special factor is the primitive edge direction e_2−e_1: the two endpoint axes glue to P¹. Distinct edge orbit closures share no invariant vertex and hence no orbit. Segre degree gives multiplicity q. The cone is nonsimplicial (2q rays in dimension q+1), as is its product at the special endpoint; the transverse cone persists over the line's torus, so the non-Q-factorial support is exactly the singular support. At n=5, q=2 on the lines and q=3 at isolated points; for n=4 the line chart is smooth. The lattice and minor arguments are characteristic-free. Read but did not execute the frozen finite checker.

## originality

FAIL

The earlier complete-multipartite edge-toric classification in Resultary 99655ba7daaa gives this exact result after specializing the part sizes to (2,1,…,1), and more (pointwise chart, local class group and canonical class). It states its theorem over C; passing to an arbitrary algebraically closed field does not introduce a new singularity analysis here. The prior proof uses equal integer exponents, saturated marginal semigroups, solving the minors on nonzero entries, Segre degrees, and toric cones. All remain valid over the new field without a characteristic-sensitive step. The broader field statement is correct but does not leave a substantive distinct theorem under this comparison.

## value

FAIL

The minimal parallel-pair example is geometrically well motivated, but as a separate finding its component counts and transverse types are routine substitutions in a known exact multipartite classification. Extending the same integer-exponent, minor and toric-cone computations to arbitrary characteristic supplies no new obstruction, geometry, or nontrivial bound. The worked example could be useful as an illustration of the general result, not a distinct research contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
