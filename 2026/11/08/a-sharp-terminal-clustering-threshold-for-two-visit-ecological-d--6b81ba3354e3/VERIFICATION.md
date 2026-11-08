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

# Verification record

Run `python3 checker.py` with Python 3 and no third-party dependencies. It produced:

```
exact_and_numeric_checks_passed 30800
example_Hc_t1_Poptimal_Pterminal_gain (0.5493061443340549, 1.2746530721670275, 0.4047648693805451, 0.36813163541672467, 0.036633233963820455)
```

The checker independently propagates a two-state occupancy probability vector through both survey times, multiplying occupied-state mass by the nondetection factor at each survey. It compares this probability against the inclusion-exclusion formula for 2,500 rational parameter quadruples, checks interval bounds, tests 100 continuous-parameter designs against every admissible pair in a 21-point time grid, and checks the exact optimal gain at each design.

Exact rational assertions are exact only for the selected finite test cases. The time-grid tests are numerical diagnostics, not proofs of a continuum optimum. The proof for all positive rates and every allowable detection probability is the transition-law, monotonicity, and strict-concavity argument in `RESULT.md`. Independent mathematical validation has not been performed.
