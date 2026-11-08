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

The exact claim was checked by two different whole-space finite algorithms with no numerical approximations. Run `python verify.py` from the directory containing `verify.py`, `verify_subsets.cpp`, `verify_recursive.cpp` and `expected.tsv`, with a local C++20 compiler.

`verify_subsets.cpp` precomputes all induced-subgraph edge counts over 65,536 vertex subsets and enumerates disjoint ordered color classes. `verify_recursive.cpp` adds one vertex at a time, counting edges to earlier assigned vertices. Each exhausts exactly 43,046,721 labeled configurations per graph. Both results exactly match the complete 17-sector table for each graph in `expected.tsv`. The subset checker also verifies the graphs' degree, common-neighbor counts and vertex counts. Both checks passed on the packaged source paths, including after staging the files for delivery.

An independent structural proof gives the energy lower bound \(6J\) for both via the shared adjacency spectrum, sharp on Shrikhande through the displayed witness; disjoint rook-row and rook-column clique constraints strengthen the other bound to \(8J\), also attained. Every finite field interval and critical degeneracy follows by exact rational lower-envelope arithmetic on the complete sector table.

Limits: no assertion is made for larger graphs, more colors, nonuniform couplings or thermodynamic limits. No independent external audit, formal verification or historical uniqueness certificate is claimed.
