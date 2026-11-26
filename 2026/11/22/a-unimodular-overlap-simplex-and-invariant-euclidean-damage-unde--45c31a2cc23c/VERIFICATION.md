---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The first cut removes only its named vertex and meets its incident exchange edges at their other endpoints. Any new edge lies in the product-of-simplices cut facet. At an adjacent second deleted vertex its product neighbors are also single exchanges, so the second cut again creates no fractional vertices; at a nonadjacent second vertex there are no new incident edges. This proves the exact retained hull. The cap's base volume and perpendicular height give normalized volume binom(n-2,k-1) with the stated covolume sqrt(n). Nonadjacent open caps are disjoint by x(H)+x(J)<=k+|H intersection J|. In the adjacent case writing y_a=1-x_a, d=sum y, u=x_i-d, v=x_j-d and z_b=x_b yields nonnegative coordinates of sum 1, and the inverse is integer-affine and satisfies the cube constraints. The relative interior with u,v>0 is nonempty and dense up to the boundary, so the closure of the open overlap is the whole unimodular simplex. Inclusion–exclusion gives the +1 correction. The deleted-vertex foot, equal to 1-1/k on its support and 1/(n-k) off, satisfies both cuts since 1/k+1/(n-k)<=1. Its orthogonal residual has squared norm n/[k(n-k)]. Distance convexity excludes combinations using any retained vertex from the maximizer set; strict Euclidean convexity for the distinct residuals excludes the open segment between the two deleted vertices. The lower-dimensional n=4,k=2 opposite-vertex case correctly gives normalized volume zero and distance one. The supplied hull and determinant scripts were inspected, not executed. One nonblocking bibliographic locator correction: the claimed Ferroni–Schröter formula is Cor. 7.6, §7.1, in the currently retrieved arXiv PDF, not Cor. 6.7, §6.

## originality

PASS

Nonadjacent normalized volume, Euclidean projection and farthest points are previously covered by sparse-paving formulas. General alcoved enumeration applies even to adjacent deletions and is not claimed anew. The supported distinct result is the adjacent cap overlap as one explicit unimodular simplex, its one-unit volume correction relative to nonadjacent erasure, and the persistence of the same worst distance and equality cases outside the sparse-paving regime.

## value

PASS

Two deletions are the first test of interaction between natural vertex caps of the hypersimplex. The overlap is not just a small measured difference: it is a single unimodular cell, and it occurs exactly on the Johnson edges. In contrast the exact worst Euclidean distance and where it occurs do not change, including the dimension-drop regime. This separates two concrete robustness invariants of a canonical polytope and supplies a useful local geometric description beyond generic hull-volume computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
