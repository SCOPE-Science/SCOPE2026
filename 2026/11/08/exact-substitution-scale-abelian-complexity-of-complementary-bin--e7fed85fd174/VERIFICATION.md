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

Run `python3 verify.py` with Python 3.9 or later and no additional packages. The code generates complementary substitution blocks directly and enumerates every window of length \(b^k\) across all four possible adjacent level-\(k\) blocks for \(3\le b\le9\), \(k\ge0\) and \(b^k\le12000\). It tests the exact claimed integer interval, the closed complexity formula, and a constructive maximizing-prefix offset. The expected output includes:

```
VERIFY_OK tested_base_level_pairs 42 largest_factor_length 6561
EXTREMAL_PREFIX_OK
```

These checks are finite, and do not establish the infinite theorem by enumeration. The infinite statement follows from the signed-prefix recurrences, the occurrence of all four parent bigrams, and the sliding-window interval argument given in `RESULT.md`. The computation does not address other lengths or independent scientific validation.
