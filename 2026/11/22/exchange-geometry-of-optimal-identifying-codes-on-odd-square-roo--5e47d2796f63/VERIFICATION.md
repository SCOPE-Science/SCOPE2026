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

In the selected bipartite support, a 3-vertex component gives equal traces and at most one singleton or isolated edge is permitted (two small components force either equal or empty traces). The minimum size 3m+1 forces exactly m+1 tree components. A singleton then forces at least one P4, whose same-shore leaf with that singleton gives duplicate traces, so the components are one edge and m P4s. Sufficiency: for two cells sharing one endpoint to have equal traces, their other endpoints must be leaves at that shared vertex; for disjoint cells to have equal traces, nonempty star incidences force two isolated crossed edges. Neither configuration occurs. Pairing shores and choosing holes yields the stated count and transitivity. Deleting the isolated edge forces its reinsertion. Leaf deletion forces its singleton back onto its P3 at the other admissible endpoint. Central deletion leaves three K2s; either reconnect the newly separated pair through the other corner, or join one to the original K2 in two ways each. This gives 7 distinct neighbors per block; touching an intact P4 cannot give a valid decomposition. Independently generated all 7200 decompositions at n=5, tested all 6- and 7-cell candidates by precomputed board neighborhoods, and computed the exchange graph by shared six-cell cores. Replay: python3 /workspace/checks/2.py, output /workspace/checks/2.txt. Confirmed degree 14, 50400 edges, connectivity and all ten shell sizes. Transitivity turns this eccentricity into radius and diameter 9. Frozen C++ and Python sources were read, not executed.

## originality

PASS

The static optimum size, orbit and consequent optimizer count are not passed as new. The supported distinction is the odd-order move classification and degree, plus the exact five-board exchange metric.

## value

PASS

The exact move classification exposes which blocks can interact and gives a uniform all-order degree rather than another static count. The first odd case covered by the static classification has a complete exchange metric, not merely a selected pair distance or a sample. No larger-order connectivity or diameter is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
