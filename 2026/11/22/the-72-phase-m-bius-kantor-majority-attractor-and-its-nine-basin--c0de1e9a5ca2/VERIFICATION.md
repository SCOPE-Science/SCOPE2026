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

The finite-state theorem is verified by two separate exact implementations in this package. `check_projection.py` enumerates the 256 binary configurations of each eight-vertex shore, verifies all incidence-map identities, the 22/48/2 fiber partition, the nine basin classes and the four first-entry shells. `check_direct.cpp` builds the sixteen-vertex graph independently and directly enumerates 65,536 full configurations, extracting cycles and attraction basins by indegree peeling. Both were run successfully from these packaged source files, with assertions active.

Reproduce with `python3 check_projection.py`, then `c++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct` and `./check_direct`. No third-party Python dependencies or external datasets are needed. The result is a complete finite-state computation for the explicitly defined graph, not a mathematical proof for arbitrary other graphs. Independent external validation has not been performed.
