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

The self-contained `checker.py` executes under standard Python 3. It checks exactly, using rational fractions, the first 18 first-passage coefficients against the Catalan formula and 14 finite-barrier upcrossing probabilities against the martingale value. It additionally checks four central-binomial asymptotic approximations and 47 Fibonacci roof bounds; total: 83 checks.

These checks concern finite instances and numerical inequalities. They do not establish the infinite-time first-passage distribution, the general overshoot identity, or the asymptotic original-clock excursion tail. Those statements rely on the analytic derivation in RESULT.md and on the exact geometric inducing properties attributed to Ji and Ma.
