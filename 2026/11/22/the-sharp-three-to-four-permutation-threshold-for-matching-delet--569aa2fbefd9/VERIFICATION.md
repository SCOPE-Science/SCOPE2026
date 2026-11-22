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

Run `python3 verify.py` using Python 3 and no third-party dependencies. The checker independently reconstructs every pairwise adjacency by counting relative-order switches across blocks, rather than invoking the theorem formula as an oracle. It verifies:

```
FOUR_PERMUTATION_FAMILY 366 PASS
THREE_PERMUTATION_FAMILY 226 PASS
TRIPLE_ORDER_POSET_CHECK 2 4 PASS
TRIPLE_ORDER_POSET_CHECK 3 36 PASS
TRIPLE_ORDER_POSET_CHECK 4 576 PASS
TRIPLE_ORDER_POSET_CHECK 5 14400 PASS
TRIPLE_ORDER_POSET_CHECK 6 518400 PASS
VERIFY_OK
```

The finite parameter ranges are \(1\le a,b\le9\), each valid matching-deletion count, and all normalized three-block words on at most six vertices. For the unbounded theorems use the written defect-intersection equivalence, transitive-orientation obstruction, explicit two-order constructions, and induced-subgraph restriction of the published four-permutation crown word. The tests do not alone establish those unlimited quantifiers. No independent audit has been performed.
