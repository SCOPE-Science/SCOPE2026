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

# Reproducibility

The exact piecewise ODE solution, integration, subtraction, and affine sign classification are proved in `RESULT.md`. The file `verify.py` requires Python 3 and only the standard library. The command `python3 verify.py` returned `ASSERTIONS_PASSED 22813` for the embedded script. It performs independent direct integration for each order, randomized positive-parameter tests, midpoint quadrature on both intervals, both winner directions, tie checks, and a small-separation asymptotic consistency test.

Numerical experiments do not prove universal claims; the universal conclusion rests on algebra and the exact sign of a linear function of a decaying exponential. The result assumes zero initial induced response pools, equal pulse masses, constant positive decay rates, and a bilinear response proxy. Independent audit and ecological validation have not been performed.
