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

The proof uses Sherman–Morrison and elementary graph-neighborhood equivalence, with exact matrix identities. `verify.py` is a supplementary exact-rational checker requiring the dependency declared in `requirements.txt`. Its graph enumeration is finite and does not itself prove the arbitrary-order result.

The checker computes the exact rank-two polarization change under one new edge, verifies the negative identity for false-twin endpoints and explicit opposite-sign test vectors for nontwins, and checks every missing edge in each labeled connected graph with one through five vertices. It additionally verifies the four-vertex rational witness in `RESULT.md`.

The checks are not an independent audit; the external independent-audit status is not performed.
