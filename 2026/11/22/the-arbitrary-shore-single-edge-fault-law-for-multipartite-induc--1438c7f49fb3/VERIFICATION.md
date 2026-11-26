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

Every new face contains x,y. With a third shore, any fourth vertex forms a surviving triangle (if not in that third shore) or a surviving four-cycle (if in that shore). Without a third shore the only changed faces are 2+2 with both x,y; with a third vertex on either of these shores the two same-shore vertices not incident to the fault create K₂,₂ with the opposite pair. All proper faces of the new triangles and tetrahedra are old. For an intact pair piece the two contractible joins intersect in the complete bipartite 1-complex, so the piece is its suspension. The attaching boundaries of the new tetrahedra go to the fundamental four-cycles of the explicit double-star tree, with unit signs; the pair's H₂ is killed integrally without higher homology, fundamental group unchanged. This leaves a contractible piece even in the singleton case. Collapsing the mutually disjoint shore simplices is a homotopy equivalence (each is a contractible cofibration). Each pair quotient can be replaced relative to its two marked points by an interval with its two-spheres attached: choose a joining path and representative sphere maps and apply Whitehead to the simply connected pieces. This replacement glues along the marked points. Each new triangle boundary is the intended graph loop up to homotopy because the chosen edge paths are homotopic relative endpoints within simply connected pair pieces. With the star at shore 1 collapsed, the first triangle for each k≥3 fills a different whole free circle generator, and the other n_k−1 fillings have null attaching maps. This gives the full faulted wedge. For the natural maps use the relative chains of the pair: the added polytopes individually have all proper faces in the old complex, with free relative groups on the tetrahedra in degree 3 and triangles in degree 2. The degree-3 connecting map is the unit basis of the old exceptional-pair sphere lattice. The degree-2 connecting map sends each triangle to the primitive graph-basis vector 1–2–k–1 for its shore (coherent signs). Its kernel is free of rank s. The relative exact sequence proves both split integral map assertions, including all singleton and zero-rank boundary cases. The bundled mod-two checker was inspected, not executed; those checks do not prove primitive integral maps.

## originality

PASS

The supported distinct theorem is the joint homotopy and inclusion-map law for arbitrary nonempty (possibly unequal) shores and r≥3. The intact result and exceptional two-shore transition are prior ingredients, and the all-size-two subfamily has material catalogue overlap, not a distinct part of the originality pass.

## value

PASS

This is a natural robustness question for a known graph-complex family: a single local edge deletion can kill an entire two-shore sphere lattice while simultaneously creating new two-dimensional classes on other shores. Giving the topology alone would obscure which classes persist. The arbitrary-size and singleton-compatible integral map law makes the calculation useful for one-step forest-complex persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
