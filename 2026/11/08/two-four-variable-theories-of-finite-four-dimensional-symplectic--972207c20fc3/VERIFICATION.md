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

`python3 verify.py` uses no external mathematical packages. It enumerates all projective points for fields of orders 2, 3, 4, and 5, computes the orthogonality relation and the projective triple-span predicate, and computes all extension possibilities for every ordered triple at order 3. It checks the same catalogue on seeded ordered-triple samples in orders 4 and 5, including explicit representatives with repeated entries. It confirms that a four-clique exists at orders 3, 4, and 5 but not at order 2.

Observed output:

```text
q=2: vertices=15, enriched_stationary_types=16, nonuniform_types=0, K4=False
q=3: vertices=40, enriched_stationary_types=16, nonuniform_types=0, K4=True
q=4: vertices=85, enriched_stationary_types=16, nonuniform_types=0, K4=True
q=5: vertices=156, enriched_stationary_types=16, nonuniform_types=0, K4=True
q=3 vs q=4: matching types 16, profile mismatches 0 (sample for q=4)
q=3 vs q=5: matching types 16, profile mismatches 0 (sample for q=5)
Finite corroboration passed; the field-uniform theorem requires the separate algebraic proof.
```

The finite tests cannot prove the assertion for all prime powers or unrestricted quantifier depth; those require the explicit algebraic extension lemma in the result. Independent mathematical audit has not been performed.
