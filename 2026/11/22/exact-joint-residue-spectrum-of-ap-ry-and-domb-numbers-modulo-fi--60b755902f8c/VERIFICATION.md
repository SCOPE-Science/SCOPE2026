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

# Verification of the stated joint census

The accompanying standalone `verify_apery_domb.py` recomputes the source integer sums, their residue pairs, the base-five digit factors, and the exact closed pair-frequency formulas. It was executed with Python and completed all assertions, including 300 direct integer-sum comparisons, the full base-five blocks through length four in digit form, direct integer-sum blocks through length three, and exact formulas through length eleven.

The proof gives the all-length result independently of any finite computation. No external scientific audit has been performed. The upper finite comparison bound is not an exhaustive verification of every integer.
