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

# Verification and reproducibility

The proof is analytic and complete over \(\alpha\ge4\) and unequal maxima in \([1/2,1)^2\). The mixed step is derived from the original max operation, not postulated. The finite-transition proof covers arbitrarily long initial unmixed runs without a numerical termination bound depending only on \(\alpha\); the bound also depends on the initial odds ratio. Subsequent invariance and the \(55/64\) Lipschitz bound are uniform in initial condition and resource value within the claimed regime.

Run `python checker.py` with Python 3 and SymPy installed. The executable contains independent exact rational updates of the original maxima map, fixed-seed sampling of 700 rational initial conditions, four post-switch mixed steps in each case, 1500 long numerical trajectories at six resource values, and exact SymPy checks of the Jacobian and fixed point. Observed stdout:

```
PASS: 700 exact initial trajectories enter permanently mixed regime; repeated map identities exact.
PASS: 1500 float initial trajectories converged to exact high-resource limit.
PASS: symbolic Jacobian, positive fixed point and physical-coordinate formulas.
```

These finite tests would not establish eventual branch absorption for every real initial state, or infinite-time convergence. Those conclusions are supported by the finite-transient inequality and the invariant-rectangle contraction in RESULT.md. Unproved extensions: resources in \(2<\alpha<4\), optimality of the sufficient threshold, and other update rules. Independent mathematical audit has not been performed.
