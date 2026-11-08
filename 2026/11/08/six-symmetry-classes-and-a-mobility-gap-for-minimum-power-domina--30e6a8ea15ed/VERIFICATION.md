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

# Reproduction

In the directory containing the scientific documents, execute `python3 verification/check_orbits.py` and separately `g++ -std=c++17 -O2 verification/check_independent.cpp -o check && ./check`. The two included output texts show actual successful executions from these commands. No external datasets, packages, optimization solvers, or internet access are required. Both programs enumerate the finite domain and use assertions; a successful text output does not replace inspecting or executing the code.

The first program checks all 5488 candidate monitoring sets of cardinality at most three, all 35960 four-element candidate sets, every Hamming symmetry image of six orbit representatives, the complete TS/TJ exchange relation, and breadth-first searches from the six representatives. The second separately checks the smaller-cardinality cases, reconstructs every four-element state by sequential propagation, enumerates all exchanges with a different state encoding, and performs breadth-first search from all 3600 states. Both confirm 3600 minimum placements, no legal token slide, 35200 token jumps, connectivity, radius five and diameter six.

Scientific limitations: the finite computation is exhaustive only for the dimension-five cube, with a dimension-four consistency check. No general result for larger hypercubes, no independent scholarly review, and no claim about uniqueness in the whole literature is certified.
