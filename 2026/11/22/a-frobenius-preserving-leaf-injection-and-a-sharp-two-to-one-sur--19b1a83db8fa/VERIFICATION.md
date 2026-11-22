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

# Reproducibility

Run `python3 VERIFY.py` from the extracted artifact directory with Python 3 and its standard library only. Expected exact output is:

```
VERIFY_OK F_range=3..299 leaf_checks=5093
```

The checker independently determines semigroup membership and minimal generators, compares leaf status with the four-family criterion, verifies every exact fixed-F count, checks the map has unique images and that all targets are valid, internal and have the same Frobenius number. All admissible Frobenius numbers from 3 to 299 and all their multiplicity-four semigroups are covered by this finite test. The mathematical theorem ranges over every admissible Frobenius number and is proved symbolically in `RESULT.md`; finite tests are not an exhaustive infinite argument. Independent audit has not been performed.
