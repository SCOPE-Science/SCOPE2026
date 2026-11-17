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

Exact arithmetic check: `python3 verify.py` from this directory, Python standard library only. Tested periods 4 through 18 and enumerated all primitive necklaces at those periods. Output: `VERIFY_OK lengths=4..18 exact_primitive_necklace_orders=15 endpoint_comparisons=86`.

The finite computation is supportive, not a proof for arbitrarily large periods. The analytical argument relies on a cited previously established weight-monotonicity lemma; no independent full-text audit or outside mathematical certification is asserted.
