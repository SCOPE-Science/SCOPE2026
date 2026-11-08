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

# Verification of the two-median formula

The analytic derivation is in `RESULT.md` and controls the full range of real initial conditions and arbitrary positive finite weights. The only nontrivial outside premise is the global non-expansiveness of the selected weighted-median operator, explicitly proved for the initiating model in Han et al., arXiv:2404.16318v1; uniqueness also follows locally along the strict-median trajectory.

Run `python verify.py` with Python's standard library. The verified output is:

```
VERIFY_OK exact_cases=1289 boundary_cases=4
```

The checker evaluates \(q=e^{-t}\) at \(1,1/2,2/3,1/7,1/19\), with exact fractions for 1,289 qualifying profiles. These arise from exhaustive small odd uniform profiles over three opinion values, plus deterministic varied finite part sizes, positive nonuniform weights, and fractional initial values. It checks selected medians, both vector-field derivatives, and preservation of all within-group differences. It separately tests the closest-observed-median selection for the nonunique \(K_{2,2}\) boundary at four positive rational values of \(q\). The checker does not establish originality or any infinite-dimensional generalization. No independent external audit was performed.
