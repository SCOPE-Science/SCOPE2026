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

The standard-library source file `reduced_tree_checker.py` was executed against the included source. It generated unlabelled trees by leaf attachment with center-rooted canonical codes; the final output was `REDUCED_METRIC_TREE_SHARP_ORDER_15_PASS`. It counted reduced trees for orders 3–15 as 0,1,1,2,2,4,5,10,14,26,42,78,132, found no collisions below 15 and three doubletons at 15 with the exact histograms given in the theorem. Canonical encodings distinguish each pair; the script prints all six representatives and their fourteen edges. No floating point arithmetic, stochastic simulation or outside data files are used. The experiment alone is not a proof of exhaustive coverage; the induction that every tree is obtained by adding a leaf and the unique center-rooted representation supply that missing mathematical step. The full historical literature cannot be exhaustively searched; independent originality and mathematical audit have not been performed.
