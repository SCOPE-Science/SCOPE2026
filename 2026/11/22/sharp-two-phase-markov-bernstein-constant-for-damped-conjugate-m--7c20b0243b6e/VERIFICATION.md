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

The analytic proof in `RESULT.md` is the primary verification. It uses initial-velocity reduction, an exact two-dimensional phase parametrization, monotonicity of the unique contact-switch function, a piecewise scalar maximization, explicit extremizers, and standard implicit differentiation. This proves sharpness and the parameter classification on the full continuum, not merely on sampled phases or damping values.

The pure-standard-library checker `check.py` was executed successfully: 174,116 phase and trajectory probes on 58 damping parameters, five independent coefficient-space phase searches, numerical root localization, and the large-damping limit. Command: `python3 check.py`. These numerical checks are diagnostic and neither establish originality nor certify continuum results independently.

The ratio threshold is defined exactly by its unique scalar root. Its decimal value is approximate. No proof of a Markov–Bernstein inequality for larger complex-exponential spaces is supplied. Independent mathematical audit has not been performed.
