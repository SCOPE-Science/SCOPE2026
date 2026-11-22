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

# Verification record

The result is established by the direct mathematical proof in `RESULT.md`, not by finite enumeration. The standalone Python 3.10+ program `check_regular_pretrees.py` is pure standard-library code. Running `python3 check_regular_pretrees.py` produced:

```
VERIFY_OK shapes 57 brute_tree_counts 24 cluster_brute 4 shape_rigidity 375 branch_obstruction 259
```

The independent direct function enumerator tests actual finite-point cone equality, and compares against the weighted formula; the separate source-shape checks test the claimed extremal rigidity in bounded cases. The full all-sizes argument uses a maximal-depth fiber to establish the necessary bounds, the full-ary tree vertex identity, and a canonical leaf-padding construction. The counting step applies surjection counts and inclusion-exclusion over immediate target leaves. These checks do not certify unseen large instances or historical priority. No independent mathematical audit has been performed.
