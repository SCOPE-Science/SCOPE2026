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

# Reproducible checks

Run `python verify_star_two_input.py` with Python 3 standard library. The checker computes direct graph-distance balls independently of the closed-form branch map, tests all explicit attaining pairs, and checks exact rational input-pair and strict-Jacobian inequalities.

Observed output:

```text
EXACT_ATTAINING_NONNEGATIVE_PAIRS_PASSED 23
DIRECT_BALL_VS_BRANCH_FORMULA_PASSED 3905
TWO_INPUT_EXACT_RATIONAL_CHECKS_PASSED 39098
STRICT_BRANCH_COLUMN_NORMS_PASSED 11949
ALL_STAR_UNCENTERED_TWO_INPUT_DIAGNOSTICS_PASSED
```

The unrestricted dimension parameter and the quantification over all real admissible data are established by the proof in `RESULT.md`, not by finite test exhaustion. The three-leaf active-set incompatibility is an analytical lemma. No independent mathematical audit or external proof assistant certification has been performed.
