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

The analytical proof covers every integer \(m\ge1\) and every admissible nonnegative input pair; no computer enumeration is treated as an infinite proof.

Reproduce exact-rational diagnostic checks using `python check_star_maximal.py`. A completed execution returned:

```
EXACT_SHARP_WITNESSES_PASSED 64
EXACT_INTEGER_GRID_SINGLE_COORDINATE_PERTURBATIONS_PASSED 21321
TWO_INPUT_RATIONAL_TOTAL_VARIATION_CHECKS_PASSED 8399
SYMBOLIC_ACTIVE_BRANCH_BUDGETS_PASSED 1375
EXACT_SIGNED_DOMAIN_OBSTRUCTIONS_PASSED 160
ALL_STAR_MAXIMAL_TWO_INPUT_BV_DIAGNOSTICS_PASSED
```

The grid and pseudorandom input checks are finite corroboration. The sharp branch analysis, coverage of all real inputs, endpoint cases and signed obstruction appear in the proof. The exact rational checker uses only Python's standard library.
