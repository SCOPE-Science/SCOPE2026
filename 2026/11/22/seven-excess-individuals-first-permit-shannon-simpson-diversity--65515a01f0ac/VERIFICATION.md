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

# Verification of the integer-partition certificate

The accompanying `verify_diversity.py` is a standalone Python 3 standard-library checker. Run `python3 verify_diversity.py` in the folder containing both files. Its exact partition-generation and majorization checks cover all integer partitions of excess \(t\) from zero through seven. It compares product and square-sum invariants with integer arithmetic, verifies the complete six incomparable-pair certificate and confirms the unique strict reversed pair at \(t=7\).

The checker independently lists all fixed-richness positive abundance profiles for \(3\le k\le11\) as a redundant finite cross-check. This is not proof for arbitrary \(k\); that statement is established by the uniform zero-padding and Karamata argument in the main mathematical proof. Nothing here is a claim of independent audit, formal verification, empirical ecological validation or exhaustive historical priority.
