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

# Reproducible checks

Run `python verify.py` in the directory containing this file. Dependencies: Python 3, SymPy and SciPy. The checker reconstructs the allowed cyclic configurations, verifies the transfer characteristic polynomial and discriminant, confirms the defective eigenvalue at \(z=27/4\), compares exact cycle partition polynomials through length fourteen, verifies the partial-fraction identity and eighty-one critical covariance coefficients, and checks seven parameter spectra and two pairs of endpoint approximations.

The expected success line is `VERIFY_OK: symbolic discriminant, defective double eigenvalue, 12 exact ring partitions, 81 exact correlations, 7 spectra, endpoint scales`.

These finite checks do not prove the theorem for all activities or distances. That claim is established by the symbolic transfer, renewal, and monotonicity arguments in `RESULT.md`. The checker does not assess publication priority or supply an independent audit.
