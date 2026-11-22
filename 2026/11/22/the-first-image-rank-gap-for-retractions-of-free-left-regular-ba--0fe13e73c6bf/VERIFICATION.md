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

The included `verify.py` is a self-contained exhaustive certificate. Run `python3 verify.py`; it enumerates all generator tuples for the three specified free monoids, compares two implementations of their multiplication and endomorphism idempotence tests, and asserts equality to every coefficient displayed in RESULT.md. The verified terminal marker is `FIRST_FREE_LRB_RETRACTION_RANK_GAP_CERTIFIED`.

Limits: The script checks all finite cases claimed (\(n=1,2,3\)); it does not examine \(n\ge4\). No independent external mathematical audit has been performed. Publication priority is qualified by incomplete access to one closely related older submonoid paper.
