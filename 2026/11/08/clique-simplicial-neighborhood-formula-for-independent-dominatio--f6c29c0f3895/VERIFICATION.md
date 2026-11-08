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

# Reproduction

Run `python verify.py` with Python 3 and no third-party packages. The test reconstructs original base graphs and their central graphs, enumerates all independent dominating sets from actual adjacency, and compares every cardinality with separately evaluated clique and multipartite formulas. It also independently checks the triangle-free degree formulas on a finite exhaustive family.

Observed output from the standalone source:

```
ALL_LABELLED_GRAPHS_N1_THROUGH_N4_OK 75
SEEDED_RANDOM_CONNECTED_GRAPHS_N5_N6_OK 20
MULTIPARTITE_BOUNDARY_FORMULAS_OK 112
MULTIPARTITE_DIRECT_EXAMPLES_OK
TRIANGLE_FREE_MINIMUM_DEGREE_TWO_FORMULA_OK 560
VERIFY_OK
```

The tests are finite: arbitrary graphs of unbounded order are not enumerated. The proof in `RESULT.md` establishes the unrestricted theorem by an exact bijection and a necessary-and-sufficient domination criterion. The computation verifies examples, not publication priority or independent certification.
