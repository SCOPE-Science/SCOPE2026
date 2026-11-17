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

# Verification evidence
The embedded standalone Python checker uses exact integer and rational arithmetic and independent explicit Winsorization evaluation. Running `python winsor_gini_check.py` gives:

```text
ALL_REPLICATION_MULTIPLICITIES_EXACT 2352
ALL_WINSORIZED_CHAMBERS_AND_ATTAINMENT_EXACT 165
EXACT_RANDOM_TWO_INPUT_INEQUALITIES 10800
ALL_WINSORIZED_GINI_DIAGNOSTICS_PASSED
```

The enumeration covers all multiplicity vectors in dimensions two through seven (not dimensions above seven), all rank pairs in dimensions two through ten, and the stated rational samples. It is not an infinite proof. The complete analytic proof of the unrestricted statement is in RESULT.md. No external independent audit has been performed.
