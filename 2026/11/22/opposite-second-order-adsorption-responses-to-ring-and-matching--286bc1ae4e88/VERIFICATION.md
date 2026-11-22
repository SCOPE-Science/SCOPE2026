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

# Exact finite-state verification

The graph is specified by the three edge generators in `RESULT.md` and independently built inside each verification script. Execute the two standalone scripts with standard Python 3: `python3 verify_vertices.py` and `python3 verify_matchings.py`.

`verify_vertices.py` enumerates 7,314 reachable occupied-vertex states, derives derivatives through order two with exact rational arithmetic, verifies the baseline terminal distribution, and asserts both rate-curvature signs. `verify_matchings.py` independently generates the graph, enumerates 11,068 reachable partial matching edge sets, and checks the same exact values. A successful execution prints `VERTEX_STATE_EXACT_OK` and `MATCHING_STATE_EXACT_OK`, respectively.

The claimed strict local extremum statements follow from analyticity for positive rates, zero first derivative, and the calculated nonzero second derivative. No global extremum, universality across graph families, statistical empirical observation, or independent external validation is asserted.
