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

# Verification instructions and scope

The result is proved by exhaustive analysis of a finite deterministic state space with exactly \(3^{14}=4{,}782{,}969\) states. The mathematical reason enumeration is exhaustive is that each base-three integer in the full range is visited and mapped to one successor, followed by exact finite functional-graph period computation. The two finite-state algorithms differ in graph representation and classification method; agreement is corroboration, not a substitute for the coverage argument.

From the package root run:

```
python3 verification/replay.py
```

Python 3 and a C++17 compiler accepting `g++` are required, with no external scientific libraries or network access. The replay compiles `verification/census_indegree.cpp` and `verification/census_paths.cpp` into a temporary directory and compares the complete stdout of each with `verification/census_indegree.out` and `verification/census_paths.out`. It verifies all ten nonzero joint classes and their total, and checks both witness trajectories under a third independent, cyclic presentation of the Fano plane after finding an incidence-preserving relabeling.

The known expected terminal message is included verbatim in `verification/replay.out`. The paths are relative to the package root. All programs use integer calculations; no floating-point tolerances, random seeds, external downloads or extrapolation are used.

**Limits:** The full enumeration certifies only the stated finite graph and fixed update rules. It does not certify priority, independent external validation, conclusions for arbitrary graph families, or claims about graphs not included in the program.
