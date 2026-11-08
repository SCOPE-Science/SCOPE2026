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

Run `python verify.py` with Python 3.10 or later and SymPy installed. The program builds adjacency masks without using the stated domination-polynomial formula, directly enumerates dominating subsets for nine small windmills, and compares all coefficient counts. Separately, SymPy exact real-root isolation counts the nonzero roots in four specified intervals for every parameter pair \(2\le k,m\le7\), accounting for their endpoints and checking the simple zero at the origin.

A successful execution reports:

```text
GRAPH_DEFINITION_EXHAUSTIVE_OK 9
EXACT_STURM_INTERVAL_COUNTS_OK 36
VERIFY_OK
```

The proof of the unrestricted real-root classification, root simplicity, bounded limits, and divergent-root asymptotic is analytical in `RESULT.md`. These finite verifications test but cannot independently establish the unrestricted statements. No independent audit has been performed.
