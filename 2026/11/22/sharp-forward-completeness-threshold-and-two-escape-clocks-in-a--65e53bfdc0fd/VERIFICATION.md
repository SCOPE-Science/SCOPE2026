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

# Mathematical verification

The proof in `RESULT.md` establishes (1) finite-horizon barriers for all real initial states when the cubic term has negative sign; (2) a uniform invariant escape region for either cubic curvature sign at positive coefficient; and (3) a logarithmic-velocity invariant escape region at zero cubic coefficient. These are analytical arguments and do not depend on numerical testing.

`verify.py` was executed with Python, SymPy and SciPy. It checks the reciprocal-curvature series coefficients \(1/\gamma\), \(\sigma\alpha/\gamma^2\), \(1/\alpha\) and \(1/\alpha^2\), as well as the asymptotic inverse constants \(\sigma\alpha/(3\gamma)\) and \(1/(2\alpha)\) by exact symbolic limits. It then runs three finite curvature-coordinate ODE diagnostics for both positive-cubic escape signs and the zero-cubic negative escape. The output ends in `VERIFY_OK`.

To reproduce: `python verify.py` from the directory containing this file and the checker. The finite diagnostics are not exhaustive and do not independently certify the infinite-range theorem. No independent mathematical audit is represented.
