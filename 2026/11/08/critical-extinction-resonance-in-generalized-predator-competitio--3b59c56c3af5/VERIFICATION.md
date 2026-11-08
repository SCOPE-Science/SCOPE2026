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

# Reproducibility and limits

Run the standalone `verification/check.py` file with Python 3 and SciPy installed. It verifies exact identities for a rational parameter tuple and numerically integrates the original flow after the bijective positive transform \(u=y^{-(p-1)}\), at three time horizons for \(p=5/4,3/2,7/4,2\), from two positive initial conditions each. Expected final line:

```
VERIFY_OK rational_coefficients=5 fractional_regimes=3 quadratic_endpoint=1 parameter_cases=8 finite_times=3
```

Exact rational identities used in the tests are \(B=3/2\), \(\delta=15/14\), \(A=4/7\), \(\beta=2/5\), \(\Lambda=24/343\) and \(\beta+\Lambda=806/1715\). The numerical integration checks signs, approximate decay normalizations, the finite-shift, logarithmic and power-correction behavior and the quadratic endpoint. At very late times \(K-x\) can be smaller than machine precision, so the stable-filter ratio check is deliberately confined to adequate finite horizons. Finite trajectories cannot prove convergence for every initial state, exclude other asymptotic rates or certify priority. These claims are supported analytically by positivity, comparison inequalities, the exact stable-filter equation, expansion of the rational response and asymptotic integration. No independent audit has been performed.
