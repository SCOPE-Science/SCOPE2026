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

The accompanying `verify_exact.py` uses Python's standard-library rational type. The full proof has three reductions: finite active-ball selector matrices, decomposition of cyclic gradients into oriented arc indicators, and a convex endpoint-box maximum. For the complete family of cycles with diameter at most two, it exhausts exactly 104 rational vertices across five interval boxes. It separately checks three explicit nonnegative two-input witnesses and 3000 exact rational stress tests.

Run `python3 verify_exact.py` from the extracted package directory. No external input files or third-party packages are required. The finite endpoint-box enumeration closes the only finite combinatorial calculation in the proof; the 3000 stochastic tests are not proofs. The result does not cover longer cycles, signed input pairs, nonuniform averaging masses, or weighted edge variation. Independent audit has not been performed.
