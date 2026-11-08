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

The self-contained `verify.py` uses only the Python standard library and may be run using `python3 verify.py`. The observed successful output was:

```
CYCLIC_WORD_ENUMERATION_OK
RECURSIVE_TILE_AND_RESIDUE_CODE_OK
DIRECT_SMALL_OPTIMA_OK
THEOREM_CHECKS_OK
```

The checks enumerate every binary cyclic word through length thirteen, compare exact half-\(\ell_1\) separations, verify recursively generated clique partitions through \(m=60\), test residue-code sizes, and independently search optimal independent sets at lengths four and eight. These are finite checks of key proof constituents; the theorem for unbounded \(m\) relies on the explicit inductive proof in `RESULT.md`. No independent audit or external certification is claimed.
