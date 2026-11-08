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

# Verification and limits

Run `python3 verify.py` with Python 3 and no third-party packages. The direct exact count enumeration, finite outcome enumeration, and finite-sum formula are implemented separately, with integer arithmetic; the program also checks all tested pair transfers and their explicit positive lower bound. Actual run output:

```
PASS: exact formula/direct count comparison, optimum, uniqueness: 7920 instances
PASS: independent complete binary-state enumeration: 1458 instances
PASS: strict pair transfers and uniform lower bound: 30240 comparisons
PASS: 3 agents / 6 goods with p=1/2: balanced 23/32; (1,2,3) 9/16
```

The tests cover \(n\in\{2,3,4,5\}\), the finite ranges encoded in the script (up to ten goods for the first three population sizes and eight goods for five agents), and three rational success probabilities. The exact proof of the infinite theorem is contained in `RESULT.md`; enumeration alone establishes no untested case. The Gaussian asymptotic uses the standard local binomial central limit theorem and is not a computer-certified infinite assertion. Independent audit has not been performed.
