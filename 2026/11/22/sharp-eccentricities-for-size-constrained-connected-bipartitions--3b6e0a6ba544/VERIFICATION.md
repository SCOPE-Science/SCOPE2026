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

The checker independently constructs the state and move graphs without using the lift-distance formula for graph generation. It performs breadth-first searches and compares each computed distance, eccentricity, component count and state/edge count with the derived claims. Run `python3 verify.py` with Python 3 (standard library only). The recorded run checked every \(3\le n\le30\), every admissible \(s\), 224 parameter cases and 5,572,560 ordered distances. This verifies finite cases only. The proof in RESULT.md establishes the all-integer theorem; no independent audit was performed.
