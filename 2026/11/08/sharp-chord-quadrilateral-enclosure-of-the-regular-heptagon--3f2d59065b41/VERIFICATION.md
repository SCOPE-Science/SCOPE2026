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

## Reproduction

Execute `python3 heptagon_cert.py` from the extracted research files. It uses only Python's standard-library `fractions` and `itertools` packages. Its success line is:

`HEPTAGON_CHORD_QUADRILATERAL_EXACT_OK bounded_four_line_sets 511 optimizers 7 exact_zero_slacks 14 minimum_scaled_area_gap_gt 0.02251624042544506 minimum_strict_slack_gt 0.37651019722331774`

The reported decimal lower bounds display exact rational interval results; all actual comparisons in the verifier use rational endpoints, not floating-point tests. It checks finite exhaustiveness, positivity of the support intersections, exact vanishing of algebraic equality slacks, and a strict area gap for all nonoptimizers. For the global finite-to-infinite inference, the proof in `RESULT.md` explains why every chord quadrilateral reduces to one of those 511 supporting-line choices.

## Scope of verification

The certificate is a finite exhaustive exact-algebra proof for this specific heptagon. It is not a proof for arbitrary heptagons, unrestricted enclosing quadrilaterals, other regular polygon orders, or either general enclosing-quadrilateral conjecture. The originality and mathematical-value assessments are same-model assessments only. Independent audit has not been performed.
