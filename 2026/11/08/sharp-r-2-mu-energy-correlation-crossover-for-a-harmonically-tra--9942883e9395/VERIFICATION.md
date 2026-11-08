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

# Reproduction and mathematical verification

The article `RESULT.md` specifies the full stochastic generator, stationarity assumptions and all limits. Its proof reconstructs degree-four moments, the three-component mixed-time covariance ODE, the exact convolution solution, strict positivity, leading asymptotic amplitudes, critical repeated pole, and compact-uniform coalescence profile.

With Python 3 and no third-party packages, run `python3 checks/verify_energy_autocovariance.py` from the extracted directory. This script evaluates stationary rational generator moments at nine positive parameter values, reconstructs covariances from raw moments, integrates the three-component ODE for 70 parameter-time cases, and checks explicit leading and crossover relations. Its recorded output is:

```
PASS: 265 exact and finite checks; independent moment recurrence and ODE integration
```

The exact-rational identities and finite calculations test algebra and selected times. Universal positivity, infinite-time decay, uniqueness of the stationary law, and locally uniform crossover are established by the analytic arguments in `RESULT.md`, not by a finite simulation. The model is restricted to a harmonic particle driven by Poisson-reset Brownian noise with positive \(\mu,r,D\). No independent scientific assessment has been performed.
