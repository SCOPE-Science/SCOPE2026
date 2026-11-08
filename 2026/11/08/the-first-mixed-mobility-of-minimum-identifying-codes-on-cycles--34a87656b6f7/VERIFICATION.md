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

# Reproducibility

Run `python3 verify_exhaustive.py` and `python3 verify_orbits.py` with standard Python. The captured standard outputs in `exhaustive_output.json` and `orbit_output.json` were reproduced exactly in a clean execution from extracted package contents. Every program uses only the standard library.

The first program constructs every minimum identifying code through all-subsets enumeration for the labeled cycles of orders \(4\) through \(11\); it makes no assumption about the minimum size or the transition graph. The second program uses the independently derived omitted-vertex criterion and orbit classification and independently checks all representative one-move neighbors.

The cyclic-orbit proof uses exactly \(55\) independent omitted four-sets of the step-three \(11\)-cycle and rules out omitted five-sets via domination. Its three valid translation orbits are exhaustive, and its move table gives a purely combinatorial explanation of the frozen and mobile sectors. BFS verification of the jumping radius and diameter is an exhaustive finite computation only.

The reported scope is the finite first-coexistence theorem. No claim is made about all larger cycle orders, different radii, or independent scholarly validation.
