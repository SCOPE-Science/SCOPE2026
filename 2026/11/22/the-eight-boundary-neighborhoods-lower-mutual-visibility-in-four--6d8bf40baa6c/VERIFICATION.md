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

# Verification scope

The mathematical claim applies to every integer \(n\ge2\) and has two logically separate components: a reduction of configurations of size at most four to cylinders of at most 17 columns, and an exhaustive classification within that finite domain. The reduction is proved by the geodesic normal form in `RESULT.md`; a finite test cannot independently prove that lemma. The geodesic-mask program directly examines every subset of sizes three and four for each \(2\le n\le17\), enumerating all shortest paths and testing all single additions. Exact equality, not just the counts, to the predicted closed neighborhoods is checked. The independent BFS program separately builds product graphs and tests shortest distances after blocking selected internal vertices, and checks heights 2 through 8. A randomized compression test compares both selected-pair feasibility and inclusion maximality on 1,430 instances.

# Reproduce the recorded checks

From the directory containing these files:

```
g++ -O2 -std=c++17 cylinder_minfacet.cpp -o cylinder_minfacet
for n in $(seq 2 17); do ./cylinder_minfacet "$n"; done

g++ -O2 -std=c++17 cylinder_bfs_verify.cpp -o cylinder_bfs_verify
for n in $(seq 2 8); do ./cylinder_bfs_verify "$n"; done

python3 compression_smoke.py
```

`minfacet_counts.txt`, `bfs_counts.txt`, and `compression_smoke.txt` preserve the actual outputs of these commands. All main enumeration rows must have `size3_facets=0`, `incorrect=0`, `agreement=YES`, with ten four-sets at height two and eight at every other height. No unexplained partial enumeration, numerical approximation, inaccessible dependency, or pending computation is used in the theorem statement.

# Unproved limits

The programs do not prove results for widths other than four, or for arbitrary sets beyond minimum cardinality. Historical priority and independent expert validation remain unestablished. The infinite extension depends on the mathematical compression lemma as written, not on claiming a test at every order.
