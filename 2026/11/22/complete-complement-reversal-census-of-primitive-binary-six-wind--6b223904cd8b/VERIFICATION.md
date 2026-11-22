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

The complete six-window universe was generated from the proper-period test for periods 1, 2 and 3. The reproducible pure-Python script `verify.py` rebuilt the 32-vertex and 16-vertex Laplacians and checked exact integer cofactors, degree distributions, the voltage parity, symmetric windows and Burnside arithmetic. It returned `VERIFY_OK` with determinants 389120 and 320.

A separate C++ implementation `enumerate.cpp` rooted each full Euler tour at the uniquely occurring edge `000001`, counted 389120 tours and checked each tour's normalized bit-complement, reversal and reverse-complement images. Its output was `total=389120 F_C=320 F_R=0 F_CR=0 orbits=97360`. The two computations use different methods: exact matrix-tree determinants versus direct edge-exhaustive enumeration.

No claim is made about window orders other than six or about a general all-length enumeration. The symmetry nonexistence proof uses four primitive palindromic windows and six primitive antipalindromic windows, each exceeding the two possible reflection-fixed start positions. An independent mathematical audit has not been performed.
