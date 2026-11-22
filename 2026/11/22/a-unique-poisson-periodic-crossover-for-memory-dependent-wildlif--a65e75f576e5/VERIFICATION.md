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

# Reproduction of calculations

Run `python3 checker.py` using Python 3 and the standard library only. At package review, the program completed successfully and printed:

```
PASS: 1236 deterministic assertions plus 28,000 Monte Carlo histories
J(1)=0.796599599297056; unique crossing rate at k=g=1: 2.279008229727
Poisson rate stationary extrema, example: 1.327628549271 6.768458109866
```

The checker independently evaluates the integral using numerical quadrature and a convergent power series, verifies strict sign changes over randomly selected parameters, confirms the two response-rate extrema and the exact critical floor criterion, and simulates finite-window stationary Poisson histories. The simulation truncates histories after 30 memory lifetimes; the expected omitted memory is \((\lambda/\gamma)e^{-30}\), and the proof does not depend on these numerical results. Uncountably many parameter settings and all stochastic histories cannot be certified by numerical sampling. The all-parameter uniqueness, derivative classification, and asymptotics follow from the analytic arguments in RESULT.md, not from executable tests.

No externally independent audit or biological calibration has been performed.
