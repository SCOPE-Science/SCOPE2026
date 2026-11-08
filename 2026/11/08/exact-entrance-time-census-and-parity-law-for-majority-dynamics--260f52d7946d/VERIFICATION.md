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

# Reproducibility and scientific limits

Extract `verify_direct.py`, `verify_weighted.py`, `direct_output.txt`, and `weighted_output.txt` from the same finding record. Use Python 3.10 or newer and only its standard library:

```
python verify_direct.py
python verify_weighted.py
```

The direct script checks 131,056 distinct labelled initial configurations on triangular books with page counts 2 through 14, identifies the least eventual period and minimum entry time from actual graph updates, and verifies the five formulas. The independent weighted script checks all page counts from 2 through 120 using the exact quotient map and binomial multiplicities. Both programs completed successfully; captured stdout is present in the two text files. The included proof, not these finite computations, establishes all page counts.

The theorem makes no claim for page count one, alternative update conventions, or larger clique cores. The only external audit status is not performed; these checks do not constitute independent validation or a formal proof certificate.
