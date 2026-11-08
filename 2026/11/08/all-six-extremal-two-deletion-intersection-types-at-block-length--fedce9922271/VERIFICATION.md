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

Compile the included `checker.cpp` with `g++ -std=c++17 -O2 checker.cpp -o checker` and execute `./checker`. Its complete restricted-growth enumeration covers all 4140 partitions of eight positions, checks the one-deletion intersection constraint directly, and asserts the number of admissible patterns (3690), the sharp maximum (4), and the exact set of six maximizing patterns. The code uses standard C++17 only and no outside packages, input tables, or randomization. An independent all-pairs word enumeration for alphabet sizes two through four also checked the labeled maxima counts (2, 30, 132). These numerical checks alone do not establish an arbitrary-length theorem; the all-alphabet claim follows because equality-pattern canonicalization exhausts the underlying eight positions.

Limits: no conclusion is claimed beyond length four or beyond the specified deletion/disjointness conditions. Independent external mathematical review has not been performed.
