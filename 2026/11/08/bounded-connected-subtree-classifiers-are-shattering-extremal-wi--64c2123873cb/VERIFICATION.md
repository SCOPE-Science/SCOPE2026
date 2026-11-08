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

# Verification

The constructive hull-leaf theorem was checked by direct exhaustive evaluation on each of the 48 nonisomorphic tree shapes with 1–8 vertices (including the one-vertex tree), across every integral budget and every proposed support: 59,906 tree/support/budget cases. The checker also compared the rooted bivariate subtree recurrence against complete connected-subset enumeration; independently checked 11 star sizes and 39 star homology cases by GF(2) boundary rank.

Run `python check_subtree_shattering.py` with Python 3 and `networkx` installed. Expected verification markers:

```
BOUNDED_SUBTREE_SHATTERING_PASS 48 tree_shapes 59906 support_radius_cases
STAR_FACETS_PASS 11
STAR_HOMOLOGY_PASS 39
```

The checker is finite, tests mod-two rather than integral homology, and is not an infinite or independent certification. The unrestricted proof in `RESULT.md` supplies the all-parameter argument, including integral homotopy through the sphere-wedge decomposition. The source-comparison limitations are stated in `REVIEW.md`.
