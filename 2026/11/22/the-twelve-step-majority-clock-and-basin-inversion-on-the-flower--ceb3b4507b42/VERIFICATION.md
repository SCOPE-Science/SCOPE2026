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

Both included checkers were executed on their actual source paths. `code/check_peeling.py` builds the graph independently, enumerates every labelled transition, strips transient vertices from the functional graph, and emits all basins and entrance/period cells. `code/check_forward.cpp` builds edges in a different sequence and traces each state directly until the least periodic entry, independently checking the full basin spectrum. Their exact counts coincide. The complete finite proof is conditional only on replaying these explicit deterministic arithmetic programs and the stated graph definitions; no formal proof assistant or independent external audit was used.
