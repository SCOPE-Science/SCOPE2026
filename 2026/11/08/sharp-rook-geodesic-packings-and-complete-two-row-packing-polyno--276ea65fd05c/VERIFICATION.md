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

# Reproducibility and verification
Execute `python verify_rook_packing.py` with a standard Python interpreter. The script reads no external files and uses no third-party libraries. It builds actual shortest-path distances on each two-row rook graph by breadth-first search, enumerates all length-two geodesic paths without using the formula, enumerates all vertex-disjoint path families in canonical index order, and tests inclusion-maximality from the original definition. For each \(2\le n\le7\), it compares every coefficient of both stated polynomials, including the empty family and nonmaximal families. It also verifies 225 explicit constructive witnesses for dimensions \(2\le m,n\le16\), including the exceptional \(4\)-by-\(4\) base board.

Observed output:
```
CONSTRUCTIONS_OK rectangles 225 range_each_dimension=2..16
DIRECT_OK n 2 max_size 1 maximum_count 4 total_packings 5 inclusion_maximal 4
DIRECT_OK n 3 max_size 2 maximum_count 6 total_packings 19 inclusion_maximal 6
DIRECT_OK n 4 max_size 2 maximum_count 72 total_packings 97 inclusion_maximal 72
DIRECT_OK n 5 max_size 3 maximum_count 240 total_packings 581 inclusion_maximal 240
DIRECT_OK n 6 max_size 4 maximum_count 360 total_packings 3661 inclusion_maximal 1320
DIRECT_OK n 7 max_size 4 maximum_count 12600 total_packings 26335 inclusion_maximal 12600
VERIFY_OK shortest_paths=PASS all_packings=PASS inclusion_maximal=PASS extremal_counts=PASS rectangular_witnesses=PASS
```

Finite computation is corroboration rather than proof for arbitrary \(m,n\). Proof assumptions, normalization, boundary cases and counting argument are stated in `RESULT.md`. Numerical lists are not used to infer an infinite statement. Independent audit has not been performed.
