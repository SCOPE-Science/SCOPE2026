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

# Reproducibility checks and their boundaries

Extract `VERIFY.py` beside this file and run `python VERIFY.py` with Python 3 standard library only. The executed program returned:

```
VERIFY_OK comb_depths=9 exhaustive_nested_structures=22207 unique_K2_shape=((1,), (1,), (1, 1, 3))
```

For each merger depth from one through nine, the program computes all ordered triple merger-level signatures of the explicit comb and matches the complete analytic classification. For one named equivalence, it exhausts all set partitions on at most five points; for two named equivalences, it exhausts all 22,207 nested chains on up to seven points. It checks that no smaller universal structure exists and that all minimum structures in these cases have the asserted unlabelled class tree.

All claims for arbitrary hierarchy height rely on the written proof: the strong triangle inequality, one three-child branch per level, the leaf-count identity, and forced ancestry for pairs of branching nodes. The program is not an independent or formal proof, and a finite search cannot verify universal quantifiers over all sizes. Literature comparisons remain a self-review subject to historical-priority risk.
