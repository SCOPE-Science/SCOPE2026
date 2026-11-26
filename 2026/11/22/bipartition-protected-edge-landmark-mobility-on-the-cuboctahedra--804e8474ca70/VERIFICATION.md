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

Cube-edge incidence determines the full 12-vertex, 24-edge graph. Resolving means the distance-to-edge columns restrict to distinct signatures; the fresh exhaustive check found no resolving set through size four and 168 at size five, each omitting exactly one cube vertex and 21 omissions of each vertex. A slide replaces ab by ac, so only the coverage on the parity class of b and c can change. Switching the omitted parity would change both classes' coverage counts from (3,4) to (4,3), which is impossible. Enumeration of all legal moves and all finite state distances gives 948 jumps in one component of radius and diameter 5; 360 slides in two 84-state components, each of radius and diameter 6, exactly the parity classes. A bit flip interchanges them. Every triangle of the line graph is a star of the triangle-free cube, so the line-graph automorphism group induces the cube group on those eight stars; the action is faithful and every cube automorphism induces one in return. The 48 coordinate permutations and independent bit flips exhaust the group since the image of a cube corner and of its three neighbours determines the automorphism. Its basis orbits are 24,48,48,48. Ordinary vertex resolution gives dimension 3, 96 optima, connected slides, radius 7 and diameter 8. Replay: python3 /workspace/branches/fefce843-c088-4901-b7d4-ebad2819196f/independent_check_record5.py. This is a complete enumeration of this finite graph, not extrapolation.

## originality

PASS

The definition of edge-metric dimension, the graph and its cube-line-graph representation, and the move rules are antecedent. The verified distinct result is the cuboctahedral minimum edge-basis reconfiguration classification with its missing-parity obstruction and connected ordinary vertex-metric comparison. The closest indexed Heawood result has the same minimum size, number of edge bases, and jump diameter, but has a different base graph and a materially different slide classification. The checked general papers do not establish the target exact classification.

## value

PASS

This is an exact benchmark on a canonical graph for how optimum edge-location sensor sets may be moved. An invariant tied to the omitted cube vertex explains the disconnectedness rather than merely reporting it; the exhaustive counts show that the invariant is also sufficient for slide connectivity. On exactly the same base network, optimum vertex-location sensors have connected slides, establishing a natural, task-dependent contrast.

The dated certificate retains the supplied scientific assessment, sources and limitations.
