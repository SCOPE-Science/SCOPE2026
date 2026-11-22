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

# Reproducible checks

Execute `python3 verify.py` (Python standard library only). The verified output was:

```text
CHECKS_OK 5626 optimal_norm 0.20000000000000007 equal_norm 0.57876450952618 single_norm 1.3150996611745185
```

The code checks exact rational identities for 606 dimensionless allocation parameters, exact-rational strict-improvement witnesses for 20 parameter pairs, 5,000 seeded numerical instances, and independent two-factor matrix computations for a concrete example. The proof in `RESULT.md` establishes the full continuum of allocations; the finite checks cannot establish universal optimality or historical novelty.

The source comparisons are scientific-literature comparisons, not independent manuscript review. Source publication priority, broad equivalence, and generalization beyond the explicitly stated Jordan family remain unverified by an independent examiner.
