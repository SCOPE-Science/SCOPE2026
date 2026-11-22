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

# Reproducibility

Run `python3 verify_inversion_connectivity.py` in a Python 3 environment. Only the standard library is used. The checker independently enumerates permutations for orders four through eight, computes actual inversion-graph adjacency, tests exact vertex deletion connectivity through order seven, checks all four-vertex induced subgraphs at order eight, and compares the structural class and all noninversion-weight coefficients against a separate block-composition recurrence.

Observed output (final lines):

```text
n= 4 perms= 24 kappa_ge_n-3= 13 fib= 5 high_exact= 8 WEIGHTED_PASS
n= 5 perms= 120 kappa_ge_n-3= 29 fib= 8 high_exact= 21 WEIGHTED_PASS
n= 6 perms= 720 kappa_ge_n-3= 68 fib= 13 high_exact= 55 WEIGHTED_PASS
n= 7 perms= 5040 kappa_ge_n-3= 156 fib= 21 high_exact= 135 WEIGHTED_PASS
n= 8 perms= 40320 kappa_ge_n-3= 357 fib= 34 high_exact= 323 WEIGHTED_PASS
VERIFY_OK
```

No external proof assistant, independent review, or infinite computational certificate is claimed. The unrestricted proof relies on the structural graph argument and standard facts about permutation inversion graphs, not on extrapolation from these finite cases.
