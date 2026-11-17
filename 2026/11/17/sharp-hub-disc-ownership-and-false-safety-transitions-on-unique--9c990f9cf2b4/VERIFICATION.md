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

# Verification performed

The included `verify.py` was executed with Python, SymPy, NumPy and SciPy and printed:

```
VERIFY_OK similarity_cases=27 star_cases=24 nonstar_cases=3
VERIFY_OK universal_threshold_examples=3
```

It tests twenty-four star choices using exact SymPy arithmetic; three non-star exact similarity instances; and three examples of the two numerical hub-radius roots. The proof in `RESULT.md` is an analytic argument for every eligible finite graph and every real \(q\ge0\); these finite examples do not establish the universal quantifiers. The Perron bounds and strict monotonicity are proved separately, not inferred from sampling. The limits exclude ties for maximum degree and do not assert stability properties of a nonlinear source system. Independent validation has not been performed.
