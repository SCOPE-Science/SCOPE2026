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

# Reproducibility verification

Run `python verify.py` with Python 3.9+ and NetworkX 3.x. The program enumerates all unlabelled trees at orders 3 through 15 (the complete per-order counts are printed), tests the exact pairwise-distance mean inequalities using edge cuts, and checks all three 15-vertex broom witnesses by an independent direct shortest-path computation. No floating point, random sampling, or timeout-based inference is used.

Expected final lines:
```
15 7741 3 -1/10
THREE_BROOM_ISOMORPHISM_CLASSES_AND_DIRECT_PAIRWISE_DISTANCE_CHECK_PASS
EXHAUSTIVE_TREE_CENSUS_PASS
```
This confirms the finite search and the stated exact fractions. The completeness relies on the standard `nonisomorphic_trees` generator; it is not a separate formal proof of that library's generator algorithm. Independent audit has not been performed.
