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

Rotation reduces every graph-vertex deletion to that of residue 0. The nonempty faces are all nonempty subsets of the remaining open graph neighborhoods. Reconstructing them and testing the pivot certificate independently reproduces 46 and 58 faces, 22 and 27 disjoint pairs, and verifies acyclicity on the entire directed Hasse diagram. Critical faces are {1}, {2,3} for n=8 and {1}, {2,3}, {2,6}, {4,8} for n=9, so Forman's theorem gives a single vertex with one or three loops. A different independent check uses elementary simplicial collapses: always remove the lexicographically least pair consisting of an edge or triangle and its unique proper coface, of dimension one higher. Face vectors are (7,20,16,3) and (8,26,20,4); after 16 and 20 collapses the remaining complexes are connected graphs on 7 and 8 vertices with 7 and 10 edges, respectively. Contracting a spanning tree then gives the claimed integral homotopy types. Both checks are exact and bounded to the specified orders. The uploaded checker was read, not executed.

## originality

PASS

The supported precise claim is the homotopy type after deleting a graph vertex, and then rebuilding the open neighborhood complex, at the two specified orders. The closest intact classification and the same-day edge-deletion theorem give actual nearby statements but neither covers this graph operation or implies both types. The judgment is limited to the comparisons made, not a guarantee of historical priority.

## value

PASS

These are not arbitrary tiny graph orders: they are the adjacent exceptional and first stable toroidal orders of the canonical intact family. Determining the exact integral homotopy response to one graph vertex loss on the two sides specifies a basic local robustness invariant that the intact and edge-fault results cannot supply. The distinct ranks, together with all higher cells collapsed, give a useful comparison for future deletion arguments without claiming a general vertex-fault theorem or any maps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
