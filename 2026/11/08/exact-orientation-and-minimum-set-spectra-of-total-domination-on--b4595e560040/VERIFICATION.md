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

The standalone `verify_bouquet.py` reconstructs each graph's labelled edges and examines every edge orientation directly. The verifier computes incoming-neighbor bitsets, excludes orientations with any indegree-zero vertex, then independently enumerates all vertex subsets to obtain the directed total-domination minimum and the number of minimum-cardinality dominating sets. It checks both coefficient distributions against polynomial expansions obtained from the displayed products, not from simulated local orientation types.

Command: `python3 verify_bouquet.py`

Observed terminal output:

```text
CHECK (3, 3, 3) valid_orientations 56 scores {3: 24, 4: 24, 5: 8} minimum_sets {3: 24, 4: 48, 5: 24}
CHECK (3, 4, 4) valid_orientations 82 scores {5: 42, 6: 32, 7: 8} minimum_sets {5: 64, 6: 80, 7: 24}
CHECK (4, 4, 4) valid_orientations 98 scores {6: 54, 7: 36, 8: 8} minimum_sets {6: 96, 7: 96, 8: 24}
VERIFY_OK profiles 14 valid_orientations 424 all_signed_edge_orientations_and_directed_total_domination=PASS minimum_set_enumerator=PASS
```

There are 14 checked cycle-length tuples, including one-petal boundary controls and unequal-length two-/three-petal examples. The code's complete finite checks are not a proof for unrestricted numbers or lengths of petals; this rests on the case classification and sharp forcing arguments in RESULT.md. No separate independent mathematical audit has been performed.
