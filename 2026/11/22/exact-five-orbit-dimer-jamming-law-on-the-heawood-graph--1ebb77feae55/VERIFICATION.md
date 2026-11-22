---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification

Execute the three accompanying standalone scripts using standard Python 3:

```sh
python3 check_vertex.py
python3 check_edge.py
python3 check_orbits.py
```

The first implements the occupied-vertex-state recurrence using the cyclic Fano difference set and verifies the terminal law, mean, and two eight-element second-edge classes. The second creates the Fano plane independently from nonzero three-bit vectors and verifies the same rational terminal distribution with an edge-conflict-state recursion. The third exhaustively enumerates all terminal matchings, 168 Fano collineations and their dual partners, and checks all five orbit sizes and exact per-matching deposition weights.

The proofs are exact finite arithmetic: there are fourteen vertices and twenty-one labelled edges; every transition consumes two vacant vertices. The scripts print PASS only after all hard-coded mathematical assertions succeed. Their execution does not independently establish worldwide novelty, statistical-mechanical scaling, or independent external validation. The explicit finite recurrences, rather than their logs, justify completeness.
