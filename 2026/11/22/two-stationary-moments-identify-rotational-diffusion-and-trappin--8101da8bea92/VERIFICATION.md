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

The checked theorem uses exact stationary population moments in spatial dimensions \(d\ge2\). `check.py` needs only the Python 3 standard library and runs the independent stationary-generator rational recurrence for second/fourth moments and the numerical inverse for calibrated parameter grids. The checker returned `PASS: 362 exact-rational and independent numerical assertions` when executed against this package's code.

The finite grid verifies examples, not the infinite-parameter result. The proof of the universal open feasible region uses symbolic positivity and the strict derivative of \(F_d\). The lower and upper fourth-cumulant boundaries are limiting values, not attained by positive finite angular and trap rates. A simulation or a finite search alone would not establish these claims. No external or independent scientific audit has been performed.
