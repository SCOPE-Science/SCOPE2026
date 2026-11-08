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

Run `python3 checks/check_matrix.py` and `python3 checks/check_orbits.py` from the directory containing this document. Both programs require only a standard Python 3 installation. The corresponding `.out` files capture exact standard output from the tested scripts.

The matrix checker enumerates every labelled simple graph on one through five vertices, tests whether its binary adjacency is nilpotent, and for each eligible base graph constructs the corona adjacency and its reversible wave companion. It checks the exact operator order by matrix powers and checks the fixed-space nullities for updates \(k\in\{1,2,3,4,6,12,24,48,96\}\). It reports 1,099 simple graphs, 278 nilpotent-base graphs, and additional specific tests of \(P_3,P_7,P_{15},C_4,Q_4\).

The separate state checker does not call the matrix-power checker; it enumerates 69,648 binary two-time-level states of the three coronas based on an isolated vertex, \(P_3\), and \(C_4\), advances the local wave rule, and independently compares the first return time with the claimed formula. Both programs finished successfully and their output matches the packaged `.out` files. They test finite cases only; correctness for all finite base graphs and all characteristic-two extension fields rests on the written algebraic proof.

No independently conducted audit or validation is represented by these checks.
