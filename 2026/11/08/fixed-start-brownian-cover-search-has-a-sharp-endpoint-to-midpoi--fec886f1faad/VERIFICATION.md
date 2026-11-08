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

# Reproducibility and verification

Execute `python verify_location_transition.py` using Python 3 with SymPy, mpmath, NumPy and SciPy. The script checks the exact symbolic hyperbolic objective reduction, differentiates the rational objective and factors the endpoint difference, verifies the cubic root and its sign, checks 54 high-precision hyperbolic identities, and independently builds a 3-state endpoint-history continuous-time random walk with reflected boundaries and resetting to a grid site. It solves sparse linear systems for two lattice spacings at several reset rates and site choices, confirming convergence to the continuous formula. The packaged script executed successfully, reporting `ALL CHECKS PASSED`.

The global theorem requires no finite cutoff: its proof uses positivity of a polynomial's root, the derivative sign, and an exact cubic comparison. The grid is **not** evidence that a finite enumeration establishes the continuum optimality statement. No independent scientific audit or publication-priority certification has been performed.
