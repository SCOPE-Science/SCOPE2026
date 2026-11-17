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

# Reproducibility and scientific verification

The theorem concerns the reduced Chialvo map \(f_{r,k}(x)=x^2e^{r-x}+k\). The standalone executable `check_chialvo.py` requires Python, SymPy, NumPy and SciPy and is run as `python check_chialvo.py`. It uses exact symbolic arithmetic to verify 12 identities at \(q=2+\sqrt2\), \(r_c=q-\log[q(q-2)]\). It solves nine actual period-two equations with positive half-gap over three positive detunings, checks both defining equations, the explicit amplitude cap, the leading center shift and a locally attracting return multiplier. It also iterates the neutral map for 80,000 steps to check the predicted inverse-square asymptotic numerically. Its completed output is:

```
CHIALVO_TANGENTIAL_FLIP_CHECK_OK exact_identities=12 cycle_cases=9 relaxation_steps=80000
```

The exact proof rests on the analytic implicit-function theorem for the symmetric cycle equations and on rigorous local Taylor expansions; neither finite sampling nor symbolic simplifications alone establish the full local asymptotic or uniqueness assertions. No global dynamics, error bounds on the size of the local neighborhood, or independent mathematical validation are claimed. The critical constant uses the full single-step index \(n\), not the half-speed even-return clock.
