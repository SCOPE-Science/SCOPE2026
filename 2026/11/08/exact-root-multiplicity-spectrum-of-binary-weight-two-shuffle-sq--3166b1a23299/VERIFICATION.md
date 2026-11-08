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

# Reproducibility checks

Execute the included standalone file with `python3 verify_shuffle_roots.py`. It uses only the Python standard library. It checks independent dynamic-programming interleaving membership for every candidate root of each weight-two word at half-lengths 1 through 11, tests the derived interval and four threshold conditions, and cross-checks tail counts by direct gap enumeration through half-length 64.

Observed output:

```
VERIFY_OK direct_words=946 direct_root_memberships=1001 max_roots_tested=4 lengths=1..64
```

The dynamic program operates on two independent source-copy positions; it does not use the analytic interval to decide membership. These finite tests support the independently written all-length proof in `RESULT.md`. The checks do not certify historical novelty or an unrestricted generalization. Independent audit has not been performed.
