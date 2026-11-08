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

# Verification notes

Run `python verify.py` with Python 3.10 or later and no external libraries. It prints:

```
VERIFY_OK 140 exact identity and finite-enumeration checks
```

The executable recomputes graph-local minimum/maximum pair covariance using exact fractions, enumerates label permutations on paths through seven vertices and small complete trees, checks the exact path and finite-branching formulas, verifies strict signs at several arities and heights, and independently tests the claimed linear variance coefficient at heights three and four.

The infinite all-arity sign theorem is proved analytically in `RESULT.md` by explicit local integration, finite tree level counts and positivity of polynomial expansions in \(m-2\). No finite computation is presented as an infinite proof. Independent mathematical audit has not been performed; historical-priority comparisons remain qualified.
