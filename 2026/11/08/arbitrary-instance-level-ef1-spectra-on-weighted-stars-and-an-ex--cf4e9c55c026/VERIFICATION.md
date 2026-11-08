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

Run `python3 verify.py` (Python 3 standard library; no optional dependencies). The program directly evaluates ordinary EF1 and connectivity on labeled partitions, independently of the symbolic prefix condition, and checks the constructive infinite-family formulas on finite parameter ranges.

Observed output:

```
VERIFIED: direct labeled-partition EF1 tests: 320
VERIFIED: sampled nonnegative common-weight profiles: 80
VERIFIED: arbitrary-pattern words: 510
VERIFIED: direct candidate-center-subset checks: 3586
VERIFIED: 5-vertex witness labeled counts: [1, 2, 0, 24, 120]
```

The finite tests sample weights and exhaust agent-to-item assignments for the sampled instances, but they do not exhaust all valuations or all sizes. The proof in RESULT.md establishes the unrestricted integer-parameter statements by the hub-bundle decomposition, monotone exchanges, unique-prefix counting, and constructive induction. No automated or independent proof certification is claimed.
