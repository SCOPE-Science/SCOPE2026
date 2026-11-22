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

Finite numerical diagnostics: run `python checks/two_basis_trace_kernel_check.py` in the extracted package directory with NumPy installed. The script checks singular-value block diagonalization, positivity and worst-case bounds on Fourier, Haar, reducible and monomial examples; it also checks numerical finite-difference approximations to the entropy slopes. Expected successful output: `TWO_BASIS_TRACE_KERNEL_CHECK_OK 2262`.

All dimensions and exponents are established by the analytic proof in RESULT.md. Numerical experiments do not establish the global classification, the sharp equality cases, the connected-component simplicity claim, or asymptotic estimates by themselves. No independent mathematical audit has been performed.
