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

The double has one vertex per original edge and one adjacency per pair of opposite edges in a boundary tetrahedron; no simplex of dimension at least two fits in a 3-dimensional boundary. An independent exact reconstruction at unit circumradius in Q(sqrt(5)) recovered all 600 tetrahedra by affine-rank and strict support tests, using the classical identification/count to ensure completeness. It gave 720 vertices, 1800 edges, degree 5 throughout, and one component. Removing each double edge in turn and taking the shortest alternate path gives girth 6, with a six-cycle witness. The supplied parent array was separately relabelled into this reconstruction and all 719 parent edges and root paths verified. The quotient map contracting a spanning tree is a homotopy equivalence to a wedge of 1800−720+1=1081 circles; no assertion that this quotient is literally an embedded retract is needed. The integral homology and fundamental group follow.

## originality

PASS

Best of knowledge: the new part is the connectedness and exact classification of the opposite-edge graph, including girth, not the classical face counts or the graph-to-wedge reduction. No inspected result covers that classification.

## value

PASS

For a canonical regular 3-sphere triangulation the general doubling theorem leaves even connectedness open. Resolving it and giving the exact wedge rank and a shortest-cycle invariant supplies concrete data for comparison with doubles of other 3-spheres.

The dated certificate retains the supplied scientific assessment, sources and limitations.
