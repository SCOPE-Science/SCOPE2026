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

# Reproduction and scope of checks

Execute `python check_tree_poisson.py` using Python 3's standard library. The script enumerates all labelled trees on two through six vertices using Prüfer sequences (\(1+3+16+125+1296=1441\) trees), compares independent exact-fraction inversions of the Poisson Laplacian with cross-cut distance sums, and checks all edge-row sign witnesses. It additionally samples 120 trees on seven, eight and ten vertices, verifies the sharp star/path values for every order two through fifteen, and exhaustively enumerates cube vertices in smaller cases. The resulting diagnostics are:

```
EXACT_PSEUDOINVERSE_VS_CROSS_CUT_DISTANCE_PASSED 1441
ADDITIONAL_EXACT_RANDOM_TREES_PASSED 120
SHARP_STAR_AND_PATH_ENDPOINTS_PASSED 14
ALL_TREE_POISSON_CHECKS_PASSED
```

The general tree formula, equality classification and complexity estimate are established by the written edge-flux and cut-distance proof; the finite checker is an independent implementation check, not a proof of the quantified theorem. Independent audit has not been performed.
