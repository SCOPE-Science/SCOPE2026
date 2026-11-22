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

`check.py` uses Python 3 standard-library modules only. Run `python3 check.py` in the same directory as this document. It independently tests the Rees product/marginal membership condition against the row-ratio census for two finite nonabelian groups, enumerates small binary-valued quotient patterns, and checks the exact count and normalized shape of extremizers in complete small nonabelian group-valued families.

Recorded successful output:

```
MARGINAL_DEFECT_CHECK_OK 74896 binary matrices 4232 equality matrices 200 group instances
EXTREMIZER_COUNT_OK S3 2x2 2x3 3x2
NORMALIZED_PATTERNS_OK S3 2x4 3x3
RAW_NORMALIZATION_OK 400 S3 instances
```

The symbolic proof is in `RESULT.md`. The program tests finite instances only and cannot establish the infinite dimension-uniform statement or historical originality. Independent mathematical audit has not been performed.
