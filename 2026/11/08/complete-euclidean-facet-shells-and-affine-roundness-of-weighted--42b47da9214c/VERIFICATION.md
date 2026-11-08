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

# Reproducibility and limits

`verify.py` is standalone Python 3 requiring `sympy`. Run `python verify.py` from a folder containing that file. In this package it was run on its own contents before acceptance and passed 15 configurations: 3 rational weight vectors in each dimension 2 through 6. Checks include exact vertex counts, direct support inequalities, supporting affine ranks, exact origin-radius comparisons, longest interval uniqueness, the pulled-back type-A quadratic form, and balanced-subset John support bounds. These finite tests are not an exhaustive argument for all real weights or dimensions. The paper's proof provides unrestricted reasoning. The self-review is not an external mathematical certification.
