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

The standalone `verify_profiles.py` runs on Python 3 standard library alone. It enumerates all 25 possible complete quantifier-free ordered triple types, enumerates all simple bipartite graphs of up to six edges in a four-by-four class grid, canonically identifies four minimum types, and enumerates all disjoint unions of complete bipartite components with at most nine edges.

From the extracted package, execute `python3 verify_profiles.py`. Expected output:

```
VERIFY_OK types=25 unrestrained_min=6 unrestrained_classes=4 commuting_min=9 commuting_classes=3 labelled_4x4=1296
```

The finite checks are exhaustive for the specified size-bounded families. The graph-theoretic proof, not finite enumerations, establishes the unrestricted bounds, the four and three extremizer classifications, and realizability of all larger sizes. The code does not verify a general first-order small-model theorem. Historical priority and independent validation remain open.
