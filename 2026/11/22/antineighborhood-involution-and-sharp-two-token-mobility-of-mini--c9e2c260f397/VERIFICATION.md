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

Both standalone verification programs, `check_a.cpp` and `check_b.py`, were executed on their extracted source and produced the same complete numerical summary saved as `CHECKS.txt`. These programs construct isomorphic models of the Clebsch graph in different ways, enumerate all assignments up to the optimum weight, and check every exact two-token adjacency and all-source shortest path.

The classification and lower bound also have a direct mathematical proof in `RESULT.md`. The metric statements are finite exhaustive conclusions, not extrapolations to larger graphs. Independent scholarly validation was not performed. Compilers/interpreters: C++17 and Python 3 standard library.
