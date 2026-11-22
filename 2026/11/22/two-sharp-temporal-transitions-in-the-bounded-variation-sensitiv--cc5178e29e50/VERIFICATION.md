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

Run `python3 check_star_heat_derivative.py` using Python 3 with the standard library only. The checker computes vertex heat solutions by their independently derived two-eigenspace decomposition and checks their centered finite-difference time derivatives against the exact edge transfer. It also checks the analytic piecewise formula against the signed-column expression, exact single-edge equality, finite random-signal norm bounds and turning-point locations. Rational arithmetic verifies the two decisive degree-threshold inequalities without rounding.

Observed output:

```text
CLOSED_FORM_AND_ONE_EDGE_SHARPNESS_PASS k=2..80
INDEPENDENT_VERTEX_HEAT_FINITE_DIFFERENCES_AND_INPUT_STRESS_PASS cases=1740
SECONDARY_TURNING_TIME_AND_PEAK_SAMPLED_PASS k=4..150
EXACT_DEGREE_EIGHT_NINE_UNIT_GAIN_TRANSITION_PASS 10330523392/10460353203 536870912/341796875
ALL_STAR_HEAT_TEMPORAL_BV_CHECKS_PASS
```

Finite data alone cannot prove the statements for every star size and time; the exact rank-one evolution, induced-column norm and symbolic monotonicity argument are the proof. The script does not test nonuniform conductances, and no independent audit was performed.
