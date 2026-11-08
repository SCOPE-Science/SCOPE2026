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

# Exact finite checks

Run `python3 verify.py` with Python 3 (no third-party packages). The script constructs semigroup elements by independent unbounded-knapsack dynamic programming, computes the complement of the union of translated generator ideals, and compares it with the claimed interval support. It checks every \(2\le n\le31\), \(1\le t<n\), \(2\le q\le11\), yielding 4650 footprint cases, along with 900 binary/ternary closed-form instances and 250 sharp-cutoff witnesses.

Expected successful output:

```text
FOOTPRINT_EXACT_DP_OK n=2..31 q=2..11 cases=4650
BINARY_TERNARY_EXACT_OK cases=900
SHARP_CUTOFF_WITNESSES_OK cases=250
VERIFY_OK finite_checks_only=True infinite_proof_separate=True
```

The finite tests are not exhaustive for unbounded integer parameters; the proof in RESULT.md is the mathematical justification. No independent audit or external validation has been performed.
