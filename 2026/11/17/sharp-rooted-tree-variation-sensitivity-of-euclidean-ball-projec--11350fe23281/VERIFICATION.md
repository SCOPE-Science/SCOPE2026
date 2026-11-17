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

# Reproducible checks and proof boundary

Run `python verify.py` using Python 3 standard library. The program:

1. Exhaustively enumerates all labelled unrooted trees represented by Prüfer sequences, with the root fixed at zero, through six vertices (1441 cases), then enumerates every dual sign pattern to verify the extremal degree-square identity; it also directly checks the subtree indicator inversion relation for every vertex.
2. Checks the exact path and star degree-square formula for dimensions two through seventy.
3. Constructs the smaller-eigenvalue tangent direction independently on five shapes and numerically checks that nearby finite input pairs approach the predicted sharp Lipschitz coefficient from below.

Observed output:

```
ALL_LABELLED_TREES_TO_N6_SIGN_AND_SUBTREE_CERTIFICATES_PASS 1441
PATH_STAR_EXACT_ALL_N2_TO_N70_PASS
TANGENT_SPECTRAL_EXTREMIZER_AND_FINITE_PAIR_APPROACH_PASS
ALL_ROOTED_TREE_RADIAL_BV_DIAGNOSTICS_PASS
```

The unrestricted theorem, the all-dimension extremal classification, and global nonattainment depend on the proof in RESULT.md, not extrapolation from the tests. No independent external validation was performed.
