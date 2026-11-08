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

Run `python3 verify.py` in a directory containing the accompanying standalone verifier. It uses integer-only subset-sum dynamic programming and checks all allowable window lengths at each integer index from 7 through 21. Observed output:

```
VERIFY_OK max_m=21 H_tests=17683 reflection_tests=17689 singleton_checks=17712 exact_integer=yes
```

The checks compare the full minimizer sets (not just minimum values), verify the complementary reflection equation on every allowed finite input, and verify the singleton characterization for each enumerated integer. The exhaustive nature of each finite test range is explicit. None of these tests is a proof for unbounded indices; that follows from the counting and induction arguments in `RESULT.md`. Only the stated theorem is reviewed, and independent audit has not yet been performed.
