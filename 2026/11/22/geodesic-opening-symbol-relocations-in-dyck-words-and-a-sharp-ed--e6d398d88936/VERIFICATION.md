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

The theorem is established by the gap-prefix transport proof and a separate constant-run obstruction. `verify_metric.py` generates all Dyck words, builds literal delete/insert edges for opening-only and both-symbol moves, and uses exhaustive BFS on every source through semilength seven. `verify_routes.py` independently builds all shortest opening-only routes using surplus/deficit pairing and checks prefix feasibility after each step. Both recorded run outputs are embedded as plain text. These are finite sanity checks; the proof applies to all positive semilengths. The exact mixed-symbol pair distances are not claimed. The independent audit channel has not been performed.
