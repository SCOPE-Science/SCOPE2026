---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The twelve arc graph is precisely L(sd(K4)): same first label gives incident half-edges at original vertex, reversal gives pair meeting at a subdivision midpoint. Independently enumerated 162 nonempty independence faces with f-vector (12,48,72,30), reproduced the given pivot sequence producing 78 matched pairs, a single critical 0-cell and five critical 2-cells, and topologically sorted all 432 directed nonempty Hasse covers with 162 visits, proving acyclicity (not merely mod-two rank). Forman then yields integral wedge^5 S^2. Independent enumeration of 24 S4 permutations verified augmented signed Lefschetz character 1+sgn(g)*number of fixed labels, yielding the rational representation. Each group element preserves a nonempty independent arc face, hence fixes its barycenter; Armstrong orbit-space theorem gives simply-connected quotients and rational finite-transfer invariants give the stated averaging formula; S4 and A4 ranks 1 and 2. All finite computations are exhaustive for this stated finite object, not a theorem for all subdivisions.

## originality

PASS

The closest published truncated-tetrahedron matching result studies M(G) for the 12-vertex truncated graph with 18 edges and has wedge^22 S^3; this submission studies Ind(G)=M(sd(K4)) with 12 simplicial vertices and wedge^5 S^2, plus an S4 character and all subgroup quotient ranks. Other cited simplicial-vertex recursion does not apply to this graph because none of its graph vertices is simplicial. The exact object and symmetry calculation were not found covered by the inspected papers.

## value

PASS

This is a natural small matching complex M(sdK4), not an arbitrary set of graph faces. Exact integral five-sphere homotopy and full tetrahedral S4 rational character, plus simply-connected quotient classification for every subgroup, provide concrete reusable exact topological and representation invariants; finite cardinality does not remove mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
