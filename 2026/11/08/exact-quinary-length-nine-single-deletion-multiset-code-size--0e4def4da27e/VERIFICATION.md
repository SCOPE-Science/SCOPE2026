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

Two separate executable verifiers generate the *entire* finite problem. `checker.py` constructs all 715 weight-nine vectors and 495 weight-eight vectors, checks the 143-element checksum construction and all 10,153 unordered construction pairs, and runs an optimality-certified 715-variable binary integer program with 495 clique inequalities. `checker_edges.py` independently enumerates 4,950 conflicting unordered pairs and runs an equivalent integer program using pair constraints.

Run with `OPENBLAS_NUM_THREADS=1 python checker.py` and `OPENBLAS_NUM_THREADS=1 python checker_edges.py`. Dependencies are listed in `requirements.txt`; no input data files are needed. Both verified mixed-integer solutions must have global optimal status (zero optimality gap) and size 143. The first model replay returned `VERIFY_OK S_5(9,1)=143`. An incomplete optimization or a feasible solution without a matching global dual bound does not establish the upper bound.

The integer-model encoding is proved equivalent to correction of one multiset deletion in `RESULT.md`. Solver-based numerical branch-and-bound is the finite exhaustive upper-bound method; no separate exact rational proof trace is supplied. Independent verification is not yet performed.
