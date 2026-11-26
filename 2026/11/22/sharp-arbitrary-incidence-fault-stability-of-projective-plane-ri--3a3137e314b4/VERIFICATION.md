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

For recomputed distances after at most q deletions, the union of the faulty lines has at most q(q+1)<N points. A point outside that union has an intact joining line to every other point. Dually there is a line avoiding all faulty point pencils. Positive retained degrees then give connectivity and the clean point has distance at most three to every vertex. In the radius-two flag complex a mixed clique cannot have two vertices in each shore, by absence of four-cycles. The two pieces of cliques with at most one vertex of one shore intersect in precisely the retained graph. Each collapses to its pure-shore complex by removing a simplex attached along its nonempty neighbor face, separately for each exceptional vertex; the pure-shore complexes are cones on the clean witnesses. The cofibration pushout gives the suspension of the retained graph, whose cycle rank is (q+1)N-t-2N+1=q^3-t. Radius one is that graph and radius three onward is a cone; integral distances give the stated half-open bars. For nested faults the Mayer–Vietoris connecting maps to the graph cycle groups are natural. A spanning tree of the smaller graph works in both graphs, so the smaller fundamental cycle basis is a subset of the larger one; the free cokernel has exactly |F'|-|F| generators. The simplicial cofiber is simply connected by van Kampen and has just that reduced H2 by the relative sequence; Hurewicz plus the simply connected homology Whitehead theorem gives the wedge. Deleting all q+1 incidences at a point defeats uniform connectivity. This is an analytic check of RESULT.md lines 18–30. The frozen Python verifier was inspected but not run; its exact binary homology samples in prime orders are supplementary, not an integral certificate or an all-order proof.

## originality

PASS

Credit the intact classification and suspension construction, the primitive single-vertex deletion result, and in particular the full one-star overlap. The supported distinct claim is the same sharp radius-two stability for every placement of up to q deleted incidences with recomputed distances, together with the arbitrary nested-fault comparison/cofiber. The closest catalogue record is dated the same day and is not discarded on that account; its explicit star hypothesis prevents full coverage. This is a best-of-knowledge comparison, not a priority claim.

## value

PASS

Fault tolerance of the graph-metric filtration is a natural structural question because every deleted edge can change distances, not just remove itself. One simultaneous witness argument handles all layouts and all existing planes, reaches the sharp uniform budget, and controls primitive maps and cofibers rather than just equal field Betti counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
