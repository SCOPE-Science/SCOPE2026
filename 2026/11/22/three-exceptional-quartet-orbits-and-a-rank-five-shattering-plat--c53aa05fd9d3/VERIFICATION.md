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

# Reproducibility and scope

All recorded checks are **complete finite integer computations**. Two programs use separate implementations of the field arithmetic and trace algorithm: `verify_bitmask.cpp` propagates candidate-center bit masks, and `verify_direct.cpp` generates the complete pattern set by iterating all \(81\) centers. Both test every zero-containing support through size six. An additional Python program, `verify_orbits.py`, independently enumerates all normalized four-supports, constructs semilinear translation-normalized orbits, checks orbit-uniform traces, and tests the existence of shattered five-extensions orbitwise.

The expected C++ normalized counts at ranks one through six are \((1,80,3160,81920,587400,0)\), from \((1,80,3160,82160,1581580,24040016)\) tested supports. The direct implementation finishes with `DIRECT_OK`. The Python program finishes with `ORBIT_OK` and checks three nonshattered four-orbits and two nonextendable shattered four-orbits.

The mathematically exact finite proof consists of the trace-partition invariant, complete bounded enumeration over normalized subsets, and the translation double-counting identity. These computations do not establish a result at any other field size. Verification is same-model and reproducible; no independent mathematical audit has been carried out.
