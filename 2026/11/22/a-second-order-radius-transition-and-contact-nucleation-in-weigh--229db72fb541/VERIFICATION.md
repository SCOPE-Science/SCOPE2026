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

# Verification

Execute `python verify.py` using Python 3 standard library. The actual successful result was:

`SPLIT_DISCOTOPE_PASS cases=560 one_variable_grid=560560 full_simplex_tests=16800 max_grid_excess=1.42e-14`

The checker independently reconstructs the support from all clique and cross disks at the predicted squared-coordinate maximizer, compares against 560,560 equally spaced reduced-coordinate values, and tests 16,800 independently sampled unsymmetrized unit-direction squared-coordinate distributions. A separate symbolic-algebra manipulation confirmed matching values and first derivatives and the exact second derivative jump; independent numerical simplex optimization corroborated 210 configurations. Such finite checks do not prove the universal statement. The proof is in `RESULT.md`, including the strict-concavity reduction, exact one-variable optimization, equality cases, and completeness of contacts.

Important boundaries: positive cross weight, integers \(a\ge2,b\ge1\), standard Euclidean metric, filled coordinate-plane disks. There is no independent audit or independent validation.
