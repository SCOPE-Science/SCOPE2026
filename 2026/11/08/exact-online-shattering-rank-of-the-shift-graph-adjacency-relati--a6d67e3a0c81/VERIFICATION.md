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

## Reproducible finite checks

Run `python3 check_shift_online.py` with Python 3.10+ and no dependencies. The checker constructs each graph from increasing pairs, recomputes all hypothesis-query adjacency bits, and uses a memoized exact recurrence that maximizes one plus the minimum dimension of the two nonempty answer fibers. It does not rely on a table of previously calculated dimensions.

Observed output:

```
n=2 hypotheses=1 Ldim=0 checked_states=1
n=3 hypotheses=3 Ldim=1 checked_states=6
n=4 hypotheses=6 Ldim=2 checked_states=24
n=5 hypotheses=10 Ldim=2 checked_states=86
n=6 hypotheses=15 Ldim=3 checked_states=309
n=7 hypotheses=21 Ldim=3 checked_states=1145
n=8 hypotheses=28 Ldim=3 checked_states=4366
n=9 hypotheses=36 Ldim=3 checked_states=16980
SHIFT_NEIGHBORHOOD_VERIFIED exact_cases=8 total_states=22917 checked_arm_orders=11 depth3_leaves=8
```

The checker separately evaluates every listed answer along all four depth-two paths and all eight depth-three paths. A further bounded exhaustive loop checks the arm-classification identity and permitted query fibers for orders two through twelve.

## Mathematical limits of computation

The finite cases alone cannot establish any unbounded assertion. The written proof gives an all-order upper bound by deriving, for every positive fiber, an exact two-arm structure and bounding its adaptive dimension by two; the displayed depth-three tree persists under natural inclusions. The infinite-graph statement concerns the membership formula, not its complete first-order theory. The checker provides no proof of historical novelty, and independent validation has not been performed.
