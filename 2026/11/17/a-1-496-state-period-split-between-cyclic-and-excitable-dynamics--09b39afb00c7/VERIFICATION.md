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

Two standalone C++17 programs, `verify_memory_walk.cpp` and `verify_indegree_peel.cpp`, verify the entire state space using graph descriptions and graph algorithms that differ. Their outputs, `memory_walk_output.txt` and `indegree_peel_output.txt`, are embedded and were reproduced from these exact source files. A C++17 compiler is the only required executable dependency. The programs do not need external data files or any private resource.

The first program builds the Frucht graph using a 12-cycle plus LCF offsets and memoizes first-return paths. The second creates the exact 18-edge representation and uses indegree peeling; it additionally checks the explicit label-isomorphism, exact eight-class joint distribution, both primitive-cycle populations and both sharp first-entry depths. All 531,441 initial configurations are examined in each program. The two approaches therefore independently test the central cross-period claim without relying on an estimated distribution or finite sample.

A direct witness under the edge-list labels starts at code `4234`, is CCA-periodic with least period eight immediately, and has GHM first periodic entry at update two into a least-period-four orbit. Its CCA states, one cycle in order, are `4234,199214,286560,427458,121345,203258,439785,171624`. Its GHM states through one full recurrence are `4234,201401,459333,132213,4219,201395,459333`.

These checks establish a complete exact finite classification of this one graph. They do not certify historical priority, claims for other graphs, or independent external mathematical validation.
