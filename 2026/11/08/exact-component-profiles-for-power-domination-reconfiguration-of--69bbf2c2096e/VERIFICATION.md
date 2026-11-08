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

# Verification

Compile and run the standalone program from the extracted files:

```sh
c++ -std=c++17 -O2 verify.cpp -o verify
./verify
```

The checker enumerates subsets in the exact finite domains stated below. It does not certify the unrestricted theorem, which is proved in `RESULT.md`.

Expected final status from the executed program:

```
VERIFY_OK orders=4..8 budget_component_cases=14 exact_minimal_sets=5784 direct_PDS_checked=40650 full_direct_orders=4..7 matching_partition_counts=PASS components=PASS
```

Detailed budget-component checks include \(n=6\): \(45,61,1\) at budgets \(2,3,4\); \(n=7\): \(735,106,1\) at budgets \(3,4,5\); and \(n=8\): \(420,4201,169,1\) at budgets \(3,4,5,6\). These counts are verified by BFS over feasible sets, not inferred from the theorem. Direct power-domination simulation is exhaustive for every subset at orders four through seven, and additionally applied to selected feasible subsets of order eight. A separate rooted-star-partition enumeration matches the analytic minimal-set counts. All arithmetic involved in the finite checker is integer/bitwise. No source downloaded from the web is required to execute it.

The standalone checker has a finite scope: it cannot rule out a counterexample at higher order. Missing independent peer assessment and publication-priority uncertainty are distinct from computational correctness checks.
