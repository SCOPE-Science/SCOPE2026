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

# Reproduction and limits

Execute `python3 verify_triangular_dissociation.py` using Python 3.8+ standard library. The checker constructs every \(T_n\) from the intersection rule for its two-element vertices, independently tests induced degree at most one on each subset, and tests inclusion-maximality by all single-vertex additions. It compares both resulting cardinality profiles with counts generated separately using labeled \(K_2\)/\(P_3\)/singleton decompositions.

The executed command reported:

```
n=3, all={0: 1, 1: 3, 2: 3}, maximal={2: 3}
n=4, all={0: 1, 1: 6, 2: 15}, maximal={2: 15}
n=5, all={0: 1, 1: 10, 2: 45, 3: 30}, maximal={3: 30}
n=6, all={0: 1, 1: 15, 2: 105, 3: 195, 4: 90}, maximal={3: 15, 4: 90}
n=7, all={0: 1, 1: 21, 2: 210, 3: 735, 4: 945}, maximal={4: 945}
VERIFY_OK n=3..7 subsets=2131016 dissociation_sets=2433 maximal_sets=1098 full_polynomial=PASS maximal_polynomial=PASS interval_spectrum=PASS
```

This computation exhausts finite instances only and does not establish the formulas for all \(n\). Unlimited correctness uses the written component classification proof. Neither independent audit nor certification is claimed.
