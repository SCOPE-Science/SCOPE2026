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

# Reproducible finite checks

Use the accompanying `verify.py` with Python 3; it requires no nonstandard packages. It constructs each subdivision directly and detects forbidden pairs by searching for a third edge joining distinct endpoints of two selected edges. This is independent of the arc decomposition used in the proof.

For orders \(n=2,3,4,5\), all \(2^{n(n-1)}\) possible edge subsets are tested against the original definition and one-edge addition maximality, and the actual complete maximal families are compared, not merely their sizes. For \(2\le n\le8\), every predicted maximal set is constructed, directly validated, and counted coefficientwise.

Verified output:

```
n= 2 poly= [(2, 1)] generated= 1 exhaustive= True
n= 3 poly= [(2, 9)] generated= 9 exhaustive= True
n= 4 poly= [(3, 8), (4, 9)] generated= 17 exhaustive= True
n= 5 poly= [(4, 85), (6, 20)] generated= 105 exhaustive= True
n= 6 poly= [(5, 132), (6, 105), (8, 30), (9, 20)] generated= 287 exhaustive= False
n= 7 poly= [(6, 959), (8, 420), (10, 42), (12, 70)] generated= 1491 exhaustive= False
n= 8 poly= [(7, 2032), (8, 1365), (10, 840), (11, 560), (12, 56), (15, 112), (16, 70)] generated= 5035 exhaustive= False
VERIFY_OK raw_bridge_conflicts=PASS exact_families_n2_to5=PASS maximal_generated_n2_to8=PASS subset_masks= 1052740 exhaustive_maximal= 132 generated= 6945
```

The exact theorem holds for all \(n\ge3\) by the proof in `RESULT.md`, not by finite computation. No exhaustive search was performed beyond \(n=5\); all larger-order checks are constructive and only confirm the predicted configurations. Scientific publication priority remains provisional.
