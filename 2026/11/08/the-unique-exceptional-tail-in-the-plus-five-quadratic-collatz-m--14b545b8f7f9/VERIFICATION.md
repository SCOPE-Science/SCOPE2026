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

# Reproducible verification

The included `verify.py` is self-contained and uses exact integer arithmetic. Run `python3 verify.py` from the same directory as this document. Tests include 24,000 sampled odd-step factorizations, exhaustive terminal-hit searches in the documented finite grid, direct cycle-length checks for all integers from 3 through 20, and exact bounded-count comparisons to direct enumeration at the reported cutoffs. Inspect the output to confirm each check. These are finite tests; the infinite classification is proved in RESULT.md. An independent audit has not been performed.

Observed verifier output:

```
ODD_STEP_OK count=24000
TERMINAL_ENTRY_OK j=1..12 odd_k=3..2001 unique=(1,3,3,1,3)
PERIOD_OK m=3..20 plus_unique_tail=1_to_3
COUNT_OK X=1,2,10,100,1000,10000
VERIFY_OK exact_arithmetic=true finite_checks_only=true
```
