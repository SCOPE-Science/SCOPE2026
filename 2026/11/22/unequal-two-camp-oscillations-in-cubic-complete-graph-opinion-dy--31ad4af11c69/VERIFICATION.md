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

# Verification of exact cubic two-camp calculations

Run `python checker.py` with Python 3. It performs 65 exact rational construction and Jacobian checks for agent counts 3 through 12 and tests the sharp strict spectral conditions against computed rational eigenvalues. It also independently evaluates the rational five-agent witness using the source model parameters and checks the exact return multipliers.

Observed output from execution on these files:

```
PASS: 65 exact two-cluster checks, plus exact five-agent witness and multipliers
```

Every comparison is exact using `fractions.Fraction`; no floating-point tolerance is involved. The all-parameter proof, including the cluster-size barrier and the mean-convergence argument, is provided in `RESULT.md`. Finite tests neither enumerate every orbit nor establish global attraction. Nonlinear behavior at eigenvalue-modulus-one boundaries and empirical robustness outside complete-graph coupling are not verified.
