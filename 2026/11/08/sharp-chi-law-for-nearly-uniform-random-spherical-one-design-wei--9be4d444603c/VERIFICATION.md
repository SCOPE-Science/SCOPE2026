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

# Verification record

The analytical proof establishes finite-dimensional LP duality, a uniform strong law for absolute projected deviations, and the fixed-dimensional Gaussian limit. The packaged `verify.py` script independently assembles the affine moment equations and tests the primal relative-box minimization against the dual multipliers returned by a linear-programming solver.

Run `python verify.py` in an environment with NumPy and SciPy installed. The actual execution returned `VERIFY_OK 72 primal/dual and moment checks`; trials covered dimensions \(d=2,3,5\), four sample counts per dimension, and six independent seeded node sets at each setting.

The direct checks use floating-point tolerances of \(10^{-8}\). They are not exhaustive over all node samples, and neither the almost-sure uniform convergence nor the Gaussian limit has been deduced from any finite experiment. The mathematical proof, rather than a numerical frequency estimate, supplies the circle's exact asymptotic constant and the general-dimensional chi-law.
