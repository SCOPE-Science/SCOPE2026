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

The included standalone checker reproduced spherical cap intersection integrals by an independent 1D quadrature and tested contact densities against finite differences. It also sampled 800,000 isotropic directions and checked endpoint tail ratios and contact asymptotics. These checks are corroborative only; the analytic argument is in RESULT.md.

Run `python checker.py` with NumPy and SciPy. No independent audit has been performed.
