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
# Verification of the integer-lattice theorem

The included `verify.py` uses only standard-library Python and exact integer arithmetic. Run `python3 verify.py` to check both distinct primitive cycles, 20,301 cone states, five integer-square counts and the sharpness witness. The verified output is:

```
VERIFY_OK period_cycles=2 transformed_cases=20301 square_counts=5 sharpness=1
```

The proof of universal five-step capture and exact basin classification is the explicit exhaustive integer case split in `RESULT.md`; finite enumeration cannot establish universal assertions. No proof assistant or independent auditor was used. The result does not claim real-plane capture, parameters outside the specified one, or definitive novelty.
