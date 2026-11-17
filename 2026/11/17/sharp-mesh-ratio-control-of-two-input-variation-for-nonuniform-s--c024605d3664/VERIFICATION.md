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

# Analytical and computational verification

The argument is reconstructed in `RESULT.md`. The critical exact polynomial identities and exact local witness are explicitly tested by `steffen_nonuniform_verify.py` using Python's standard-library `fractions.Fraction`. The executable also runs 2,500 seeded irregular-grid stress tests of one-input variation preservation and two-input variation bounds.

Replay with `python3 steffen_nonuniform_verify.py`; the recorded successful terminal lines were:

```text
EXACT_BASIS_INTEGRALS_AND_FOUR_CORNER_IDENTITIES_PASS 8/27
EXACT_WITNESS_COEFFICIENT_PASS 107/27
NONUNIFORM_RANDOM_TWO_INPUT_AND_ONE_INPUT_BV_CHECKS_PASS 2500
ALL_STEFFEN_NONUNIFORM_CHECKS_PASS
```

The finite sample tests do not establish the theorem for infinite or arbitrary grids. The infinite claim is supported by the piecewise-affine derivative bounds, the analytic integral identities, the truncation step, and the explicit exact extremizer. Original source availability and historical priority limitations are described separately in `AUDIT.json`.
