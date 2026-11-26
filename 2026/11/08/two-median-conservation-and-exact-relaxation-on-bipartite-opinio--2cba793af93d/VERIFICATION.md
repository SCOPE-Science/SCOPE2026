---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the two-median formula

The analytic derivation is in `RESULT.md` and applies to arbitrary real initial values and positive finite weight profiles satisfying the stated unique-median condition. Uniqueness follows from a pointwise comparison with the explicit trajectory's unique group medians and Grönwall's inequality; no global non-expansiveness assertion or openness of the unique-median regime is needed.

Run `python verify.py` with Python's standard library. The verified output is:

```
VERIFY_OK exact_cases=1289 boundary_cases=4
```

The checker evaluates \(q=e^{-t}\) at \(1,1/2,2/3,1/7,1/19\), with exact fractions for 1,289 qualifying profiles. These arise from exhaustive small odd uniform profiles over three opinion values, plus deterministic varied finite part sizes, positive nonuniform weights, and fractional initial values. It checks selected medians, both vector-field derivatives, and preservation of all within-group differences. It separately tests the closest-observed-median selection for the nonunique \(K_{2,2}\) boundary at four positive rational values of \(q\). The checker does not establish originality or any infinite-dimensional generalization. No independent external audit was performed.
