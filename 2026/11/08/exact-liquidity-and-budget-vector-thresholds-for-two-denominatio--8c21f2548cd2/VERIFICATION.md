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

# Verification and reproducibility

`check.py` is a standalone, standard-library-only program. Run it with `python3 check.py` from a directory containing the extracted files. In the tested environment it printed:

```
exact individual-budget tests 11232 minimum budget levels 725 Bernoulli enumerations 480
```

The program independently enumerates all placements of large and unit goods in integer capacity bins for small parameter instances and checks the exact inequalities, brute-force minimal aggregate budget and Bernoulli-budget Boolean support counts. The proof of the infinite-family statements is in `RESULT.md`; exhaustive testing on bounded instances does not establish the claims for arbitrary parameters.

Only the six science documents and standalone verifier are required to reproduce the reported checks. Public-source comparisons are documented in `AUDIT.json` and `REVIEW.md`. Independent audit: not performed.
