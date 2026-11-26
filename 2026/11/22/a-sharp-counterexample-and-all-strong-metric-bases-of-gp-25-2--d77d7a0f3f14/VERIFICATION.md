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

For a mutually maximally distant (MMD) pair, a resolving vertex other than either endpoint would extend a geodesic at one endpoint and contradict MMD. Conversely a longest geodesic containing the geodesic subpath between a given pair has MMD endpoints, so a vertex cover of the MMD graph resolves that pair. Therefore complements of maximum independent sets are exactly strong metric bases. I independently constructed the graph, computed integer distances by Floyd–Warshall and reconstructed every MMD edge. Counts were 125 outer, 50 inner, no cross edges, and the complete difference table matched. Pivoted Bron–Kerbosch on the entire complement (no assumed classification or orbit truncation) enumerated 21,000 maximal cliques, with maximum size 16 and exactly 125 maximum cliques. Their actual vertex sets equal the 25×5 claimed patterns; direct evaluation of the distance equality for all 1,225 pairs and each of the 125 complements also passed. Replay: python3 /workspace/reviews/evidence/gp25-independent.py. Both uploaded implementations and the verification notes were inspected but not executed. This certifies the specific graph, not the family. For k=6, 34 contradicts the proposed equality at 35, not the proved upper bound.

## originality

PASS

The inspected Petersen-graph source conjectures the wrong equality at this index and does not tabulate it; neither nearby indexed invariant nor the standard MMD reduction gives the sharp value or the bases. No claim of exhaustive historical priority.

## value

PASS

The graph and order are motivated before computation by a published family proposal. This case gives a directly checkable counterexample and an exact sharp value, not just a stronger upper bound. The Cartesian pattern of all minimum bases separately answers a natural structural question and makes the phenomenon reproducible without requiring any all-order extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
