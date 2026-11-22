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

Run `python3 verify_fixed_forests.py` using Python 3 and the standard library. The code enumerates full permutation groups for fourteen explicit non-singleton-block configurations, computes all orbits of graph edges, independently tests orbit admissibility and every subset of eligible orbits against the complete join criterion, and computes forest Euler sums through six fixed labels. It prints `VERIFY_OK` if and only if every assertion succeeds.

Observed output ends with:

```
beta_m m=3..6: [1, 6, 51, 560]
VERIFY_OK
```

The actual statement is an unrestricted combinatorial argument, not a finite enumeration extrapolation. The calculation checks finite instances of the key orbit/face lemma. The proof of matroid shellability and the closed forest Euler formula are external established mathematical results specifically attributed in the references. No formal proof assistant or external independent validation is claimed.
