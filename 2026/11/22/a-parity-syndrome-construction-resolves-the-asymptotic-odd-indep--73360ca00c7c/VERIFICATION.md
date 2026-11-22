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

The construction and its universal proof are in RESULT.md. Reproduce the separate finite checks with `python3 verify.py` (standard library only). Checked directly are every selected vertex, each edge's independence condition, all outside vertex neighborhood counts, the syndrome map rank, cardinalities, and the published dimension-four/six/eight numbers. The unrestricted result is mathematical, not inferred from these finite tests. The code also verifies the label multiplicities and dimension inequalities for 2048 even dimensions. No external or independent audit was performed.
