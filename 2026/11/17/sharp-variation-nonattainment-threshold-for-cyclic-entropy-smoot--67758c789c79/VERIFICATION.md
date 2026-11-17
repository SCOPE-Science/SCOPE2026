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

# Reproducible verification

Execute `python3 check_cyclic_softmax_bv.py` with a standard Python 3 interpreter in this directory. The checker uses `fractions.Fraction` and seeded test inputs to validate the identity \(D J=C D\), the exact column-stochasticity and strictly positive support of \(C\), and overlap when \(2w>n\). It also tests full-window constancy, finite equality witnesses when \(2w\le n\), numerical two-input inequalities over positive site weights and temperatures, and near-saturation examples on shorter cycles.

The recorded run produced:

```text
EXACT_RATIONAL_JACOBIAN_COLUMN_STOCHASTIC_CASES_PASS 792
STRICT_COLUMN_OVERLAP_CASES_PASS 360
FINITE_ATTAINMENT_CASES_PASS 36
WEIGHTED_POSITIVE_TEMPERATURE_TWO_INPUT_CHECKS_PASS 198
FULL_WINDOW_CONSTANT_OUTPUT_PASS
ALL_CYCLIC_SOFTMAX_BV_CHECKS_PASS
```

The program does not exhaust all inputs or parameters and is **not** an infinite proof. Analytical justification for every quantifier is supplied in `RESULT.md`, including the derivative factorization, overlap strictness, limiting witnesses, and full-window boundary case. The test uses floating point only for positive-temperature softmax secants and exact rational arithmetic for the critical Jacobian identities. The result has not received independent mathematical audit.
