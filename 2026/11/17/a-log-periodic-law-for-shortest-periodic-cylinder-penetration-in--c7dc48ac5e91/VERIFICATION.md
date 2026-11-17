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

# Reproducibility and proof checks

Run the accompanying `verify.py` using Python 3.9 or newer, without third-party packages. The program enumerates every length-\(n\) binary block in each listed dyadic-period orbit, includes the fixed all-zero configuration, and keeps the minimum actual periodic extension period of each distinct block. At each \(1\le n\le110\), it checks the complete predicted frequency histogram, the exact factor-complexity identity, and both integer-valued moment-sum formulas. The actual run printed:

```
VERIFY_OK exact_histogram_1_to_110=110 exact_moment_identities=220
```

Verification beyond finite checks: the proof in RESULT.md establishes the exact list of periodic points in the closure, disjoint cylinder families, the period histogram for **arbitrary** window length, and uniform summability of the remaining geometric-series weights. These infinite conclusions are arguments, not empirical extrapolations. Differentiating the explicit rational mean profile yields the sharp \(2/3\) and \(3/4\) extrema. This is not a formally verified proof, and independent validation has not been performed.
