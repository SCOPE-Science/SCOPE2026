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

# Reproducible verification

Execute `python verify_polygon_triple_tupling.py` using Python 3 and its standard library. The program builds every facet of the join and all unordered partitions into two triangles, checks that the independently constructed graph is exactly the occupancy-predicted disjoint union, enumerates all connected components, and checks componentwise Euler circle ranks. Tested triples: \((4,4,4)\), \((4,4,5)\), \((4,5,5)\), \((5,5,5)\), \((4,5,6)\), \((5,6,7)\), \((6,6,7)\), \((5,7,7)\). The output is recorded in `verify_polygon_triple_tupling_output.txt` and finishes with the PASS marker.

The computed graph equality, parity counts and ranks are exact for each tested finite case. No finite experiment by itself proves the universal classification. That conclusion follows from the stated combinatorial isomorphism and graph-product walk-parity argument. No independent audit was performed.
