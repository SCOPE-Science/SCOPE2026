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

# Reproducibility and verification

Run `python3 hetero_checker.py` with Python 3. The embedded program uses only the standard library and rational arithmetic. It independently enumerates rank-constrained binary vertices, constructs projection candidates, checks the supporting-normal first-order optimality condition, verifies the exact rational distance, compares all maxima with profiles containing at most one partial block, and checks the equal-sum PARTITION equivalence on a bounded test family.

Observed output:

```text
HETEROGENEOUS_COMPRESSION_PASS configurations=122 exact_vertices=38606 maximal_vertices=819
PARTITION_THRESHOLD_PASS instances=1360 yes_instances=591
```

The mathematical proof covers every number and size of blocks with strictly interior rank; the finite checks do not establish an infinite theorem. The reduction uses a succinct binary block-parameter input and classical PARTITION. There is no claim about strong NP-hardness or an explicitly expanded coordinate representation. The self-review is complete; independent mathematical audit has not been performed.
