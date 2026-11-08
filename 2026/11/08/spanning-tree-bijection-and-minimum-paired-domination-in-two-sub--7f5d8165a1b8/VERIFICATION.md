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

The `verify_min_paired_kg2.cpp` source is standalone C++17. Compile with `c++ -O2 -std=c++17 verify_min_paired_kg2.cpp -o verify` and run `./verify`.

The program constructs `KG(n,2)` adjacency from disjointness of pairs, checks domination using closed neighborhoods, and checks perfect matchability recursively by selecting an unmatched vertex and trying all partners. For orders 4 through 7, the program evaluates all nonempty selected subsets and validates the claimed minimum size and exact number of optimal sets. On order 5 it separately checks the complement-tree property for each optimal set. At orders 6 and 7, it checks the required three-edge matching in every optimal four-edge auxiliary graph. For order 8, it checks every four-element selected subset against the auxiliary matching criterion and compares the result with the all-parameter formula.

Observed run: `VERIFY_OK full_orders=4..7 full_subsets=2131004 paired_sets=1013127 n8_four_subsets=20475 minimum_counts=1,125,180,1575,7665 tree_bijection_n5=PASS three_families=PASS`.

The exact results beyond the finite tested orders depend on the preceding proof, not the experiments. No external or independent mathematical audit is claimed.
