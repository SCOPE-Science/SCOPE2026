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

The self-contained `checker.py` uses only Python's standard library and constructs all simplices directly from the two punctured squared cycles. It verifies 46 and 58 nonempty faces, 22 and 27 matched pairs, the exact critical cells, and directed acyclicity of the complete matched Hasse diagrams. Reproduced at packaging time using `python3 checker.py`. These exhaustive finite checks support only the two claimed orders. Independent audit has not been performed.
