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

# Verification

The complete proof and its finite assumptions appear in `RESULT.md` and the exact checker is `verify_function_cover.py`. The verifier uses no third-party package.

Execute `python3 verify_function_cover.py` with Python 3.9 or later. Expected final message:

```
PASS: 1355 all-profile pair comparisons through n=13; independent checks and infinite-family endpoint identities
```

The certificate compares 1,355 unordered equal-size/equal-group-count profile pairs across all totals 1 through 13. Every coefficient for each integer partition is calculated by two independent integer algorithms (polynomial convolution and inclusion–exclusion), so there is no numerical tolerance or floating-point inference. The three first-layer examples are independently replayed by exhaustive enumeration of all 13-species subsets. Infinite-family sample checks are diagnostics; the proof for all integers \(m\ge5\) is the explicit first-budget product and penultimate-budget singleton count in the manuscript.

The verifier does not test ecological empirical assumptions or prove historical priority. No independent audit has been performed.
