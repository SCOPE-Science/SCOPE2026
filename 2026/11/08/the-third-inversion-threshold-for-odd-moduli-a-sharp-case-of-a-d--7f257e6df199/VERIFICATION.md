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

# Computational and mathematical verification

Run `python3 verify.py` in the directory containing this file. The verifier requires Python 3 only and tests the third distinct inversion-number bound for every odd \(b\) between \(7\) and \(1001\), inclusive. All coprime multipliers are computed by exact-integer reciprocity, and all odd \(b\le103\) are independently cross-checked by explicitly counting inversions of the permutation. It checks \(J_b(a)=J_b(a^{-1})\), known first and second minima, the universal third minimum bound, and the exact equality-multiplier classification. The successful saved-package replay is expected to print:

```
VERIFY_OK odd_moduli=7..1001 rows= 498 unit_entries= 203374 direct_rows= 49 direct_entries= 2202 threshold_equalities= 332 reciprocity=PASS independent_inversion_enumeration=PASS third_distinct_bound=PASS equality_classification=PASS
```

The unrestricted theorem requires the published Proposition 2.6, as identified in the paper references, and the algebraic proof in `RESULT.md`. The exact critical endpoint formulas are given there so the argument can be checked without guessing computational ranges. Neither these finite tests nor any incomplete external search proves the infinite statement or definitive novelty. The independent mathematical audit has not been performed.
