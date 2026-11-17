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

# Reproduction of exact finite classification

The two source programs `verify_indegree.cpp` and `verify_trajectory.cpp` were copied into this scientific package and **compiled and replayed from these exact paths** with standard C++17 and integer arithmetic. The first was executed with parameters `4 5`, the second has these dimensions built into a separate column-major construction. Raw expected outputs are `out_indegree.txt` and `out_trajectory.txt`.

```sh
g++ -O3 -std=c++17 verify_indegree.cpp -o check_indegree
./check_indegree 4 5 > actual_indegree.txt
g++ -O3 -std=c++17 verify_trajectory.cpp -o check_trajectory
./check_trajectory > actual_trajectory.txt
diff -u out_indegree.txt actual_indegree.txt
diff -u out_trajectory.txt actual_trajectory.txt
```

Both programs exhaust the \(2^{20}=1,048,576\) distinct states. Program one implements a full indegree-based functional-graph decomposition and union-find cycle-equivalence classes; program two traces trajectories with separately constructed transitions, independently tests every state's fixedness and period-two return, and applies Burnside's lemma to 160 symmetries. The two agree on both classes of temporal cycles, all 12 period/entry cells, all basins, and a sharp maximal first-entry depth five. Their group orbit counts are 53 fixed and 67 two-cycle classes. Burnside fixed-cycle sums equal 8,480 and 10,720 for those periods.

**Limits.** Finite exhaustive computations prove claims for the specified 20-site grid; they are not a theorem for arbitrary sizes. Neither implementation has received independent external mathematical validation. A separate general theorem already supplies eventual period at most two; the new contribution is only the explicit finite census.
