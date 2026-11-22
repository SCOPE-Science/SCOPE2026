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

## Checks executed

The accompanying standard-library `CHECKER.py` was executed against the exact embedded `CENSUS.csv`: it lists every normalized projective pair of candidate free points over the five stated finite fields, and separately evaluates the necessary cubic parameter equation on every triple. All computed ten-tuples are checked for definedness, ten distinct points, ten required incidences and absence of any additional collinear triple. The independent enumerations agree. The five rows are `(q, equation roots, distinct candidates, strict classes)`: `(2,4,0,0)`, `(3,13,0,0)`, `(4,22,0,0)`, `(5,31,0,0)`, `(7,50,1,1)`. The asserted unique witness has parameters `(5,6,6)` over the seven-element field.

This exact bounded certificate uses no random tests, external software, or unstated computational dependencies. It does not prove formulas for arbitrary larger finite fields. Independent audit is not performed.
