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

For a nonempty finite simple graph, all palette set maps act simplicially by contraposition of the product adjacency rule. The merger endomorphisms are commuting integral chain idempotents; the Boolean products of p_i and 1-p_i split the reduced chains and project homology onto the stated intersections of kernels. The empty color subset has image X_1, a simplex. More than d+1 nonbase colors cannot occur in a d-simplex. At exactly d+1 colors, they each occur once in any surviving d-face; its underlying vertices are mutually nonadjacent, so appending a base-color copy of one yields an independent simplex. Every other boundary face omits a required color and is killed by the projection, proving integral vanishing at s=d+1. Palette inclusion respects the projections and has a merger retraction. At d+1 colors each surviving cross-effect occurs; its group is read using a named projection. This proves the repaired consequence and leaves the unmarked torsion-free test intact, also for d=0 and n=1. The original consequence would be false if read as abstract groups alone: at d=3, two disjoint edges give rank (n−1)^2, since each edge product has the homotopy type of a wedge of n−1 circles and disjoint union gives the simplicial join. Three graph-joined copies of C_7 give degree-3 rank 3 binomial(n−1,2) and are torsion-free in that degree by the C_7 calculation. Graph join adds the degree-3 groups because the only extra faces are in monochromatic simplices attached along a pair of disjoint simplices, yielding relative homology only in degree 1. Thus both stage-4 groups are Z^9, but at stage 2 the groups have ranks 1 and 0.

## originality

PASS

Credit the classical FI-sharp splitting and the stronger homotopy/symmetry information already proved in particular cycle families. The supported distinct content is the uniform graph-specific cone vanishing, hence the improved degreewise integral cutoff for all finite simple graphs.

## value

PASS

The extra vanishing reduces an infinite torsion-detection problem to one explicitly bounded palette in each degree and yields all degrees' palette-wise Betti formulas with nonnegative binomial coefficients. The gain is integral and functorial for palette inclusions, not just a restatement of rational polynomiality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
