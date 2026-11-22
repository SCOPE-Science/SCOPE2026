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

Run `python checker.py` using Python's standard library. It passed 1,732 rational-grid and numerical assertions checking the discriminant, inversion, Fourier moments and null variance. The proof uses exact symbolic identities plus bounded multivariate CLT and a Taylor/Hellinger comparison, rather than relying on finite experimental output for an infinite statement.

The Hellinger lower bound is only for tests of the composite exponential null with uniform near-rate size control; no independent mathematical audit or externally certified historical priority is asserted.
