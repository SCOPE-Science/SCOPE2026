---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The incidence rule gives a simple cubic bipartite graph and makes both local orders unambiguous. Independently exhaust all proper assignments by branching on an unassigned edge with the fewest available colours at its two endpoints; this yields exactly 120 states. For each state pair, the changed edges must all exchange the same two colours and form a single connected degree-two subgraph; properness then forces alternation. Testing all state pairs gives 216 length-six edges and 324 unrestricted edges, and the frozen labelled vertex and hexagon-edge tables agree entrywise and by their quoted digests. For each hexagon component, the six degree-nine hubs are independent, deleting them leaves nine six-cycles, the hub attachments alternate, and the incidence pairs are exactly K3,3. Distances from every state give eccentricity 6 under hexagon moves and 4 under unrestricted moves, with 60 vertices on each side of the sign partition. Sign is invariant since each switch transposes local colours at an even number of vertices. The global S3 action is free and the neighbor maps bijectively onto the neighboring orbits, giving the stated six-sheeted cover. Independent quotient distances and edge counts agree.

## originality

FAIL

The abstract windmill quotient alone does not determine a labelled cover. The distinct catalogue comparator supplies more, namely all two-colour cycle signatures by orbit: all three pairs at a center have three hexagons, while at a peripheral state only one pair has three hexagons and the others are spanning 18-cycles. These signatures and the quotient force the frozen lift, not just its size. For a fixed pair at a named hub, independently switching its three disjoint hexagons gives an 8-state cube. Its antipodal pairs are precisely the orbit identifications within that cube, because the untouched third matching forces a global rename to fix its colour. One antipodal pair is the two named hubs related by the active transposition. The other three pairs fill one quotient triangle. At a hub the nine moves must project to nine distinct orbit neighbors, so the three colour pairs account for the three distinct triangles. All peripheral hexagon moves stay in their active cube. Label the six hubs by S3: a cube connects antipodal hubs g and gτ with τ a colour transposition, and the nine hub pairs form the transposition Cayley graph K3,3. Removing each cube's antipodal hubs leaves its six-cycle with alternating attachments. The unrestricted edges are also forced: each of the other two colour-pair swaps at a peripheral state is a global transposition on its spanning 18-cycle. Thus both distance tables are mechanical outputs of these forced graphs, without inspecting any of the original labelled-state enumeration. The local sign completeness is a direct consequence: (x,y)↦(x,−y), (m,b)↦(−m,−b) is a Pappus automorphism that swaps two local slopes at each of nine points and keeps the line orders, so interchanges the two signs; switch invariance then identifies the two components. This is demonstrated corollary coverage, not an inference of priority from catalogue dates.

## value

FAIL

The named-state locality cost and a concrete structural lift are natural questions. But here the published exact orbit signatures force the lift and both move graphs by the above construction. The remaining distance difference is a finite distance tally on those forced graphs. Under the standard for narrow exact invariants, the frozen enumeration does not supply a surviving independent contribution beyond that known orbit/signature data. The intrinsic interest of the labelled graph is not in dispute.

The dated certificate retains the supplied scientific assessment, sources and limitations.
