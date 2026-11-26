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

A selected same-part pair fails exactly when at most one outside vertex is unselected, since every geodesic has one middle vertex, and distinct middle vertices are equivalent to internal disjointness. Thus dual faces satisfy |T∩P_i|≤n_i−2 and |T\P_i|≤1 for some i. The pair spaces cover exactly these faces. The two joins making up one pair space intersect in the complete bipartite graph; both joins are simply connected, so this graph has null maps into both. The homotopy pushout therefore gives the two joins and the suspended graph as a wedge. For the global gluing, distinct pair spaces meet only along their shared part skeleton if they share an index. These intersections and the disjoint unions of the two skeletons at each pair are subcomplex cofibrations. Replacing each incidence by a constant map gives a cylinder diagram. For each vertex skeleton, collapse one of its incidence cones to the chosen pair basepoint; the remaining deg(i)−1 cylinders are suspensions attached at their poles, with a marked pole-to-pole arc in each. Collapsing a spanning tree in the resulting incidence spine splits off the edge spaces, the suspended skeletons and one circle for each independent graph cycle. This accounts for all multiplicities including the (t−2)(n_i−1) contribution. Integral Alexander duality uses degree N−q−3, giving exactly the stated ranks of the original complex, not its homotopy type. Separately computed the signed integral dual chains for (5,6,5,5) via the graph common-neighbor test: reduced ranks 3,108,180,70 in degrees 1–4, no torsion.

## originality

PASS

The dual wedge and integral classification for arbitrary unequal parts in the stated t≥4 range are distinct from the inspected smaller-part cases. The balanced t=3 homology is existing overlap at the adjoining boundary, with same-day release order unresolved, not a new contribution here. Available broader multipartite topology results treat a different visibility predicate.

## value

PASS

The classification applies to an infinite unequal-size family, identifies the actual dual attaching-space mechanism and shows how the number of independent dual circles grows with the number of shores. It gives exact integral invariants for the original visibility complexes rather than only a visibility number or a finite/modular computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
