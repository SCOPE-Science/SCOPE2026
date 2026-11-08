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

The included `verify.py` uses only the standard library. To reproduce, run `python3 verify.py` from the extracted package directory. It checks 2,064 exact dynamic-programming coefficient cells against the independently formed bivariate rational identity for alphabet sizes 2 through 8 and lengths 0 through 54, enumerates 79,497 admissible finite words, directly tests 9,771 subsequence-universality instances, and checks all shortest-length and attainable-support assertions within these ranges. It also compares exact rational derivatives of the arch-length probability generating function with the two moment formulae.

Observed output:

```
VERIFY_OK q=2..8 recurrence_n=0..54 coefficient_cells= 2064 exhaustive_proper_words= 79497 direct_subsequence_tests= 9771
```

Finite enumeration is not an infinite proof; the formal-language identities and renewal limit statements rely on the proof in `RESULT.md`. The value of the exact all-length rational identity is not inferred from these finite tests alone.
