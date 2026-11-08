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

This result is proved for every integer \(n\ge3\) using a direct bijection and the labelled permutation exponential formula; computations below are corroboration only.

The standalone `verify.py` constructs the Cartesian graph directly and computes pairwise distances by breadth-first search without using the theorem. It enumerates all maximal three-vertex geodesics, and obtains unordered perfect path packings by exact-cover recursion on the occupied cell mask. It extracts a column permutation and independently computes proper-coloring weighted permutation-cycle distributions. Tests for \(2\le n\le7\) provide an additional boundary case at \(n=2\), outside the stated family.

Actual output of `python3 verify.py`:

```text
GRAPH_OK 2 12 6 {1: 6}
GRAPH_OK 3 36 12 {1: 12}
GRAPH_OK 4 72 216 {1: 108, 2: 108}
GRAPH_OK 5 120 1440 {1: 720, 2: 720}
GRAPH_OK 6 180 22320 {1: 7920, 2: 11160, 3: 3240}
GRAPH_OK 7 252 272160 {1: 90720, 2: 136080, 3: 45360}
VERIFY_OK direct_shortest_paths=PASS disjoint_exact_covers=PASS cycle_count_distribution=PASS closed_formula=PASS
```

The first numeric column after graph order is the independently enumerated number of maximal shortest three-vertex paths, the next is the number of unordered perfect packings, and the dictionary records their canonical permutation-cycle distribution. The recursion is exhaustive for these finite orders, but it is not a proof of infinitely many cases. Mathematical limitations and the preexisting OEIS sequence are disclosed in the proof and review. Independent mathematical audit has not been performed.
