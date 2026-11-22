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

# Verification and reproducibility

Run `python3 verification/check_cycles.py` and `python3 verification/check_colorings.py` using Python 3.9 or later. No third-party packages are needed. Compare the full stdout against `verification/check_cycles.out` and `verification/check_colorings.out`.

The first program independently traverses the complete finite transition digraph for six labeled graph instances. The second separately enumerates all balanced proper three-phase assignments on five instances and checks the exact counts. The finite checks include a four-cycle on a triangle-free graph, positive examples with variable even degrees, and zero-oscillation examples with triangles. Neither program attempts to verify an infinite family by finite sampling. The proof in RESULT.md provides the arbitrary-graph argument; no independent external review is claimed.
