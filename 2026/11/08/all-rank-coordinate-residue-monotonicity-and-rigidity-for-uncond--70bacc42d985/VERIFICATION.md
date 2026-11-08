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

# Reproducibility checks

Run `python3 verify_unconditional_residues.py` using only Python 3 standard-library modules. The script enumerates finite absolute ideals and small lattice cross-polytope balls in dimensions one through four, directly forms modular coset keys, independently tests centered representatives and verifies the exact equality-box criterion. Output:

```
ABSOLUTE_IDEALS_OK cases=416 monotonic_pairs=1664 strict=1533 equal=131 formula_checks=2080
THREE_DIMENSIONAL_L1_COUNTS 1,7,19,22,25
EQUALITY_BOX_CHECKS 1664
```

The analytic proof gives all dimensions and moduli; computational samples are supplementary and cannot establish infinite claims. The equality statement assumes an absolute coordinate ideal and a diagonal coordinate subgroup; skew subgroups remain unproved. Independent mathematical audit was not performed.
