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

# Verification and reproducibility

Run `python order_ridge_checker.py` with Python 3 and NumPy. No random system entropy, network access, or external datasets are needed. This enumerates every naturally labeled poset of size two through six (obtained as all transitively closed subsets of the forward relations of a fixed total order), then independently checks the rank of the common tight-vertex set of every pair of facets and compares normal angles with the proposed local rule. It also checks the closed count identities. Two hundred seeded random naturally labeled examples each of sizes seven and eight are tested additionally.

Observed output:

```text
ALL_NATURALLY_LABELED_PASS n=2 posets=2
ALL_NATURALLY_LABELED_PASS n=3 posets=7
ALL_NATURALLY_LABELED_PASS n=4 posets=40
ALL_NATURALLY_LABELED_PASS n=5 posets=357
ALL_NATURALLY_LABELED_PASS n=6 posets=4824
RANDOM_POSETS_PASS n=7 cases=200
RANDOM_POSETS_PASS n=8 cases=200
ORDER_RIDGE_ANGLE_PASS total_exhaustive=5230 random=400
```

The checker constructs independent-set-style order-preserving binary vertices directly from the partial order and measures the resulting affine rank. This is independent of the interval/crossing predicate used for its expected answers. All ranks are computed on small integral vectors. These are finite tests, not an exhaustive proof beyond size six and not an independent mathematical audit. The theorem's general proof is contained in `RESULT.md`. The formula applies only to the canonical Euclidean coordinate metric, and the two added marked extrema must be distinct new elements.
