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

# Exact verification procedure

The certificate uses exhaustive breadth-first search from one representative of each conjugacy class; the conjugacy reduction is proved in `RESULT.md`. Both checks are standalone and require no data download.

Compile and execute the first implementation:

```sh
c++ -O3 -std=c++17 verify_crown_switch.cpp -o verify_crown_switch
./verify_crown_switch
```

Execute the independently structured second implementation:

```sh
python3 verify_crown_switch_independent.py
```

Both programs check 133496 derangements, 8 cycle-type representatives, radius 8, diameter 10, and the unique inverse antipode for the 2240 vertices of cycle type (3,3,3), implying 1120 unordered extremal pairs. The C++ program also asserts the exact edge count, degree distribution and reverse adjacency. The Python program uses a different state generator and direct on-the-fly legal switch expansion, checks that each traversal visits precisely its independently generated full state set, and agrees on all type-specific distance shells.

Actual executions from the packaged source content terminated successfully and printed `all_checks_passed` and `independent_checks_passed`, respectively. The programs prove the specified finite facts by exhaustive traversal; their output does not assert results for other orders. Independent scholarly audit remains unperformed.
