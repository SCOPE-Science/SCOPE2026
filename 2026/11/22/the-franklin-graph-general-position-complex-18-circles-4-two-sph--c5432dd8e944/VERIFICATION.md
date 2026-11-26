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

The graph with the stated chord convention gives 144 geodesic-forbidden triples and face vector (12,66,76,45,12,2). An independent reconstruction using Floyd–Warshall distances and a different free-face tie-break made 60 elementary simplicial collapses to (12,53,28), then contracted a spanning tree and eliminated 24 of 42 generators against relators in which they occurred exactly once. Such a relation is a primitive loop after a free basis change; the remaining attaching maps are carried along by substitution, and collapsing the resulting loop-plus-disk is a homotopy equivalence. Four remaining words freely reduce to empty, proving the wedge of 18 circles and four 2-spheres, not merely its Betti numbers. Independently enumerated all 48 distance-preserving permutations and actual flag-orbit cells of the barycentric subdivision quotient; stabilizers preserve each flag position. The flag-orbit chain ranks are (18,83,180,203,120,30) and the rational boundary ranks in degrees 0–5 are (0,17,66,113,90,30), giving Betti numbers (1,0,1,0,0,0). This also verifies the quotient result without assuming the original simplicial orbit set is a simplicial complex. Replay: python /workspace/checks/franklin.py (helper words.py; output franklin.txt in the same directory).

## originality

PASS

The exact geodesic-GP homotopy and reduced rational full-automorphism quotient computation were not found for a distinct record in the inspected evidence. The closest same-graph claims have demonstrably different face predicates, and same-predicate homotopy computations concern different graphs.

## value

PASS

The Franklin graph is a standard small cubic graph and provides an exact mixed-dimensional test case for the geodesic general-position construction, where extremal cardinality or integral homology alone does not control the attaching maps. The nonabelian reduction and a separate full geometric symmetry-quotient invariant are useful to subsequent computations on comparable graphs. No quotient homotopy type or integral quotient assertion is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
