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

Reproducibility: `CHECKER.cpp` was compiled with `g++ -O3 -std=c++17` and executed on the full 85,766,121-matrix search space. It returned the three nonresonant spectral strata (720, 3600, 720 matrices; 1, 5, 1 relabeling classes) and proved strong connectivity of every accepted graph. `CROSSCHECK.py` was run under Python 3; its independent 46,656 block-pair enumeration returned 72, 360, 72 cases per fixed bipartition, agreeing after multiplying by ten partitions. The proof outside the finite space is the analytic five-cell impossibility and the six-cell forced real eigenvalue.

Limits: The enumeration does not address seven or more cells. The nonlinear normal form and invariant tori were not computed; the smooth admissible coupling is used only to realize and transverse-cross the linear spectrum. Independent audit not performed.
