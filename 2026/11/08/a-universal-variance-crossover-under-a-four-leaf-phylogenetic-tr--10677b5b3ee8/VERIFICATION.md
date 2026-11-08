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

# Reproduction

With Python 3.9 or later, run `python3 check_pd_swap.py` from the extracted package. No packages or network access are required. The program uses integer-coefficient polynomial arithmetic and exact rational evaluations; it first constructs edge descendant sets and applies the covariance identity, and then independently enumerates all surviving-leaf subsets for small trees.

Observed output:

```
PASS: 61 symbolic/independent finite checks; smallest shape counts 1,1,1,2
PASS: exact variance identity n=4..12; independent all-survivor enumerations n=4..9
PASS: mean difference q^2(1-q), one crossing for each n, monotone n-dependence
```

Finite checks verify specific instances and formula implementations; they do not by themselves establish the all-integer theorem. The unlimited-range proof uses an exact local covariance difference and an elementary derivative sign in `RESULT.md`. The decimal thresholds are approximations; their definitions are the stated unique polynomial roots. The independent audit has not been performed.
