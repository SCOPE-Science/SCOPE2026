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

# Reproduction and limits

Run `python3 check_geodesic_cycles.py` using Python 3.9 or newer; the checker requires only the standard library. Its output is included as `check_output.txt`.

The checker constructs both clockwise and counterclockwise shortest paths from unordered vertex endpoints, including both in a diametral tie. It computes all Boolean labels on each vertex support of sizes one, two, three and four, checks the exact triple classification, and rejects all four-supports. A separate exact binary rank routine computes homology dimensions from the boundaries of shattered triangles in every cycle of order \(3\le n\le18\). All tests ended with the marker `ALL_CYCLE_GEODESIC_SHATTERING_CHECKS_PASS`.

The finite test range does not imply the all-order theorem. The universal shattering classification is proved directly in `RESULT.md`, and its integral wedge decomposition uses an explicit CW-complex collapse and null-homotopic attachment argument, not mod-two computations. Historical-priority verification is not exhaustive; no independent mathematical audit has been performed.
