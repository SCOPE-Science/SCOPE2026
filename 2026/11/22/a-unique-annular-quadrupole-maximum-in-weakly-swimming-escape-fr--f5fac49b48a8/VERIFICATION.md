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

# Reproducibility and boundaries

The supplied `check.py` is executable with Python 3, NumPy and SciPy. It evaluates the exact coefficient and derivative, checks positive signs over seven rates, locates the interior critical point, and checks the forced second-harmonic ODE residual and the small rotational-diffusion limit. These are finite checks, not an exhaustive numerical proof.

The mathematical proof establishes all infinite and parameter-uniform statements through Bessel differential identities, positivity of power-series coefficients and modified-Bessel asymptotics. The result is the second-order angular Taylor coefficient of mean first exit time and does not establish finite-speed optimality. There is no independent validation.
